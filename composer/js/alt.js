	var gmap; //global map variable
 	var glat = 33.6431859; //global lat and png values. Set initially to irvine
 	var glng = -117.8413502; //global lat and png values. Set initially to irvine
 	var geocoder; //global geocoder from google's geocoder API
 	var markersArray = new Array(); //array to store markers on map
 	var pixelSizeAtZoom0 = .000001; //the size of a pixel at map-zoom = 0
 	var maxPixelSize = 350; //restricts the maximum size of the icon, otherwise the browser will choke at higher zoom levels trying to scale an image to millions of pixels
 	var conditions; //weather conditions from the forecast.io api
 	var forecast = new ForecastIO(); //Forecast.io API

 	//console.log(forecast);
 	google.maps.visualRefresh = true; //show the new Google Maps API as of May 2013
 	
	function initialize() 
	{
		
		var tutorialcomplete4=false;
		var tutorialcomplete5=false;
		var tutorialcomplete6=false;
		
		geocoder = new google.maps.Geocoder();
		var pos = new google.maps.LatLng(60, 50);
		mapDiv = document.getElementById('map-canvas');
		
		var mapOptions = {
		    zoom: 20,
		    center: pos,
		    panControl: true,
		    zoomControl: true,
		    scaleControl: true,
		    mapTypeControl: true,
		    streetViewControl: false,
		    overviewMapControl: false,
		    mapTypeId: google.maps.MapTypeId.ROADMAP
		  }
		
		gmap = new google.maps.Map(mapDiv, mapOptions);
		//gmap.setTilt(0);
		drawingManager = new google.maps.drawing.DrawingManager();
		drawingManager.setMap(gmap);			
		
		
		$('#composer-icons').slideDown();
		$('#inspector').slideDown();
		$('#dashboard').slideDown();
		removePolygonDrawing();
		//addPolygonDrawing();
		 /*
		google.maps.event.addListener(drawingManager, 'polygoncomplete', function(polygon) {
				  
		});*/
		
		google.maps.event.addListener(drawingManager, 'overlaycomplete', function(event) {
		  if (event.type == google.maps.drawing.OverlayType.MARKER) {
		    //event.overlay.setTitle("Hello");
		    /*if(event.overlay.icon == "img/null.png"){
		    	$("#q1").html('Please select a key species <i class="icon-arrow-down"></i>');
		    	$("#q1").slideDown();
		    }
		    else{*/
			    console.log(event);
			    var icon_midpoint = event.overlay.getIcon().size.height/2;
			    console.log(icon_midpoint);
			    $("#q1").slideUp();
			    var size = $("#composer-icons button.active").attr("data-size");
			    var name = $("#composer-icons button.active").attr("data-name");
			    console.log("size:" + size);
			    progress = addMarker(event.overlay, size, size, name);
			    var infowindow = new google.maps.InfoWindow({
			      content: '<div id="content" onmouseover="updateContent()"><h4>'+ name+'</h4><label class="control-label">Plant Viability</label><div class="progress"><div class="nitrogen-bar-total bar bar-info" style="width:0%"></div><div class="pests-bar-total bar bar-success" style="width:0%"></div></div>',
			      pixelOffset: new google.maps.Size(0, icon_midpoint)
			    });
			    google.maps.event.addListener(event.overlay,'click',function(){
			    	infowindow.open(gmap,event.overlay);
			    	updateProgressBars();
			    });
			    addGuildList();
			    if(!tutorialcomplete4){
			    	tutorialcomplete4=true;
			    	$('#joyRideTipContent4').joyride({
						  autoStart : true,
						  postStepCallback : function (index, tip) {
							  if (index == 2) {
								$(this).joyride('set_li', false, 1);
							  }
							},
  						  postRideCallback: function(){
							$('#joyRideTipContent4').joyride('destroy');
						  },
						  modal:true,
						  expose: true
					});
			 }
			 if(!tutorialcomplete5){
			 	if(progress == "tut5"){
			    	tutorialcomplete5=true;
			    	$('#joyRideTipContent5').joyride({
						  autoStart : true,
						  postStepCallback : function (index, tip) {
							  if (index == 2) {
								$(this).joyride('set_li', false, 1);
							  }
							},
  						  postRideCallback: function(){
							$('#joyRideTipContent5').joyride('destroy');
						  },
						  modal:true,
						  expose: true
					});
				}
			}
			if(!tutorialcomplete6){
			 	if(progress == "tut6"){
			    	tutorialcomplete5=true;
			    	$('#joyRideTipContent6').joyride({
						  autoStart : true,
						  postStepCallback : function (index, tip) {
							  if (index == 2) {
								$(this).joyride('set_li', false, 1);
							  }
							},
  						  postRideCallback: function(){
							$('#joyRideTipContent6').joyride('destroy');
						  },
						  modal:true,
						  expose: true
					});
				}
			}
		  }
		 /* else if (event.type == google.maps.drawing.OverlayType.POLYGON) {
			  	console.log(event);
			  	event.overlay.setOptions({fillColor: '#FFFFFF'});
			   	$('#q1').slideUp(function(){
					$('#composer-icons').slideDown();
					$('#inspector').slideDown();
					$('#dashboard').slideDown();
			   		removePolygonDrawing();
			   });
		  }*/
		});
		
		google.maps.event.addListener(gmap, 'zoom_changed', function() {
			console.log("zoom:" + gmap.getZoom());
		    
		    var zoom = gmap.getZoom();
		    var relativePixelSize = pixelSizeAtZoom0*Math.pow(2,zoom); // use 2 to the power of current zoom to calculate relative pixel size.  Base of exponent is 2 because relative size should double every time you zoom in
		
		    /*if(relativePixelSize > maxPixelSize) //restrict the maximum size of the icon
		        relativePixelSize = maxPixelSize;*/
		
		    //change the size of the icon
		    _.each(markersArray, function(value, key, list){
		    	console.log(value.width + "*" + relativePixelSize);
		    	console.log(value.marker.getIcon());
		    	value.marker.setIcon(
		    	    new google.maps.MarkerImage(
		    	        value.marker.getIcon().url, //marker's same icon graphic
		    	        null,//size
		    	        null,//origin
		    	        null, //anchor
		    	        new google.maps.Size(value.width*relativePixelSize, value.height*relativePixelSize) //changes the scale
		    	    )
		    	);   
		    
		    });
		    
		         
		});
			
		var weatherLayer = new google.maps.weather.WeatherLayer({
		 		temperatureUnits: google.maps.weather.TemperatureUnit.FAHRENHEIT
				});
		weatherLayer.setMap(gmap);
			
		var cloudLayer = new google.maps.weather.CloudLayer();
		cloudLayer.setMap(gmap);
		
		
		//slide the map menu item from the navigation bar down
			$("#menu-map").slideDown();
			//make an address variable with the text from the location input
			var address = '28 Murasaki, Irvine, CA 92617';
				//get the gps location for the address from google's geolocation service
				getGPS(address, function(data){
					//log the return data
					console.log(data);
					//slide the map down
					slideMapDown(data);
				});
			//change the drawing tools to include the polygon tool	
			//addPolygonDrawing();
			//refresh the spy-scroll, check bootstrap docs
			refreshSpy();
			
	} 

	google.maps.event.addDomListener(window, 'load', initialize);
	
	
	
	function slideMapDown(pos)
	{
		var mapRow = $("#map");
		mapRow.show("normal", function()
		{
			console.log(pos);
			scroll("#map");
			TweenMax.to(mapRow, 1, {
				 height:"400px", ease:Quad.easeOut, onComplete: function()
				 {
					 google.maps.event.trigger(gmap, 'resize');
					 gmap.setZoom( gmap.getZoom() );
					 gmap.setCenter(pos);
					 //gmap.setTilt(0);
					 var marker = new google.maps.Marker({
						 map: gmap,
						 position: pos
					 });
					 $("#q1").slideDown();
					 loadForecast(pos.lat(), pos.lng());
					 readTextFile('weather/temp.09.25.2013.txt');
				 }
			});  
		});     
	}
	
	
	function loadForecast(lat, longitude)
	{
		conditions = forecast.getCurrentConditions(lat, longitude);
		var temp = conditions.getTemperature();
		var humidity = (Math.round(conditions.getHumidity()*100));
		var wind_speed = conditions.getWindSpeed();
		var wind_bearing = conditions.getWindBearing();
		
			
		$("#temperature #value").text(temp);
		$("#humidity #value").text(humidity);
		$("#wind-speed #value").text(wind_speed);
		$("#wind-bearing").css("transition","all 1s ease-in-out");
		$("#wind-bearing").css("transform", "rotate("+wind_bearing+"deg)");
		$("#wind-bearing-value #value").text(wind_bearing);

	}
		
	function getGPS(address, output)
	{
	    geocoder.geocode( { 'address': address}, function(results, status) 
	        {
	          if (status == google.maps.GeocoderStatus.OK) 
	          {
	          	console.log(results);
	          	output(results[0].geometry.location);
	          }
	          else 
	          {
	              console.log(status);
	          }
	        }
	    );
	}
		
	function getAddress(location, output)
	{
		console.log(location);
		//glat = location.lat();
		//glng = location.lng();
	    geocoder.geocode( { 'latLng': location }, function(results, status)
	        {
	        	//console.log(status);
	          if (status == google.maps.GeocoderStatus.OK)
	          {
		          	output(results[0].formatted_address);
	          }
	          else
	          {
	          		//console.log(status);
	          }
	        }
	    );
	}
		
	function getCurrentLocation(callback)
	{
		navigator.geolocation.getCurrentPosition(function(position){
			var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
			glat = position.coords.latitude;
			glng = position.coords.longitude;
			slideMapDown(pos);    
			callback(pos);
			console.log(pos);
		}, displayError);
	}
		
	function displayError(error) 
	{
	  var errors = { 
		1: 'Permission denied',
		2: 'Position unavailable',
		3: 'Request timeout'
	  };
	  alert("Error: " + errors[error.code]);
	} 		      
		  
	function setDrawing(icon, title, name, size) 
	{
		var relativePixelSize = pixelSizeAtZoom0*Math.pow(2,gmap.getZoom());
		
		var markerImage = new google.maps.MarkerImage(
		    icon,
		    new google.maps.Size(size*relativePixelSize,size*relativePixelSize), //size
		    null, //origin
		    null, //anchor
		    new google.maps.Size(size*relativePixelSize,size*relativePixelSize) //scale
		);
	
	
		drawingManager.setOptions({
		   drawingMode: google.maps.drawing.OverlayType.MARKER,
		   drawingControl: true,
		   drawingControlOptions: {
			 position: google.maps.ControlPosition.TOP_CENTER,
			 drawingModes: [
			   google.maps.drawing.OverlayType.MARKER,
			   //google.maps.drawing.OverlayType.POLYGON,
			 ]
		   },
		   markerOptions: {
			 icon: markerImage,
			 draggable: true,
			 title: title,
			 raiseOnDrag: false
		   }
	 	});
   	}
		   
   	function removePolygonDrawing()
   	{
	   drawingManager.setOptions({
		 drawingMode: google.maps.drawing.OverlayType.MARKER,
		 drawingControl: true,
		 drawingControlOptions: {
		   position: google.maps.ControlPosition.TOP_CENTER,
		   drawingModes: [google.maps.drawing.OverlayType.MARKER]
		 },
		 markerOptions: {
		 	icon: 'img/null.png'
		 }
	   });
   	}
   
   	function addPolygonDrawing()
   	{
	   drawingManager.setOptions({
		 drawingMode: google.maps.drawing.OverlayType.POLYGON,
		 drawingControl: true,
		 drawingControlOptions: {
		   position: google.maps.ControlPosition.TOP_CENTER,
		   drawingModes: [google.maps.drawing.OverlayType.POLYGON]
		 }
	   });
   	}
   	
   	// Removes the overlays from the map, but keeps them in the array
   	function addMarker(marker, width, height, name) {
   	  markersArray.push({'marker': marker, 'width': width, 'height':height, 'name':name});
   	  return updateProgressBars();
   	}
						  
	// Removes the overlays from the map, but keeps them in the array
	function clearOverlays() {
	  if (markersArray) {
		for (i in markersArray) {
		  markersArray[i].setMap(null);
		}
	  }
	}
			
	// Shows any overlays currently in the array
	function showOverlays() {
	  if (markersArray) {
		for (i in markersArray) {
		  markersArray[i].setMap(gmap);
		}
	  }
	}
			
	// Deletes all markers in the array by removing references to them
	function deleteOverlays() {
	  if (markersArray) {
		for (i in markersArray) {
		  markersArray[i].setMap(null);
		}
		markersArray.length = 0;
	  }
	}
	
	
	function scroll(id)
	{
		$("html, body").animate({ scrollTop: $(id).offset().top - 75}, 1000);
	}
		
	function refreshSpy()
	{
		$('[data-spy="scroll"]').each(function () {
		  $(this).scrollspy('refresh');
		});
	
	}
 	
 	function updateProgressBars()
 	{
 		var tutorialval = "none";
 		var newArray = _.pluck(markersArray, 'marker');
 		key_size = _.size(_.where(newArray, {title: "key"}));
 		n_size = _.size(_.where(newArray, {title: "nitrogen"}));
 		p_size = _.size(_.where(newArray, {title: "pests"}));
 		both_size = _.size(_.where(newArray, {title: "both"}));
 		
 		n_width = ((n_size+both_size)/(key_size*4))*100;
 		p_width = ((p_size+both_size)/(key_size*3))*100;
 		
 		if(n_width > 100){
 			n_width = 100;
 		}
 		if(p_width > 100){
 			p_width = 100;
 		}
 		
 		nwidthpx = Math.round(350*n_width/100);
 		pwidthpx = Math.round(350*p_width/100);
 		new_css_nwidth = n_width + "%";
 		new_css_pwidth = p_width + "%"
 		console.log("nitrogen bar width " + $(".nitrogen-bar").css("width") + "new width " + nwidthpx);

 		if($(".nitrogen-bar").css("width") != nwidthpx+"px"){
 			$(".nitrogen-bar").css("width", new_css_nwidth);
 			tutorialval = "tut5";
 		}
 		if($(".pests-bar").css("width") != pwidthpx+"px"){
 			$(".pests-bar").css("width", new_css_pwidth);
 			tutorialval = "tut5";
 		}
 		
 		if(n_width == 100 && p_width ==100){
 			tutorialval = "tut6";
 		}
 		
 		$(".nitrogen-bar-total").css("width", n_width*(4/7) + "%");
 		$(".pests-bar-total").css("width", p_width*(3/7) + "%");
 		
 		console.log("tutorial val:" +tutorialval);
 		return tutorialval;
 	
 	}
 	
 	function addGuildList(){
 		
 		insert = false;
 		name = $("#composer-icons button.active").attr("data-name");
 		console.log("inAddGuildList: Name is "+ name);
 		category  = $("#composer-icons button.active").attr("data-category");
 		
 		
 		//if plant is a key species, add to the key list
 		if (category == "key"){
 			console.log("inAddGuildList: category is key");
 			key_members = $("#guild-list-key").find("div");
 			console.log("inAddGuildList: key_members.length:"+key_members.length);
 			//if data-category is in guild-member-key
 				//increment data-category
 			for(i = 0; i< key_members.length; i++){
 				console.log("inAddGuildList: key_member[i] data-name is " + key_members);
 				if($(key_members[i]).attr("data-name") == name){
 					
 					quant = $(key_members[i]).find("span");
 					curr_quant = parseInt(quant.attr("quantity"));
 					curr_quant++;
 					console.log("inAddGuildList: old_quant is "+curr_quant);
 					
 					
 					quant.attr("quantity", curr_quant);
 					console.log("inAddGuildList: new_quant is "+ quant.attr("quantity"));
 					
 					
 					quant.text(quant.attr("quantity"));
 					insert = true;
 					break;
 				}
 			}
 			//else, add to guild-member-key
 			if(!insert){
 				console.log("inAddGuildList: adding to key members");
 				$("#guild-list-key").append('<div data-name="'+name+'">'+name+' x<span quantity="1">1</span></div>');
 			}
 		}
 			
 		//otherwise it is  a support species so add it to the support list
 		else{
 			console.log("inAddGuildList: category is support");
 			support_members = $("#guild-list-support").find("div");
 		
 			//if data-category is in guild-member-support
 				//increment data-category
 			for(i = 0; i< support_members.length; i++){
 				if($(support_members[i]).attr("data-name") == name){
 					quant = $(support_members[i]).find("span");
 					curr_quant = parseInt(quant.attr("quantity"));
 					curr_quant++;
 					quant.attr("quantity", curr_quant);
 					quant.text(quant.attr("quantity"));
 					insert = true;
 					break;
 				}
 			}
 				
 				
 			//else, add to guild-member-support
 			if(!insert){
 					$("#guild-list-support").append('<div data-name="'+name+'">'+name+' x<span quantity="1">1</span></div>');
 			}
 		
 		}
 			
 		
 		
 	}

 ///weather by Juliet
 
 function importData(contents){
	//first row are the data labels
	rows = contents.split("\n");
	label_array = rows[0].split(",");
	
	var value_array = [];
	value_array.length = rows.length-1;
	
	//we start at one because the first entry in rows were stored in label_array
	for(i=1; i<rows.length; i++){
		value_array[i-1]= rows[i].split(",");
	}
	
	//temperature chart
	chart_data = [];
	chart_data[0] = new Array("Date", label_array[1], label_array[2], label_array[3]);
	
	for(i=0; i< value_array.length; i++){
			chart_data[i+1] = new Array(value_array[i][0], parseInt(value_array[i][1]), parseInt(value_array[i][2]), parseInt(value_array[i][3]));
	}
	
	var google_data = google.visualization.arrayToDataTable(chart_data, false);
	
	var options = {
		width: 650,
		height: 230,
		chartArea: {width: "70%", left:"60"},
		title: "One Year Temperature History",
		vAxis: {title: "Fahrenheit"},
		lineWidth: ".05",
		pointSize: "1",
		legend: {position: 'right', alignment: 'start'},
		colors: ['#d9005b', '#00b945', '#e2fa00', '#bd003b']
	}
	
	var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
		
	chart.draw(google_data, options);
	
	console.log("The chart data is... "+ chart_data);
	
	//precipitation chart
	chart_data = [];
	chart_data[0] = new Array("Date", label_array[19]);
	
	for(i=0; i< value_array.length; i++){
			chart_data[i+1] = new Array(value_array[i][0], parseFloat(value_array[i][19]));
	}
	
	var options = {
		title: "One Year Precipitation History",
		chartArea: {width: "65%", left:"75"},
		vAxis: {title: "Inches"},
		lineWidth: ".05",
		pointSize: "1",
		legend: {position: 'right'},
		width: 650,
		height: 230,
		colors: ['#d9005b', '#00b945', '#e2fa00', '#bd003b']
	}
	
	drawLineChart(chart_data, options, "chart_div_rain");
	
	//wind speed and gust chart
	chart_data = [];
	chart_data[0] = new Array("Date", label_array[17], label_array[18]);
	
	for(i=0; i< value_array.length; i++){
			chart_data[i+1] = new Array(value_array[i][0], parseInt(value_array[i][17]), parseInt(value_array[i][18]));
	}
	var options = {
		title: "One Year Wind Speed History",
		chartArea: {width: "65%", left:"75"},
		vAxis: {title: "MPH"},
		lineWidth: ".05",
		pointSize: "1",
		legend: {position: 'right'},
		width: 650,
		height: 230,
		colors: ['#d9005b', '#00b945', '#e2fa00', '#bd003b']
	}
	drawLineChart(chart_data, options, "chart_div_windspeed");
	
	//wind direction
	chart_data = [];
	chart_data[0] = new Array("Date", label_array[22]);
	
	for(i=0; i< value_array.length; i++){
			chart_data[i+1] = new Array( value_array[i][0], parseInt(value_array[i][22]));
	}
	
	var options = {
		title: "One Year Wind Direction History",
		chartArea: {width: "65%", left:"75"},
		vAxis: {title: 'Direction (N: 360, S: 180)', minValue: 0, maxValue: 360},
		lineWidth: "0",
		pointSize: "2",
		legend: {position: 'right'},
		width: 650,
		height: 230,
		colors: ['#d9005b', '#00b945', '#e2fa00', '#bd003b']
	}
	
	drawLineChart(chart_data, options, "chart_div_winddirection");
}

  function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                importData(allText);
            }
        }
    }
    rawFile.send(null);
}
  
  function readSingleFile(evt) {
    //Retrieve the first (and only!) File from the FileList object
    
    var f = evt.target.files[0]; 

    if (f) {
      var r = new FileReader();
      r.onload = function(e) { 
	      var contents = e.target.result;
        /*alert( "Got the file.\n" 
              +"name: " + f.name + "\n"
              +"type: " + f.type + "\n"
              +"size: " + f.size + " bytes\n"
              + "starts with: " + contents.substr(1, contents.indexOf("\n"))
        );  */
        
        importData(contents);
        
      }
      r.readAsText(f);
    } else { 
      alert("Failed to load file");
    }
    
    document.getElementById('fileinput').style.visibility = 'hidden';
  }
  
  function toggle_weather_f (){
	//from forecast to historical
  	document.getElementById('forecast-dash').parentNode.parentNode.style.display = 'none';
  	document.getElementById('weatherhistory-dash').parentNode.parentNode.style.display = 'inline';
  
    }
function toggle_weather_h (){
    //from historical to forecast
   
      	document.getElementById('weatherhistory-dash').parentNode.parentNode.style.display = 'none';
  	document.getElementById('forecast-dash').parentNode.parentNode.style.display = 'inline';
  	}  
  	
  	
  	
