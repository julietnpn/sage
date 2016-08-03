

var EditPlant = function(){
	//----------------- BEGIN MODULE SCOPE VARIABLES ------------
	var pub = {},
        jqueryMap = {},
        //setJqueryMap,
        transactionId,
        userId,
        filters = [];
        //isNew;
	//----------------- END MODULE SCOPE VARIABLES --------------

	//----------------- BEGIN PUBLIC METHODS --------------------
    //pub.init = function(pCommonName, pGenus, pSpecies, pVariety, transactionId, userId){
    pub.init = function(pCommonName, pScientificName, transactionId, userId){
        setUserId(userId);
    	setJqueryMap();
        transactionId = transactionId == "None" ? 0 : transactionId;
        common_name = pCommonName;
        scientific_name = pScientiicName;
        resetUpdateAttributeModal();


        // -----------------------------------------------------------------------
        // Hide the undefined attribute blocks if all are defined in that category
        if(checkIfEmpty($("#characteristics-undefined"))){
            $("#characteristics-undefined").parent().hide();
        }
        if(checkIfEmpty($("#needs-undefined"))){
            $("#needs-undefined").parent().hide();
        }
        if(checkIfEmpty($("#tolerances-undefined"))){
            $("#tolerances-undefined").parent().hide();
        }
        if(checkIfEmpty($("#behaviors-undefined"))){
            $("#behaviors-undefined").parent().hide();
        }
        if(checkIfEmpty($("#products-undefined"))){
            $("#products-undefined").parent().hide();
        }
        // ----------------------------------------------------------------------


        // ----------------------- BEGIN JQUERY LISTENERS -----------------------
        // jQuery Event: Mouse enters plant names (common name, latin name, family, etc.) 
        // Reslting Action Summary: Display "click to edit"
        jqueryMap.$plantNames.mouseenter(function(e){
            $("#clicktoedit").show()
        });

        // jQuery Event: Mouse leaves (common name, latin name, family, etc.)
        // Reslting Action Summary: Hide "click to edit"
        jqueryMap.$plantNames.mouseleave(function(e){
            $("#clicktoedit").hide()
        });

        // jQuery Event: Plant Names (common name, latin name, family, etc.) are clicked
        // Reslting Action Summary: Display modal to edit plant names
        jqueryMap.$plantNames.click(function(e){
            if (userId < 1){
                userNotAuthenticated();
                e.stopPropagation();
                return;
            }
            resetNameChangeFlags();
            $("#hidden-plantId-names").val(getPlantId());
            $("#transaction-id").val(transactionId);
            $("#input-scientificName").val($("#scientificName").text().trim());
            $("#input-commonName").val($("#commonName").text().trim());
            var val = $("#family").text().trim();
            if(val != ""){
                $("#id_family").find('option:contains("'+ val+ '")').attr("selected",true);
            }
            val = $("#familyCommonName").text().trim();
            if(val != ""){
                $("#id_familyCommonName").find('option:contains("'+ val+ '")').attr("selected",true);
            }
            val = $("#endemicStatus").text().trim();
            if(val != ""){
                $("#id_endemicStatus").find('option:contains("'+ val+ '")').attr("selected",true);
                $("#endemicStatus-text").val(val);
            }

            $("#id_family").select2({tags:true});
            $("#id_familyCommonName").select2({tags:true});
            $("#id_endemicStatus").select2();

            jqueryMap.$updateNamesMdl.modal();

            jqueryMap.$updateNamesMdl.on('keypress', function(e){
                var keycode = (event.keyCode ? event.keyCode : event.which);
                if(keycode == '13'){
                    $("#updateNames-submit").trigger('click');
                }
            });
        });

        // jQuery Event: A plant attribute is clicked (whether defined already or not)
        // Reslting Action Summary: Display modal for filling in attribute value
        $(document).on('click', '.edit-attribute', function(){
            if (userId < 1){
                userNotAuthenticated();
                return;
            }
            clearForms();
            $("#id_select").find('option').remove();

            var isNewAttribute = $(this).attr("data-isNewAttribute");
            if(isNewAttribute == "1"){
                $(".rmvBtn").hide();
            }
            else{
                $(".rmvBtn").show();
            }

            // $(this) == the attribute that was clicked
            var attribute_prop = $(this).attr('id');
            var attribute_className = $(this).attr('data-className');
            var attribute_displayName = $(this).text();
            var attribute_fieldType = $(this).attr("data-fieldType");
            var defaultVal = $(this).next().text().split(", ");

            $("#hidden-dataType").val(attribute_fieldType); //other, many_to_many, many_to_one
            $("#hidden-transactionId").val(transactionId);

            jqueryMap.$attributeLabel.html(attribute_displayName);
            jqueryMap.$attributeLabel.attr("data-block", $(this).attr("data-block"));
            jqueryMap.$attributeLabel.attr("data-isNewAttribute", $(this).attr("data-isNewAttribute"));
            $("#hidden-className").val(attribute_className);
            jqueryMap.$attributePropName.val(attribute_prop);
            $("#hidden-plantId").val(getPlantId());

            if(attribute_fieldType == 'other'){
                $("#id_text").show();
                // if($("#id_select").data('select2'))
                //     $("#id_select").select2('destroy');
                // $("#id_select").hide();
                // if($("#id_multi").data('select2'))
                //     $("#id_multi").select2('destroy');
                // $("#id_multi").hide(); 
                $("#id_text").attr("placeholder", $(this).next().text());                
            }
            else if(attribute_fieldType == 'many_to_many'){
                
                load_values(true, attribute_className, defaultVal);

                // $("#id_text").hide();
                // $("#id_select").hide();
                // if($("#id_select").data('select2'))
                //     $("#id_select").select2('destroy');
                $("#id_multi").show(); 

            }
            else {
                load_values(false, attribute_className, defaultVal);
                // $("#id_text").hide();
                $("#id_select").show();
                // if($("#id_multi").data('select2'))
                //     $("#id_multi").select2('destroy');
                // $("#id_multi").hide(); 

                

            }
            
            $("#updateAttributeMdl").modal();
        });

        // jQuery Event: Plant Names (common name, latin name, family, etc.) are hovered
        // Reslting Action Summary: Display "click to edit"
        $('.submitBtn').click(function(){ //not update names
            if (userId < 1){
                 userNotAuthenticated();
                return;
            }
            var $form = $(this).closest(".modal-content").find("form").submit(); //need var? // use jquery map here
        });

        $('.rmvBtn').click(function(){ //not update names
            if (userId < 1){
                userNotAuthenticated();
                return;
            }

            $.post('/removeAttribute/', $("#updateAttributeMdl form").serialize(), function(data){
                var property = $("#hidden-propName").val();

                $property = $("#" + property);
                $property.attr("data-isNewAttribute", 1);
                $property.attr("data-block", jqueryMap.$attributeLabel.attr("data-block"));
                $property.removeClass("col-xs-4");
                $property.addClass("col-xs-10")
                $val = $("#" + property).next();
                $val.html("undefined");
                $val.css("visibility", "hidden");
                $val.removeClass("col-xs-8");
                $val.addClass("col-xs-2");
                $row = $("#" + property).parent();


                $row.remove();
                var $block = $("#" + jqueryMap.$attributeLabel.attr("data-block") + "-undefined");
                $block.parent().show();
                $row.appendTo($block);

            })
            .fail(function(){
                alert("Fail");
            });
        });

        // Submits general plant information form when modal button is clicked
        $("#updateNames-submit").on("click", function(){
            if (userId < 1){
                userNotAuthenticated();
                return;
            }

            $.post('/updateNames/', $("#updateNamesMdl form").serialize(), function(data){
                //alert($("#genus-flag").val());
                //alert($("#species-flag").val()); //RESET FLAGS??????????????????????????????!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                $("#scientificName").html($("#input-scientificName").val());
                // if($("#genus-flag").val() == "1"){
                //     $("#commonName").
                // }
                $("#commonName").html($("#input-commonName").val());
                //$("#familyCommonName").html($("#input-familyCommonName").val());
                //$("#family").html($("#input-family").val());
                var family = $("#id_family option:selected").text();
                if($("#id_family option:selected").text().indexOf("--") < 0){
                    $("#family").html( $("#id_family option:selected").text());
                    //$("#family").show();
                }
                if($("#id_familyCommonName option:selected").text().indexOf("--") < 0){
                    $("#familyCommonName").html( $("#id_familyCommonName option:selected").text());
                    //$("#familyCommonName").show();
                }
                if($("#id_endemicStatus option:selected").text().indexOf("--") < 0){
                    $("#endemicStatus").html( $("#id_endemicStatus option:selected").text());
                    $("#endemicStatusWrapper").show();
                }
                $("#updateNamesMdl").modal("hide");
                displayMessage();
            })
            .fail(function(){
                alert("Error - Could not update names.");
            });
        });

        // Opens modal and displays flickr image options
        jqueryMap.$addNewImg.click(function(){
            if (userId < 1){
                userNotAuthenticated();
                return;
            }
            searchFlickrPictures(generateSearchString());
        });

        // Changes CSS on images displayed in the modal
        jqueryMap.$imgMdlContent.on({ //these arent visible enough
            click: function(){
                resetBorderColor($(this).siblings());
                $(this).css('border-color', '#66CD00');
                $(this).addClass('selected');
            },
            mouseenter: function(){
                $(this).css('border-color', '#66CD00');
            },
            mouseleave: function(){
                if(!$(this).hasClass('selected'))
                $(this).css('border-color', '#ddd');
            }
        }, '.modalimg');


        $("#input-scientificName").on('keydown', function(){
             $("#scientificName-flag").val(1);
        });
        $("#input-commonName").on('keydown', function(){
             $("#commonName-flag").val(1);
        });
        $("#id_family").on('change', function(){
             $("#family-flag").val(1);
        });
        $("#id_familyCommonName").on('change', function(){
             $("#familyCommonName-flag").val(1);
        });
        $("#id_endemicStatus").on('change', function(){
            $("#endemicStatus-text").val( $("#id_endemicStatus option:selected").text());
            $("#endemicStatus-flag").val(1);
        }); 

        $("#updateAttributeMdl form").submit(function(e){
            if (userId < 1){
                userNotAuthenticated();
                return;
            }
            
            var dataType = $("#hidden-dataType").val();
            var isNewAttribute = jqueryMap.$attributeLabel.attr("data-isNewAttribute");
            if(dataType === "other"){
                var value = $("#id_text").val();
                var url = '/updateText/' + transactionId + "/";
                url += isNewAttribute == "1" ? "INSERT/" : "UPDATE/";
            }
            else if(dataType == "many_to_many"){
                //alert("This is multi TEST");

                var selections = $('#id_multi').select2('data');
                var value = selections[0].text;
                for(var i = 1; i < selections.length; i++){
                    value += ", " + selections[i].text;
                }
                var url = '/updateMulti/' + transactionId + "/";
                url += isNewAttribute == "1" ? "INSERT/" : "UPDATE/";
            }
            else{
                //alert("This is select");
                var value = $('#id_select').select2('data')[0].text;
                var url = '/updateSelect/' + transactionId + "/";
                url += isNewAttribute == "1" ? "INSERT/" : "UPDATE/";
            }

            //alert("Posting " + url);
            $.post(url, $(this).serialize(), function(data){
                var label = jqueryMap.$attributeLabel.text()
                var className = $("#hidden-className").val();
                var propertyName = jqueryMap.$attributePropName.val();

                $("#updateAttributeMdl").modal('hide');

                resetUpdateAttributeModal();


                if(isNewAttribute == "1" ){
                    var $newRow = $("<div>")
                    $newRow.addClass("row");
                    var $attributeName = $('<div>');
                    $attributeName
                        .addClass("col-xs-4 italic edit-attribute")
                        .attr("id", propertyName)
                        .attr("data-fieldType", dataType)
                        .attr("data-className", className)
                        .attr("data-block", jqueryMap.$attributeLabel.attr("data-block"))
                        .attr("data-isNewAttribute", 0)
                        .html(label)
                        .appendTo($newRow);
                    var $attributeVal = $('<div>');
                    $attributeVal.addClass("col-xs-8 bold").html(value).appendTo($newRow);

                    var block = "#" + jqueryMap.$attributeLabel.attr("data-block") + "-defined";
                    

                    $(block).find('#' + propertyName).next().remove();
                    $(block).find('#' + propertyName).remove();

                    $newRow.appendTo($(block));
                    $('.undefined-attributes').find('#' + propertyName).parent().remove();


                    var block2 = "#" + jqueryMap.$attributeLabel.attr("data-block") + "-undefined";
                    if(checkIfEmpty($(block2))){
                        $(block2).parent().hide();
                    }


                }
                else{
                    $("#" + propertyName).next().text(value);
                }

                transactionId = data;
                displayMessage();
            })
            .fail(function(data){
                transactionId = data;
            });
            e.preventDefault();
        });


        jqueryMap.$chooseImg.on("click", function(){
            if (userId < 1){
                userNotAuthenticated();
                return;
            }
            url = jqueryMap.$addImgModal.find(".selected").attr("src");

            $("#hidden-plantId-img").val(getPlantId());
            $("#hidden-url-img").val(url);

            $.post('/addImg/', $("#addImg form").serialize(), function(data){
                $("<img />").attr("src", url)
                    .addClass('cardimg')
                    .attr('id', 'imagelightbox')
                    .appendTo($("#populated-images"));
                jqueryMap.$addImgModal.modal('hide');
                displayMessage();

                if($("#populated-images").children().length >= 5){
                    $("#add-new-img").remove();
                }
            })
            .fail(function(){
                alert("Error - Could not add image.");
            });
        });

        $("#flickrSearchBtn").click(function(){
            searchFlickrPictures($("#flickrSearchText").val());
            updateImgModalMessage($("#flickrSearchText").val());
        });

        $("#flickrSearchText").on("keypress", function(){
            $("#flickrSearchBtn").show();
        });

        // ----------------------- END JQUERY LISTENERS -----------------------

    }
    return pub;

    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------

    function setFlag($flag){
        $flag.val(1);
    }

    function resetNameChangeFlags(){
        $("#scientificName-flag").val(0);
        $("#commonName-flag").val(0);
        $("#family-flag").val(0);
        $("#familyCommonName-flag").val(0);
        $("#endemicStatus-flag").val(0);
     }

    function setUserId(id){
        userId = id;
    }

    function setJqueryMap() {
        jqueryMap = {
        	$attribute : $(".edit-attribute"),
            $addNewImg : $('#add-new-img'),
            $addImgModal : $('#addImg'),
            $imgMdlContent : $("#img-mdl-content"),
            $plantNames : $(".name"),
            $updateNamesMdl : $("#updateNamesMdl"),
            $chooseImg : $("#choose-img"),
            $attributeLabel : $('#mdl-label'),
            $attributePropName : $('#hidden-propName')
        };
    }

    function generateSearchString(){
        var searchString = "";
        var searchStringDisplay = "";

        if(common_name != "None"){
            searchString = escapeString(common_name);
            searchStringDisplay = common_name;
        }
        // if(genus != "None"){
        //     searchString += searchString.length > 0 ? "," + escapeString(genus) : escapeString(genus);
        //     searchStringDisplay += searchStringDisplay.length > 0 ? " " + genus : genus;
        // }
        // if(species != "None"){
        //     searchString += searchString.length > 0 ? "," + escapeString(species) : escapeString(species);
        //     searchStringDisplay += searchStringDisplay.length > 0 ? " " + species : species;
        // }

        //alert(searchString + "\n" + searchStringDisplay + "\n" + searchStringDisplay.split(" ").join(","));

        //searchFlickrPictures(searchString, searchStringDisplay);

        return searchStringDisplay;
    }

    function searchFlickrPictures(searchStringDisplay){
        var pageNumber = 1;
    
        
        $(".back").hide();
        loadNewImages(searchStringDisplay, pageNumber);
        jqueryMap.$addImgModal.modal();

        
    }

    function updateImgModalMessage(searchString){
        $("#addImg-tag").html(searchString);
    }

    function loadNewImages(searchString, pageNumber){
        updateImgModalMessage(searchString);

        var escapedString = escapeString(searchString)
        var url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=0dde4e72b0091627e13df41e631b85ec&tags="
                    +escapedString+"&safe_search=1&per_page=3&page=" + pageNumber+ "&format=json&nojsoncallback=1";
        var src;
        $.getJSON(url, function(data){
            jqueryMap.$imgMdlContent.html("");
            $.each(data.photos.photo, function(i,item){
                src = "http://farm"+ item.farm +".static.flickr.com/"+ item.server +"/"+ item.id +"_"+ item.secret +"_m.jpg";
                $("<img />").attr("src", src).addClass('modalimg').appendTo(jqueryMap.$imgMdlContent);
            });

            $("#flickrSearchBtn").hide();
            $("#flickrSearchText").val("");


            $(".forward").off("click").on("click", function(e){
                loadNewImages(searchString, ++pageNumber);
                $(".back").show();
                e.stopPropagation();
            });

            $(".back").off("click").on("click", function(e){
                if(pageNumber == 1){
                    return;
                }
                else{
                    loadNewImages(searchString, --pageNumber);
                    if(pageNumber == 1)
                        $(".back").hide();
                }
                e.stopPropagation();
            });
        });
    }


    function load_values(isMultiSelect, className, defaultValArray){
        var $select
        if(isMultiSelect){
            $("#id_multi").addClass("js-example-basic-multiple");
            $select = $("#id_multi")
        }
        else{
            $("#id_select").addClass("js-example-basic-single");
            $select = $("#id_select")
        }
        $select.empty();
        $.ajax({
            type: 'GET',
            url: "/reload_controls/" + className,
            data:{'defaultVals[]': defaultValArray},
            dataType: 'json',
            contentType: 'json',
            success: function(result)
            {
                $("#hidden-oldVals-m").val(result.defaultIds);
                // $select.empty();
                for(var i = 0; i < result.dropdownvals.length; i++){
                    var dictionary = result.dropdownvals[i]
                    if(result.defaultIds.indexOf(dictionary.id) > -1)
                        $select.append("<option selected value='" + dictionary.id + "'>"+dictionary.text+"</option>")
                    else
                        $select.append("<option value='" + dictionary.id + "'>"+dictionary.text+"</option>")
                }
                $select.select2();
            },
            error: function(xhr, status, error) 
            {
                alert("Error. Could not load values for " + className);
            }
        });
    }

    function displayMessage(){
        $("#alert").fadeIn(2000).delay(5000).fadeOut(400)
    }

    function resetBorderColor(elements){
        for(var i=0; i < elements.length; i++){
            $(elements[i]).removeClass("selected");
            $(elements[i]).css('borderColor', '#ddd');
        }
    }

    function userNotAuthenticated(){
        alert("Please log in before editing plant attributes.");
    }

    function escapeString(s){
        return s.split(' ').join('%2C');
    }

    function getPlantId(){
        return $("#hiddenPlantId").text();
    }

    function clearForms(){
        $('form').find("input[type=text], input[type=select]").val("");
    }

    function checkIfEmpty($div){
        if($div.children().length <= 0)
            return true;
        else
            return false;
    }

    function resetUpdateAttributeModal(){
        if($("#id_select").data('select2'))
            $("#id_select").select2('destroy');
        if($("#id_multi").data('select2'))
            $("#id_multi").select2('destroy');
        $("#id_text").hide();
        $("#id_select").hide();
        $("#id_multi").hide();
    }

    //----------------- END DOM METHODS -----------------------
}(); 