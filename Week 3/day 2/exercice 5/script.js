let anim = document.querySelector("h1");
console.log(anim)
anim.addEventListener("click", function(event){
	anim.style.color="blue";
})
anim.addEventListener("mouseover", function(event){
	anim.style.textAlign="center"})
anim.addEventListener("mouseout", function(event){
	anim.style.fontSize ="43px"
})
anim.addEventListener("dblclick", function(event){
	document.body.style.backgroundColor ="violet"
})