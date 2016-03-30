
$("#search-magnifying-glass").on('click', function(){
	searchValue = $("#searchbar").val();
	alert("Searching for " + searchValue)

	$(this).closest(".modal-content").find("form").submit();
});