var Filter = function(){
	//----------------- BEGIN MODULE SCOPE VARIABLES ------------
	var pub = {},
        jqueryMap,
        filters;
	//----------------- END MODULE SCOPE VARIABLES --------------

	//----------------- BEGIN PUBLIC METHODS --------------------
    pub.init = function(){
    	setJqueryMap();
    	//setFilters();

        // ----------------------- BEGIN JQUERY LISTENERS -----------------------
        jqueryMap.$dropdown.on("mouseenter", displayDropdown)

        // jQuery Event: Mouse leaves the dropdown div area
		// Reslting Action Summary: Reset elements and collapse the dropdown menu
		jqueryMap.$dropdown.on("mouseleave", collapseDropdown);

		jqueryMap.$dropdown.on("blur", collapseDropdown);



        // jQuery Event: Item (an <a> element) in a drop down list is clicked
		// Resulting Action Summary: Change the <a> element to a <select> (dropdown) 
		//							 and prepopulate it with plant attributes that fall under that category
		jqueryMap.$dropdownContent.on("click", "a", function(){
			var siblings = $(this).siblings();
			for(var i = 0; i < siblings.length; i++){
				if(siblings[i].nodeName == 'SELECT' || siblings[i].nodeName == 'INPUT')
					resetItem(siblings[i]);
			}
			
			var category = $(this).html(); // Category is a plant-attribute category such as "Characteristics" or "Products"
			var $toBeReplaced = $(this);
			//remove name
			/*if(category == "Name"){
				$toBeReplaced.replaceWith("<input type='text' id='searchByName' class='dropdown-select' placeholder='"+category+"' data-category='"+category+"'></input>");
			}
			else{*/
			    $.ajax({
		        	type: 'GET',
		            url: "/get" + category,
		            dataType: 'json',
		            contentType: 'json',
		            success: function(result)
		            {
		            	$toBeReplaced.replaceWith("<select id='category' class = 'dropdown-select' placeholder='"+category+"' data-category='"+category+"'></select>");
						$("#category").focus();
						$select = $("#category")
						$select.append("<option disabled selected value>Choose a "+ category + "</option>");

		                for(var i = 0; i < result.length; i++){
		                        $select.append("<option data-fieldname='" + result[i].name + "' data-field_type='"+result[i].field_type+"'>"+ result[i].label +"</option>")
		                }
		            }
		        });
			//}
		});

		// jQuery Event: A drop-down option is selected (this is the field the user wants to filter by)
		// Reslting Action Summary: Populate the hidden form values with parameters for the filter
		jqueryMap.$dropdownContent.on("change", "select", function(){
			category = $("#category").attr("data-category")
			$selected = $("#category").find(":selected")

		 	$("#filter_field_label").val($selected.val());
		   	$("#filter_field").val($selected.attr("data-fieldname"));
		   	$("#filter_field_type").val($selected.attr("data-field_type"));

		   	//addFilter($selected.val(), $selected.attr("data-fieldname"), $selected.attr("data-field_type"), -1)
		   	$("#category").replaceWith("<input type='text' id='filtertextfield' data-category='"+category+"'  class='dropdown-select' placeholder='"+ $selected.val() + ' ' + "'></input>");
		   	$("#filtertextfield").focus();
		});

		// jQuery Event: A text box is typed in (this is the value that the user is filtering for)
		// Reslting Action Summary: Check if the user presses "enter," if so, populate form field and submit the form
		jqueryMap.$dropdownContent.on("keypress", "#filtertextfield", function(){
			var keycode = (event.keyCode ? event.keyCode : event.which);
		    if(keycode == '13'){
		    	$("#filter_value").val($(this).val());
		    	$("#filter_form").submit();


		    	//filters[filters.length-1][3] = $(this).val();
		    	// $.ajax({
		    	// 	type: 'GET',
		    	// 	url: '/filter/',
		    	// 	//data:{'filters[]':'test'},
		    	// 	contentType: 'json',
		    	// 	dataType: 'json',
		    	// 	success: function(){
		    	// 		alert("success");
		    	// 	},
		    	// 	error: function(){
		    	// 		alert("fail");
		    	// 	}
		    	// });
		    }
		});

		// jQuery Event: A name is typed into the #seasrchByName text box (which is under the filter) and "enter" is pressed
		// Resulting Action Summary: Right now, filtering through a name does the same behavior as searching for the name
		//							We'll use the search form instead 
		jqueryMap.$dropdownContent.on("keypress", "#searchByName", function(){
			var keycode = (event.keyCode ? event.keyCode : event.which);
		    if(keycode == '13'){
		    	$("#searchbar").val($(this).val());
		    	$("#searchform").submit();
		    }	
		});

        // ----------------------- END JQUERY LISTENERS -----------------------

    }
    return pub;

    //----------------- END PUBLIC METHODS --------------------

    //----------------- BEGIN DOM METHODS -----------------------
    function setJqueryMap(){
    	jqueryMap = {
    		$dropdown : $(".dropdown"),
    		$dropdownContent : $(".dropdown-content"),
    		$hoverArea : $(".dropdown", "dropdown-select")
    	};
    }

    // function setFilters(){ //order is important
    // 	filters = new Array();
    // }

    // function addFilter(label, field, type, value){
    // 	filters[filters.length] = new Array(label, field, type, value)
    // }

	// Summary: Transform contentItem to <a> element
	// Parameter: contentItem - an HTML DOM element (presumably select element)
	function resetItem(contentItem){
		var category = $(contentItem).attr("data-category");
		$(contentItem).replaceWith("<a href='#' data-category='"+category+"'>"+category+"</a>")
	}

	function collapseDropdown(){
		jqueryMap.$dropdownContent.css("display", "none");

		var dropdownOptions = jqueryMap.$dropdownContent.children();
		for(var i = 0; i < dropdownOptions.length; i++){
			resetItem(dropdownOptions[i]);
		}
	}

	function displayDropdown(){
		jqueryMap.$dropdownContent.css("display", "block");
	}
    //----------------- END DOM METHODS -----------------------
}(); 