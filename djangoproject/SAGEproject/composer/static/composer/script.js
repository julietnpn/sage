$(document).ready(function(){
	$("#time-box-button").click(function(){
		$("#time-box").append('<div class="row">\
				<div class="col-xs-4 col-xs-offset-4 form-inline">\
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
			</div>\
		');
	});
});
