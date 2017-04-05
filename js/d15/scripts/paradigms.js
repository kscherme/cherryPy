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

function Dropdown() {
	this.createDropdown= function(dict, id, selected) {
		// Create form HTML element
		this.item = document.createElement("select");
		this.item.setAttribute("id", id);

		for (var key in dict) {

			var tmp = document.createElement("option");
			tmp.setAttribute("value", key);
			tmp.setAttribute("label", dict[key]);
			if(dict[key] === selected){
				tmp.setAttribute("selected", "selected");
			}
			this.item.appendChild(tmp);
		}

	}

	this.getSelected= function() {
		return (this.item.options[this.item.selectedIndex].value);
	}
}