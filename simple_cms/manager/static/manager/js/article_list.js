/*
*  Container is the place where the ArticleList will draw itself and its a jquery element
*/

function ArticleList(container){
	self = this;
	this.container = container;
	this.content = {};

	this.update = function(){
		$.ajax({
			url: "/get_articles/",
			type: "GET",
			success: function(data){
				self.content = data;
				self.render();
			}
		});
	}

	this.render = function(){
		var article_list = "";

		for (var i = 0; i < self.content["articles"].length; i++) {
			article_list += "<tr><td><a href='/" + self.content["articles"][i]["link"] + "'>" + self.content["articles"][i]["title"] + "</a></td></tr>";
		}

		var article_list_final = "<div class=\"panel panel-default\">"
		  + "<div class=\"panel-heading\"><h2>Available Articles</h2></div>" 
		  + "<table class=\"table\">"
			+ "<tbody>"
		    	+ article_list
		    + "</tbody>"
		  + "</table>"
		+ "</div>";

		this.container.empty();
		this.container.append(article_list_final);
	}
}