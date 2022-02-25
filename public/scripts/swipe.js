var page = 0
var pages = ["bodyMap", "DataFilter", "itemDisplay"]



let touchstartX = 0
let touchendX = 0

const slider = document.getElementById('slider')

function handleGesture() {
  if (touchendX < touchstartX) swipe(-1)
  if (touchendX > touchstartX) swipe(1)
}

slider.addEventListener('touchstart', e => {
  touchstartX = e.changedTouches[0].screenX
})

slider.addEventListener('touchend', e => {
  touchendX = e.changedTouches[0].screenX
  handleGesture()
})

function swipe(direction) {
    /**
     * @direction : -1 if swiping to right page
     *               1 if swiping to left page
     */
    if ((page==2 && direction==-1) || (page == 0 && direction==1)){
        return
    }
    document.getElementById(pages[page]).style.display = "none"
    page -= direction
    document.getElementById(pages[page]).style.display = "block";
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