function startMap() {
	var mapOptions = {
		center: new google.maps.LatLng(33.640133,-117.840165),
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    }
    google.maps.event.addDomListener(window, 'load', startMap);

