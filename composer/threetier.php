<?php
// Copyright (c) 2009 3TIER, Inc. All rights reserved.
// Redistribution and use of this software in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
// 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
// 3. The name of 3TIER, Inc., may not be used to endorse or promote products derived from this software without specific prior written permission of 3TIER, Inc.
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


function fetch_from_3tier($fieldname, $latitude, $longitude, $height=null) {
 
 // This key is only valid over Yellowstone National Park
 $api_key = 'SAMPLE-API-KEY';

 $base = 'https://data.3tier.com/api/rest/0.9/get_point/';
 $query_string = "";

 $params = array( 'apikey' => $api_key,
		   'product' => 'FirstlookBasicAPI',
		   'field' => $fieldname,
		 'lon'  => $longitude,
		 'lat'  => $latitude
		 );

 if(null != $height) {
   $params['height'] = $height;
 }

 foreach ($params as $key => $value) {
   $query_string .= "$key=" . urlencode($value) . "&";
 }

 $url = "$base?$query_string";

 $output = file_get_contents($url);

 $dom = new domDocument;
 $dom->loadXML($output);

 $return_value = simplexml_import_dom($dom);

 $mean_value =  (float) $return_value->Data->FieldResult->FieldResultItem->Value;
 $error_estimate =  (float) $return_value->Data->FieldResult->FieldResultItem->ErrorEstimate;

 $min_value = $mean_value - $error_estimate;
 $max_value = $mean_value + $error_estimate;


 return array ($min_value, $max_value, $mean_value);
}


var_dump(fetch_from_3tier('weather',44,110));
?>
