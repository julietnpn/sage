var EditPlant = function(){
	//----------------- BEGIN MODULE SCOPE VARIABLES ------------
	var pub = {},
        jqueryMap = {},
        setJqueryMap,
        transactionId,
        isNew;
        // common_name,
        // species,
        // genus, 
        // variety;
	//----------------- END MODULE SCOPE VARIABLES ------------

	//----------------- BEGIN PUBLIC METHODS --------------------
    pub.init = function(pCommonName, pGenus, pSpecies, pVariety, transactionId, userId){
    	setJqueryMap();
        transactionId = transactionId;
        isNew = transactionId != 0;
        common_name = pCommonName;
        genus = pGenus;
        species =pSpecies;
        variety = pVariety;
        userId = userId;


        // Opens modal to edit the general plant information
        jqueryMap.$plantNames.click(function(e){
            if (userId < 0){
                userNotAuthenticated();
                e.stopPropagation();
                return;
            }
            $("#hidden-plantId").val(getPlantId());
            $("#transaction-id").val(transactionId);
            $("#input-genus").val($("#genus").text().trim());
            $("#input-species").val($("#species").text().trim());
            $("#input-variety").val($("#variety").text().trim());
            $("#input-commonName").val($("#commonName").text().trim());
            $("#input-family").val($("#family").text().trim());
            $("#input-familyCommonName").val($("#familyCommonName").text().trim());
            var val = $("#endemicStatus").text().trim();
            if(val != ""){
                $("#id_endemicStatus").find('option:contains("'+ val+ '")').attr("selected",true);
                $("#endemicStatus-text").val(val);
            }

            jqueryMap.$updateNamesMdl.modal();
        });

        //Opens modal to edit an attribute
        $(document).on('click', '.edit-attribute', function(){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            clearForms();
            var attribute_className = $(this).attr('data-className');
            var attribute_prop = $(this).attr('id');
            var attribute_displayName = $(this).text();
            var attribute_fieldType = $(this).attr("data-fieldType");
            var defaultVal = $(this).next().text().replace(",", "");

            if(attribute_fieldType == 'other'){
                document.getElementById("mdl-label-text").innerHTML = attribute_displayName;
                $("#mdl-label-text").attr("data-block", $(this).attr("data-block"));
                $("#mdl-label-text").attr("data-isNewAttribute", $(this).attr("data-isNewAttribute"));
                $("#new-attribute-text").attr("placeholder", $(this).next().text());

                $("#hidden-className-t").val(attribute_className);
                $("#hidden-propName-t").val(attribute_prop);
                $("#hidden-plantId-t").val(getPlantId());

                $("#updateTextMdl").modal();
                
            }
            else if(attribute_fieldType == 'many_to_many'){
                
                load_values(true, attribute_className, defaultVal);
                document.getElementById("mdl-label-multi").innerHTML = attribute_displayName

                $("#mdl-label-multi").attr("data-block", $(this).attr("data-block"));
                $("#mdl-label-text").attr("data-isNewAttribute", $(this).attr("data-isNewAttribute"));
                $("#hidden-className-m").val(attribute_className);
                $("#hidden-propName-m").val(attribute_prop);
                $("#hidden-plantId-m").val(getPlantId());

                $("#updateMultiMdl").modal();
            }
            else {
                document.getElementById("mdl-label-select").innerHTML = attribute_displayName
                $("#mdl-label-select").attr("data-block", $(this).attr("data-block"));
                $("#mdl-label-text").attr("data-isNewAttribute", $(this).attr("data-isNewAttribute"));
                load_values(false, attribute_className, defaultVal);
                $("#hidden-className-s").val(attribute_className);
                $("#hidden-propName-s").val(attribute_prop);
                $("#hidden-plantId-s").val(getPlantId());

                $("#updateSelectMdl").modal();
            }
        });

        // Submits form when modal save button is pressed.
        $('.submitBtn').click(function(){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            var $form = $(this).closest(".modal-content").find("form").submit();
        });

        // Submits general plant information form when modal button is clicked
        $("#updateNames-submit").on("click", function(){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            $.post('/frontend/updateNames/', $("#updateNamesMdl form").serialize(), function(data){
                $("#genus").html($("#input-genus").val());
                $("#species").html($("#input-species").val());
                $("#variety").html($("#input-variety").val());
                $("#commonName").html($("#input-commonName").val());
                $("#familyCommonName").html($("#input-familyCommonName").val());
                $("#family").html($("#input-family").val());
                if($("#id_endemicStatus option:selected").text().indexOf("--") < 0)
                    $("#endemicStatus").html( $("#id_endemicStatus option:selected").text());
                $("#updateNamesMdl").modal("hide");
                displayMessage();
            })
            .fail(function(){
                alert("Error - Could not update names.");
            });
        });

        // Opens modal and displays flickr image options
        jqueryMap.$addNewImg.click(function(){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            searchFlickrPictures()
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
        }, '.cardimg');


        $("#input-genus").on('keydown', function(){
             $("#genus-flag").val(1);
        });
        $("#input-species").on('keydown', function(){
             $("#species-flag").val(1);
        });
        $("#input-variety").on('keydown', function(){
             //$("#variety-flag").val(1);
             setFlag($("#variety-flag"));
        });
        $("#input-commonName").on('keydown', function(){
             $("#commonName-flag").val(1);
        });
        $("#input-family").on('keydown', function(){
             $("#family-flag").val(1);
        });
        $("#input-familyCommonName").on('keydown', function(){
             $("#familyCommonName-flag").val(1);
        });
        $("#id_endemicStatus").on('change', function(){
            $("#endemicStatus-text").val( $("#id_endemicStatus option:selected").text());
            $("#endemicStatus-flag").val(1);
        }); 


        //I THINK THESE ARE ALL THE SAME WITH DIFFERENT ATTR VALS......
        $("#updateTextMdl form").submit(function(e){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            var value = $("#new-attribute-text").val();
            var isNewAttribute = $("#mdl-label-text").attr("data-isNewAttribute");
            var url = '/frontend/updateText/' + transactionId + "/";
            url += isNewAttribute == "1" ? "INSERT/" : "UPDATE/";


            $.post(url, $(this).serialize(), function(data){
                var label = $("#mdl-label-text").text();
                var className = $("#hidden-className-t").val();
                var propertyName = $("#hidden-propName-t").val();
                
                $("#updateTextMdl").modal('hide');

                if(isNewAttribute == "1" ){
                    var $newRow = $("<div>")
                    $newRow.addClass("row");
                    var $attributeName = $('<div>');
                    $attributeName
                        .addClass("col-xs-4 italic edit-attribute")
                        .attr("id", propertyName)
                        .attr("data-fieldType", "other")
                        .attr("data-className", className)
                        .attr("data-block",$("#mdl-label-text").attr("data-block"))
                        .html(label)
                        .appendTo($newRow);
                    var $attributeVal = $('<div>');
                    $attributeVal.addClass("col-xs-8 bold").html(value).appendTo($newRow);

                    var block = "#" + $("#mdl-label-text").attr("data-block");

                    $(block).find('#' + propertyName).next().remove();
                    $(block).find('#' + propertyName).remove();


                    $newRow.appendTo($(block));
                    $('.undefined-attributes').find('#' + propertyName).remove();
                }
                else{
                    $("#" + propertyName).next().text(value);
                }

                transactionId = data;
                displayMessage();
            });
            e.preventDefault();
        });

        $("#updateSelectMdl form").submit(function(e){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            var isNewAttribute = $("#mdl-label-text").attr("data-isNewAttribute");
            var label = $("#mdl-label-select").text();
            var className = $("#hidden-className-s").val();
            var propertyName = $("#hidden-propName-s").val();
            var value = $('#id_select').select2('data')[0].text;
            var url = '/frontend/updateSelect/' + transactionId + "/";
            url += isNewAttribute == "1" ? "INSERT/" : "UPDATE/";


            $.post(url, $(this).serialize(), function(data){
                
                $("#updateSelectMdl").modal('hide');

                if(isNewAttribute == "1"){
                    var $newRow = $("<div>")
                    $newRow.addClass("row");
                    var $attributeName = $('<div>');
                    $attributeName
                        .addClass("col-xs-4 italic edit-attribute")
                        .attr("id", propertyName)
                        .attr("data-fieldType", "one_to_many")
                        .attr("data-className", className)
                        .attr("data-block",$("#mdl-label-select").attr("data-block"))
                        .html(label)
                        .appendTo($newRow);
                    var $attributeVal = $('<div>');
                    $attributeVal.addClass("col-xs-8 bold").html(value).appendTo($newRow);

                    var block = "#" + $("#mdl-label-select").attr("data-block");

                    $(block).find('#' + propertyName).next().remove();
                    $(block).find('#' + propertyName).remove();
                    $newRow.appendTo($(block));
                    $('.undefined-attributes').find('#' + propertyName).remove();
                }
                else{
                    $("#" + propertyName).next().text(value);
                }

                transactionId = data;
                displayMessage();
            });
            e.preventDefault();
        });


        $("#updateMultiMdl form").submit(function(e){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            var isNewAttribute = $("#mdl-label-text").attr("data-isNewAttribute");
            var label = $("#mdl-label-multi").text();
            var className = $("#hidden-className-m").val();
            var propertyName = $("#hidden-propName-m").val();
            var selections = $('#id_multi').select2('data');
            var value = selections[0].text;
            for(var i = 1; i < selections.length; i++){
                value += ", " + selections[i].text;
            }
            var url = '/frontend/updateMulti/' + transactionId + "/";
            url += isNewAttribute == "1" ? "INSERT/" : "UPDATE/";

            $.post(url, $(this).serialize(), function(data){
                $("#updateMultiMdl").modal('hide');

                if(isNewAttribute == "1"){
                    var $newRow = $("<div>")
                    $newRow.addClass("row");
                    var $attributeName = $('<div>');
                    $attributeName
                        .addClass("col-xs-4 italic edit-attribute")
                        .attr("id", propertyName)
                        .attr("data-fieldType", "many_to_many")
                        .attr("data-className", className)
                        .attr("data-block",$("#mdl-label-select").attr("data-block"))
                        .html(label)
                        .appendTo($newRow);
                    var $attributeVal = $('<div>');
                    $attributeVal.addClass("col-xs-8 bold").html(value).appendTo($newRow);

                    var block = "#" + $("#mdl-label-multi").attr("data-block");

                    $(block).find('#' + propertyName).next().remove();
                    $(block).find('#' + propertyName).remove();
                    $newRow.appendTo($(block));
                    $('.undefined-attributes').find('#' + propertyName).remove();
                }
                else{
                    $("#" + propertyName).next().text(value);
                }

                transactionId = data;
                displayMessage();
            });
            e.preventDefault();
        });

        jqueryMap.$chooseImg.on("click", function(){
            if (userId < 0){
                userNotAuthenticated();
                return;
            }
            url = jqueryMap.$addImgModal.find(".selected").attr("src");

            $("#hidden-plantId-img").val(getPlantId());
            $("#hidden-url-img").val(url);


            $.post('/frontend/addImg/', $("#addImg form").serialize(), function(data){
                $("<img />").attr("src", url).addClass('cardimg').appendTo($("#populated-images"));
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

    }
    return pub;

    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------
    function setFlag($flag){
        $flag.val(1);
    }

    function resetNameChangeFlags(){
        $("#genus-flag").val(0);
        $("#species-flag").val(0);
        $("#variety-flag").val(0);
        $("#commonName-flag").val(0);
        $("#family-flag").val(0);
        $("#familyCommonName-flag").val(0);
        $("#endemicStatus-flag").val(0);
     }

    function setJqueryMap() {
        jqueryMap = {
        	$attribute : $(".edit-attribute"),
            $addNewImg : $('#add-new-img'),
            $addImgModal : $('#addImg'),
            $imgMdlContent : $("#img-mdl-content"),
            $plantNames : $(".name"),
            $updateNamesMdl : $("#updateNamesMdl"),
            $chooseImg : $("#choose-img")
        };
    }

    function searchFlickrPictures(){
        var pageNumber = 1;
        var searchString = "";
        var searchStringDisplay = "";

        if(common_name != "None"){
            searchString = escapeString(common_name);
            searchStringDisplay = common_name;
        }
        if(genus != "None"){
            searchString += searchString.length > 0 ? "," + escapeString(genus) : escapeString(genus);
            searchStringDisplay += searchStringDisplay.length > 0 ? " " + genus : genus;
        }
        if(species != "None"){
            searchString += searchString.length > 0 ? "," + escapeString(species) : escapeString(species);
            searchStringDisplay += searchStringDisplay.length > 0 ? " " + species : species;
        }

        $("#addImg-tag").attr('placeholder', searchStringDisplay);
        $(".back").hide();
        loadNewImages(searchString, pageNumber);
        jqueryMap.$addImgModal.modal();

        jqueryMap.$addImgModal.on("click", ".forward", function(){
            loadNewImages(searchString, ++pageNumber);
            $(".back").show();
        });

        jqueryMap.$addImgModal.on("click", ".back", function(){
            if(pageNumber == 1){
                return;
            }
            else{
                loadNewImages(searchString, --pageNumber);
                if(pageNumber == 1)
                    $(".back").hide();
            }
        });
    }

    function loadNewImages(searchString, pageNumber){
        var url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=0dde4e72b0091627e13df41e631b85ec&tags="
                    +searchString+"&safe_search=1&per_page=3&page=" + pageNumber+ "&format=json&nojsoncallback=1";
        var src;
        $.getJSON(url, function(data){
            jqueryMap.$imgMdlContent.html("");
            $.each(data.photos.photo, function(i,item){
                src = "http://farm"+ item.farm +".static.flickr.com/"+ item.server +"/"+ item.id +"_"+ item.secret +"_m.jpg";
                $("<img />").attr("src", src).addClass('cardimg').appendTo(jqueryMap.$imgMdlContent);
            });
        });
    }

    function load_values(isMultiSelect, className, defaultVal){
        var $select
        if(isMultiSelect){
            $("#id_multi").addClass("js-example-basic-multiple");
            $select = $("#id_multi")
        }
        else{
            $("#id_select").addClass("js-example-basic-single");
            $select = $("#id_select")
        }
        $.ajax({
            type: 'GET',
            url: "/frontend/reload_controls/" + className+ "/" + defaultVal,
            dataType: 'json',
            contentType: 'json',
            success: function(result)
            {
                $("#hidden-oldVals-m").val(result.defaultIds);
                $select.empty();
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
        if(!isNew)
            $("#edit-msg").show(400).delay(5000).hide(400);
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
    //----------------- END DOM METHODS -----------------------
}(); 