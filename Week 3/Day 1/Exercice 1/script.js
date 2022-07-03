let a = document.getElementsByTagName('div')
console.log(a)

let b = document.getElementsByClassName ('list')
b[0].lastElementChild.textContent="Adam"

let c= document.getElementsByClassName ("list")
c[0].firstElementChild.textContent="Alon"

let d= document.getElementsByClassName ("list")
d[1].firstElementChild.textContent="Alon"

let e = document.getElementsByClassName ("list")
let f = e[1].children[1]
e[1].removeChild(f)