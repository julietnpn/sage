var AddPlant = function(){
	//----------------- BEGIN MODULE SCOPE VARIABLES ------------
	var pub = {},
        jqueryMap = {},
        setJqueryMap;

	//----------------- END MODULE SCOPE VARIABLES ------------

	//----------------- BEGIN PUBLIC METHODS --------------------
    /// <summary>
    /// Method initializes the release target module.  This method should always be called 
    /// prior to any other public methods since it acts as the constructor.
    /// </summary>
    pub.init = function(){
    	setJqueryMap();

		// jqueryMap.$addThis.click(function () {
  //           var latinName = jqueryMap.$latinName.val().split(" ");
  //           var genus, species, variety;
  //           genus = latinName[0];
  //           if(latinName.length > 1){
  //               species = latinName[1];
  //               if(latinName.length > 2)
  //                   variety = latinName[2];
  //           }
  //           var commonName = jqueryMap.$commonName.val();
  //           var pictureURL = $('.selected').prop('src');

  //           $.ajax({
  //               type:"POST",
  //               url: "/home/edit/",
  //               data: {
  //                   'genus': 'genus',
  //                   'species':'species',
  //                   'variety': 'variety',
  //                   'commonName': 'commonName',
  //                   'url':'url'
  //               },
  //               dataType: 'json'
  //               //success: function(){},
  //               //error: function(){},
  //           });
  //       });

        jqueryMap.$commonName.blur(function(){
            validateNames();
        });

        jqueryMap.$latinName.blur(function () {
            validateNames();
        });

        // jqueryMap.$thumbnails.on({
        //     click: function(){
        //         resetBorderColor($(this).siblings());
        //         $(this).css('border-color', '#66CD00');
             
        //         $(this).addClass('selected');
        //         displayElements(jqueryMap.$addThis.children());
        //     },
        //     mouseenter: function(){
        //         $(this).css('border-color', '#66CD00');
        //     },
        //     mouseleave: function(){
        //         if(!$(this).hasClass('selected'))
        //         $(this).css('border-color', '#ddd');
        //     }
        // }, '.thumbnail-img');

        jqueryMap.$clearAddPlant.click(function(){
            jqueryMap.$latinName.val("");
            jqueryMap.$commonName.val("");
            // hideElements(jqueryMap.$thumbnails.children());
            hideElements(jqueryMap.$clearAddPlant);
            hideElements(jqueryMap.$addThis.children());
            // resetBorderColor(jqueryMap.$thumbnails.children(".thumbnail-img"));
        });
    }

    return pub;
    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------

        
    function setJqueryMap() {
        jqueryMap = {
        	$latinName : $("#add-plant-latin-name"),
            $lNameLabel :$("#latin-name-label"),
            $cNameLabel:$("#common-name-label"),
        	$commonName : $("#add-plant-common-name"),
        	$addThis: $("#add-plant-submit-container"),
        	$sidebarSection: $('#sidebar-bottom-content'),
        	$thumbnailImages:$(".thumbnail-img"),
            $thumbnails:$("#thumbnail-container"),
            $clearAddPlant:$('#sidebar-clear')

        };
    }

    function validateNames(){
        var isValidated = 0;
        if(jqueryMap.$latinName.val() == ""){
            jqueryMap.$lNameLabel.css("color", "red"); //#66CD00
        }
        else{
            jqueryMap.$lNameLabel.css("color", "#999");
            isValidated += 1;
        }
        if(jqueryMap.$commonName.val() == ""){
            jqueryMap.$cNameLabel.css("color", "red");
        }
        else{
            jqueryMap.$cNameLabel.css("color", "#999");
            isValidated += 1;
        }
        if(isValidated > 0){
            displayElements(jqueryMap.$clearAddPlant);
        }
        if(isValidated == 2){
            displayElements(jqueryMap.$addThis.children());
        }
    }

    // function searchFlickrPictures(){
    //     displayElements(jqueryMap.$clearAddPlant);
    //     jqueryMap.$thumbnails.html("");

    //     var latinName = escapeString(jqueryMap.$latinName.val());
    //     var commonName = escapeString(jqueryMap.$commonName.val());

    //     var url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=0dde4e72b0091627e13df41e631b85ec&tags="
    //                 +latinName+"%2C" + commonName+"&safe_search=1&per_page=3";
    //     var src;
    //     $.getJSON(url + "&format=json&nojsoncallback=1", function(data){
    //         $.each(data.photos.photo, function(i,item){
    //             src = "http://farm"+ item.farm +".static.flickr.com/"+ item.server +"/"+ item.id +"_"+ item.secret +"_m.jpg";
    //             $("<img class='thumbnail-img' style='object-fit:cover;padding:0px;border-radius:5px;' id='" + i + "'/>").attr("src", src).appendTo("#thumbnail-container");
    //         });
    //         $("<br><p class='input-label italic'>results from flickr</p>").appendTo('#thumbnail-container');
    //         setThumbnailSize();
    //         setJqueryMap(); 
    //     });
    // }

    // function setThumbnailSize(){
    // 	var width = jqueryMap.$sidebarSection.width() - 81;
    //     for(var i = 0; i < jqueryMap.$thumbnails.children().length; i++){
    //         jqueryMap.$thumbnails.children('#' + i).width(width/3);
    //         jqueryMap.$thumbnails.children('#' + i).height(width/3);
    //     }
    // }

    // function escapeString(s){
    //     return s.split(' ').join('%2C');
    // }

    function displayElements(elements){
        for(var i=0; i < elements.length; i++){
            elements[i].style.visibility='visible';
        }
    }

    function hideElements(elements){
        for(var i=0; i < elements.length; i++){
            elements[i].style.visibility='hidden';
        }
    }

    // function resetBorderColor(elements){
    //     for(var i=0; i < elements.length; i++){
    //         $(elements[i]).removeClass("selected");
    //         $(elements[i]).css('borderColor', '#ddd');
    //     }
    // }

    // function displayImages(data){
    //     displayElements(jqueryMap.$thumbnails.children());
    // }
    //----------------- BEGIN DOM METHODS -----------------------
}(); 