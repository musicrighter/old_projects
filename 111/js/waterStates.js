function waterState(temp, unit){
		//For user input error
	place = document.getElementById("outputDiv")
	if (!temp & temp != 0) throw place.innerHTML = 'Please enter at least a temperature'

		// Works for Celsius or Fahrenheit
	if (!unit)
		unit = 'Fahrenheit'
	else if (unit[0].toUpperCase() == 'C'){
		var original = temp
		var change = true
		temp = (temp * 9) / 5 + 32
		unit = 'Celsius'
	}
	else unit = 'Fahrenheit'

		// Regular function
	var state = ""
	if (temp > 21140.6)
		state = "plasma"
	else if (temp >= 212)
		state = "gas"
	else if (temp > 32)
		state = "liquid"
	else
		state = "solid"

		//Put temp back into Celsius
	if (change == true)
		temp = original

	return ('At ' + temp.toLocaleString() + '° ' + unit + ', water is in a <i><b>' + state + '</b></i> state')
}


var button1 = document.getElementsByTagName("input")[2];

button1.onclick = function(){
	document.getElementById("outputDiv").innerHTML =
	waterState(parseFloat(document.getElementById('tempBox').value), 
		       String(document.getElementById('unitBox').value));
};
