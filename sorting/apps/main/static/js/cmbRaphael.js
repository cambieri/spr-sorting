function pathArrayToString(pathArray)
{
	var length1 = pathArray.length,
		length2 = 0,
		element1 = null,
		element2 = null,
		segType = null,
		ret = "";
	for (var i = 0; i < length1; i++) {
		element1 = pathArray[i];
		length2 = element1.length;
		segType = element1[0];
		ret += (" " + segType);
		for (var j = 1; j < length2; j++) {
			element2 = element1[j];
			ret += element2;
			if ((j == 1) || (j%2 == 1 && segType.toUpperCase() != "A") || (segType.toUpperCase() == "A" && j >= 4 && j%2 == 0)) {
				ret += ",";
			} else {
				ret += " ";
			}														
		}
	}
	return ret.trim();
}

function iconUnderPoint(x, y, width, height)
{
	retIcon = "";
	isNotUnload = false;
	isPicked = false;
	isInsideExternal = false;
	isInsideInternal = false;		
	cmbI.forEach(function(i){
		myIcon = i.id;
//			isNotUnload = ($.inArray(i, cmbNotunload) > -1);
//			isPicked  = ($.inArray(i, cmbPicked) > -1);
		isInsideExternal = false;
		isInsideInternal = false;
		i.forEach(function(p){
			var profile = p.data("id");
			var isInternal = (p.data("class").toLowerCase() == "internal");
			var path = p.data("pathstring");
			isNotUnload = (p.data("notunload") == 1);
			isPicked = (p.data("picked") > 0);
			var isInside = [];
			isInside.push(Raphael.isPointInsidePath(path, x, y));
			if(typeof width !== "undefined") {
				isInside.push(Raphael.isPointInsidePath(path, x + width/2, y));
				isInside.push(Raphael.isPointInsidePath(path, x - width/2, y));
			}
			if(typeof height !== "undefined") {
				isInside.push(Raphael.isPointInsidePath(path, x, y + height/2));
				isInside.push(Raphael.isPointInsidePath(path, x, y - height/2));
			}				 
			if ($.inArray(true, isInside) > -1) {
				retIcon = myIcon;
				if (!($.inArray(false, isInside) > -1)) {
					if (isInternal) {
						isInsideInternal = true;
					} else {
						isInsideExternal = true;
					}
				}					
			}
		});
		if (retIcon == "") {
			return true;
		} else {
			return false;
		}
	});
	var ret = new Array();
	ret['icon'] = retIcon;
	ret['isInsideExternal'] = isInsideExternal;
	ret['isInsideInternal'] = isInsideInternal;
	ret['isNotUnload'] = isNotUnload;
	ret['isPicked'] = isPicked;
	return ret;
}

function animateSuctionCup(x, y, dimX, dimY)
{
	var icon = iconUnderPoint(x, y, dimX, dimY);
	var myColor = "#000";
	if (icon['icon'] == "") {
		myColor = "#909090";
	} else {
		if (icon['isNotUnload'])
		{
			myColor = "#FFFF00";
		} 
		else if (icon['isPicked'])
		{
			myColor = "#FF8000";
		}
		else if (icon['isInsideExternal'] && !icon['isInsideInternal'])
		{
			myColor = "#00FF00";
		}
		else
		{
			myColor = "#FF0000";				
		}
	}
		
	ellipse = cmbR.ellipse(x, y, 0, 0).attr({"fill": "#000", "stroke": "none"});
	ellipse.animate({rx:dimX, ry:dimY}, 0, function() {
		ellipse.animate({fill:myColor}, 0);			
	});
}
