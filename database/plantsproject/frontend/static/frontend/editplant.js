var EditPlant = function(){
	//----------------- BEGIN MODULE SCOPE VARIABLES ------------
	var pub = {},
        jqueryMap = {},
        setJqueryMap,
        common_name,
        species,
        genus, 
        variety;
	//----------------- END MODULE SCOPE VARIABLES ------------

	//----------------- BEGIN PUBLIC METHODS --------------------
    pub.init = function(pCommonName, pGenus, pSpecies, pVariety){
    	setJqueryMap();
        common_name = pCommonName;
        genus = pGenus;
        species =pSpecies;
        variety = pVariety;

        //resetNameChangeFlags();

        jqueryMap.$attribute.click(function(){
            clearForms();
            var attribute_className = $(this).attr('data-className');
            var attribute_prop = $(this).attr('id');
            var attribute_displayName = $(this).text();
            var attribute_fieldType = $(this).attr("data-fieldType");
            var defaultVal = $(this).next().text().replace(",", "");

            if(attribute_fieldType == 'other'){
                document.getElementById("mdl-label-text").innerHTML = attribute_displayName;
                $("#new-attribute-text").attr("placeholder", $(this).next().text());

                $("#hidden-className-t").val(attribute_className);
                $("#hidden-propName-t").val(attribute_prop);
                $("#hidden-plantId-t").val(getPlantId());

                $("#updateTextMdl").modal();
                
            }
            else if(attribute_fieldType == 'many_to_many'){
                load_values(true, attribute_className, defaultVal);
                document.getElementById("mdl-label-multi").innerHTML = attribute_displayName

                $("#hidden-className-m").val(attribute_className);
                $("#hidden-propName-m").val(attribute_prop);
                $("#hidden-plantId-m").val(getPlantId());

                $("#updateMultiMdl").modal();
            }
            else {
                document.getElementById("mdl-label-select").innerHTML = attribute_displayName

                load_values(false, attribute_className, defaultVal);
                $("#hidden-className-s").val(attribute_className);
                $("#hidden-propName-s").val(attribute_prop);
                $("#hidden-plantId-s").val(getPlantId());

                $("#updateSelectMdl").modal();
            }
        });

        $('.submitBtn').click(function(){
            var $form = $(this).closest(".modal-content").find("form").submit();
        });

        jqueryMap.$addNewImg.click(function(){
            searchFlickrPictures()
        });

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

        jqueryMap.$name.click(function(){
            $("#hidden-plantId").val(getPlantId());
            $("#input-genus").val($("#genus").text().trim());
            $("#input-species").val($("#species").text().trim());
            $("#input-variety").val($("#variety").text().trim());
            $("#input-commonName").val($("#commonName").text().trim());
            $("#input-family").val($("#family").text().trim());
            $("#input-familyCommonName").val($("#familyCommonName").text().trim());
            var val = $("#endemicStatus").text().trim();
            $('#id_endemicStatus option:selected').removeAttr('selected');
            $("#id_endemicStatus").find('option:contains("'+ val+ '")').attr("selected",true);

            jqueryMap.$updateNamesMdl.modal();
        });

        $("#input-genus").on('keydown', function(){
             $("#genus-flag").val(1);
        });
        $("#input-species").on('keydown', function(){
             $("#species-flag").val(1);
        });
        $("#input-variety").on('keydown', function(){
             $("#variety-flag").val(1);
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
        $("#id_endemicStatus").on('keydown', function(){
             $("#endemicStatus-flag").val(1);
        }); 

        $("#updateTextMdl form").submit(function(e){
            var value = $("#new-attribute-text").val();
            $.post('/frontend/updateText/', $(this).serialize(), function(data){
                var label = $("#mdl-label-text").text();
                var className = $("#hidden-className-t").val();
                var propertyName = $("#hidden-propName-t").val();
                
                $("#updateTextMdl").modal('hide');
                var newRow = '<div class="row">' +
                    '<div class="col-xs-4 italic edit-attribute" id="'+propertyName+'" data-fieldType="other" data-className="'+className+'">'+label+'</div>' +
                    '<div class="col-xs-8 bold">'+value+'</div></div>';

                //GET CATEGORY SOMEHOW

                $('#characteristics-block').find('#' + propertyName).next().remove();
                $('#characteristics-block').find('#' + propertyName).remove();
                $("#characteristics-block").append(newRow);
                $('.undefined-attributes').find('#' + propertyName).remove();
            });
            e.preventDefault();
        });

        $("#updateTextMdl form").submit(function(e){
            var value = $("#new-attribute-text").val();
            $.post('/frontend/updateText/', $(this).serialize(), function(data){
                var label = $("#mdl-label-text").text();
                var className = $("#hidden-className-t").val();
                var propertyName = $("#hidden-propName-t").val();
                
                $("#updateTextMdl").modal('hide');
                var newRow = '<div class="row">' +
                    '<div class="col-xs-4 italic edit-attribute" id="'+propertyName+'" data-fieldType="other" data-className="'+className+'">'+label+'</div>' +
                    '<div class="col-xs-8 bold">'+value+'</div></div>';

                //GET CATEGORY SOMEHOW

                $('#characteristics-block').find('#' + propertyName).next().remove();
                $('#characteristics-block').find('#' + propertyName).remove();
                $("#characteristics-block").append(newRow);
                $('.undefined-attributes').find('#' + propertyName).remove();
            });
            e.preventDefault();
        });

        $("#updateTextMdl form").submit(function(e){
            var value = $("#new-attribute-text").val();
            $.post('/frontend/updateText/', $(this).serialize(), function(data){
                var label = $("#mdl-label-text").text();
                var className = $("#hidden-className-t").val();
                var propertyName = $("#hidden-propName-t").val();
                
                $("#updateTextMdl").modal('hide');
                var newRow = '<div class="row">' +
                    '<div class="col-xs-4 italic edit-attribute" id="'+propertyName+'" data-fieldType="other" data-className="'+className+'">'+label+'</div>' +
                    '<div class="col-xs-8 bold">'+value+'</div></div>';

                //GET CATEGORY SOMEHOW

                $('#characteristics-block').find('#' + propertyName).next().remove();
                $('#characteristics-block').find('#' + propertyName).remove();
                $("#characteristics-block").append(newRow);
                $('.undefined-attributes').find('#' + propertyName).remove();
            });
            e.preventDefault();
        });

        $("#updateTextMdl form").submit(function(e){
            var value = $("#new-attribute-text").val();
            $.post('/frontend/updateText/', $(this).serialize(), function(data){
                var label = $("#mdl-label-text").text();
                var className = $("#hidden-className-t").val();
                var propertyName = $("#hidden-propName-t").val();
                
                $("#updateTextMdl").modal('hide');
                var newRow = '<div class="row">' +
                    '<div class="col-xs-4 italic edit-attribute" id="'+propertyName+'" data-fieldType="other" data-className="'+className+'">'+label+'</div>' +
                    '<div class="col-xs-8 bold">'+value+'</div></div>';

                //GET CATEGORY SOMEHOW

                $('#characteristics-block').find('#' + propertyName).next().remove();
                $('#characteristics-block').find('#' + propertyName).remove();
                $("#characteristics-block").append(newRow);
                $('.undefined-attributes').find('#' + propertyName).remove();
            });
            e.preventDefault();
        });
    }
    return pub;

    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------

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
            $name : $(".name"),
            $updateNamesMdl : $("#updateNamesMdl")
        };
    }

    function searchFlickrPictures(){
        var searchString;
        if(typeof common_name === "undefined")
            searchString = escapeString(common_name);
        else
            searchString = escapeString(genus) + "%2C" + escapeString(species);
        var url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=0dde4e72b0091627e13df41e631b85ec&tags="
                    +searchString+"&safe_search=1&per_page=3";
        var src;
        $.getJSON(url + "&format=json&nojsoncallback=1", function(data){
            jqueryMap.$imgMdlContent.html("");
            $.each(data.photos.photo, function(i,item){
                src = "http://farm"+ item.farm +".static.flickr.com/"+ item.server +"/"+ item.id +"_"+ item.secret +"_m.jpg";
                $("<img />").attr("src", src).addClass('cardimg').appendTo(jqueryMap.$imgMdlContent);
            });
            jqueryMap.$addImgModal.modal();
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
                        $select.append("<option selected value='" + dictionary.id + "''>"+dictionary.text+"</option>")
                    else
                        $select.append("<option value='" + dictionary.id + "''>"+dictionary.text+"</option>")
                }
                $select.select2();
            },
            error: function(xhr, status, error) 
            {
                alert("Error. Could not load values for " + className);
            }
        });
    }

    function resetBorderColor(elements){
        for(var i=0; i < elements.length; i++){
            $(elements[i]).removeClass("selected");
            $(elements[i]).css('borderColor', '#ddd');
        }
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