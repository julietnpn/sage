function getElementsFromId(parent, id_key)
{
	var propertyArray = new Array();
	children = parent.childNodes;
	for(var i = 0; i < children.length; i++){
		var temp =children[i];
		if(temp.nodeType == 1){
			var id = temp.attributes.getNamedItem("id");
			if(id != undefined){
				if(id.textContent.indexOf(id_key) != -1)
				{
					propertyArray.push(temp);
				}
			}
		
		}
	}
	
	return propertyArray;

}

function DeletePlant(pl_id){
	if (confirm("This plant will be permanently DELETED from the database.")){
		url='db_work.php?action=delete_Plant&vars='+pl_id;
		window.location.replace(url);
	}

}

function UpdatePlant(pl_id){
	if(ProcessImageUploads()){
		var varArray = pl_id+"|"+ProcessPlantInfo()+"|"+ProcessNewPlantData()+"|"+ProcessDeletedPlantData();//also process Deleted Plant Data
		//url= 'db_work.php?action=update_Plant&vars='+varArray;
		url= 'index.php?action=update_Plant&vars='+varArray; //For Debug 
		window.location.replace(url);
		
	}
}

function SubmitPlant(){
	if(ProcessImageUploads()){
		var varArray = ProcessPlantInfo()+"|"+ProcessNewPlantData();
		//url= 'db_work.php?action=add_New_Plant&vars='+varArray;
		url= 'index.php?action=add_New_Plant&vars='+varArray; //For Debug 
		window.location = url;
	}
}

function UploadImages(){
	var uploader = document.getElementById("uploadForm");
	uploader.submit();
	uploader.innerHTML='<input type="hidden" name="MAX_FILE_SIZE" value="30000">Your images have been uploaded.';
	//alert("submitted form");
}

function ProcessImageUploads(){
	var uploadForm = document.getElementById("uploadForm");
	if(getElementsFromId(uploadForm, "iUploader").length >0){
		if(confirm("Would you like to continue without uploading images?"))
			return true;
		else
			return false;
	}
	return true;
}

function ProcessPlantInfo(){
	//add family, endemic status here.
	g_cur = document.getElementById("genus");
	s_cur = document.getElementById("species");
	c_cur = document.getElementById("commonnames");
	
	var plantinfo = new Array( new Array(g_cur.value, g_cur.getAttribute("placeholder"), "genus"), new Array(s_cur.value, s_cur.getAttribute("placeholder"), "species"), new Array(c_cur.value, c_cur.getAttribute("placeholder"), "common_names")); 
	
	var updated = "";
	for(i = 0; i < plantinfo.length; i++){
		if(plantinfo[i][0] != plantinfo [i][1]){
			updated += plantinfo[i][2]+"{"+plantinfo[i][0]+"";
			if(i != plantinfo.length-1)
				updated += "},";
		}
	}
	return updated;
}

function ProcessDeletedPlantData(){
	deletedEntries = "";
	tableArray = new Array("intrinsic", "needs", "products", "behaviors", "images");
	
	for(var t = 0; t < tableArray.length; t++){
		searchString = "DELETE"+tableArray[t];
		pi_properties = "";
		if(t<4)
			pi_properties = getElementsFromId(document.getElementById("plant"+tableArray[t]), searchString);
		else
			pi_properties = getElementsFromId(document.getElementById("saved"+tableArray[t]), searchString);
		if(pi_properties.length > 0){
			
			for(var i = 0; i< pi_properties.length; i++)
			{
				//get the # out of the id, add it to the delete list.
				var divid = pi_properties[i].attributes.getNamedItem("id").textContent;
				var dbid = divid.substring(searchString.length); //
				deletedEntries+= dbid;
			}
			if(i < pi_properties.length-1)
				deletedEntries+=",";
		}	
		deletedEntries+="$$";
	}
	
	return deletedEntries;
}

function ProcessNewPlantData(){

var intrinsic="", needs="", products="", behaviors="";
	
	//Intrinsic Chars 
	pi_properties = getElementsFromId(document.getElementById("plantintrinsic"), "newIntrinsicChar");
	if(pi_properties.length > 0){
		for(var i = 0; i<pi_properties.length; i++){
			var id = pi_properties[i].attributes.getNamedItem("id").textContent;
			var property = document.getElementById(id+"proplist").value;
			intrinsic+= property+"{";
					
			if(property == "height" || property == "spread"){
				var unit = document.getElementById(id+"valueunits").value;
				var val = parseFloat(document.getElementById(id+"valuetext").value);
				if(unit == "inches")
					val *= 2.54;
				else if(unit == "feet")
					val *= 30.48;
				else if(unit == "meters")
					val *= 100;
				intrinsic+=val;
			}else{
				var val = document.getElementById(id+"valuelist").value;
				intrinsic+= val;	
			}
			
			if(i != pi_properties.length-1)
				intrinsic += "},";
		}
	}
	//else
		//intrinsic += ".";
	intrinsic+="$$";
	
	//Needs
	pn_properties = getElementsFromId(document.getElementById("plantneeds"), "newNeed");
	if(pn_properties.length > 0){
		for(var i = 0; i<pn_properties.length; i++){
			var id = pn_properties[i].attributes.getNamedItem("id").textContent;
			var property = document.getElementById(id+"proplist").value;
			needs+=property+"{";
			
			needs+=document.getElementById(id+"valuelist").value;
			
			if(i != pn_properties.length-1)
				needs += "},";
		}
	}
	needs+="$$";
	
	
	//Products
	pp_properties = getElementsFromId(document.getElementById("plantproducts"), "newProduct");
	if(pp_properties.length > 0){
		for(var i = 0; i<pp_properties.length; i++){
			var id = pp_properties[i].attributes.getNamedItem("id").textContent;
			var property = document.getElementById(id+"proplist").value;
			products+=property+"{";
					
			/*var plantpart = document.getElementById(id+"plantpart").value;
			products+=plantpart+"*";
					
			var yield = document.getElementById(id+"yield").value;
			products+=yield+"*";
				
			if(property == "food"){
				products+=document.getElementById(id+"valuelist").value;	
			}else{
				products+=document.getElementById(id+"valuetext").value;
			} */
			
			products +=document.getElementById(id+"valuelist").value;
			
			if(i != pp_properties.length-1)
				products += "},";
		}
	}
	products+="$$";
	
	
	
	//Behaviors
	
	pb_properties = getElementsFromId(document.getElementById("plantbehaviors"), "newBehavior");
	if(pb_properties.length > 0){
		for(var i = 0; i<pb_properties.length; i++){
			var id = pb_properties[i].attributes.getNamedItem("id").textContent;
			var property = document.getElementById(id+"proplist").value;
			behaviors+=property+"{";
			
			var val = document.getElementById(id+"valuelist").value;		
			behaviors+=val;
			if(i != pb_properties.length-1)
				behaviors += "},";
		}
	}
	behaviors+="$$";
	
	var newProperties = intrinsic+needs+products+behaviors;
	
	return newProperties;
	
}

function FunctionalAnalysisSetUp(i_array, n_array, p_array, b_array){
	
	FunctionalAnalysis.intrinsics_lib = i_array;
	FunctionalAnalysis.needs_lib = n_array;
	FunctionalAnalysis.products_lib = p_array;
	FunctionalAnalysis.behaviors_lib = b_array;
	
	//alert(JSON.stringify(FunctionalAnalysis.Need, null, 4));
	
}

 FunctionalAnalysis = {
	intrinsics_lib : {	},
	needs_lib : { },
	products_lib : {	},
	behaviors_lib : {}	
};

function FAToolSetUp($tools){
	//alert("FA Tool SetUp "+JSON.stringify($tools));
	FunctionalAnalysisTools = $tools;
	//alert("FA Tool SetUp "+JSON.stringify(FunctionalAnalysisTools));
}

FunctionalAnalysisTools = {};

function printNewPropertyList(property_data,divID){
		var htcontents = addDeleteProperty(divID) + "    Property: ";
		htcontents += '<select id="'+divID+'proplist" onchange="updateValue(FunctionalAnalysis.'+property_data["name"]+',\''+divID+'proplist\');">';
		
		for (p in property_data) {
			if(p == "name"){
				htcontents+='<option value=""></option>'; //so that you're not forced to choose an option.
			}else{
				htcontents+='<option value="'+p+'">'+p+'</option>'; /* onchange update the value field.*/
			}
		}	
		htcontents+='</select>';
		return htcontents;
	}

function printNewValueList(prop, val, divID){
		var htcontents = "ERROR: PrintNewValueList";
		
		//alert("val is: "+val+"  "+JSON.stringify(prop, null, 4));
		valuelist = prop[val];
		
		
		if(valuelist == "text") //only text box (e.g. building materials)
		{
			htcontents = '<textarea id="'+divID+'text"></textarea>';	
			return htcontents;
		}
		else{
			if(valuelist == "int(8)"){//meaning that the input is open with  a unit type (e.g. temparature).
				htcontents = '<textarea id="'+divID+'text"></textarea>';
				htcontents += '<select id="'+divID+'units">'
				units = new Array("inches", "feet", "centimeters", "meters");
				var i;
				for(i = 0; i <units.length; i++){
					htcontents +='<option>'+units[i]+'</option>';
				}
				htcontents += '</select>';
				return htcontents;
			}
			else{ //meaning that there are predetermined options
				htcontents = '<select id="'+divID+'list">';
				var i;
				for(i = 0; i <valuelist.length; i++){
					htcontents +='<option>'+valuelist[i]+'</option>';
				}
				htcontents += '</select>';
				return htcontents;
			}
		
		}
		
	}
	
function printFATool(tool, divID){
	var t = FunctionalAnalysisTools[tool];
	var htcontents = '<select id="'+divID+tool+'">';
	for(var i=0; i< t.length; i++){
		htcontents += '<option value="'+t[i]+'">'+t[i]+'</option>';
	}
	htcontents += '</select>';
	return htcontents;
}


var inival=500; // Initialise starting element number

function addDeleteProperty(divID)
{
 return "<a onclick='delete_Element(\""+divID+"\")' href='#'> X </a>";
}

function delete_Element(name) {
	element = document.getElementById(name);
	if (element != undefined){
		if(name.indexOf("new") == -1){
			//this is an existing entry in the database.
			element.id = "DELETE"+ element.id;//I have to rename the tag to delete, and then Delete all those that say delete when we move to the next page.
			element.setAttribute("style", "display:none"); //change the style to this div to be strike-thru or hidden?
		}else
			element.parentNode.removeChild(element);
	}
}

// Call this function to add textbox
function addProperty(property_data, divID)
{
//alert(JSON.stringify(property_data, null, 4));
var newArea = add_New_Element("new"+property_data.name,divID, "div");
var htcontents = printNewPropertyList(property_data, newArea);   /* to do: determine if the text area name needs to have the [] or why I did it like that... */
document.getElementById(newArea).innerHTML = htcontents; // You can any other elements in place of 'htcontents' 
return newArea;
}

function addProductProperty(type, divID)
{
	//1. add property
	property = addProperty(type,divID);
	//2. add plant part and yield option
	document.getElementById(property).innerHTML += " Plant Part: " +printFATool("plant part",property)+" Yield: " +printFATool("yield",property);
}



function addValue(prop, divID)
{
	var val = document.getElementById(divID).value;
	var parent = document.getElementById(divID).parentNode;
	var newArea = add_New_Element(parent.id+"value", parent.id, "div");
	document.getElementById(newArea).setAttribute('style', "display:inline");
	
	//2. determine the contents of that class - eg. if its a text area or another option list...
	var htcontents = "";
	htcontents = "Value: "+printNewValueList(prop, val, newArea);
	
	
	/*if(divID.indexOf("behavior") >-1){
		htcontents = "Details: "+printNewValueList(prop, val, newArea);
	}else if(divID.indexOf("product") > -1){
		htcontents = "Value: "+printNewValueList(prop, val, newArea);
		for( p in prop){
			if(p != "property"){
				htcontents +=  p+": "+printNewValueList(prop, p, newArea);
			}
		}
	}else{ htcontents = "Value: "+printNewValueList(prop, val, newArea);}*/
	//3. add that stuff to the value div element
	document.getElementById(newArea).innerHTML += htcontents;
}


function updateValue(prop, divID)
{
	var parent = document.getElementById(divID).parentNode.id;
	// 1. remove current value
	delete_Element(parent+"value");
	// 2. add new value
	addValue(prop, divID);
}

function addImageUploader(){
	var newInputID = add_New_Element("iUploader", "uploadForm", "input");
	var newForm = document.getElementById(newInputID);
	newForm.setAttribute('name', newInputID);
	newForm.setAttribute('type', 'file');
	newForm.setAttribute('accept', 'image/*');
	newForm.parentNode.appendChild(document.createElement("br"));
}


function add_New_Element(type, parentID, eleType) {
	var ni = document.getElementById(parentID);
	var newEle = document.createElement(eleType); // Create dynamic element
	var eleIdName;
	if(type.indexOf("value") != -1 ){
		eleIdName = type; // There can only be one value div per property,
	}else{
		inival=inival+1; // Increment element number by 1
		eleIdName = type+inival; 
	}
	newEle.setAttribute('id',eleIdName);
	newEle.setAttribute('class', "num_val");
	ni.appendChild(newEle);
	return eleIdName;
}


/*
//	CREDITS
// --------------------------------------------------------
// Author : Daxa
// Website : http://www.beyondmart.com/
// methods: addProperty, add_New_Element
// --------------------------------------------------------

*/
	
