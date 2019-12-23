def extract_hit(item_id, hit):
    # hit_dict = {}
    # hit_dict['id'] = hit['_id']
    # hit_dict['title'] = hit['_source']['title']
    # hit_dict['douban_link'] = hit['_source']['douban_link']
    # hit_dict['year'] = hit['_source']['year']
    # hit_dict['lang'] = hit['_source']['lang']
    # hit_dict['runtime'] = hit['_source']['runtime']
    #
    # overview = hit['_source']['overview'][0:250].strip()
    # dot = overview.rfind('。')
    # comma = overview.rfind('.')
    # hit_dict['overview'] = overview[0:max(dot, comma)] + '......'
    #
    # # hit_dict['overview'] = hit['_source']['overview'][0:250].strip()
    #
    # hit_dict['release_at'] = hit['_source']['release_at']
    # hit_dict['genres'] = " / ".join(hit['_source']['genres'][0:3])
    # hit_dict['rating'] = hit['_source']['rating']
    # # hit_dict['season_count'] = hit['_source']['season_count']
    #
    # hit_dict['small_image'] = hit['_source']['small_image']
    #
    # hit_dict['directors'] = " / ".join(hit['_source']['directors'][0:2])
    # hit_dict['casts'] = " / ".join(hit['_source']['casts'][0:5])

    hit['id'] = item_id

    overview = hit['overview'][0:230].strip()
    peroid = overview.rfind('。')
    comma = overview.rfind('，')
    dot = overview.rfind('.')
    hit['overview'] = overview[0:max(max(dot, comma), peroid)] + '......'
    hit['genres'] = " / ".join(hit['genres'][0:3])

    hit['directors'] = " / ".join(hit['directors'][0:2])
    if len(hit['casts'][0]) < 5:
        hit['casts'] = " / ".join(hit['casts'][0:7])
    else:
        hit['casts'] = " / ".join(hit['casts'][0:4])

    return hit
