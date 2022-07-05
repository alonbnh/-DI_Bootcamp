setTimeout(function(){
	alert("hello")
},2000)

let id

setTimeout(function(){
	let div1 = document.createElement("p")
	div1.innerText = "Hello World"
	document.querySelector("div").appendChild(div1)
},2000)
let counter =0
id = setInterval(function(){
		let div2 = document.createElement("p")
	div2.innerText = "Hello World"
	document.querySelector("div").appendChild(div2)
	counter++
	if (counter>=5){
    _clear()
	}
	},2000)

function _clear(){
         clearInterval(id)
    }

let p =document.querySelectorAll("div")[0];
console.log(p)
function _clear(){
	clearInterval(id)
}

    