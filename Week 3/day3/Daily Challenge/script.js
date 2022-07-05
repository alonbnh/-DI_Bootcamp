// let x= document.getElementsByTagName("input")[0]
// console.log(x)
// let input = document.querySelector("input.area");
// regexSpecial = /^[A-Za-z]+$/
// input = document.addEventListener("keyup", function(event){
// 	if(input==regexSpecial)
// 	{return false}
// })

function lettersOnly(input){
	var regex=/[^a-z]/gi;
	input.value = input.value.replace(regex,"")
}