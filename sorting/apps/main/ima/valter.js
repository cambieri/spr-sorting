var windowWidth = $('#cmbR').width() * 0.95; 
var windowHeight = $('#cmbR').height() * 0.95; 
var xRatio = windowWidth / 2500.0; 
var yRatio = windowHeight / 1250.0; 
var ratio = (xRatio < yRatio) ? xRatio : yRatio; 

var cmbR = Raphael('cmbR', 2500.0 * ratio, 1250.0 * ratio); 
cmbR.setViewBox(0,0,2500.0,1250.0); 
cmbI = cmbR.set(); 
cmbNotunload = cmbR.set(); 
cmbPicked = cmbR.set(); 
var r000 = cmbR.rect(0,0,2500.0,1250.0); 
r000.id = "r000"; 
$(r000.node).attr('class', 'sheet'); 
$(r000.node).attr('id', 'r000'); 
r000.attr({'x': '0', 'y': '0', 'fill': '#F7FE2E', 'stroke': '#000', 'stroke-width': '0', 'stroke-opacity': '1'}); 

var cmbS = new Array(); 
cmbS.push({"index":1, "x":0, "y":0, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":2, "x":230, "y":0, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":3, "x":450, "y":0, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":4, "x":670, "y":0, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":5, "x":0, "y":130, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":6, "x":230, "y":130, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":7, "x":450, "y":130, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":8, "x":670, "y":130, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":9, "x":1070, "y":0, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":10, "x":1290, "y":0, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":11, "x":1510, "y":0, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":12, "x":1740, "y":0, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":13, "x":1070, "y":130, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":14, "x":1290, "y":130, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":15, "x":1510, "y":130, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":16, "x":1740, "y":130, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":17, "x":200, "y":230, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":18, "x":0, "y":360, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":19, "x":230, "y":360, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":20, "x":450, "y":360, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":21, "x":670, "y":360, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":22, "x":0, "y":490, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":23, "x":230, "y":490, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":24, "x":450, "y":490, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":25, "x":670, "y":490, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":26, "x":200, "y":620, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":27, "x":1270, "y":230, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":28, "x":1070, "y":360, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":29, "x":1300, "y":360, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":30, "x":1520, "y":360, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":31, "x":1740, "y":360, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":32, "x":1070, "y":490, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":33, "x":1300, "y":490, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":34, "x":1520, "y":490, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":35, "x":1740, "y":490, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":36, "x":1270, "y":620, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":37, "x":0, "y":720, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":38, "x":230, "y":720, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":39, "x":450, "y":720, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":40, "x":670, "y":720, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":41, "x":0, "y":850, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":42, "x":230, "y":850, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":43, "x":450, "y":850, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":44, "x":670, "y":850, "dimX":40, "dimY":40, "position":"left"}); 
cmbS.push({"index":45, "x":1070, "y":720, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":46, "x":1290, "y":720, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":47, "x":1510, "y":720, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":48, "x":1740, "y":720, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":49, "x":1070, "y":850, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":50, "x":1290, "y":850, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":51, "x":1510, "y":850, "dimX":40, "dimY":40, "position":"right"}); 
cmbS.push({"index":52, "x":1740, "y":850, "dimX":40, "dimY":40, "position":"right"}); 

function drawSheet() 
{ 
	var g001 = cmbR.set(); 
	g001.id = "g001"; 
	pathString = "M-190.0,-49.2700265   L-190.0,49.2700265   L190.0,49.2700265   L190.0,-49.2700265   L-190.0,-49.2700265"; 
	pathTransform = "t0,1250.0 s1,-1 t263.9337,1183.8898"; 
	pathArray = Raphael.transformPath(pathString, pathTransform); 
	pathToString = pathArrayToString(pathArray); 
	var p001001 = cmbR.path(pathArray); 
	p001001.id = "p001001"; 
	$(p001001.node).attr('class', 'external'); 
	$(p001001.node).attr('id', 'p001001'); 
	p001001.attr({'fill': '#585858', 'stroke': '#000', 'stroke-width': '0', 'stroke-opacity': '1'}); 
	p001001.data("id", "p001001"); 
	p001001.data("class", "external"); 
	p001001.data("picked", 0); 
	p001001.data("notunload", 0); 
	p001001.data("parent", g001); 
	p001001.data("pathstring", pathToString); 
	g001.push(p001001); 
	pathString = "M151.5,7.7758844   L151.5,20.7758844   L158.5,20.7758844   L158.5,7.7758844   L151.5,7.7758844"; 
	pathTransform = "t0,1250.0 s1,-1 t263.9337,1183.8898"; 
	pathArray = Raphael.transformPath(pathString, pathTransform); 
	pathToString = pathArrayToString(pathArray); 
	var p001002 = cmbR.path(pathArray); 
	p001002.id = "p001002"; 
	$(p001002.node).attr('class', 'internal'); 
	$(p001002.node).attr('id', 'p001002'); 
	p001002.attr({'fill': '#F7FE2E', 'stroke': '#000', 'stroke-width': '0', 'stroke-opacity': '1'}); 
	p001002.data("id", "p001002"); 
	p001002.data("class", "internal"); 
	p001002.data("picked", 0); 
	p001002.data("notunload", 0); 
	p001002.data("parent", g001); 
	p001002.data("pathstring", pathToString); 
	g001.push(p001002); 
	pathString = "M31.5,7.7758844   L31.5,20.7758844   L38.5,20.7758844   L38.5,7.7758844   L31.5,7.7758844"; 
	pathTransform = "t0,1250.0 s1,-1 t263.9337,1183.8898"; 
	pathArray = Raphael.transformPath(pathString, pathTransform); 
	pathToString = pathArrayToString(pathArray); 
	var p001003 = cmbR.path(pathArray); 
	p001003.id = "p001003"; 
	$(p001003.node).attr('class', 'internal'); 
	$(p001003.node).attr('id', 'p001003'); 
	p001003.attr({'fill': '#F7FE2E', 'stroke': '#000', 'stroke-width': '0', 'stroke-opacity': '1'}); 
	p001003.data("id", "p001003"); 
	p001003.data("class", "internal"); 
	p001003.data("picked", 0); 
	p001003.data("notunload", 0); 
	p001003.data("parent", g001); 
	p001003.data("pathstring", pathToString); 
	g001.push(p001003); 
	pathString = "M-151.5,7.7758844   L-151.5,20.7758844   L-158.5,20.7758844   L-158.5,7.7758844   L-151.5,7.7758844"; 
	pathTransform = "t0,1250.0 s1,-1 t263.9337,1183.8898"; 
	pathArray = Raphael.transformPath(pathString, pathTransform); 
	pathToString = pathArrayToString(pathArray); 
	var p001004 = cmbR.path(pathArray); 
	p001004.id = "p001004"; 
	$(p001004.node).attr('class', 'internal'); 
	$(p001004.node).attr('id', 'p001004'); 
	p001004.attr({'fill': '#F7FE2E', 'stroke': '#000', 'stroke-width': '0', 'stroke-opacity': '1'}); 
	p001004.data("id", "p001004"); 
	p001004.data("class", "internal"); 
	p001004.data("picked", 0); 
	p001004.data("notunload", 0); 
	p001004.data("parent", g001); 
	p001004.data("pathstring", pathToString); 
	g001.push(p001004); 
	pathString = "M-31.5,7.7758844   L-31.5,20.7758844   L-38.5,20.7758844   L-38.5,7.7758844   L-31.5,7.7758844"; 
	pathTransform = "t0,1250.0 s1,-1 t263.9337,1183.8898"; 
	pathArray = Raphael.transformPath(pathString, pathTransform); 
	pathToString = pathArrayToString(pathArray); 
	var p001005 = cmbR.path(pathArray); 
	p001005.id = "p001005"; 
	$(p001005.node).attr('class', 'internal'); 
	$(p001005.node).attr('id', 'p001005'); 
	p001005.attr({'fill': '#F7FE2E', 'stroke': '#000', 'stroke-width': '0', 'stroke-opacity': '1'}); 
	p001005.data("id", "p001005"); 
	p001005.data("class", "internal"); 
	p001005.data("picked", 0); 
	p001005.data("notunload", 0); 
	p001005.data("parent", g001); 
	p001005.data("pathstring", pathToString); 
	g001.push(p001005); 
	cmbI.push(g001); 
	
} 