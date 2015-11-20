function driver(n){
	var reverse = reverseN(n);
	var diff = reverse - n;
	var diffReverse = reverseN(diff);
	var sum = diff + Number(diffReverse);

	var message = 'The reverse of ' + n + ' is ' + reverse + '<br>' +
				  'The difference between ' + n + ' and ' + reverse + ' is ' + diff + '<br>' +
				  'The reverse difference is ' + diffReverse + '<br>' +
				  'The sum of the difference and reverse difference is ... (Drum roll, please ;-) <br>' + sum;
	return message
}

button1 = document.getElementById('btn1');

button1.onclick = function(){
	n = document.getElementById('inBox').value;
	document.getElementById('outDiv').innerHTML = driver(n);
};
