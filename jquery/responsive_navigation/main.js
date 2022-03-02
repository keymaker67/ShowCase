$(function() {
    $(".ham-menu").click(function(){
        $(this).toggleClass("open");
        $(".menu").slideToggle();
        setTimeout(function(){
            $(".menu li a").removeClass("active");
            $("#home").addClass("active")
        }, 500)
    });
    $(".menu li a").click(function(){
        $(".menu li a").removeClass("active");
        $(this).addClass("active")
    })
});