function arrAvg (array) {
	var total = 0
	for (var i = 0; i < array.length; i++) {
		total += array[i]
	};
	return total/array.length
}

function arrMax (array) {
	return Math.max.apply(Math, array)
}

function arrHasOneEven (array) {
	for (var i = 0; i < array.length; i++) {
		if (array[i] % 2 === 0)
			return true
	};
	return false
}
