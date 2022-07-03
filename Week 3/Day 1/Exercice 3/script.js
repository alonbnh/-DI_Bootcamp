let a= document.getElementById("navBar")
console.log(a)
a.setAttribute("id", "SocialNetworkNavigation");

const lol = document.createElement("li");
lol.innerText = "list";
document.getElementsByTagName ("ul")[0].appendChild (lol) ;


let tg = document.createTextNode("hey")
lol.appendChild(tg)