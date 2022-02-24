"use strict";

// RPC wrapper
function invoke_rpc(method, args, timeout, on_done){
  $("#crash").hide();
  $("#timeout").hide();
  $("#rpc_spinner").show();
  //send RPC with whatever data is appropriate. Display an error message on crash or timeout
  var xhr = new XMLHttpRequest();
  xhr.open("POST", method, true);
  xhr.setRequestHeader('Content-Type','application/json; charset=UTF-8');
  xhr.timeout = timeout;
  xhr.send(JSON.stringify(args));
  xhr.ontimeout = function () {
    $("#timeout").show();
    $("#rpc_spinner").hide();
    $("#crash").hide();
  };
  xhr.onloadend = function() {
    if (xhr.status === 200) {
      $("#rpc_spinner").hide();
      var result = JSON.parse(xhr.responseText)
      $("#timeout").hide();
      if (typeof(on_done) != "undefined"){
        on_done(result);
      }
    } else {
      $("#crash").show();
    }
  }
}

// Resource load wrapper
function load_resource(name, on_done) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", name, true);
  xhr.onloadend = function() {
    if (xhr.status === 200) {
      var result = JSON.parse(xhr.responseText);
      on_done(result);
    }
  }
  xhr.send();
}

// Code that runs first
$(document).ready(function(){
    // race condition if init() does RPC on function not yet registered by restart()!
    //restart();
    //init();
    invoke_rpc( "/restart", {}, 0, function() { } )
});

function restart() {
  invoke_rpc( "/restart", {} )
}
const sampleCircuit={"junctions": [{"label": "'A'", "pos": [0, 100]}, {"label": "'B'", "pos": [100, 100]}, {"label": "'C'", "pos": [100, 0]}], "wires": [{"id": "'1'", "resistance": 0, "voltage": -5, "pos": [[0, 100], [0, 0], [100, 0]], "soln": 1.0, "current": 1.0, "startJunction": "'A'", "endJunction": "'C'"}, {"id": "'2'", "resistance": 2, "voltage": 0, "pos": [[100, 100], [100, 0]], "soln": -0.09999999999999998, "current": -0.09999999999999998, "startJunction": "'B'", "endJunction": "'C'"}, {"id": "'3'", "resistance": 3, "voltage": 0, "pos": [[0, 100], [100, 100]], "soln": -1.0, "current": -1.0, "startJunction": "'A'", "endJunction": "'B'"}, {"id": "'4'", "resistance": 7, "voltage": 10, "pos": [[100, 0], [200, 0], [200, 100], [100, 100]], "soln": 0.9, "current": 0.9, "startJunction": "'C'", "endJunction": "'B'"}]};

const JUNCTION_RADIUS=3;
const WIRE_THICKNESS=1;
const WIRE_RECTANGLE_THICKNESS=4*JUNCTION_RADIUS;
const BATTERY_WIDTH=6;
const BATTERY_SHORT_LENGTH=12;
const BATTERY_LONG_LENGTH=25;
const BATTERY_SHORT_THICKNESS=2*WIRE_THICKNESS;
const BATTERY_LONG_THICKNESS=WIRE_THICKNESS;
const RESISTANCE_LENGTH=8; 
const RESISTANCE_NUMBER=3; 
const RESISTANCE_ANGLE=15*Math.PI/180; 
const RESISTANCE_WIDTH=4*RESISTANCE_NUMBER*RESISTANCE_LENGTH*Math.sin(RESISTANCE_ANGLE);

const mainElement=document.getElementById("circuit");
const testElement=document.getElementById("details");
const messageElement=document.getElementById("message");
const selectorElement=document.getElementById("selector");
const svgElementInit=document.createElementNS("http://www.w3.org/2000/svg","svg");

const hoverColor = '#005BFF';

var previousSelectedWire=undefined;
var previousSelectedWireColor=undefined;

var loadedTestCase=undefined;

var junctions = {};
var wires = {};
var junctionNext = {};

function displayFloat(value) {
	return Math.round(value*1000000)/1000000;
}

function highlight(element) {
	if(previousSelectedWire) {
		previousSelectedWire.setAttribute("stroke",previousSelectedWireColor);
		previousSelectedWire.setAttribute("fill",previousSelectedWireColor);
		previousSelectedWire=undefined;
	}
	previousSelectedWire=element;
	previousSelectedWireColor=previousSelectedWire.getAttribute("stroke");
	previousSelectedWire.setAttribute("stroke",hoverColor);
	previousSelectedWire.setAttribute("fill",hoverColor);
}

function handleMouseLeave() {
	if(testElement.classList.contains("show")) {
		testElement.classList.remove("show");
	}
	if(previousSelectedWire) {
		previousSelectedWire.setAttribute("stroke",previousSelectedWireColor);
		previousSelectedWire.setAttribute("fill",previousSelectedWireColor);
		previousSelectedWire=undefined;
	}
}

function displayWireDetails(wireNumber) {
	if(!testElement.classList.contains("show")) {
		testElement.classList.add("show");
	}
	highlight(document.getElementById("wire_"+wireNumber));
	var detailString="<center><b>Wire Details</b></center> \n\nID: "+wires[wireNumber]["id"]+"\n<br>\nStarting Junction: "+wires[wireNumber]["startJunction"]+"\n<br>\nEnding Junction: "+wires[wireNumber]["endJunction"]+"\n<br>\nResistance: "+displayFloat(wires[wireNumber]["resistance"])+"\n<br>\nBattery Voltage:      "+displayFloat(wires[wireNumber]["voltage"])+"\n<br>\nExpected Current: "+displayFloat(wires[wireNumber]["soln"]);
	if(wires[wireNumber]["current"]!==undefined) {
		detailString+="\n<br>\nReturned Current: "+displayFloat(wires[wireNumber]["current"])+"\n<br>\nDifference: "+displayFloat(wires[wireNumber]["current"]-wires[wireNumber]["soln"])+"\n<br>\n<center><b>\n"+((Math.abs(wires[wireNumber]["current"]-wires[wireNumber]["soln"])<1e-5 ? "Correct!":"Incorrect Current")+"\n</b></center>");
	} 
	testElement.innerHTML=detailString+"";
}

function displayJunctionDetails(junctionNumber) {
	if(!testElement.classList.contains("show")) {
		testElement.classList.add("show");
	}
	highlight(document.getElementById("junction_"+junctionNumber));
	var detailString="<center><b>Junction Name</b><br> "+junctions[junctionNumber]["label"]+"\n</center>";
	testElement.innerHTML=detailString;
}

function angleCompare(angle1,angle2) {
	return angle1-angle2;
}

function getLabelPosition(pos,neighbors,textSize,label) {
	const angles=[];
	for(var neighbor of neighbors) {
		angles.push(getAngle(pos,neighbor));
	}
	var angle=0;
	var maxDiff=0;
	var foundSubOpt=false;
	angles.sort(angleCompare);
	angles.push(angles[0]);
	for(var angnum=0;angnum<angles.length-1;angnum++) {
		var diff=angles[angnum+1]-angles[angnum];
		while(diff<0) {
			diff+=2*Math.PI;
		}
		if(diff>=Math.PI-0.0001) {
			angle=angles[angnum]+diff/2;
			break;
		}
		if(diff>=50*Math.PI/180&&Math.abs(angles[angnum+1])<=10*Math.PI/180) {
			angle=angles[angnum]+diff/2;
			foundSubOpt=true;
		}
		if(!foundSubOpt&&diff>maxDiff) {
			maxDiff=diff;
			angle=angles[angnum]+diff/2;
		}
	}
	const centerPosition=getLineOfLengthEnd(pos,3+JUNCTION_RADIUS+Math.sqrt(textSize[0]*textSize[0]+textSize[1]*textSize[1])/2,angle);
	return [Math.round(centerPosition[0]-0.4*textSize[0]),Math.round(centerPosition[1]+0.333*textSize[1])];
}

function addJunction(x,y,label,svgElement,junctionNum) {
    const junctionGroup=document.createElementNS("http://www.w3.org/2000/svg","g");
	junctionGroup.setAttribute("id","junction_"+junctionNum);
	junctionGroup.setAttribute("fill","black");
    junctionGroup.addEventListener("mouseenter",()=>displayJunctionDetails(junctionNum));
    junctionGroup.addEventListener("mouseleave",handleMouseLeave);

	const junction=document.createElementNS("http://www.w3.org/2000/svg","circle");
	junction.setAttribute("cx", x);
    junction.setAttribute("cy", y);
    junction.setAttribute("r", JUNCTION_RADIUS);
    junction.setAttribute("id",label);

    const junctionLabel = document.createElementNS("http://www.w3.org/2000/svg","text");

    const junctionName = junctions[junctionNum]['label'].substring(1,junctions[junctionNum]['label'].length-1);
    junctionLabel.setAttribute("font-size","10px");
    junctionLabel.setAttribute("id", "junctiontext_"+junctionNum);
    const junctionText = document.createTextNode(junctionName);
    junctionLabel.appendChild(junctionText);
    junctionGroup.appendChild(junction);
    junctionGroup.appendChild(junctionLabel);
    svgElement.appendChild(junctionGroup);
    const bbox=junctionLabel.getBBox();
    const position = getLabelPosition([x,y],junctionNext[junctions[junctionNum]['label']],[bbox.width,bbox.height],junctions[junctionNum]['label']);
    junctionLabel.setAttribute("x",position[0]);
    junctionLabel.setAttribute("y",position[1]);
}

function getDist(start,end) {
	return Math.sqrt((start[0]-end[0])*(start[0]-end[0])+(start[1]-end[1])*(start[1]-end[1]));
}

function getAngle(start,end) {
	return Math.atan2(end[1]-start[1],end[0]-start[0]);
}

function getLine(start,end) {
	const line=document.createElementNS("http://www.w3.org/2000/svg","line");
	line.setAttribute("x1",Math.round(start[0]));
    line.setAttribute("y1",Math.round(start[1]));
    line.setAttribute("x2",Math.round(end[0]));
    line.setAttribute("y2",Math.round(end[1]));
    return line;
}

function getRectangle(start,end) {
	const rectangle=document.createElementNS("http://www.w3.org/2000/svg","rect");
	rectangle.setAttribute("x",Math.round(start[0]));
    rectangle.setAttribute("y",Math.round(start[1]-WIRE_RECTANGLE_THICKNESS/2));
    rectangle.setAttribute("height",WIRE_RECTANGLE_THICKNESS);
    rectangle.setAttribute("width",getDist(start,end));
    rectangle.setAttribute("stroke","none");
    rectangle.setAttribute("fill","white");
    rectangle.setAttribute("transform","rotate("+(180*getAngle(start,end)/Math.PI)+" "+start[0]+" "+start[1]+")");
    return rectangle;
}

function getLineOfLength(start,end,length) {
	const dist=getDist(start,end);
	return getLine(start,[start[0]+(end[0]-start[0])*length/dist,start[1]+(end[1]-start[1])*length/dist]);
}

function getLineOfLengthEnd(start,length,angle) {
	return [start[0]+length*Math.cos(angle),start[1]+length*Math.sin(angle)];
}

function getLineOfLengthAtAngle(start,length,angle) {
	return [getLine(start,getLineOfLengthEnd(start,length,angle)),getLineOfLengthEnd(start,length,angle)];
}

function getBattery(start,angle) {
	const nextStart=[start[0]+BATTERY_WIDTH*Math.cos(angle),start[1]+BATTERY_WIDTH*Math.sin(angle)];
	const battery=[getLineOfLengthAtAngle(start,BATTERY_SHORT_LENGTH/2,angle+Math.PI/2)[0],getLineOfLengthAtAngle(start,BATTERY_SHORT_LENGTH/2,angle-Math.PI/2)[0],getLineOfLengthAtAngle(nextStart,BATTERY_LONG_LENGTH/2,angle+Math.PI/2)[0],getLineOfLengthAtAngle(nextStart,BATTERY_LONG_LENGTH/2,angle-Math.PI/2)[0]];
	battery[0].setAttribute("stroke-width", BATTERY_SHORT_THICKNESS);
	battery[1].setAttribute("stroke-width", BATTERY_SHORT_THICKNESS);
	battery[2].setAttribute("stroke-width", BATTERY_LONG_THICKNESS);
	battery[3].setAttribute("stroke-width", BATTERY_LONG_THICKNESS);
	return battery;
}

function getBatteryWire(start,end) {
	const angle=getAngle(start,end);
	const length=getDist(start,end);
	const firstSegment=getLineOfLengthAtAngle(start,(length-BATTERY_WIDTH)/2,angle);
	const battery=getBattery(firstSegment[1],angle);
	const secondSegment=getLineOfLengthAtAngle(end,(length-BATTERY_WIDTH)/2,angle+Math.PI);
	return [firstSegment[0],secondSegment[0]].concat(battery);
}

function getResistor(start,angle) {
	var nstart=start;
	const resistor=[];
	for(var j=0;j<RESISTANCE_NUMBER;j++) {
		const firstSegment=getLineOfLengthAtAngle(nstart,RESISTANCE_LENGTH,angle-Math.PI/2+RESISTANCE_ANGLE);
		nstart=firstSegment[1];
		resistor.push(firstSegment[0]);
		const secondSegment=getLineOfLengthAtAngle(nstart,2*RESISTANCE_LENGTH,angle+Math.PI/2-RESISTANCE_ANGLE);
		nstart=secondSegment[1];
		resistor.push(secondSegment[0]);
		const thirdSegment=getLineOfLengthAtAngle(nstart,RESISTANCE_LENGTH,angle-Math.PI/2+RESISTANCE_ANGLE);
		nstart=thirdSegment[1];
		resistor.push(thirdSegment[0]);
	}
	return resistor;
}

function getResistanceWire(start,end) {
	const angle=getAngle(start,end);
	const length=getDist(start,end);
	const firstSegment=getLineOfLengthAtAngle(start,(length-RESISTANCE_WIDTH)/2,angle);
	const resistor=getResistor(firstSegment[1],angle);
	const secondSegment=getLineOfLengthAtAngle(end,(length-RESISTANCE_WIDTH)/2,angle+Math.PI);
	return [firstSegment[0],secondSegment[0]].concat(resistor);
}

function getDoubleWire(start,end) {
	const angle=getAngle(start,end);
	const length=getDist(start,end);
	const firstSegment=getLineOfLengthAtAngle(start,length/3-BATTERY_WIDTH/2,angle);
	const battery=getBattery(firstSegment[1],angle);
	const secondSegment=getLineOfLengthAtAngle(end,length/3-RESISTANCE_WIDTH/2,angle+Math.PI);
	const batteryEnd=getLineOfLengthEnd(start,length/3+BATTERY_WIDTH/2,angle);
	const thirdSegment=getLineOfLengthAtAngle(batteryEnd,length/3-BATTERY_WIDTH/2-RESISTANCE_WIDTH/2,angle);
	const resistor=getResistor(thirdSegment[1],angle);
	return [firstSegment[0],secondSegment[0],thirdSegment[0]].concat(battery).concat(resistor);
}

function addWire(resistance,voltage,pos,id,svgElement,wireColor,wireNumber,endpoint) {
	if(junctionNext[endpoint[0]]===undefined) {
		junctionNext[endpoint[0]]=[];
	}
	if(junctionNext[endpoint[1]]===undefined) {
		junctionNext[endpoint[1]]=[];
	}
	junctionNext[endpoint[0]].push(pos[1]);
	junctionNext[endpoint[1]].push(pos[pos.length-2]);
	if(voltage<0) {
		pos.reverse();
	}
	const numSegments=pos.length-1;
	const segmentType=[];
	for(var i=0;i<numSegments;i++) {
		segmentType.push(0);
	}
	if(resistance!==0.0) {
		if(voltage!==0.0) {
			if(numSegments===1) {
				segmentType[0]=3;
			} else {
				segmentType[Math.floor(numSegments/3)]=2;
				segmentType[numSegments-1-Math.floor(numSegments/3)+(numSegments==3 ? 1:0)]=1;
			}
		} else {
			segmentType[Math.floor(numSegments/2)]=1;
		}
	} else if (voltage!==0) {
		segmentType[Math.floor(numSegments/2)]=2;
	}
	const group=document.createElementNS("http://www.w3.org/2000/svg","g");
	group.setAttribute("stroke",wireColor);
	group.setAttribute("stroke-width",WIRE_THICKNESS+(wireColor==="darkred" ? 1:0));
	group.setAttribute("id",id);
	for(var i=0;i<numSegments;i++) {
		if(segmentType[i]===0) {
			group.appendChild(getLine(pos[i],pos[i+1]));
		} else if(segmentType[i]===1) {
			for(var element of getResistanceWire(pos[i],pos[i+1])) {
				group.appendChild(element);
			}			
		} else if(segmentType[i]===2) {
			for(var element of getBatteryWire(pos[i],pos[i+1])) {
				group.appendChild(element);
			}			
		} else {
			for(var element of getDoubleWire(pos[i],pos[i+1])) {
				group.appendChild(element);
			}
		}
	}
    group.addEventListener("mouseleave",handleMouseLeave);
	group.addEventListener("mouseover",()=>displayWireDetails(wireNumber));
	svgElement.appendChild(group);
}

function addWireRectangle(pos,id,svgElement,wireNumber) {
	const numSegments=pos.length-1;
	const segmentType=[];
	const group=document.createElementNS("http://www.w3.org/2000/svg","g");
	group.setAttribute("id",id+"_rectangle");
	for(var i=0;i<numSegments;i++) {
		group.appendChild(getRectangle(pos[i],pos[i+1]));
	}
    group.addEventListener("mouseleave",handleMouseLeave);
	group.addEventListener("mouseover",()=>displayWireDetails(wireNumber));
	svgElement.appendChild(group);
}

function getDimensions(circuit) {
	var maxx=-1000000;
	var minx=1000000;
	var maxy=-1000000;
	var miny=1000000;
	for(var wire of circuit.wires) {
		for(var wirepos of wire.pos) {
			maxx=(wirepos[0]>maxx ? wirepos[0]:maxx);
			minx=(wirepos[0]<minx ? wirepos[0]:minx);
			maxy=(wirepos[1]>maxy ? wirepos[1]:maxy);
			miny=(wirepos[1]<miny ? wirepos[1]:miny);
		}
	}
	return [[minx,maxx],[miny,maxy]];
}

function renderCircuit(circuit) {
	if(circuit.error!==undefined) {
		messageElement.innerHTML="Your code crashed with the following error message.<br><br><tt>"+circuit.error.split("\n").join("</tt><br><tt>")+"</tt>";
		return;
	} 
	junctions={};
	wires={};
	junctionNext={};
	const dimensions=getDimensions(circuit);
	const svgElement=document.createElementNS("http://www.w3.org/2000/svg","svg");
	svgElement.setAttribute("width",dimensions[0][1]-dimensions[0][0]+2*BATTERY_LONG_LENGTH+60);
	svgElement.setAttribute("height",dimensions[1][1]-dimensions[1][0]+2*BATTERY_LONG_LENGTH);
	svgElement.setAttribute("xmlns","http://www.w3.org/2000/svg");
	mainElement.childNodes[0].remove();
	mainElement.appendChild(svgElement);
	var xoffset=dimensions[0][0]-BATTERY_LONG_LENGTH-30;
	var yoffset=dimensions[1][1]+BATTERY_LONG_LENGTH;
	var wireNum=0;
	for(var wire of circuit.wires) {
		for(var wirepos of wire.pos) {
			wirepos[0]=wirepos[0]-xoffset;
			wirepos[1]=yoffset-wirepos[1];
		}
		wireNum++;
		wires[wireNum]=wire;
		addWireRectangle(wire.pos,"wire_"+wireNum,svgElement,wireNum);
	}
	wireNum=0;
	var isCorrect=true;
	for(var wire of circuit.wires) {
		wireNum++;
		const wireColor=(wire.current===undefined ? "black":(wire.current-wire.soln>1e-5||wire.current-wire.soln<-1e-5 ? "darkred":"#01da93"));
		if(wire.current===undefined||wireColor==="darkred") {
			isCorrect=false;
		}
		addWire(wire.resistance,wire.voltage,wire.pos,"wire_"+wireNum,svgElement,wireColor,wireNum,[wire.startJunction,wire.endJunction]);
	}
	var junctionNum=0;
	for(var junction of circuit.junctions) {
		junction.pos=[junction.pos[0]-xoffset,yoffset-junction.pos[1]];
		junctionNum++;
		junctions[junctionNum]=junction;
		addJunction(junction.pos[0],junction.pos[1],"junction_"+junctionNum,svgElement,junctionNum);
	}
	if(!isCorrect) {
		messageElement.innerHTML="Your code either produced an incorrect output.";
	} else {
		messageElement.innerHTML="All currents are correct!";
	}
}

function loadCircuit() {
	if(!selectorElement.value) {
		return;
	}
	const testCase="SolveCircuit_"+selectorElement.value;
	messageElement.innerHTML="Loading test case ...";
	invoke_rpc("/load",testCase,10000,(solution)=>{loadedTestCase=testCase;renderCircuit(solution);messageElement.innerHTML="Circuit loaded!";});
}

function runCode() {
	if(loadedTestCase) {
		messageElement.innerHTML="Your code is running ...";
  		invoke_rpc("/runTest",loadedTestCase,360000,(solution)=>{renderCircuit(solution);});
  	} else {
  		messageElement.innerHTML="Please select a test case first by using the above drop down menu.";
  	}
}