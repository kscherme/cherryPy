var theButton = document.getElementById("theButton")

theButton.onclick = changeText

var label = document.createElement("p")

label.setAttribute("id","thelabel")
var textLabel = document.createTextNode("who?")
label.appendChild(textLabel)
document.body.appendChild(label)

function changeText() {

	document.getElementById("thelabel").childNodes[0].nodeValue = "Katie Schermerhorn";


}