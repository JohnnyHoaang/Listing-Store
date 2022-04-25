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
    createHeaders()
    console.log(data)
    data.forEach(e=> {

        // let p = document.createElement('p');
        // p.textContent = e.username + " " + e.groups__name
        // global.div.appendChild(p)
        let tr = document.createElement('tr')
        let username = document.createElement('td')
        username.textContent = e.username
        let group = document.createElement('td')
        group.textContent = e.groups__name
        tr.appendChild(username)
        tr.appendChild(group)
        global.table.append(tr)
        createButtons(tr)
    })
    
}

function createHeaders(){
    let tr = document.createElement('tr')
    let username = document.createElement('th')
    username.textContent="Username"
    let group = document.createElement('th')
    group.textContent="Group"
    tr.append(username, group)
    //tr.appendChild(group)
    global.table.append(tr)
}

function createButtons(tr){
    let edit = document.createElement('button')
    edit.textContent = "Edit Details"
    edit.id = "edit"
    let modify = document.createElement('button')
    modify.textContent = "Modify Groups"
    modify.id = "modify"
    let flag = document.createElement('button')
    flag.textContent = "Flag"
    flag.id = "flag"
    let warn = document.createElement('button')
    warn.textContent = "Warn"
    warn.id = "warn"
    let delete_but = document.createElement('button')
    delete_but.textContent = "Delete"
    delete_but.id = "delete"
    tr.append(edit, modify, flag, warn, delete_but)
}
