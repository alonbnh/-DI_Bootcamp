let a = document.getElementsByTagName ("h1")
console.log(a)


let b = document.querySelector("article");
console.log(b)
let c = document.querySelectorAll("p") [3]
b.removeChild(c)


let red = document.querySelector('h2')
red.addEventListener('click',function()
{
   red.style.backgroundColor = "red"
})


let hide = document.querySelector("h3")
hide.addEventListener('click', function(){
	hide.style.display ='none'
})


let bold = document.querySelector("button")
bold.addEventListener("click",function() {
	document.body.style.fontWeight = 'bold'
})


let number = document.querySelector("h1");
number.addEventListener("mouseover", function(event){
   event.target.style.fontSize = Math.random()*100+'px'

})
