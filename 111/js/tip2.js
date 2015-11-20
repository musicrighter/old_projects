function calculateTip(){
	var amount = document.getElementById('amountBox').value;
    var tipPct = document.getElementById('tipBox').value;
    var tip = amount * (tipPct/100);
    document.getElementById('outputDiv').innerHTML = 
    'You should tip $' + tip.toFixed(2);
	}

var button1 = document.getElementsByTagName("input")[2];

button1.onclick = calculateTip;