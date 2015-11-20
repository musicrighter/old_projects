var calculateTip = function(amount, tipPct){
    var tip = amount * (tipPct/100);
    message = 'You should tip $' + tip.toFixed(2);
    return message
	}

var button1 = document.getElementsByTagName("input")[2];

button1.onclick = function(){
	document.getElementById("outputDiv").innerHTML =
	calculateTip(document.getElementById('amountBox').value, 
		         document.getElementById('tipBox').value);
};