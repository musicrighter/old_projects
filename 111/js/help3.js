//select the button
var button1 = document.getElementById("btn1");
 
//register the onclick handler
button1.onclick = function() {
   document.getElementById('outputDiv').innerHTML = 
   'If you have any trouble with this site, ' + 'contact <i>admin@foo.bar</i>.'; 
};