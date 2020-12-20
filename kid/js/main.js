//wait till all page content is loaded
jQuery( document ).ready(function() {

	//cache pages references
	var $p01 = jQuery('#p01'); 
	var $p02 = jQuery('#p02'); 
	var $p02_1 = jQuery('#p02-1'); 
	var $p02_2 = jQuery('#p02-2');
	var $p03 = jQuery('#p03'); 
	var $p04 = jQuery('#p04');
	var $p04_1 = jQuery('#p04-1'); 
	var $p05 = jQuery('#p05');

	//if audio toggle present, assign action
	jQuery( ".audio-toggle" ).on( "click", function() {
		jQuery("#audio").get(0).play();
	});

	// PAGE 1
	if($p01.length > 0) {
		var splash_screen_audio = document.getElementById("splash-audio");
		//shake egg on rollover, play audio, then go to the next screen
		jQuery( ".egg" ).on( "click", function() {
			jQuery(this).addClass('egg-shake');
			jQuery(this).parent().removeClass('bounce');
			//wrap woth flexbox so we center the egg
			jQuery(this).parent().wrap( "<div class='wrapper'></div>" );
			//play audio
			splash_screen_audio.play();

			//set timeout to go to next page
			setTimeout(function(){ 
				window.location = "02-start.html";
			}, 7000);

		});
	}

	// PAGE 2
	if($p02.length > 0) {
		var audio = document.getElementById("audio");
		$( "#kidname" ).focus(function() {
			audio.play();
		});
	}

	//
	if($p02_2.length > 0) {
		//autoplay audio on page loads
		var play_audio = document.getElementById("audio");
		jQuery( ".egg" ).on( "click", function() {
			play_audio.volume = 0.7;
			play_audio.play();

			//set timeout to go to next page
			/*setTimeout(function(){ 
				window.location = "03-library.html";
			}, 3000);*/
		});
	}
	



	if($p04_1.length > 0) {
		jQuery( ".numbers-transition" ).on( "click", function(event) {
			event.preventDefault();
			numbers();
		});
		var numbers = function() {
			var $text_container = jQuery('.text-overlay');
			$text_container.html('$9,800');

			//set timeout to go to next page
			setTimeout(function(){ 
				window.location = "08.1-library.html";
			}, 3000);

			/*var countUp = new CountUp(target_ID, target_num);
            if (!countUp.error) {
              countUp.start();
            } else {
              console.error(countUp.error);
            }*/
		}
	}

});



