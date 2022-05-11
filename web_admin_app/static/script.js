"use strict"

document.addEventListener("DOMContentLoaded", setUp);
let global;
function setUp(){
    global = {}
    global.flagButton = document.querySelectorAll('.flag')
    checkFlag()
}

function checkFlag(){
    console.log(global.flagButton)
    global.flagButton.forEach((button, i) => {
        console.log(button)
        if (button.value=="true"){
            button.textContent = "Unflag"
        } else if (button.value=="false") {
            button.textContent = "Flag"
        }

    })
}





