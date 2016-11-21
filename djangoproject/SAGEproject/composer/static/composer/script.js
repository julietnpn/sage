$(document).ready(function(){
	$("#time-box-button").click(function(){
		console.log("test");
		$(".time-box").append('<div class="row add-margin-top-sm">\
			<div class="col-xs-4 col-xs-offset-4 text-center form-inline">\
				<select class="form-control" name="time-number" value="Time Amount">\
					<option value="" disabled selected>Amount</option>\
					<option value="1">1 hour</option>\
					<option value="2">2 hours</option>\
					<option value="3">3 hours</option>\
					<option value="4">4 hours</option>\
					<option value="5">5 hours</option>\
					<option value="6">6 hours</option>\
					<option value="7">7 hours</option>\
					<option value="8">8 hours</option>\
					<option value="9">9 hours</option>\
					<option value="10">10 hours</option>\
				</select>\
				<span>per</span>\
				<select class="form-control" name="time-number" value="Time Unit">\
					<option value="" disabled selected>Unit</option>\
					<option value="1">day</option>\
					<option value="2">week</option>\
					<option value="3">month</option>\
				</select>\
			</div>\
		</div>');
	});

	$("#to-goalchart-button").click(function(){
		var productsSerialzed = $("#products-form").serialize();
		var servicesSerialzed = $("#services-form").serialize();
		var wildlifeSerialzed = $("#wildlife-form").serialize();
		var ecosystemSerialzed = $("#ecosystem-form").serialize();
		$.post("/composer/", productsSerialzed);
		$.post("/composer/", servicesSerialzed);
		$.post("/composer/", wildlifeSerialzed);
		$.post("/composer/", ecosystemSerialzed);
	});

	// $("#to-constraints-button").click(function(){
	// 	var productsSerialzed = $("#time-form").serialize();
	// 	$.post("/composer/", productsSerialzed);
	// 	$.post("/composer/", servicesSerialzed);
	// 	$.post("/composer/", wildlifeSerialzed);
	// 	$.post("/composer/", ecosystemSerialzed);
	// });

});
