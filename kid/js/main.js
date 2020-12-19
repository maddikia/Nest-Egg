//wait till all page content is loaded
jQuery( document ).ready(function() {

	var splash_screen_audio = document.getElementById("splash-audio");
	//shake egg on rollover, play audio, then go to the next screen
	jQuery( ".egg" ).on( "click", function() {
		jQuery(this).addClass('egg-shake');
		//play audio
		splash_screen_audio.play();

		//set timeout to go to next page
		setTimeout(function(){ 
			window.location = "02-start.html";
		}, 3000);

	});
});