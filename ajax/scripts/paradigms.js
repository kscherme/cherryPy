function Item() {
	this.addToDocument= function() {
		document.body.appendChild(this.item);
	}
};

function Label() {
	this.createlabel= function(text, id) {
		this.item = document.createElement("p");
		this.item.setAttribute("id",id);
		var textLabel = document.createTextNode(text);
		this.item.appendChild(textLabel);
	}

	this.setText= function(text) {
		this.item.innerHTML = text;
	}

};

function Image() {
	this.createImage= function(src, id) {
		this.item = document.createElement("img");
		this.item.setAttribute("id", id);
		this.item.setAttribute("src", src);
	}

	this.changeSource= function(src) {
		this.item.setAttribute("src", src);
	}
};

function Button() {
	this.createButton= function(text, id) {
		this.item = document.createElement("button");
		this.item.setAttribute("id", id);
		var textButton = document.createTextNode(text);
		this.item.appendChild(textButton);
	}

	this.addCLickEventHandler= function(handler, args) {
		this.item.onmouseup = function() {
			handler(args);
		}; 
	}
};

function Div() {
	this.createDiv= function(id) {
		this.item = document.createElement("div");
		this.item.setAttribute("id", id);
	}

	this.addItemToDiv= function(item) {
		this.item.appendChild(item.item);

	}
};