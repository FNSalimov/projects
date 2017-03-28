jQuery('document').ready(function() {
	var top_flag = true;
	var left_flag = false;
	function ball() {
		var val = jQuery('#ball').offset();
		if (val.top >= jQuery(window).height() - 39)
			top_flag = false;
		if (val.left >= jQuery(window).width() - 39)
			left_flag = false;
		if (val.top <= 0)
			top_flag = true;
		if (val.left <= 15)
			left_flag = true;
		jQuery('#ball').offset({top:(top_flag)?val.top+10:val.top-10, left:(left_flag)?val.left+10:val.left-10});
	}
	setInterval(ball, 10);

});