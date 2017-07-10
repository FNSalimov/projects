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
	jQuery(document).keyup(function(e) {
		var valleft = jQuery('#left').offset();
		var valright = jQuery('#right').offset();
		var win_height = jQuery(window).height();
		if (e.which == 87 && valleft.top > 0)
			jQuery('#left').offset({top: valleft.top-20, left: valleft.left});
		if (e.which == 83 && valleft.top < win_height - 160)
			jQuery('#left').offset({top: valleft.top+20, left: valleft.left});
		if (e.which == 38 && valright.top > 0)
			jQuery('#right').offset({top: valright.top-20, left: valright.left});
		if (e.which == 40 && valright.top < win_height - 160)
			jQuery('#right').offset({top: valright.top+20, left: valright.left});
	});
});