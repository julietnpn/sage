function load_map()
{


var map;
	function initialize() {
  	var mapOptions = {
    	zoom: 16,
    	center: new google.maps.LatLng(
    	33.640133,-117.840165),
    	mapTypeId: google.maps.MapTypeId.HYBRID
  		};
  	map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
      
    var drawingManager = new google.maps.drawing.DrawingManager({
        drawingMode: google.maps.drawing.OverlayType.MARKER,
        drawingControl: true,
        drawingControlOptions: {
          position: google.maps.ControlPosition.TOP_CENTER,
          drawingModes: [
            google.maps.drawing.OverlayType.MARKER,
            google.maps.drawing.OverlayType.CIRCLE,
            google.maps.drawing.OverlayType.POLYGON,
            google.maps.drawing.OverlayType.POLYLINE,
            google.maps.drawing.OverlayType.RECTANGLE
          ]
        },
        markerOptions: {
          icon: 'images/beachflag.png'
        },
        circleOptions: {
          fillColor: '#ffff00',
          fillOpacity: 1,
          strokeWeight: 5,
          clickable: false,
          editable: true,
          zIndex: 1
        }
      });
      drawingManager.setMap(map);
}

	google.maps.event.addDomListener(window, 'load', initialize);














}