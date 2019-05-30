(function($){
<<<<<<< HEAD
    var $content_md = $('#div_id_content_md');
    var $content_ck = $('#div_id_content_ck');
=======
    var $content_md = $('#id_title').parent();
    var $content_ck = $('#id_content_ck').parent();
>>>>>>> c7210108bdbdd9bc7d9b86c09f6c05d99d5be466
    var $is_md = $('input[name=is_md]');
    var switch_editor = function(is_md) {
        if (is_md) {
            $content_md.show();
            $content_ck.hide();
        } else {
            $content_md.hide();
            $content_ck.show();
        }
    }
    $is_md.on('click', function() {
        switch_editor($(this).is(':checked'));
    });
    switch_editor($is_md.is(':checked'));
})(jQuery);
