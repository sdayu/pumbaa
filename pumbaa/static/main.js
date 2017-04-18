import showdown from "showdown";


$(".button-collapse").sideNav();

let converter = new showdown.Converter();
let comments = document.getElementById("show-last-comments").querySelectorAll("div[id^=comment-]");
comments.forEach(function(comment){
	let comment_html = converter.makeHtml(comment.innerHTML);
	comment.innerHTML = comment_html;
});

