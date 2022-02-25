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
    page += -direction
    document.getElementById(pages[page]).style.display = "block";
    var interval = setInterval(()=>{
        if (step == 10){
            step = 0
            clearInterval(interval);
        }
        step++
    }, 50)
    actualizeArrows()
}

function actualizeArrows(){
    if (page==0){
        document.getElementById("arrow-left").style.display="none"
    }else{
        document.getElementById("arrow-left").style.display="block"
    }
    if (page==2){
        document.getElementById("arrow-right").style.display="none"
    }else{
        document.getElementById("arrow-right").style.display="block"
    }
}

function switchStyleDisplay(){

    setInterval(()=>{
        if (window.innerWidth <= 700){
            actualizeArrows();
            for (let index = 0; index < pages.length; index++) {
                if (index!=page){
                    document.getElementById(pages[index]).style.display = "none"
                }
            }
        }else{
            document.getElementById("arrow-left").style.display="none"
            document.getElementById("arrow-right").style.display="none"
            for (elem of pages){
                document.getElementById(elem).style.display = "block"
            }
        }
    })
}