var overlays = [];

function initMap() {
    var uluru = {
        lat: 50.0194,
        lng: 21.9873
    };
    var map = new google.maps.Map(document.getElementById('mainMap'), {
        zoom: 17,
        center: uluru,
        gestureHandling: 'greedy'
    });
    var places;
    map.addListener('zoom_changed', function () {
        setPlaces(map, places);
    });

    downloadUrl('http://127.0.0.1:8000/places/', function (data) {
        places = JSON.parse(data.responseText);
        setPlaces(map, places);
    });
}


function setPlaces(map, list) {
    console.log(overlays.length);
    for (var i = 0; i < overlays.length; i++) {
        overlays[i].setMap(null);
    }
    overlays = [];

    var zl = map.getZoom();
    size = Math.pow(2, 20 - zl) * 0.000035
    for (var i in list) {
        var bounds = {
            north: parseFloat(list[i]["Latitude"]) + size,
            south: parseFloat(list[i]["Latitude"]) - size,
            east: parseFloat(list[i]["Longitude"]) + size,
            west: parseFloat(list[i]["Longitude"]) - size
        };

        var overlay = new google.maps.GroundOverlay(
            list[i]["IconURL"],
            bounds
        );
        overlay.setMap(map);
        overlays.push(overlay);
    }
}


function downloadUrl(url, callback) {
    var request = window.ActiveXObject ?
        new ActiveXObject('Microsoft.XMLHTTP') :
        new XMLHttpRequest;
    request.onreadystatechange = function () {
        if (request.readyState == 4) {
            callback(request, request.status);
        }
    };
    request.open('GET', url, true);
    request.send(null);
}
