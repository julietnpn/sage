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
    /// <summary>
    /// Method initializes the release target module.  This method should always be called 
    /// prior to any other public methods since it acts as the constructor.
    /// </summary>
    pub.init = function(pCommonName, pGenus, pSpecies, pVariety){
    	setJqueryMap();
        common_name = pCommonName;
        genus = pGenus;
        species =pSpecies;
        variety = pVariety;

        jqueryMap.$attribute.click(function(){
            clearForms();
            var attribute_className = $(this).attr('data-className');
            var attribute_prop = $(this).attr('id');
            var attribute_displayName = $(this).text();
            var attribute_fieldType = $(this).attr("data-fieldType");
            var defaultVal = $(this).next().text().replace(",", " ");

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
            var $form = $(this).closest(".modal-content").find("form");
            $form.submit();
        });

        jqueryMap.$addNewImg.click(function(){
            searchFlickrPictures()
        });


        jqueryMap.$imgMdlContent.on({
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


        jqueryMap.$commonTitle.on("click", function(){
            alert("common title clicked");
        });

        jqueryMap.$latinTitle.on("click", function(){
            alert($(this).val());
        });
    }

    return pub;
    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------
    function setJqueryMap() {
        jqueryMap = {
        	$attribute : $(".edit-attribute"),
            $value : $(".col-xs-8"),
            $addNewImg : $('#add-new-img'),
            $addImgModal : $('#addImg'),
            $imgMdlContent : $("#img-mdl-content"),
            $img : $('.cardimg'),
            $imgContainer : $('#plant-images'),
            $latinTitle : $('.latin'),
            $commonTitle : $('.common'),
            $updateMdlForm : $('#mdl-update-form'),
            $updateMdlText : $("#updatePropertyText"),
            $addAttribute : $('.add-attribute-label'),
            $addNewAttribute : $('.add-new-attribute')
        };


    }

    function getPlantId(){
        return $("#hiddenPlantId").text();
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



    function escapeString(s){
        return s.split(' ').join('%2C');
    }

    // function displayElements(elements){
    //     for(var i=0; i < elements.length; i++){
    //         elements[i].style.visibility='visible';
    //     }
    // }

    function hideElements(elements){
        for(var i=0; i < elements.length; i++){
            elements[i].style.visibility='hidden';
        }
    }

    function resetBorderColor(elements){
        for(var i=0; i < elements.length; i++){
            $(elements[i]).removeClass("selected");
            $(elements[i]).css('borderColor', '#ddd');
        }
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
            url: "/home/reload_controls/" + className+ "/" + defaultVal,
            dataType: 'json',
            contentType: 'json',
            //data: {"className":className, "default":""},
            success: function(result)
            {
                $("#hidden-oldVals-m").val(result.defaultIds);
                 //empty month drop down list
                $select.empty()

                // //add months with no report
                for(var i = 0; i < result.dropdownvals.length; i++){
                    var dictionary = result.dropdownvals[i]
                    //alert(dictionary.id + " " + dictionary.text)
                    //$('#id_select').append('<option id="'+dictionary.id+'"value="'+dictionary.text+'">'+dictionary.text+'</option>')
                    if(result.defaultIds.indexOf(dictionary.id) > -1)
                        $select.append("<option selected value='" + dictionary.id + "''>"+dictionary.text+"</option>")
                    else
                        $select.append("<option value='" + dictionary.id + "''>"+dictionary.text+"</option>")
                }

                $select.select2();


            },
            error: function(xhr, status, error) 
            {
                alert("error");
            }
        });
    }

    function clearForms(){
        $('form').find("input[type=text], input[type=select]").val("");
    }



    //----------------- BEGIN DOM METHODS -----------------------


}(); 