$(function() {
    $(".input-field").focusout(function(){
        var inputValue = $(this).val();
        if (inputValue==="") {
            $(this).removeClass("has-value")
        } else {
            $(this).addClass("has-value")
        }
    })
})