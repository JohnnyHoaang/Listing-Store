"use strict"

document.addEventListener("DOMContentLoaded", setUp);
let global;
function setUp(){
    console.log("Hello World")
    global = {}
    global.count = 0
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
        let tr = document.createElement('tr')
        let userid = document.createElement('td')
        userid.textContent = global.count
        let username = document.createElement('td')
        username.textContent = e.username
        let group = document.createElement('td')
        group.textContent = e.groups__name
        tr.append(userid, username, group)
        global.table.append(tr)
        createButtons(tr, global.count)
        global.count++
    })
    
}

function createHeaders(){
    let tr = document.createElement('tr')
    let id = document.createElement('th')
    id.textContent = "User ID"
    let username = document.createElement('th')
    username.textContent="Username"
    let group = document.createElement('th')
    group.textContent="Group"
    tr.append(id, username, group)
    global.table.append(tr)
}

function createButtons(tr, count){
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
