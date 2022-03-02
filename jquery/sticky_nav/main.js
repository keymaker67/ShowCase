$(function(){
    $(window).on("scroll", function(){
        if ($(this).scrollTop() > 80) {
            $("header").addClass("sticky");
        } else {
            $("header").removeClass("sticky");
        }
    });
});