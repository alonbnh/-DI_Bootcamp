allBoldItems=[]
 function getBold_items (){
 	let bold = document.getElementsByTagName("strong")
 	console.log(bold)
 	for (i=0; i<bold.length; i++){
 		allBoldItems.push(bold[i])
 		console.log(allBoldItems)
 	}
 }
 getBold_items()
 function highlight() {
 	for(i=0; i<allBoldItems.length; i++){
 		allBoldItems[i].style.color = "blue"
 	}
 	// allBoldItems.style.color = ‘blue’
 	console.log(allBoldItems)
 }
 highlight()
 function return_normal (){
  	for(i=0; i<allBoldItems.length; i++){
 		allBoldItems[i].style.color = "black"
 	}
 }
 return_normal()
 let change = document.querySelector("p");
 console.log (change)
 change.addEventListener("mouseover", highlight)
 change.addEventListener("mouseout", return_normal)