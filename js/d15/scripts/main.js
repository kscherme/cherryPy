Label.prototype = new Item();
var mylabel = new Label();
mylabel.createlabel("which movie?", "theLabel");
mylabel.addToDocument();

Button.prototype = new Item();
var mybutton = new Button();
mybutton.createButton("Click Here", "theButton");
mybutton.addToDocument();

args = [mylabel];
mybutton.addCLickEventHandler(changeText, args);

function changeText(args) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://ash.campus.nd.edu:40001/movies/32", true);
	xhr.onload = function(e) {
		args[0].setText(xhr.responseText);
	};
	xhr.onerror = function(e) {
		console.error(xhr.statusText);
	};
	xhr.send(null);
}