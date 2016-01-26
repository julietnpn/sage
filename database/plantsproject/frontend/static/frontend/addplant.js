var AddPlant = function(){
	//----------------- BEGIN MODULE SCOPE VARIABLES ------------
	var pub = {},
        jqueryMap = {},
        setJqueryMap,
        dataMap = {
            descriptionsByProfileId: undefined,
            paramsByProfileId: undefined,
            paramsByParamName: undefined,
            paramNamesByParamId: undefined,
            numResults: 0
        };

	//----------------- END MODULE SCOPE VARIABLES ------------

	//----------------- BEGIN PUBLIC METHODS --------------------
    /// <summary>
    /// Method initializes the release target module.  This method should always be called 
    /// prior to any other public methods since it acts as the constructor.
    /// </summary>
    pub.init = function(){
    	setJqueryMap();

    	setThumbnailSize();

		jqueryMap.$addThis.click(function () {
            //get info from form 
            //send to new page
        });

        jqueryMap.$commonName.blur(function () {
           displayElements(jqueryMap.$thumbnails.children());
           displayElements(jqueryMap.$clearAddPlant);
        });

        jqueryMap.$thumbnailImages.click(function(){
            resetBorderColor($(this).siblings());
            $(this).css('border-color', '#66CD00');
            displayElements(jqueryMap.$addThis.children());
        });


        jqueryMap.$clearAddPlant.click(function(){
            jqueryMap.$latinName.val("");
            jqueryMap.$commonName.val("");
            hideElements(jqueryMap.$thumbnails.children());
            hideElements(jqueryMap.$clearAddPlant);
            hideElements(jqueryMap.$addThis.children());
            resetBorderColor(jqueryMap.$thumbnails.children(".img-thumbnail"));
        });
    	
    }

    return pub;
    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------
    function setJqueryMap() {
        jqueryMap = {
        	$latinName : $("#add-plant-latin-name"),
        	$commonName : $("#add-plant-common-name"),
        	$addThis: $("#add-plant-submit-container"),
        	$sidebarSection: $('#sidebar-bottom-content'),
        	$thumbnailImages:$(".img-thumbnail"),
            $thumbnails:$("#thumbnail-container"),
            $clearAddPlant:$('#sidebar-clear')
        };
    }

    function setThumbnailSize(){
    	var width = jqueryMap.$sidebarSection.width() - 81;
    	jqueryMap.$thumbnailImages.width(width/3);
    	jqueryMap.$thumbnailImages.height(width/3);
    }

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

    function resetBorderColor(elements){
        for(var i=0; i < elements.length; i++){
            $(elements[i]).css('borderColor', '#ddd');
        }
    }

    //----------------- BEGIN DOM METHODS -----------------------
}(); 