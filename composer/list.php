<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Sortable List</title>
  <link rel="stylesheet" href="http://code.jquery.com/ui/1.10.2/themes/smoothness/jquery-ui.css" />
  <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
  <script src="http://code.jquery.com/ui/1.10.2/jquery-ui.js"></script>
  <link rel="stylesheet" href="/resources/demos/style.css" />
  <style>
  //#sortable { list-style-type: none; margin: 0; padding: 0; width: 60%; }
  //#sortable li { margin: 0 3px 3px 3px; padding: 0.4em; padding-left: 1.5em; font-size: 1.4em; height: 18px; }
  //#sortable li span { position: absolute; margin-left: -1.3em; }
  .item {  	background-color: #CCCCCC; -webkit-transition: all .05s ease-out;}
  .item:hover { -webkit-transform: scale(1.02) rotate(0deg);}
  </style>
  <script>
  $(function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
  });
  </script>
</head>
<body>
 
<ul id="sortable">
<li class="item">Item 1</li>
<li class="item">Item 2</li>
<li class="item">Item 3</li>
<li class="item">Item 4</li>
<li class="item">Item 5</li>
<li class="item">Item 6</li>
</ul>
 
 
</body>
</html>