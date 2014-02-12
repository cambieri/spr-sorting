// CLASSE Mission BEGIN
function Mission(paper, missionNum) {
//		paper: cmbR,
	this.paper = paper;
	this.missionNum = missionNum;
	
	this.minOffsetX = 0;
	this.minOffsetY = 0;
	this.maxOffsetX = 400;
	this.maxOffsetY = 300;
	this.offsetX = 20;
	this.offsetY = 15;
	
	this.icons = null;
	this.suctionCups = new Array();
	this.picked = new Array();
	this.leftWing = 0;
	this.rightWing = 0;
};		
Mission.prototype.decOffsetX = function(valore) {
	this.offsetX = this.offsetX>this.minOffsetX ? this.offsetX-10 : this.minOffsetX;
	$('#btnDecOffsetX').prop('disabled', this.offsetX==this.minOffsetX);
	$('#btnIncOffsetX').prop('disabled', false);
	this.refreshCircles();
};
Mission.prototype.incOffsetX = function(valore) {
	this.offsetX = this.offsetX<this.maxOffsetX ? this.offsetX+10 : this.maxOffsetX;
	$('#btnIncOffsetX').prop('disabled', this.offsetX==this.maxOffsetX);
	$('#btnDecOffsetX').prop('disabled', false);
	this.refreshCircles();
};
Mission.prototype.decOffsetY = function(valore) {
	this.offsetY = this.offsetY>this.minOffsetY ? this.offsetY-10 : this.minOffsetY;
	$('#btnDecOffsetY').prop('disabled', this.offsetY==this.minOffsetY);
	$('#btnIncOffsetY').prop('disabled', false);
	this.refreshCircles();
};
Mission.prototype.incOffsetY = function(valore) {
	this.offsetY = this.offsetY<this.maxOffsetY ? this.offsetY+10 : this.maxOffsetY;
	$('#btnIncOffsetY').prop('disabled', this.offsetY==this.maxOffsetY);
	$('#btnDecOffsetY').prop('disabled', false);
	this.refreshCircles();
};
Mission.prototype.drawSuctionCup = function(posX, posY, radiusX, radiusY) {
	var x = posX + this.offsetX;
	var y = posY + this.offsetY;
	var suctionCup = this.paper.ellipse(x, y, radiusX, radiusY);
	suctionCup.attr("fill", "#909090");
	suctionCup.attr("stroke", "#FFFFFF");
	suctionCup.node.onclick = function() { 
		if (suctionCup.attr("fill") == "#00FF00") { suctionCup.animate({fill:"#FF0000"},200); }
		else if (suctionCup.attr("fill") == "#FF0000") { suctionCup.animate({fill:"#00FF00"},200); }
		else if (suctionCup.attr("fill") == "#909090") { suctionCup.animate({fill:"#00FF00"},200); }
		else if (suctionCup.attr("fill") == "#FF8000") { suctionCup.animate({fill:"#00FF00"},200); }
	}
	this.suctionCups.push(suctionCup);
};
Mission.prototype.drawSuctionCups = function() {
	this.suctionCups.length = 0;
	for (var i=0; i<cmbS.length; i++) {
		var item = cmbS[i];
		var offset = item.position=='left' ? this.leftWing : this.rightWing;
		this.drawSuctionCup(item.x + offset, item.y, item.dimX, item.dimY);
	}
};
Mission.prototype.drawIcons = function() {
	cmbI.clear();
	drawSheet();
	// metto in grigio chiaro le picked in precedenti missioni
	for (var i=0; i<cmbI.length; i++) {
		for (var j=0; j<app.missions.length; j++) {
			if (app.missions[j].picked.indexOf(cmbI[i]["id"])>-1) { // se picked
				cmbI[i][0].animate({fill:"#AAAAAA"},200);
				cmbI[i][0].data("picked", 1);
			}
		}
	}
	this.icons = cmbI;
};
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
			for (var i=0; i<cmbI.length; i++) {
				if (cmbI[i]["id"] == iconId) {
					cmbI[i][0].animate({fill:"#FFFFFF"},200);
					this.picked.push(cmbI[i]["id"]);
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
	this.paper.clear();
	this.drawIcons();
	this.drawSuctionCups();
	this.checkIntersection();
};
//CLASSE Mission END

var app = {
	missions: new Array(),
	currentMission: null,
	setMission: function(missionNum) {
		if (missionNum <= this.missions.length) {
			var missionDiv = Mustache.render(missionTemplate, {missionNum: missionNum});
			$('.content').append(missionDiv);
			
			var windowWidth = $('#cmbR'+missionNum).width() * 0.95; 
			var windowHeight = $('#cmbR'+missionNum).height() * 0.95; 
			var xRatio = windowWidth / 3048.0; 
			var yRatio = windowHeight / 1524.0; 
			var ratio = (xRatio < yRatio) ? xRatio : yRatio; 

			cmbR = Raphael('cmbR'+missionNum, 3048.0 * ratio, 1524.0 * ratio); 
			cmbR.setViewBox(0,0,3048.0,1524.0); 
			cmbI = cmbR.set(); 
			cmbNotunload = cmbR.set(); 
			cmbPicked = cmbR.set(); 
			var r000 = cmbR.rect(0,0,3048.0,1524.0); 
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
		}
	},
};

var missionTemplate;
$( document ).ready(function() {
	$('body').css('background-color', '#E6E6E6');
	$.get('/media/mission.html', function(d){
		missionTemplate = d;
		app.setMission(0);
	});
});
