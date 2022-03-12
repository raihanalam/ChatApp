(function() {
    var current = location.pathname;
    $('.icon-bar a').each(function() {
        var $this = $(this); 

        // we check comparison between current page and attribute redirection.
        if ($this.attr('href') === current) {
            $this.addClass('is-active');
        }
    });
})();