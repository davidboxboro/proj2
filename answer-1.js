var cookie = document.cookie.split('; ').filter(
	function(r) { return r.indexOf('PyZoobarLogin=') != -1; }
)[0];
alert(cookie);
