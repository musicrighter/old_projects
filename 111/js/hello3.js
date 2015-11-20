//Define a simple function. Does not return a value.
 
var hello3 = function(){
	var name = prompt("Enter your name", "Anon.");
	alert("Hello, " + name + "!");
	document.write("Hello, " + name + "!");
}
 
//register onload handler
window.onload = hello3;