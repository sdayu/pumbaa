import showdown from "showdown";



var converter = new showdown.Converter( { extensions: [ 'mathjax' ] } );

var text = document.getElementById('description').innerHTML;

var html = converter.makeHtml(text);
document.getElementById('description').innerHTML = html;

$(".button-collapse").sideNav();


