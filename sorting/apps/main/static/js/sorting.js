// Aggiunto a jquery metodi per abilitare / disabilitare elementi
$.fn.disable = function() {
    return this.each(function() {
        if (typeof this.disabled != "undefined") this.disabled = true;
    });
}
$.fn.enable = function() {
    return this.each(function() {
        if (typeof this.disabled != "undefined") this.disabled = false;
    });
}

// CLASSE Mission BEGIN
function Mission(paper, missionNum) {
//		paper: cmbR,
	this.paper = paper;
	this.missionNum = missionNum;
	
	this.minOffsetX = baseOffsetX;
	this.minOffsetY = baseOffsetY;
	this.maxOffsetX = app.canvasWidth - baseOffsetX;
	this.maxOffsetY = app.canvasHeight - baseOffsetY;
	this.offsetX = baseOffsetX;
	this.offsetY = baseOffsetY;
	
	this.icons = cmbI;
	this.suctionCups = new Array();
	this.picked = new Array();
	this.leftWing = 0;
	this.rightWing = 0;
};		
Mission.prototype.decOffsetX = function() {
	this.offsetX = this.offsetX>this.minOffsetX ? this.offsetX-incX : this.minOffsetX;
	this.refreshCircles();
};
Mission.prototype.incOffsetX = function() {
	this.offsetX = this.offsetX<this.maxOffsetX ? this.offsetX+incX : this.maxOffsetX;
	this.refreshCircles();
};
Mission.prototype.decOffsetY = function() {
	this.offsetY = this.offsetY>this.minOffsetY ? this.offsetY-incY : this.minOffsetY;
	this.refreshCircles();
};
Mission.prototype.incOffsetY = function() {
	this.offsetY = this.offsetY<this.maxOffsetY ? this.offsetY+incY : this.maxOffsetY;
	this.refreshCircles();
};
Mission.prototype.drawSuctionCup = function(posX, posY, radiusX, radiusY) {
	var x = posX + this.offsetX;
	var y = posY - this.offsetY;
	var suctionCup = this.paper.ellipse(x, y, radiusX, radiusY);
	suctionCup.attr("fill", "#909090");
	suctionCup.attr("stroke", "#FFFFFF");
	suctionCup.node.onclick = function() {
		var thisMissionId = this.parentNode.parentNode.parentNode.parentNode.id;
		var currentMissionId = 'mission' + app.currentMission.missionNum;
		if (thisMissionId === currentMissionId) {
			if (suctionCup.attr("fill") == "#00FF00") { suctionCup.animate({fill:"#FF0000"},200); }
			else if (suctionCup.attr("fill") == "#FF0000") { suctionCup.animate({fill:"#00FF00"},200); }
			else if (suctionCup.attr("fill") == "#909090") { suctionCup.animate({fill:"#00FF00"},200); }
			else if (suctionCup.attr("fill") == "#FF8000") { suctionCup.animate({fill:"#00FF00"},200); }
		}
	}
	this.suctionCups.push(suctionCup);
};
Mission.prototype.drawSuctionCups = function() {
	this.suctionCups.length = 0;
	var posxFirstCup = cmbS[0].x + this.leftWing + this.offsetX;
	var offsetCorrectionX = posxFirstCup < baseOffsetX ? -posxFirstCup + baseOffsetX : 0;
	this.offsetX += offsetCorrectionX;
	for (var i=0; i<cmbS.length; i++) {
		var item = cmbS[i];
		var itemOffsetX = (item.position=='left' ? this.leftWing : this.rightWing);
		this.drawSuctionCup(item.x + itemOffsetX, app.canvasHeight - item.y, item.dimX, item.dimY);
	}
	this.minOffsetX = this.leftWing != 0 ? -this.leftWing + baseOffsetX : baseOffsetX;
	if (this.offsetX<=this.minOffsetX) { clearInterval(i1); $('#btnDecOffsetX'+this.missionNum).prop('disabled', true); } else { $('#btnDecOffsetX'+this.missionNum).prop('disabled', false); }
	if (this.offsetX>=this.maxOffsetX) { clearInterval(i2); $('#btnIncOffsetX'+this.missionNum).prop('disabled', true); } else { $('#btnIncOffsetX'+this.missionNum).prop('disabled', false); }
	if (this.offsetY<=this.minOffsetY) { clearInterval(i3); $('#btnDecOffsetY'+this.missionNum).prop('disabled', true); } else { $('#btnDecOffsetY'+this.missionNum).prop('disabled', false); }
	if (this.offsetY>=this.maxOffsetY) { clearInterval(i4); $('#btnIncOffsetY'+this.missionNum).prop('disabled', true); } else { $('#btnIncOffsetY'+this.missionNum).prop('disabled', false); }
//	$('#btnDecOffsetX'+this.missionNum).prop('disabled', this.offsetX<=this.minOffsetX);
//	$('#btnIncOffsetX'+this.missionNum).prop('disabled', this.offsetX>=this.maxOffsetX);
//	$('#btnDecOffsetY'+this.missionNum).prop('disabled', this.offsetY<=this.minOffsetY);
//	$('#btnIncOffsetY'+this.missionNum).prop('disabled', this.offsetY>=this.maxOffsetY);
};
Mission.prototype.drawIcons = function() {
	this.icons.clear();
	drawSheet();
	// metto in grigio chiaro le picked in precedenti missioni
	for (var i=0; i<this.icons.length; i++) {
		this.icons[i][0].data("picked", 0);
		for (var j=0; j<app.missions.length; j++) {
			if (app.missions[j].picked.indexOf(this.icons[i]["id"])>-1) { // se picked
				this.icons[i][0].animate({fill:"#AAAAAA"},200);
				this.icons[i][0].data("picked", 1);
			}
		}
	}
};
Mission.prototype.unpickAll = function() {
	// metto in grigio chiaro le picked
	for (var i=0; i<this.icons.length; i++) {
		if (this.picked.indexOf(this.icons[i]["id"])>-1) { // se picked
			this.icons[i][0].animate({fill:"#585858"},200);
			this.icons[i][0].data("picked", 0);
		}
	}
	this.picked.length = 0; // pulisce array
}
Mission.prototype.checkIntersection = function() {
	for (var j=0; j<this.suctionCups.length; j++) {
		var icon = iconUnderPoint(this.suctionCups[j].attr('cx'), this.suctionCups[j].attr('cy'), this.suctionCups[j].attr('rx'), this.suctionCups[j].attr('ry'));
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
		this.suctionCups[j].animate({fill:myColor},200);
	}
};
Mission.prototype.acceptMission = function() {
	this.picked.length = 0; // pulisce array
	for (var j=0; j<this.suctionCups.length; j++) {
		if (this.suctionCups[j].attr('fill') == "#00FF00") {
			var icon = iconUnderPoint(this.suctionCups[j].attr('cx'), this.suctionCups[j].attr('cy'), this.suctionCups[j].attr('rx'), this.suctionCups[j].attr('ry'));
			var iconId = icon['icon'];
			for (var i=0; i<this.icons.length; i++) {
				if (this.icons[i]["id"] == iconId) {
					this.icons[i][0].animate({fill:"#FFFFFF"},200);
					this.picked.push(this.icons[i]["id"]);
				}
			}
		}
	}
	app.setMission(this.missionNum + 1);
};
Mission.prototype.refreshCircles = function() {
	for (var j=0; j<this.suctionCups.length; j++) {
		this.suctionCups[j].remove();
	}
	this.suctionCups.length = 0;
	this.drawSuctionCups();
};
Mission.prototype.refresh = function() {
	this.picked.length = 0;
	this.paper.clear();
	this.drawIcons();
	this.drawSuctionCups();
	this.checkIntersection();
};
//CLASSE Mission END

var app = {
	canvasWidth: 3048.0,
	canvasHeight: 1524.0,
	missions: new Array(),
	currentMission: null,
	setMission: function(missionNum) {
		if (app.currentMission) {
			$('#mission'+app.currentMission.missionNum + " *").disable();
		}
		if (missionNum === this.missions.length) {
			if (app.currentMission) { $('#btnRivedi'+app.currentMission.missionNum).enable(); }
			
			var missionDiv = Mustache.render(missionTemplate, {missionNum: missionNum});
			$('.content').append(missionDiv);
			
			var windowWidth = $('#cmbR'+missionNum).width() * 0.95; 
			var windowHeight = $('#cmbR'+missionNum).height() * 0.95; 
			var xRatio = windowWidth / app.canvasWidth; 
			var yRatio = windowHeight / app.canvasHeight; 
			var ratio = (xRatio < yRatio) ? xRatio : yRatio; 

			cmbR = Raphael('cmbR'+missionNum, app.canvasWidth * ratio, app.canvasHeight * ratio);
			cmbR.setViewBox(0, 0, app.canvasWidth, app.canvasHeight); 
			cmbI = cmbR.set(); 
			cmbNotunload = cmbR.set(); 
			cmbPicked = cmbR.set(); 
			var r000 = cmbR.rect(0, 0, app.canvasWidth, app.canvasHeight); 
			r000.id = "r000"; 
			$(r000.node).attr('class', 'sheet'); 
			$(r000.node).attr('id', 'r000'); 
			r000.attr({'x': '0', 'y': '0', 'fill': '#F7FE2E', 'stroke': '#000', 'stroke-width': '0', 'stroke-opacity': '1'});
			
			var m = new Mission(cmbR, missionNum);
			app.missions.push(m);
			app.currentMission = m;
			app.currentMission.refresh();
		} else {
			// tornare a missione già creata
			$('#btnRivedi'+app.currentMission.missionNum).enable();
//			alert('tornare a missione ' + missionNum);
			$('#mission'+missionNum + " *").enable();
			$('#btnRivedi'+missionNum).disable();
			app.currentMission = app.missions[missionNum];
			cmbR = app.currentMission.paper;
			cmbI = app.currentMission.icons;
//			app.currentMission.unpickAll();
			app.currentMission.refresh();
		}
	},
	deleteMission: function(missionNum) {
		if (app.missions.length > 1) {
			app.missions.splice(missionNum, 1);
			$('#mission'+missionNum).remove();
			for (var i = missionNum; i < app.missions.length; i++) {
				app.missions[i].missionNum = i;
				$('#mission'+(i+1)).attr('id','mission'+i);
				$('#txtTitolo'+(i+1)).html('MISSIONE '+(i+1));
				$('#txtTitolo'+(i+1)).attr('id','txtTitolo'+i);
				$('#btnDecOffsetX'+(i+1)).attr('id','btnDecOffsetX'+i);
				$('#btnIncOffsetX'+(i+1)).attr('id','btnIncOffsetX'+i);
				$('#btnRicalcola'+(i+1)).attr('id','btnRicalcola'+i);
				$('#btnAccetta'+(i+1)).attr('id','btnAccetta'+i);
				$('#btnDecOffsetY'+(i+1)).attr('id','btnDecOffsetY'+i);
				$('#cmbR'+(i+1)).attr('id','cmbR'+i);
				$("#btnRivedi"+(i+1)).attr('onclick','app.setMission('+i+');');
				$('#btnRivedi'+(i+1)).attr('id','btnRivedi'+i);
				$('#btnCancella'+(i+1)).attr('onclick','app.deleteMission('+i+');');
				$('#btnCancella'+(i+1)).attr('id','btnCancella'+i);
			}
			var newCurrentMission = (missionNum>0) ? app.missions[missionNum-1] : app.missions[0];
//			app.setMission(newCurrentMission);
		} else {
			alert("Impossibile cancellare tutte le missioni");
		}
	},
	saveMissionReplacer: function(key, value) {
		if (value instanceof Mission) {
			var sc = new Array();
			for (var i=0; i<value.suctionCups.length; i++) {
//				if (value.suctionCups[i].attr('fill')=="#00FF00") sc.push(cmbS[i].index);
				var on = value.suctionCups[i].attr('fill')=="#00FF00" ? 1 : 0;
				sc.push({"index":cmbS[i].index, "color":value.suctionCups[i].attr('fill'), 'on':on});
			}
			return {"missionNum":value.missionNum+1, "offsetX":value.offsetX, "offsetY":value.offsetY, "leftWing":value.leftWing, "rightWing":value.rightWing, "suctionCups":sc};
		} else {
			return value;
		}
	},
	saveMissions: function(fileName) {
        var board = $('#game-board').attr('data-board-id');
        $.ajax({
            type: "POST",
            url: "/save",
            data: {
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                file_name: fileName,
                missions: JSON.stringify(app.missions, app.saveMissionReplacer),
            },
            success: function(data) {
                alert(data);
            },
            error: function(xhr, textStatus, errorThrown) {
                alert("Errore: "+errorThrown+xhr.status+xhr.responseText);
            }
        });
    },
};

var i1, i2, i3, i4;
var missionTemplate;
$( document ).ready(function() {
	$.get('/static/mustache/mission.html', function(d){
		missionTemplate = d;
		app.setMission(0);
		if (savedMissions) {
			var missionsToRecover = JSON.parse(savedMissions.replace(/&quot;/ig, '"'));
			for (var i = 0; i<missionsToRecover.length; i++) {
				var missionData = missionsToRecover[i];
				var mission = app.missions[i];
				mission.offsetX = missionData.offsetX;
				$('#btnDecOffsetX'+i).prop('disabled', mission.offsetX<=mission.minOffsetX);
				$('#btnIncOffsetX'+i).prop('disabled', mission.offsetX>=mission.maxOffsetX);
				mission.offsetY = missionData.offsetY;
				$('#btnDecOffsetY'+i).prop('disabled', mission.offsetY<=mission.minOffsetY);
				$('#btnIncOffsetY'+i).prop('disabled', mission.offsetY>=mission.maxOffsetY);
				mission.leftWing = missionData.leftWing;
				$('#btnLeftWing'+i).prop('checked', mission.leftWing!=0);
				mission.rightWing = missionData.rightWing;
				$('#btnRightWing'+i).prop('checked', mission.rightWing!=0);
				mission.refreshCircles();
				for (var j = 0; j<missionData.suctionCups.length; j++) {
					mission.suctionCups[j].attr({fill:missionData.suctionCups[j].color});
				}
				if (i<missionsToRecover.length-1) mission.acceptMission();
			}
		}
	});
});
