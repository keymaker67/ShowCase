$(function(){
    $(".card").on("mouseenter" ,function(){
        $(this).addClass("selected").siblings().removeClass("selected");
    });
});