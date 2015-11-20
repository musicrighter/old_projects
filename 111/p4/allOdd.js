function allOdd (array) {
	for (var i = 0; i < array.length; i++) {
		if (array[i] % 2 == 0)
			return false
	};
	return true
}

/*function allOdd (arr) {
	var result;
	result = arr.every(function(num){
		return (num % 2 == 1);
	} );
	return result;
}*/
