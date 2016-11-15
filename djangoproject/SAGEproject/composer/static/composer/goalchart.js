$(document).ready(function(){
var nb_sliders = null; // nb of range sliders
var moving_id = null; // id of the moved slider
var oldValue = []; // previous values of the sliders

// pie chart radius
var radius = 100;

// setup the margins so we don't clip the outter labels
var margin = {
  top: 100,
  right: 100,
  bottom: 100,
  left: 175
};
var canvasWidth = radius * 2 + margin.left + margin.right,
  canvasHeight = radius * 2 + margin.top + margin.bottom;

// color scheme (10, 20, 20b, 20c ...)
//var color = d3.scale.ordinal()
//  .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

//var color = d3.scale.category10();
var color = d3.scale.category10();

// center legend
var legendData = [{
  label: "Sample",
  value: 300
}, {
  label: "Total People",
  value: 7200000
}]

var pi = Math.PI; // 3.14

// pie chart config
var pie = d3.layout.pie()
  .value(function(d) {
    return d.value;
  })
  //.startAngle(-90 * (pi/180))
  // .endAngle(90 * (pi/180))
  .sort(null);

// arc object
var arc = d3.svg.arc()
  .outerRadius(radius)
  .innerRadius(radius / 3);

// My slider
var range = $('.input-range'),
  value = $('.range-value');
value.html(range.attr('value'));

range.on('input', function() {
  value.html(this.value);
     showHelp();
});

// segement number sliders event
d3.selectAll('#nbFormSubmit').on('click', function() {
  nb_sliders = 5;
  init();
});

$(document).ready(function(){
  nb_sliders = 5;
  init();
});


// initialize the sliders, events and pie chart
function init() {
  oldValue = [];
  moving_id = null;


  d3.select('#rangebox tbody').html('');

  // append sliders to table
  for (i = 0; i < nb_sliders; i++) {
    var tr = d3.select('#rangebox tbody').append('tr');
    tr.append('td')
      .attr('class', 'edit')
      .attr('bgcolor', function(d, i){return color(i)})
      .attr('contenteditable', true)
      .text('' + (i + 1));


    tr.append('td')
      .append('input')
      .attr('type', 'range')
      .attr('data-id', i)
      .attr('class', 'range')
      .attr('step', 1)
      .attr('min', 0)
      .attr('max', 100);
    tr.append('td')
      .attr('class', 'range_value');
  }

  d3.selectAll('#rangebox .range').each(function() {
    var def = parseInt(100 / nb_sliders);
    this.value = def;
    oldValue[d3.select(this).attr('data-id')] = this.value;
  });

  equalize();
  showValues();
  pieChart();
  seteditboxcolor();

  // content edit event
  d3.selectAll('.edit').on('input', function() {
    updateLabels();
  });

  // slider event
  d3.selectAll('.range').on('input', function() {
    this.value = parseInt(this.value);
    if (this.value < 0) this.value = 0;
    else if (this.value > 100) this.value = 100;

    var id = d3.select(this).attr('data-id');
    moving_id = id;

    var old_value = oldValue[moving_id];
    var new_value = this.value;
    var delta = (new_value - old_value) / (nb_sliders - 1);

    d3.selectAll('#rangebox .range').each(function() {
      var r_id = d3.select(this).attr('data-id');
      var r_val = this.value;
      if (r_id != moving_id && r_val > delta) {
        var equalized = parseInt(r_val - delta);
        this.value = equalized;
        oldValue[r_id] = this.value;
      }
    });

    oldValue[moving_id] = new_value;

    equalize();
    showValues();
    updatePieChart();

  });
}

// set edit box color to match slice color
function showHelp() {
  // use jQuery to target h5 edit boxes)
  $(document).ready(function(){
    $('h5').css({"opacity":".4"});
    $('#pieImage').css({"display":"none"});});
}

// set edit box color to match slice color
function seteditboxcolor() {
  // var slicepaths= d3.selectAll('.slice')
     var mycolors = [0,1,2,3,4,5,6,7,8,9];
     var editboxes = d3.selectAll('.edit')
                       .data(mycolors)
                       .attr('bgcolor', function(d){ return color(d); })
 }


// get JSON data from sliders
function getData() {
  var json = [];
  d3.selectAll('#rangebox .range').each(function() {

    json.push({
      label: d3.select(this.parentNode.parentNode)
        .select('td:first-child')
        .text(),
      value: this.value
    });
  });
  return json;
}

// compute total percentage from sliders
function getTotal() {
  var total = 0;
  d3.selectAll('#rangebox .range').each(function() {
    total = total + parseInt(this.value);
  });
  return total;
}

// equalize the sliders (decimal delta)
function equalize() {
  var remaining = 100 - getTotal();

  if (remaining != 0) {
    var to_eq = null;
    var min = null;
    var max = null;
    var min_value = 9999;
    var max_value = 0;

    // console.log(remaining);

    d3.selectAll('#rangebox .range').each(function() {
      var id = d3.select(this).attr('data-id');

      if (id != moving_id) {
        if (parseInt(this.value) > parseInt(max_value)) {
          max_value = this.value;
          max = this;
        }
        if (parseInt(this.value) < parseInt(min_value)) {
          min_value = this.value;
          min = this;
        }
      }
    });

    if (remaining > 0) to_eq = min;
    else to_eq = max;

    if (to_eq) {
      if (remaining > 0) {
        to_eq.value = parseInt(to_eq.value) + 1;
        remaining = remaining - 1;
      } else {
        to_eq.value = parseInt(to_eq.value) - 1;
        remaining = remaining + 1;
      }
      oldValue[d3.select(to_eq).attr('data-id')] = to_eq.value;

      if (remaining != 0) equalize();
    }
  }
}

// show slider value
function showValues() {
  d3.selectAll('#rangebox .range').each(function() {
    var perct = this.value + '%';
    d3.select(this.parentNode.nextSibling).html(perct);
  });
}

// draw pie chart
function pieChart() {


  var json = getData();
  var canvaCenterX = (radius * 2 + margin.left + margin.right) / 2;
  var canvaCenterY = (radius * 2 + margin.top + margin.bottom) / 2;

  d3.select("#pie svg").remove();

  // svg canvas
  var svg = d3.select("#pie")

  .append("svg:svg")
    .attr("width", canvasWidth)
    .attr("height", canvasHeight)

  .append("svg:g")
    .attr("transform", "translate(" + canvasWidth / 2 + "," + canvasHeight / 2 + ")")

  // create the classes under the transform
  d3.select("g")
    .append("g")
    .attr("class", "slices");

  d3.select("g")
    .append("g")
    .attr("class", "labels");

  d3.select("g")
    .append("g")
    .attr("class", "lines");

  d3.select("g")
    .append("g")
    .attr("class", "legend");

  // group all ther paths into the slices class
  var arcpaths = svg.select(".slices").selectAll("path").data(pie(getData()))

  // render the slices
  arcpaths.enter()

  .append('svg:path')
    .attr("class", "slice")
    .attr("fill", function(d, i) {
      return color(i);
    })


      .attr("d", arc)
    .each(function(d) {
      this._current = d;
    })
    .append('title')
    .text(function(d, i) {
      return json[i].value + '%';
    });

  // group all ther paths into the slices class
  var arclabels = svg.select(".labels").selectAll("label").data(pie(getData()))

  // render the labels
  arclabels.enter()

  .append("svg:text")
    .attr("class", "label")
    .attr("transform", function(d) {
      return "translate(" + arc.centroid(d) + ")";
    })
    .attr("text-anchor", "middle")
    .text(function(d, i) {
      if (json[i].value > 1) return json[i].label;
      else return null;
    });
 }

// update pie chart
function updatePieChart() {
  updateArcs();
  updateLabels();
  updateLabelLines();

}

// update the slices of the pie chart
function updateArcs() {
   var json = getData();

  d3.selectAll("#pie path title")
    .text(function(d, i) {
      return json[i].value + '%';
    });

  d3.selectAll("#pie path")
    .data(pie(json))
    .transition()
    .duration(100)
    .attrTween('d', arcTween);
}

/* ------- TEXT LABELS -------*/
// update the labels of the pie chart
function updateLabels() {
  labelr = radius + 40 // radius for label anchor
  d3.selectAll("#pie text")
    .data(pie(getData()))
    .transition()
    .duration(120)

  .attr("transform", function(d) {
      var c = arc.centroid(d),
        x = c[0],
        y = c[1],
        // pythagorean theorem for hypotenuse
        h = Math.sqrt(x * x + y * y);
      return "translate(" + (x / h * labelr) + ',' +
        (y / h * labelr) + ")";
    })
    .attr("dy", ".35em")
    .attr("text-anchor", function(d) {
      // are we past the center?
      return (d.endAngle + d.startAngle) / 2 > Math.PI ?
        "end" : "start";
    })

  //.text(function(d, i) { return d.value.toFixed(2); });
  .text(function(d, i) {
    if (getData()[i].value > 0) return getData()[i].label;
    else return null;
  });
}

/* ------- SLICE TO TEXT POLYLINES -------*/

var outerArc = d3.svg.arc()
  .innerRadius(radius +50)
  .outerRadius(radius * .95);

function midAngle(d) {
  return d.startAngle + (d.endAngle - d.startAngle) / 2;
}

function updateLabelLines() {
  var polyline = d3.select(".lines").selectAll("polyline")
    .data(pie(getData()));

  //alert("I am an alert box!");

  polyline.enter()
    .append("polyline")

  polyline.transition()
    .duration(100)
    .attrTween("points", function(d) {
      this._current = this._current || d;
      var interpolate = d3.interpolate(this._current, d);
      this._current = interpolate(0);
      return function(t) {
        var d2 = interpolate(t);
        var pos = 0; // outerArc.centroid(d2);
       // pos[0] = radius * .95 * (midAngle(d2) < Math.PI ? 1 : -1);
       return [arc.centroid(d2), outerArc.centroid(d2)];
      };
    });

  polyline.exit()
    .remove();
}

// transition for the arcs
function arcTween(a) {
  var i = d3.interpolate(this._current, a);
  this._current = i(0);
  return function(t) {
    return arc(i(t));
  };
}


});
