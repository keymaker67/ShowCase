$(function(){
    $(".nav-link").on("click", function(){
        $(".nav-link").removeClass("active");
        $(this).addClass("active");
    });
    $(".ham").on("click", function(){
        $(this).toggleClass("active")
    })
});