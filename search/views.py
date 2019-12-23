import redis
from django.http import JsonResponse
from django.shortcuts import render
from elasticsearch import Elasticsearch

from search.service import extract_hit

client = Elasticsearch(hosts=["10.28.238.105"])
redis_cli = redis.StrictRedis()


# def index(request):
#     return render(request, 'index.html')


def suggest(request):
    search_text = request.GET.get('s')
    response = client.search(
        index="xingren",
        body={
            "_source": "suggest",
            "suggest": {
                "title_suggestions": {
                    "text": search_text,
                    "completion": {
                        "field": "title.suggest"
                    }
                }
            },
        }
    )
    suggestions = list(r['text'] for r in response['suggest']['title_suggestions'][0]['options'] if len(r['text']) > 0)
    return JsonResponse({"suggestions": suggestions})


def search(request):
    key_word = request.GET.get('q')
    if key_word:

        response = client.search(
            index="xingren",
            body={
                "query": {
                    "multi_match": {
                        "query": key_word,
                        "fields": "title"
                    }
                },
            }
        )

        hit_list = []
        for hit in response["hits"]["hits"]:
            hit_list.append(extract_hit(hit['_id'], hit['_source']))

        if hit_list:
            redis_cli.zincrby("id_set", 1, hit_list[0]['id'])
        if len(hit_list) > 1:
            redis_cli.zincrby("id_set", 1, hit_list[0]['id'])
            redis_cli.zincrby("id_set", 1, hit_list[1]['id'])

        context = {'key_word': key_word, 'hit_list': hit_list}
    else:
        top_ids = redis_cli.zrevrangebyscore("id_set", "+inf", "-inf", start=0, num=4)
        top_item = []
        print(top_ids)
        for id in top_ids:
            top = client.get("xingren", "doc", id)
            if top:
                top_item.append(extract_hit(top['_id'], top['_source']))
        context = {'top_item': top_item}

    return render(request, 'result.html', context)
