import showdown from "showdown";
var converter = new showdown.Converter();

var text = document.getElementById('description').innerHTML;

var html = converter.makeHtml(text);
document.getElementById('description').innerHTML = html;
