$(function(){
    $("#mode-btn").click(function(){
        $("body").toggleClass("background-change");
        $("span").text($("span").text() == "Dark Mode" ? "Light Mode" : "Dark Mode")
    })
    $("#mode-btn").click(function(){
        $(this).find("i").toggleClass("fa-moon fa-sun");
    })
})