

<?php include('header.php');
//if isset will get rid of this warning with pl_id
	if(isset($_GET['pl_id'])){
		$plantId = $_GET['pl_id'];  ///bug here...
		$plantData = load_Plant_Data($plantId);
	}
?>

<div id="plantinfo">
	<div class="plant_scientific"> <?php echo('<textarea id="genus" placeholder="'.$plantData[0].'">'.$plantData[0].'</textarea><textarea id="species" rows="2" cols="20" placeholder="'.$plantData[1].'">'.$plantData[1].'</textarea></div>');?>
	<div class="plant_common"><?php echo('<textarea id="commonnames" placeholder="'.$plantData[2].'">'.$plantData[2].'</textarea></div>');?>
</div><!--end plantinfo -->

<div id="plantimages">
	<h2>Images</h2>
	<?php 
	printImages($plantData[7]);
?>
	<form id="uploadForm" action="upload.process.php" enctype='multipart/form-data' method='post' target='_blank'>
		<input type="hidden" name="MAX_FILE_SIZE" value="<?php echo $max_file_size ?>">
	</form>
</div>
<a onclick='addImageUploader()' href='#'>Add New Image </a><br/>
<button onclick="UploadImages()">Upload Images</button>

<div id="plantintrinsic">
<h2>Intrinsic Characteristics</h2>
<?php 
	printPlantData_SingleCategory($plantData[3], "intrinsic");
?>
</div><!--end plantintrinsic-->

<a onclick='addProperty(FunctionalAnalysis.intrinsic,"plantintrinsic")' href='#'>Add New Intrinsic Characteristic </a>


<div id="plantneeds">
<h2>Needs</h2>
<?php 
printPlantData_SingleCategory($plantData[4], "needs");
?>
</div><!--end plantneeds -->
<a onclick='addProperty(FunctionalAnalysis.need,"plantneeds")' href='#'>Add New Need</a>

<div id="plantproducts">
<h2>Products</h2>
<?php 
printPlantData_SingleCategory($plantData[5], "products");
?>
</div><!--end plantproducts -->
<a onclick='addProductProperty(FunctionalAnalysis.product,"plantproducts")' href='#'>Add New Product</a>

<div id="plantbehaviors">
<h2>Behaviors</h2>
<?php 
printPlantData_SingleCategory($plantData[6], "behaviors");
?>

</div><!--end plantbehaviors -->
<a onclick='addProperty(FunctionalAnalysis.behavior,"plantbehaviors")' href='#'>Add New Behavior</a>

<div id="submitplant">
	<?php echo('<button onclick="UpdatePlant(\''.$plantId.'\')">Update Plant Information</button>');?>
	<div id="deleteplant" style="display:inline; float:right;">
		<?php echo('<button onclick="DeletePlant(\''.$plantId.'\')">Delete Plant from Database</button>');?>
	</div>
</div>



<div id="footer">

<!-- Please leave this line intact -->
</div>
</body>
</html>

<!--
//	CREDITS
// --------------------------------------------------------
// Author : Daxa
// Website : http://www.beyondmart.com/
// methods: addProperty, add_New_Element
// --------------------------------------------------------

-->