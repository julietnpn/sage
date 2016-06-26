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
        jqueryMap.$commonName.blur(function(){
            validateNames();
        });

        jqueryMap.$latinName.blur(function () {
            validateNames();
        });

        jqueryMap.$commonName.keydown(function(e){
            if(e.keyCode == 13 && validateNames() != 2){
                e.preventDefault();
                e.stopPropagation();
                return;
            }
        });

        jqueryMap.$latinName.keydown(function(e){
            if(e.keyCode == 13 && validateNames() != 2)
                e.preventDefault();
                e.stopPropagation();
                return;
        });


        jqueryMap.$clearAddPlant.click(function(){
            jqueryMap.$latinName.val("");
            jqueryMap.$commonName.val("");
            hideElements(jqueryMap.$clearAddPlant);
            hideElements(jqueryMap.$addThis.children());
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

        return isValidated;
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

    //----------------- BEGIN DOM METHODS -----------------------
}(); 