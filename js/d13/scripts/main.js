
var Item = {
	addToDocument: function() {
		document.body.appendChild(this.item);
	}
};

var Label = {
	createlabel: function(text, id) {
		this.item = document.createElement("p");
		this.item.setAttribute("id",id);
		var textLabel = document.createTextNode(text);
		this.item.appendChild(textLabel);
	},

	setText: function(text) {
		this.item.innerHTML = text;
	}

};

var Button = {
	createButton: function(text, id) {
		this.item = document.createElement("button");
		this.item.setAttribute("id", id);
		var textButton = document.createTextNode(text);
		this.item.appendChild(textButton);
	},

	addCLickEventHandler: function(handler, args) {
		this.item.onmouseup = function() {
			handler(args);
		}; 
	}
};

function changeText(args) {
	args[1].setText(args[0]);
}

Button.__proto__= Item;
Button.createButton("Click Here", "theButton");
args = ["Katie Schermerhorn", Label ];
Button.addCLickEventHandler(changeText, args);
Button.addToDocument();

Label.__proto__= Item;
Label.createlabel("guess who", "theLabel");
Label.addToDocument();
