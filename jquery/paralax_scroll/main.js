$(window).on("scroll", function() {
    var parallax = $(".parallax");
    var scrPosition = $(this).scrollTop();
    parallax.css("transform", "translateY(" + scrPosition * 0.5 + "px)");
})