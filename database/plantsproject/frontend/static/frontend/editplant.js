var EditPlant = function(){
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

        jqueryMap.$attribute.click(function(){
            var attribute = $(this).attr('id')
            var isMulti = attribute == 'ActiveGrowthPeriod';
            var $select;
            if(isMulti){
                $('#mdl-form').html('<label id="mdl-label" for="mdl-select2-multi"></label><select class="js-example-basic-multiple" multiple="multiple" id="mdl-select2-multi"></select>');
                $select = $('#mdl-select2-multi');
            }
            else{
                $('#mdl-form').html('<label id="mdl-label" for="mdl-select2"></label><select class="js-example-basic-single" id="mdl-select2" ></select>');
                $select = $('#mdl-select2');
            }

            $select.html("");
            $select.select2({
                placeholder: "Loading..."
            });


            $.ajax({ // make the request for the selected data object
                type: "GET",
                //data: dataToSend,
                url:"/home/getValues/" + attribute + "/" + $(this).next().text().replace(","," "),
                dataType:"json"
            }).then(function (data) {
                options = data.dropdownvals
                for(var i=0;i < options.length; i++){
                    //if(options[i].id == data.defaultId)
                    if(data.defaultIds.indexOf(options[i].id) > -1)
                        $select.append("<option selected value='" + options[i].text + "'' id='" + options[i].id + "'>"+options[i].text+"</option>")
                    else
                        $select.append("<option value='" + options[i].text + "'' id='" + options[i].id + "'>"+options[i].text+"</option>")
                }

                $select.trigger('change');
            });

            jqueryMap.$modal.modal();
            $('#mdl-label').html($(this).text());


        });
    }

    return pub;
    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------

        
    function setJqueryMap() {
        jqueryMap = {
        	$attribute : $(".edit-attribute"),
            $value : $(".col-xs-8"),
            $modal : $("#editAttributeModal")
        };
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

    // function displayElements(elements){
    //     for(var i=0; i < elements.length; i++){
    //         elements[i].style.visibility='visible';
    //     }
    // }

    // function hideElements(elements){
    //     for(var i=0; i < elements.length; i++){
    //         elements[i].style.visibility='hidden';
    //     }
    // }

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