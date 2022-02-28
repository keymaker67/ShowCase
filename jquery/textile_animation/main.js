$(function(){
    $(".text").textillate({
    loop:true,
    in:{
        effect:"fadeInDownBig", 
        delayScale: 3,
        delay: 20,
        // shuffle:true,

     },
     out: {
         effect: "bounceOut",
         delayScale: 2,
         delay: 20,
         reverse: true,
     }
    });
});