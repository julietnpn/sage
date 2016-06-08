$("#search-magnifying-glass").on("click", function(){
	$('#searchform').submit();
});

$("#searchform").submit(function(){
	$("#searchform").attr("action", "/search/" + $("#searchbar").val() + "/");
});