if(document.getElementById("timer-days")) {
	var countDownDate = new Date("Mar 14 2020 12:00:00").getTime();
	var x = setInterval(function() {
		var now = new Date().getTime();
		var distance = countDownDate - now;
		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.getElementById("timer-days").innerHTML = days;
		document.getElementById("timer-hours").innerHTML = hours;
		document.getElementById("timer-min").innerHTML = minutes;
		document.getElementById("timer-sec").innerHTML = seconds;
		if (distance < 0) {
			clearInterval(x);
			document.getElementById("timer-days").innerHTML = "00";
			document.getElementById("timer-hours").innerHTML = "00";
			document.getElementById("timer-min").innerHTML = "00";
			document.getElementById("timer-sec").innerHTML = "00";
		}
	}, 1000);
}