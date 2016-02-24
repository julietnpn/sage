$('#searchbar').on('keypress', function(){
	if(keycode == '13')
		alert("search me");
});

$("#search-magnifying-glass").on('click', function(){
	searchValue = $(this).siblings("#searchbar").value;
	$("#searchbar :selected").val();
	$("#searchbar :selected").text();
	alert(searchValue);
});