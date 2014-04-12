

<?php include('header.php');?>


<div id="plantinfo">
	<div class="plant_scientific"><textarea id="genus" placeholder="Genus"></textarea><textarea id="species" rows="2" cols="20" placeholder="species"></textarea></div>
	<div class="plant_common"><textarea id="commonnames" placeholder="Common Names"></textarea></div>
</div><!--end plantinfo -->

<div id="plantimages">
	<h2>Images</h2>
	<form id="uploadForm" action="upload.process.php" enctype="multipart/form-data" method="post" target="_blank">
		<?php echo('<input type="hidden" name="MAX_FILE_SIZE" value="'.$max_file_size.'">'); ?>
	</form>
</div>
<!--<a onclick='addImageUploader()' href='#'>Add New Image </a><br/>
<button onclick="UploadImages()">Upload Images</button>
-->

<div id="plantintrinsic">
<h2>Intrinsic Characteristics</h2>


</div><!--end plantintrinsic-->

<a onclick='addProperty(FunctionalAnalysis.intrinsics_lib,"plantintrinsic")' href='#'>Add New Intrinsic Characteristic </a>


<div id="plantneeds">
<h2>Needs</h2>


</div><!--end plantneeds -->
<a onclick='addProperty(FunctionalAnalysis.needs_lib,"plantneeds")' href='#'>Add New Need</a>

<div id="plantproducts">
<h2>Products</h2>


</div><!--end plantproducts -->
<a onclick='addProductProperty(FunctionalAnalysis.products_lib,"plantproducts")' href='#'>Add New Product</a>

<div id="plantbehaviors">
<h2>Behaviors</h2>


</div><!--end plantbehaviors -->
<a onclick='addProperty(FunctionalAnalysis.behavior_lib,"plantbehaviors")' href='#'>Add New Behavior</a>

<div id="submitplant">
	<button onclick="SubmitPlant()">Add Plant to Database</button>
</div>

<div id="footer">

<!-- Please leave this line intact -->
</div>
</body>
</html>

