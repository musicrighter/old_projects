function toWord (num) {
	if (num < 1){
		return 'too small'
	}
	else if (num === 1){
		return 'one'
	}
	else if (num === 2){
		return 'two'
	}
	else if (num === 3){
		return 'three'
	}
	else if (num === 4){
		return 'four'
	}
	else return 'too large'
}

button1 = document.getElementById('btn1')

button1.onclick = function(){
	var number = Number(document.getElementById('num').value)
	document.getElementById('h3').innerHTML = toWord(number);
};

