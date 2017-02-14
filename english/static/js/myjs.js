jQuery('document').ready(function() {
	var all_buttons = document.getElementsByTagName('button');
	var pre_button = -1;
	jQuery('button').on('click', function() {
		for (var i = 0; i < all_buttons.length; i++) {
			if (jQuery(all_buttons[i]).attr("disabled") && jQuery(all_buttons[i]).attr('n') == jQuery(this).attr('n')) {
				jQuery(this).css('display', 'none');
				jQuery(all_buttons[i]).css('display', 'none');
			}
			jQuery(all_buttons[i]).removeAttr("disabled");
			jQuery(all_buttons[i]).css("background-color", "#4286f4");
		}
		jQuery(this).attr("disabled", "");
		jQuery(this).css("background-color", "red");
		//jQuery(this).css("display", "none");
		//alert(jQuery(this).attr("n"));
	});
	
});