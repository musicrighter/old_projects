function timelyMsg(){
	var time = new Date()
	var hours = time.getHours()

	if (hours >= 0 && hours < 12)
		return 'Good morning!';

	else if (hours >= 12 && hours < 17)
		return 'Good afternoon!';

	else if (hours >= 17 && hours < 21)
		return 'Good evening!';

	else 
		return 'Good night!';
}

var button1 = document.getElementById("btn1");

button1.onclick = function(){
	document.getElementById('h3').innerHTML = timelyMsg();
};

