var selectedPlant = 'smallflower.png';

function startMap() {
  var mapOptions = {
    center: new google.maps.LatLng(33.640133,-117.840165),
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  var map = new google.maps.Map(document.getElementById('map-canvas'),
    mapOptions);

  var drawingManager = new google.maps.drawing.DrawingManager({
    drawingMode: google.maps.drawing.OverlayType.MARKER,
    drawingControl: true,
    drawingControlOptions: {
      position: google.maps.ControlPosition.TOP_CENTER,
      drawingModes: [
//      only left the tools that we need on in here
        google.maps.drawing.OverlayType.POLYGON,
//      google.maps.drawing.OverlayType.CIRCLE,
        google.maps.drawing.OverlayType.MARKER,
//      google.maps.drawing.OverlayType.POLYLINE,
//        //google.maps.drawing.OverlayType.RECTANGLE
      ]
    },
    markerOptions: {
      draggable: true,
//       "icon" is where the plant icon that gets stamped is selected, needs a proper listener that can be changed through the clicks on the plants
      icon: selectedPlant,
    },
    circleOptions: {
      fillColor: '#ffff00',
      fillOpacity: 1,
      strokeWeight: 1,
      clickable: false,
      editable: true,
      zIndex: 1
    }
  });
  drawingManager.setMap(map);
}

google.maps.event.addDomListener(window, 'load', startMap);


//in here are the initial hides as well as the show/hide pairs that run with the buttons
$(document).ready(function() {
	$("#loadingbayflowers, #loadingbaytitles, #vitalitybox").hide();
	
	$("#loadplants").click(function() {
    	$("#loadplants").hide();
    	$("#loadingbayflowers, #loadingbaytitles").show(200);
    	
  	});
  	
  	$("#loadweather").click(function() {
  		$("#loadweather").hide();
  		
  	});
  	
  	$("#loadvitality").click(function() {
  		$("#loadvitality").hide();
  		$("#vitalitybox").show();
  		
  		
  	});
  	
  	$("#plantTwo").click(function() {
  		selectedPlant = 'flower.png';
  		
  	});
});













//needs implementation
//  
//  function addMarker(location) {
//      marker = new google.maps.Marker({
//        position: location,
//        map: gmap,
//      });
//      markersArray.push(marker);
//    }
//    
//     Removes the overlays from the map, but keeps them in the array
//    function clearOverlays() {
//      if (markersArray) {
//        for (i in markersArray) {
//          markersArray[i].setMap(null);
//        }
//      }
//    }
//    
//     Shows any overlays currently in the array
//    function showOverlays() {
//      if (markersArray) {
//        for (i in markersArray) {
//          markersArray[i].setMap(gmap);
//        }
//      }
//    }
//    
//     Deletes all markers in the array by removing references to them
//    function deleteOverlays() {
//      if (markersArray) {
//        for (i in markersArray) {
//          markersArray[i].setMap(null);
//        }
//        markersArray.length = 0;
//      }
//    }
//  
//   
//  
//  function codeAddress(address, gmap) {
//    geocoder.geocode( { 'address': address}, function(results, status) {
//      if (status == google.maps.GeocoderStatus.OK) {
//      	$("#map").slideDown("normal", function(){
//      		
//      		google.maps.event.trigger(gmap, 'resize');
//      		gmap.setZoom( gmap.getZoom() );
//      		gmap.setCenter(results[0].geometry.location);
//      		var marker = new google.maps.Marker({
//      		    map: gmap,
//      		    position: results[0].geometry.location
//      		});
//      		
//      		$("#confirm").slideDown();
//      		var photo = document.getElementById("confirm");
//      		TweenLite.to(photo, 2, {width:"200px", height:"150px"});
//      	});
//        		            
//      } else {
//        console.log(status);
//      }
//    });
//    
//  }
//  
//
//    
//     * The HomeControl adds a control to the map that simply
//     * returns the user to Chicago. This constructor takes
//     * the control DIV as an argument.
//     
//
//    function HomeControl(controlDiv, gmap) {
//
//       Set CSS styles for the DIV containing the control
//       Setting padding to 5 px will offset the control
//       from the edge of the map
//      controlDiv.style.padding = '5px';
//
//       Set CSS for the control border
//      var controlUI = document.createElement('div');
//      controlUI.style.backgroundColor = 'white';
//      controlUI.style.borderStyle = 'solid';
//      controlUI.style.borderWidth = '2px';
//      controlUI.style.cursor = 'pointer';
//      controlUI.style.textAlign = 'center';
//      controlUI.title = 'Click to set the map to Home';
//      controlDiv.appendChild(controlUI);
//
//       Set CSS for the control interior
//      var controlText = document.createElement('div');
//      controlText.style.fontFamily = 'Arial,sans-serif';
//      controlText.style.fontSize = '12px';
//      controlText.style.paddingLeft = '4px';
//      controlText.style.paddingRight = '4px';
//      controlText.innerHTML = '<b>Current Location</b>';
//      controlUI.appendChild(controlText);
//
//       Setup the click event listeners: simply set the map to
//       Chicago
//      google.maps.event.addDomListener(controlUI, 'click', function() {
//        gmap.panTo(new google.maps.LatLng(myCoords.latitude, myCoords.longitude))
//      });
//
//    }
//    
//      function markerChange(controlDiv, gmap) {
//
//       Set CSS styles for the DIV containing the control
//       Setting padding to 5 px will offset the control
//       from the edge of the map
//      controlDiv.style.padding = '5px';
//
//       Set CSS for the control border
//      var controlUI = document.createElement('div');
//      controlUI.style.backgroundColor = 'white';
//      controlUI.style.borderStyle = 'solid';
//      controlUI.style.borderWidth = '2px';
//      controlUI.style.cursor = 'pointer';
//      controlUI.style.textAlign = 'center';
//      controlUI.title = 'Click to set the map to Home';
//      controlDiv.appendChild(controlUI);
//
//       Set CSS for the control interior
//      var controlText = document.createElement('div');
//      controlText.style.fontFamily = 'Arial,sans-serif';
//      controlText.style.fontSize = '12px';
//      controlText.style.paddingLeft = '4px';
//      controlText.style.paddingRight = '4px';
//      controlText.innerHTML = '<b>Icon Change</b>';
//      controlUI.appendChild(controlText);
//
//       Setup the click event listeners: simply set the map to
//       Chicago
//      google.maps.event.addDomListener(controlUI, 'click', function() {
//        setDrawing("img/backpack.png", gmap);
//      });
//
//    }