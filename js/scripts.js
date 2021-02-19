//Array of images which you want to show: Use path you want.
var images=new Array('./imgs/background/avengers.jpg','./imgs/background/coco.jpg','./imgs/background/mando.jpg','./imgs/background/moana.jpg','./imgs/background/tenet.jpg','./imgs/background/ww_bg.jpg');
var nextimage=0;
doSlideshow();

function doSlideshow(){
    if(nextimage>=images.length){nextimage=0;}
    $('.images-slide')
    .css('background-image:','url("'+images[nextimage++]+'")')
    .fadeIn(500,function(){
        setTimeout(doSlideshow,1000);
    });
}