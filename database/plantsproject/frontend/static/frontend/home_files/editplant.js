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


        // jqueryMap.$addAttribute.click(function(e){
        //     // e.preventDefault();
        //     // e.stopPropagation();
        //     var attributes = {
        //         'characteristic':[
        //             {'id':0, 'class':'Duration', 'text':'Duration'},
        //             {'id':1, 'class':'ActiveGrowthPeriod', 'text':'Active Growth Period'},
        //             {'id':2, 'class':'ph_min', 'text':'phMin'}
        //             ],
        //         'need':['need'],
        //         'behavior':['behaviors'],
        //         'tolerance':['tolerances'],
        //         'product':['prod']
        //     };
        //     var category = $(this).attr('id');

        //     // ----------------------------------------------------------------------------
        //     var select = $("<select class='add-new-attribute' id='add" + category + "' style='width:90%;height:100%;border:0;outline:none;'/>");
        //     for(i=0; i < attributes[category].length; i++){
        //         //alert(attributes[category][i])
        //         $("<option />",  {value: attributes[category][i].id, text:attributes[category][i].text}).appendTo(select);
        //     }
        //     $(this).replaceWith(select);
        //     //---------------------------------------------------------------------------------
        //     // $(this).html("<select class='js-example-basic-single' id='add-new-attribute'></select>")
        //     // $('#add-new-attribute').select2({
        //     //     placeholder: "Loading...",
        //     //     data:attributes[category]
        //     // });
            
        // });




        jqueryMap.$attribute.click(function(){
            var attribute = $(this).attr('id')
            var isMulti = isMultiSelect(attribute);
            var $select;
            if(isMulti){
                jqueryMap.$updateMdlForm.html('<label id="mdl-label" for="mdl-select2-multi"></label><select class="js-example-basic-multiple" multiple="multiple" id="mdl-select2-multi"></select>');
                $select = $('#mdl-select2-multi');
            }
            else{
                jqueryMap.$updateMdlForm.html('<label id="mdl-label" for="mdl-select2"></label><select class="js-example-basic-single" id="mdl-select2" ></select>');
                $select = $('#mdl-select2');
            }

            $select.html("");
            $select.select2({
                placeholder: "Loading..."
            });


            $.ajax({
                type: "GET",
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

            jqueryMap.$updateMdl.modal();
            $('#mdl-label').html($(this).text());
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
            $updateMdl : $("#updateAttributeModal"),
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

    // function hideElements(elements){
    //     for(var i=0; i < elements.length; i++){
    //         elements[i].style.visibility='hidden';
    //     }
    // }

    function resetBorderColor(elements){
        for(var i=0; i < elements.length; i++){
            $(elements[i]).removeClass("selected");
            $(elements[i]).css('borderColor', '#ddd');
        }
    }

    // function displayImages(data){
    //     displayElements(jqueryMap.$thumbnails.children());
    // }
    //----------------- BEGIN DOM METHODS -----------------------


    function isMultiSelect(attribute){
        return attribute == 'Layer' 
            || attribute == 'ActiveGrowthPeriod'
            || attribute == 'HarvestPeriod'
            || attribute == 'FlowerColor'
            || attribute == 'FoliageColor'
            || attribute == 'FruitColor'
            || attribute == 'PlantInsectAttractorByRegion'
            || attribute == 'PlantInsectRegulatorByRegion'
            || attribute == 'PlantAnimalAttractorByRegion'
            || attribute == 'PlantAnimalRegulatorByRegion'
            || attribute == 'FoodProd'
            || attribute == 'RawMaterialsProd'
            || attribute == 'MedicinalsProd'
            || attribute == 'BioChemicalMaterialProd'
            || attribute == 'CulturalAndAmenityProd'
            || attribute == 'MineralNutrientsProd';
    }

}(); 