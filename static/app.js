$('#form').submit(function (e) {
    e.preventDefault()
    var mavariable = $('#input').val()
    console.log(mavariable)
    $.get('test?name=' + mavariable, function (result) {
        result = JSON.parse(result)
        console.log(result)
        map = new google.maps.Map(document.getElementById('map'), {
            center: { lat: result.latitude, lng: result.longitude },
            zoom: 15
        });
        marker = new google.maps.Marker({
            position: { lat: result.latitude, lng: result.longitude },
            map: map
        });
        for (let page in result.page.query.pages) {
            $("#page").html(result.page.query.pages[page].extract);
            break
        }

    })

}) 