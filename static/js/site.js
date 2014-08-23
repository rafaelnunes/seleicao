 $(document).ready(function() {

/*----------------------------------------------------- Newssleter and contact Form -------------------------*/
	$("#newsletter, #contact, #request").submit(function() {
		var elem = $(this);
		var urlTarget = $(this).attr("action");
		$.ajax({
			type : "POST",
			url : urlTarget,
			dataType : "html",
			data : $(this).serialize(),
			beforeSend : function() {
				elem.prepend("<div class='loading alert'>" + "<a class='close' data-dismiss='alert'>×</a>" + "Loading" + "</div>");
				//elem.find(".loading").show();
			},
			success : function(response) {
				var json_response = JSON.parse(response);
				elem.prepend('<p>' + json_response.message + '</p>');
				elem.find(".loading").hide();
				elem.find("input[type='text'],input[type='email'],textarea").val("");
			}
		});
		return false;
	});


/*---------------------------------------------------------------- One Page Navigation ----------------------------*/

	$('.nav').onePageNav({
	filter: ':not(.external)',
	scrollThreshold: 0.25,
	scrollOffset: 90,
	});
         


/*--------------------------------------------------------------------------- Features Hover -------------------------------*/
	$('.features .item').hover(function() {
		$(this).children("i").toggleClass('animated tada');
	});




/*--------------------------------------------------------------------------- grid gallery ------------------------------*/
	$('#ri-grid').gridrotator({

		// number of rows
		rows : 3,

		// number of columns
		columns : 12,

		// rows/columns for different screen widths
		// i.e. w768 is for screens smaller than 768 pixels
		w1024 : {
			rows : 3,
			columns : 10
		},

		w768 : {
			rows : 3,
			columns : 7
		},

		w480 : {
			rows : 3,
			columns : 5
		},

		w320 : {
			rows : 2,
			columns : 4
		},

		w240 : {
			rows : 2,
			columns : 3
		},

		// step: number of items that are replaced at the same time
		// random || [some number]
		// note: for performance issues, the number should not be > options.maxStep
		step : 'random',
		maxStep : 3,

		// prevent user to click the items
		preventClick : true,

		// animation type
		// showHide || fadeInOut || slideLeft ||
		// slideRight || slideTop || slideBottom ||
		// rotateLeft || rotateRight || rotateTop ||
		// rotateBottom || scale || rotate3d ||
		// rotateLeftScale || rotateRightScale ||
		// rotateTopScale || rotateBottomScale || random
		animType : 'random',

		// animation speed
		animSpeed : 500,

		// animation easings
		animEasingOut : 'linear',
		animEasingIn : 'linear',

		// the item(s) will be replaced every 3 seconds
		// note: for performance issues, the time "can't" be < 300 ms
		interval : 3000,
		// if false the animations will not start
		// use false if onhover is true for example
		slideshow : true,
		// if true the items will switch when hovered
		onhover : false,
		// ids of elements that shouldn't change
		nochange : []

	});
	
	



/*--------------------------------------------------------------- Responsive Video plugin ------------------*/
	$('.video').fitVids();
	


/*--------------------------------------------------------------------------- ToTop -------------------------*/

	 $(window).scroll(function(){
		 if ($(this).scrollTop() > 100) {
			 $('.scrollup').fadeIn();
		 } else {
			 $('.scrollup').fadeOut();
		 }
	 }); 
 
	 $('.scrollup').click(function(){
		 $("html, body").animate({ scrollTop: 0 }, 600);
		 return false;
	 });

});


 
