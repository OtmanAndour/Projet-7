$('#form').submit(function (e) {
    e.preventDefault()
    var input = $('#input').val()
    $("#text").html("Vous : " + input + "<br><br>")
    $("#text").append('<img id="loader" src="http://loadinggif.com/generated-image?imageId=31&bgColor=%23ccc&fgColor=%23000000&transparentBg=0&download=0&random=0.00030365096131301783" />')
    $('#loader').show()
    console.log(input)
    $.get('result?name=' + input, function (result) {
        result = JSON.parse(result)
        if (result === "No results"){
            $('#loader').hide()
            $("#text").append("GrandPy : Est-ce que tu peux répéter, mon poussin? Je n'ai pas bien compris. Tu sais, je me fait vieux, je n'entend plus très bien. D'ailleurs, ça me rapelle une histoire que j'ai vécu en 1935. A cet époq- Zzzz...")
            $("#map").empty();
            $("#blockquote").empty();
        } else{
            console.log(result)
            $('#loader').hide()
            $("#text").append("GrandPy : Bien sur mon poussin, là voici! Mais laisse-moi d'abord te raconter le lieu de cette histoire!<br><br>");
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