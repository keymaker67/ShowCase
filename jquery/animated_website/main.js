$(function(){
    $(".toggle-btn").click(function(){
        $(this).toggleClass("active");
        $(".navbar-nav").toggleClass("active");
    });
});