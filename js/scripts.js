//Array of images which you want to show: Use path you want.
var images=new Array('./css/imgs/background/avengers.jpg','./css/imgs/background/coco.jpg','./css/imgs/background/mando.jpg','./css/imgs/background/moana.jpg','./css/imgs/background/tenet.jpg','./css/imgs/background/ww_bg.jpg');
let background = 0;


window.onload = function() {
        background = Math.floor(Math.random() * 6);
        document.getElementById('images-slide').style.backgroundImage="linear-gradient(to bottom, rgba(11, 23, 61, 0.685), rgb(11,23,61,1)), url("+ images[background] + ")";
        console.log(background);
}