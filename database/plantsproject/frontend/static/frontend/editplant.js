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

        // jqueryMap.$attribute.click(function(){
        //     var attribute_display = $(this).attr('data-className');
        //     var attribute_prop = $(this).attr('id')


        //     var $select;
        //     alert("I'm a " + $(this).attr('data-fieldType') + " field");
        //     if ($(this).attr('data-fieldType') == 'other'){
        //         $('#mdl-label').html($(this).text());
        //         $('#mdl-label').attr("data-propertyName", attribute_prop);
        //         $('#new-attribute-text').attr("placeholder", $(this).next().text());
        //         $('#new-attribute-text').show().siblings().not("#mdl-label").hide();
        //         //jqueryMap.$updateMdlText.modal();
        //         return;
        //     }
        //     else if($(this).attr('data-fieldType') == 'many_to_many'){
        //         $select = $('#new-attribute-multiselect');
        //     }
        //     else { //many_to_one
        //         $select = $('#new-attribute-select');
        //     }

        //     $select.siblings().not("#mdl-label").hide();
        //     $("#mdl-label").attr("data-propertyName", attribute_prop)
        //     $select.html("");
        //     $select.select2({
        //         placeholder: "Loading..."
        //     });

        // });

        jqueryMap.$attribute.click(function(){
            var attribute_className = $(this).attr('data-className');
            var attribute_prop = $(this).attr('id');
            var attribute_displayName = $(this).text();
            var attribute_fieldType = $(this).attr("data-fieldType");
            var defaultVal = $(this).next().text().replace(",", " ");

            if(attribute_fieldType == 'other'){
                $("#text").show();
                $("#select").hide();
                // $("#mutli").hide();
                // $("#multi").next().hide();
                hideElements($("#multi").children());
                $("#mdl-label").html(attribute_displayName);
            }
            else if(attribute_fieldType == 'many_to_many'){
                $("#multi").show().addClass("js-example-basic-multiple");
                $("#select").hide();
                $("#text").hide();
                $("#mdl-label").html(attribute_displayName);
                load_values(true, attribute_className, defaultVal);

            }
            else {
                $("#select").show();
                $("#text").hide();
                $("#mutli").hide();
                $("#multi").next().hide();
                $("#mdl-label").html(attribute_displayName);
                load_values(false, attribute_className, defaultVal);
            }
            
            $('#updateProperty').modal();
        });

        // $('#update-submit').click(function(){
        //     var field = $('#mdl-label').attr('data-propertyName');
        //     //var valueSelect = $('#new-attribute-select').select2("val");
        //     //var valueMultiSelect = $('#new-attribute-multiselect').select2("val");
        //     var valueText = $("#new-attribute-text").val();

        //     alert(field + ' ' + valueText)
        //     $("#mdl-update-form").submit();
           
        // });

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
            // var currentValue = $(this).innerHTML;
            // currentEdit = currentValue;
            // $self.innerHTML = "<input type='text' size='30' style='width:30px; height:20px;' value='" + currentValue + "'></input> ";
            // $self.firstChild.select();
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
            //$addAttribute : $('.add-att-btn'),
            $updateMdlForm : $('#mdl-update-form'),
            $updateMdlText : $("#updatePropertyText"),
            //$addAttributeMdlForm : $('#mdl-add-att-form'),
            //$addNewMdl : $('#addNewAttributeMdl')
            $addAttribute : $('.add-attribute-label'),
            $addNewAttribute : $('.add-new-attribute')
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
            //$("<br><p class='input-label italic'>results from flickr</p>").appendTo('#thumbnail-container');
            //setThumbnailSize();
            //setJqueryMap(); 
        });
    }

    // function setThumbnailSize(){
    // 	var width = jqueryMap.$sidebarSection.width() - 81;
    //     for(var i = 0; i < jqueryMap.$thumbnails.children().length; i++){
    //         jqueryMap.$thumbnails.children('#' + i).width(width/3);
    //         jqueryMap.$thumbnails.children('#' + i).height(width/3);
    //     }
    // }

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
        $select = $("#id_select");
        if(isMultiSelect){
            $select = $("#id_multi")
        }
        $.ajax({
            type: 'GET',
            url: "/home/reload_controls/" + className+ "/" + defaultVal,
            dataType: 'json',
            contentType: 'json',
            //data: {"className":className, "default":""},
            success: function(result)
            {
                 //empty month drop down list
                $select.empty()

                // //add months with no report
                for(var i = 0; i < result.dropdownvals.length; i++){
                    var dictionary = result.dropdownvals[i]
                    //$('#id_select').append('<option id="'+dictionary.id+'"value="'+dictionary.text+'">'+dictionary.text+'</option>')
                    if(result.defaultIds.indexOf(dictionary.id) > -1)
                        $select.append("<option selected value='" + dictionary.text + "'' id='" + dictionary.id + "'>"+dictionary.text+"</option>")
                    else
                        $select.append("<option value='" + dictionary.text + "'' id='" + dictionary.id + "'>"+dictionary.text+"</option>")
                }
                $select.select2();

            },
            error: function(xhr, status, error) 
            {
                alert("error");
            }
        });
    }




    //----------------- BEGIN DOM METHODS -----------------------


}(); 