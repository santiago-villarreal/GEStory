var page = 0
var pages = ["bodyMap", "DataFilter", "itemDisplay"]
var step = 0

function swipe(direction) {
    /**
     * @direction : -1 if swiping to right page
     *               1 if swiping to left page
     */
    if ((page==2 && direction==-1) || (page == 0 && direction==1)){
        return
    }
    var interval = setInterval(()=>{
        if (step == 10){
            step = 0
            clearInterval(interval);
        }
        step++
        for (var elem in pages){
            document.getElementById(elem).style.left += `${direction*5}%`
        }
    }, 50)
    page++
    actualizeArrows()
}

function actualizeArrows(){
    if (page>0){
        //display left arrow
    }
    if (page<2){
        //display right arrow
    }
}