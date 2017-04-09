// Create movie title label
Label.prototype = new Item();
var movieLabel = new Label();
movieLabel.createlabel("title", "movieLabel");
movieLabel.addToDocument();

// Create up and down button
Button.prototype = new Item();
var upbutton = new Button();
upbutton.createButton("UP", "upbutton");
upbutton.addToDocument();

// Create image 
Image.prototype = new Item();
var img = new Image();
img.createImage("http://www.cse.nd.edu/~cmc/teaching/cse30332/images/agy8DheVu5zpQFbXfAdvYivF2FU.jpg", "img");
img.addToDocument();

Button.prototype = new Item();
var downbutton = new Button();
downbutton.createButton("DOWN", "downButton");
downbutton.addToDocument();


// Create rating label
Label.prototype = new Item();
var ratingLabel = new Label();
ratingLabel.createlabel("rating", "ratingLabel");
ratingLabel.addToDocument();

var MID;
var uid = 32;
args = [movieLabel, ratingLabel];

// set up css
Div.prototype = new Item();
var divupbutton = new Div();
divupbutton.createDiv("buttons");
divupbutton.addItemToDiv(upbutton);
var divdownbutton = new Div();
divdownbutton.createDiv("buttons");
divdownbutton.addItemToDiv(downbutton);
var divimage = new Div();
divimage.createDiv("image");
divimage.addItemToDiv(img);
var divtitle = new Div();
divtitle.createDiv("top");
divtitle.addItemToDiv(movieLabel);
var divrating = new Div();
divrating.createDiv("bottom");
divrating.addItemToDiv(ratingLabel);
var middle = new Div();
middle.createDiv("middle");
middle.addItemToDiv(divupbutton);
middle.addItemToDiv(divimage);
middle.addItemToDiv(divdownbutton);
var main = new Div();
main.createDiv("main");
main.addItemToDiv(divtitle);
main.addItemToDiv(middle);
main.addItemToDiv(divrating);
main.addToDocument();



// get initial recs
get_rec(args);

upbutton.addCLickEventHandler(upVoteMovieHandler, args);
downbutton.addCLickEventHandler(downVoteMovieHandler, args);


function upVoteMovieHandler(args) {

	putRequest(5);

}

function downVoteMovieHandler(args) {
	putRequest(1);

}


function putRequest(vote) {

	var xhr = new XMLHttpRequest();
	var site = "http://ash.campus.nd.edu:40100/recommendations/" + uid;
	xhr.open("PUT", site, true);

	xhr.onload = function(e) {
		if(xhr.readyState == 4) {
			console.log(xhr.responseText);

			var uid = 32;

			var xhr1 = new XMLHttpRequest();
			var rec_site = "http://ash.campus.nd.edu:40100/recommendations/" + uid;
			xhr1.open("GET", rec_site, true);

			xhr1.onload = function(e) {
				var rec_output = xhr1.responseText;
				var json_rec_output = JSON.parse(rec_output);
				var mid = json_rec_output["movie_id"]
				setMID(mid);
				console.log("New: ", MID);

				var xhr2 = new XMLHttpRequest();
				var movie_site = "http://ash.campus.nd.edu:40100/movies/" + mid;

				xhr2.open("GET", movie_site, true);
				xhr2.onload = function(e) {
					var movie_output = xhr2.responseText;
					var json_movie_output = JSON.parse(movie_output);
					var movie_title = json_movie_output["title"];
					var link = json_movie_output["img"];
					var src = "http://www.cse.nd.edu/~cmc/teaching/cse30332/images" + link;
					img.changeSource(src);
					args[0].setText(movie_title);

					var xhr3 = new XMLHttpRequest();
					var rating_site = "http://ash.campus.nd.edu:40100/ratings/" + mid;

					xhr3.open("GET", rating_site, true);
					xhr3.onload = function(e) {
						var rating_output = xhr3.responseText;
						var json_rating_output = JSON.parse(rating_output);
						var rating = json_rating_output["rating"];
						args[1].setText(rating);
						
					};
					xhr3.onerror = function(e) {
						console.error(xhr3.statusText);
					};
					xhr3.send(null);
				};
				xhr2.onerror = function(e) {
					console.error(xhr2.statusText);
				};
				xhr2.send(null);
			};
			xhr1.onerror = function(e) {
				console.error(xhr.statusText);
			};
			xhr1.send(null);
		}
	};
	xhr.onerror = function(e) {
		console.error(xhr.statusText);
	};
	console.log("Put: ", MID);
	data = {"movie_id":MID, "rating":vote};
	jsondata = JSON.stringify(data);
	xhr.send(jsondata);


}

function get_rec(args) {

	var xhr = new XMLHttpRequest();
	var site = "http://ash.campus.nd.edu:40100/reset/";
	xhr.open("PUT", site, true);

	xhr.onload = function(e) {
		if(xhr.readyState == 4) {
			console.log(xhr.responseText);


		var xhr1 = new XMLHttpRequest();
		var rec_site = "http://ash.campus.nd.edu:40100/recommendations/" + uid;
		xhr1.open("GET", rec_site, true);
		xhr1.onload = function(e) {
			var rec_output = xhr1.responseText;
			var json_rec_output = JSON.parse(rec_output);
			var mid = json_rec_output["movie_id"];
			setMID(mid);
			console.log("Starting: ", MID);

			var xhr2 = new XMLHttpRequest();
			var movie_site = "http://ash.campus.nd.edu:40100/movies/" + mid;

			xhr2.open("GET", movie_site, true);
			xhr2.onload = function(e) {
				var movie_output = xhr2.responseText;
				var json_movie_output = JSON.parse(movie_output);
				var movie_title = json_movie_output["title"];
				var link = json_movie_output["img"];
				var src = "http://www.cse.nd.edu/~cmc/teaching/cse30332/images" + link;
				img.changeSource(src);
				args[0].setText(movie_title);

				var xhr3 = new XMLHttpRequest();
				var rating_site = "http://ash.campus.nd.edu:40100/ratings/" + mid;

				xhr3.open("GET", rating_site, true);
				xhr3.onload = function(e) {
					var rating_output = xhr3.responseText;
					var json_rating_output = JSON.parse(rating_output);
					var rating = json_rating_output["rating"];
					args[1].setText(rating);
					
				};
				xhr3.onerror = function(e) {
					console.error(xhr3.statusText);
				};
				xhr3.send(null);
			};
			xhr2.onerror = function(e) {
				console.error(xhr2.statusText);
			};
			xhr2.send(null);
		};
		xhr1.onerror = function(e) {
			console.error(xhr1.statusText);
		};
	xhr1.send(null);
		}

	};
	xhr.onerror = function(e) {
		console.error(xhr.statusText);
	};

	xhr.send(null);
}

function setMID(mid){
	MID = mid;
}

function getMID() {
	return MID;
}