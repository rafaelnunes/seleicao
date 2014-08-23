$(document).ready(function() {
    $('#rootwizard').bootstrapWizard({
        onTabShow: function(tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index+1;
            var $percent = ($current/$total) * 100;
            $('#rootwizard').find('.progress-bar').css({width:$percent+'%'});
        }
    });

    $('#btn_toggle_signup').on('click', function() {
        if ($('#signup').is(':hidden')) {
            $('#signup').slideDown();
            $('#signin').slideUp();
        } else {
            $('#signup').slideUp();
            $('#signin').slideDown();
        }
    });
});
