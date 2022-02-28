$(function(){
    $(".generate-btn").click(function(){
        var randomColor = "";
        var characters  = "0123456789abcdef";

        for(i=0; i<6; i++){
            randomColor = randomColor + characters[Math.floor(Math.random() * 16)];
        }

        $("#inputField").val("#" + randomColor);
        $("#inputField").css("color", "#" + randomColor);
        $("#inputField").css("border-color", "#" + randomColor);
        $(".copy-btn, .color").css("background-color", "#" + randomColor);
    });
    function add() {
        $(".alert-msg").addClass("slide-effect")
    }
    function remove() {
        $(".alert-msg").removeClass("slide-effect")
    }

    $(".copy-btn").click(function(){
        $("#inputField").select();
        document.execCommand("copy");
        add();
        setTimeout(remove, 2000);
        $(".code").text($("#inputField").val())
    })

    
});