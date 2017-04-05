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

var ratinglabel = new Label();
ratinglabel.createlabel("I thought this movie was...", "theLabel");
ratinglabel.addToDocument();

Dropdown.prototype = new Item();
var dropdown = new Dropdown();
var dropdownDict = {1:"Just Plain Bad", 2:"Not So Good", 3:"OK I Guess", 4:"Pretty Good", 5:"Awesome!"};
dropdown.createDropdown(dropdownDict, "ratingDropdown", "Awesome!");
dropdown.addToDocument();

var dropdownButton = new Button();
dropdownButton.createButton("Vote", "myButton");
dropdownButton.addToDocument();
dropdownButton.addCLickEventHandler(voteEventHandler, dropdown);
console.log("value selected: ", dropdown.getSelected());

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

function voteEventHandler(dropdown) {
	var rating = dropdown.getSelected();
	var xhr = new XMLHttpRequest();
	xhr.open("PUT", "http://ash.campus.nd.edu:40001/recommendations/24", true);
	xhr.onload = function(e) {
		console.log(xhr.responseText);
	};
	xhr.onerror = function(e) {
		console.error(xhr.statusText);
	};
	data = {"movie_id":32, "rating":rating};
	jsondata = JSON.stringify(data);
	xhr.send(jsondata);



}