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
            alert(jqueryMap.$latinName.val());
        });
    	
    }

    return pub;
    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------
    function setJqueryMap() {
        jqueryMap = {
        	$latinName : $("#add-plant-latin-name"),
        	$commonName : $("#add-plant-common-name"),
        	$addThis: $("#add-plant-go"),
        	$sidebarSection: $('#sidebar-bottom-content'),
        	$thumbnails:$(".thumbnail")
        };
    }

    function setThumbnailSize(){
    	var width = jqueryMap.$sidebarSection.width() - 81;
    	jqueryMap.$thumbnails.width(width/3);
    	jqueryMap.$thumbnails.height(width/3);
    }

    //----------------- BEGIN DOM METHODS -----------------------
}(); 