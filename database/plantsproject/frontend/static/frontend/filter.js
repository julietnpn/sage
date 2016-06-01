$(".dropdown-content").on("click", "a", function(){
	var siblings = $(this).siblings();
	for(var i = 0; i < siblings.length; i++){
		resetItem(siblings[i]);
	}
	var category = $(this).html();
	var $toBeReplaced = $(this);
	if(category == "Name"){
		$toBeReplaced.replaceWith("<input type='text' id='searchByName' class='dropdown-select' placeholder='"+category+"' data-category='"+category+"'></input>");
	}
	else{
	    $.ajax({
        	type: 'GET',
            url: "/get" + category,
            dataType: 'json',
            contentType: 'json',
            success: function(result)
            {

            	$toBeReplaced.replaceWith("<select id='category' class = 'dropdown-select' placeholder='"+category+"' data-category='"+category+"'></select>");
				//$("#category").focus();
				$select = $("#category")
				$select.append("<option disabled selected value>Choose a "+ category + "</option>");

                for(var i = 0; i < result.length; i++){
                        $select.append("<option data-fieldname='" + result[i].name + "' data-field_type='"+result[i].field_type+"'>"+ result[i].label +"</option>")
                }
                //$select.select2();
            }
        });
	}
});


$(".dropdown-content").on("change", "select", function(){
	category = $("#category").attr("data-category")
	$selected = $("#category").find(":selected")

	$("#filter_field_label").val($selected.val());
   	$("#filter_field").val($selected.attr("data-fieldname"));
   	$("#filter_field_type").val($selected.attr("data-field_type"));
   	$("#category").replaceWith("<input type='text' id='filtertextfield' data-category='"+category+"'  class='dropdown-select' placeholder='"+ $selected.val() + ' ' + "'></input>");
   	$("#filtertextfield").focus();
});

$(".dropdown-content").on("keypress", "#filtertextfield", function(){
	var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
    	$("#filter_value").val($(this).val())
    	$("#filter_form").submit();
    }
});

$(".dropdown-content").on("keypress", "#searchByName", function(){
	//condense this with search.js

	var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
    	$("#searchbar").val($(this).val());
    	$("#searchform").submit();
    }	
});


$(".dropdown").on("mouseleave", function(){
	$(".dropdown").css("display", "inline-block");

	var dropdownOptions = $(".dropdown-content").children();
	for(var i = 0; i < dropdownOptions.length; i++){
		resetItem(dropdownOptions[i]);
	}
});


function resetItem(contentItem){
	var category = $(contentItem).attr("data-category");
	$(contentItem).replaceWith("<a href='#' data-category='"+category+"'>"+category+"</a>")
}

// $(".dropdown-content").on("click", "option", function(){
// 	$(".dropdown").css("display", "block");
// });