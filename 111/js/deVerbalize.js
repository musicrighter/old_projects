function charToNumber (char) {
	var alphabet = 'abc  def  ghi  jkl  mno  pqrs tuv  wxyz';
	var lower = char.toLowerCase();

	if (/[a-z]/.test(lower)){
		return Math.floor(alphabet.indexOf(lower) / 5 ) + 2;
	}
	else return char
}

function deVerbalize (num) {
	var number = ''
	for (var i = 0; i < num.length; i++) {
		number += charToNumber(num[i])
	};
	return number
}

button1 = document.getElementById('btn1');

button1.onclick = function(){
	document.getElementById('outSpan').innerHTML =
	deVerbalize(document.getElementById('inBox').value)
}