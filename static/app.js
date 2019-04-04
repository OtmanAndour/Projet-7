$('#form').submit(function (e) {
    e.preventDefault()
    var mavariable = $('#input').val()
    console.log(mavariable)
    $.get('search?name=' + mavariable, function (result) {
        result = JSON.parse(result)
        if (result === "No results"){
            $("#text").html("Est-ce que tu peux répéter, mon poussin? Je n'ai pas bien compris. Tu sais, je me fait vieux, je n'entend plus très bien. D'ailleurs, ça me rapelle une histoire que j'ai vécu en 1935. A cet époq- Zzzz...")
            $("#map").empty();
            $("#blockquote").empty();
        } else{
            console.log(result)
            $("#text").html("Bien sur mon poussin, là voici! Mais laisse-moi d'abord te raconter le lieu de cette histoire!<br><br>");
            $("#text").append(result.quote);
            map = new google.maps.Map(document.getElementById('map'), {
                center: { lat: result.latitude, lng: result.longitude },
                zoom: 15
            });
            marker = new google.maps.Marker({
                position: { lat: result.latitude, lng: result.longitude },
                map: map
            });
            for (let page in result.page.query.pages) {
                let extract = result.page.query.pages[page].extract;
                let url = result.page.query.pages[page].fullurl;
                console.log(url);
                $("#blockquote").html(extract);
                $("#blockquote").append('<footer class="blockquote-footer">Wikipedia. Pour en savoir plus, cliquer sur ce <a href="' + url + '" target="_blank">lien</a></footer>');
                break
            }

        }
    })

}) 