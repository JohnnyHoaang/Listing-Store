"use strict"

document.addEventListener("DOMContentLoaded", setUp);
let global;
function setUp(){
    console.log("Hello World")
    global = {}
    global.div = document.querySelector('div')
    global.table = document.querySelector('table')
    load()
}

function load(){
    fetch('json')
    .then(response=> {
        if(response.ok){
            return response.json();
        }
        else{
            throw new Error('File not found')
        }
    })
    .then(data=> createTable(data))
    .catch(e=> console.log(e))
}

function createTable(data){
    console.log(data)
    data.forEach(e=> {
        let p = document.createElement('p');
        p.textContent = e.username + " " + e.groups__name
        global.div.appendChild(p)
    })
    
}