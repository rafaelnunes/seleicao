// JavaScript Document


	/*----------------------------------------------------*/
	/*	Preloader
	/*----------------------------------------------------*/

    $(window).load(function() {
	
		"use strict";	
	
       $('#status').delay(100).fadeOut('slow');
       $('#preloader').delay(500).fadeOut('slow');
       $('body').delay(500).css({'overflow':'visible'});
	   
	});


	/*----------------------------------------------------*/
	/*	Mobile Menu Toggle
	/*----------------------------------------------------*/
	$(document).ready(function() {
		
		"use strict";	

		$('.navbar-nav li a').click(function() {				
			$('#navigation-menu').css("height", "1px").removeClass("in").addClass("collapse");
			$('#navigation-menu').removeClass("open");				
		});			
	});
	

	
	/*----------------------------------------------------*/
	/*	ScrollUp
	/*----------------------------------------------------*/
	/**
	* scrollUp v1.1.0
	* Author: Mark Goodyear - http://www.markgoodyear.com
	* Git: https://github.com/markgoodyear/scrollup
	*
	* Copyright 2013 Mark Goodyear
	* Licensed under the MIT license
	* http://www.opensource.org/licenses/mit-license.php
	*/

	$(document).ready(function(){

		'use strict';

		$.scrollUp = function (options) {

			// Defaults
			var defaults = {
				scrollName: 'scrollUp', // Element ID
				topDistance: 600, // Distance from top before showing element (px)
				topSpeed: 800, // Speed back to top (ms)
				animation: 'fade', // Fade, slide, none
				animationInSpeed: 200, // Animation in speed (ms)
				animationOutSpeed: 200, // Animation out speed (ms)
				scrollText: '', // Text for element
				scrollImg: false, // Set true to use image
				activeOverlay: false // Set CSS color to display scrollUp active point, e.g '#00FFFF'
			};

			var o = $.extend({}, defaults, options),
				scrollId = '#' + o.scrollName;

			// Create element
			$('<a/>', {
				id: o.scrollName,
				href: '#top',
				title: o.scrollText
			}).appendTo('body');
			
			// If not using an image display text
			if (!o.scrollImg) {
				$(scrollId).text(o.scrollText);
			}

			// Minium CSS to make the magic happen
			$(scrollId).css({'display':'none','position': 'fixed','z-index': '2147483647'});

			// Active point overlay
			if (o.activeOverlay) {
				$("body").append("<div id='"+ o.scrollName +"-active'></div>");
				$(scrollId+"-active").css({ 'position': 'absolute', 'top': o.topDistance+'px', 'width': '100%', 'border-top': '1px dotted '+o.activeOverlay, 'z-index': '2147483647' });
			}

			// Scroll function
			$(window).scroll(function(){	
				switch (o.animation) {
					case "fade":
						$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).fadeIn(o.animationInSpeed) : $(scrollId).fadeOut(o.animationOutSpeed) );
						break;
					case "slide":
						$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).slideDown(o.animationInSpeed) : $(scrollId).slideUp(o.animationOutSpeed) );
						break;
					default:
						$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).show(0) : $(scrollId).hide(0) );
				}
			});

			// To the top
			$(scrollId).click( function(event) {
				$('html, body').animate({scrollTop:0}, o.topSpeed);
				event.preventDefault();
			});

		};
		
		$.scrollUp();

	});
	
	
	/*----------------------------------------------------*/
	/*	Statistic Counter
	/*----------------------------------------------------*/
	
	$(document).ready(function($) {
	
		"use strict";
	
		$('.statistic-block').each(function() {
			$(this).appear(function() {
				var $endNum = parseInt($(this).find('.statistic-number').text());
				$(this).find('.statistic-number').countTo({
					from: 0,
					to: $endNum,
					speed: 3000,
					refreshInterval: 30,
				});
			},{accX: 0, accY: 0});
		});

	});
	
	
	/*----------------------------------------------------*/
	/*	Carousel
	/*----------------------------------------------------*/
	
	$(document).ready(function(){

		"use strict";
				
		$("#our-customers").owlCarousel({
					  
			slideSpeed : 600,
			items : 6,
			itemsDesktop : [1199,5],
			itemsDesktopSmall : [960,4],
			itemsTablet: [768,3],
			itemsMobile : [480,2],
			navigation:true,
			pagination:false,
			navigationText : false
					  
		});
				
		// Carousel Navigation
		$(".next").click(function(){
			$("#our-customers").trigger('owl.next');
		})
		
		$(".prev").click(function(){
			$("#our-customers").trigger('owl.prev');
		})

		
	});	
	
	
	/*----------------------------------------------------*/
	/*	Lightbox
	/*----------------------------------------------------*/
	$(document).ready(function() {
	
		"use strict";
	
	  $('.image_zoom').magnificPopup({type:'image'});
	  
	});
	
	
		
	/*----------------------------------------------------*/
	/*	Intro Page Register Form Validation
	/*----------------------------------------------------*/
	
	$(document).ready(function(){
	
		"use strict";

		$(".form_register form").validate({
			rules:{ 
				first_name:{
					required: true,
					minlength: 4,
					maxlength: 16,
					},
					email:{
						required: true,
						email: true,
					},
					phone:{
						required: true,
						digits: true,
						}
					},
					messages:{
							email:{
								required: "Endereço de email obrigatório",
								email: "Email deve estar no formato name@domain.com"
							}, 
							phone:{
								required: "Por favor, somente numeros",
								digits: "Quantidade inválida"
							}, 
						}
		});

		$(".form_register form").on('submit', function(evt){
			$.ajax({
				type:'POST',
				url: '/save_contact',
				dataType: 'json',
				data: {
					'nome': $('#name').val(),
					'email': $('#email').val(),
					'qtde_canal': $('#phone').val()
				},
				success: function(response){
					$('#form_register').remove();
					$('#form_register_title').text('Contato salvo com sucesso!');
					$('#contato_salvo').append('<p class="btn btn-primary btn-lg">Obrigado!</p>')
				},
				error: function(error){
					console.warn(error);
				}
			})

			return false;
		})			
		
	});

