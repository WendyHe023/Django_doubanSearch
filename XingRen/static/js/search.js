let searchInput = document.getElementById("search");
let auto = document.getElementById("auto");

searchInput.addEventListener('compositionend', (e) => {
    fetch(
        '/suggest?s=' + searchInput.value,
        {
            method: 'get'
        })
        .then(response => response.json())
        .then(function (data) {
            let suggestions = data['suggestions'];
            let suggestList = "";
            let optionList = "";
            for (let i = 0; i < suggestions.length; i++) {
                suggestList += '<a href="/search?q=' + suggestions[i] + '">' + suggestions[i] + '</a><br>'
            }
            auto.innerHTML = suggestList;
            auto.className = "auto_show";
        })
        .catch(err => console.log(err));
});

window.addEventListener('keydown', (e) => {
    if (e.defaultPrevented) {
        return; // 如果事件已经在进行中，则不做任何事。
    }
    if (e.key === 'Enter') {
        doSearch();
        e.preventDefault();
    }
}, true);

function hideSuggest() {
    setTimeout(() => {
        auto.className = "auto_hidden";
        auto.innerHTML = "";
    }, 300);
}


function doSearch() {
    if (searchInput.value) {
        window.location.href = '/search?q=' + searchInput.value;
    }
}