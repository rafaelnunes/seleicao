$(document).ready(function() {
	$('.candidate_details').each(function(index, obj){
		$.ajax({
			url: '/profile?id=' + $(obj).attr('id'),
			type: 'GET',
			dataType: 'json',
			success: function(response){
				$(obj).empty();
				var tmpl = Mustache.render($('#tmpl_candidato_details').html(), response);
				$(obj).append(tmpl);
			},
			error: function(error){
				console.warn(error);
			}
		})
	});

	$('.btn-voto').click(function(event){
		event.preventDefault();
		var voto = $(event.currentTarget);
		$.ajax({
			url: '/votar',
			type: 'POST',
			dataType: 'json',
			data: {
				'voto': $(event.currentTarget).data('voto'),
				'candidato': $(event.currentTarget).data('candidato')
			},
			success: function(response){
				console.warn(response);
			},
			error: function(error){
				console.warn(error);
			}
		})
	});
});