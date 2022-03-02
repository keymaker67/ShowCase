$(function(){
    $(".grid-item").each(function(){
        var itemTitle = $(".grid-item-title");
        $(this).on("mouseenter", function(){
            if ($(this).data("title")) {
                itemTitle.html("<span>" + $(this).data("title") + "</span>")
                itemTitle.addClass("visible")
            }
        $(document).on("mousemove", function(e){
            itemTitle.css({
                left: e.clientX -10,
                top:  e.clientY + 25,
            });
        });
        $(this).on("mouseleave", function(){
            itemTitle.removeClass("visible")
        })
        });
    });
});