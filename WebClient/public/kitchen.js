function updateTime() {
	let date = new Date();
	let hour = date.getHours();
	let min = date.getMinutes();
	let ending = "AM";
	if (min < 10)
		min = "0" + min;
	if (hour>11) {
		hour -= 12;
		if (hour == 0)
			hour = 12;
		ending = "PM";
	}
	document.getElementById('time').innerHTML = hour + ":" + min + " " + ending;
	t = setTimeout(function() {
		updateTime()
	}, 500);
}

updateTime();