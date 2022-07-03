String[] systemsolar = {"Mercure", "Venus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"};


const lol = document.createElement("div class="planet"");
console.log(lol)
document.getElementsByTagName ("div class="planet"")[0,1,2,3,4,5,5,6,7].appendChild (lol) ;

const M = document.createElement("div class="planetM"");
function planetM() {
  document.body.style.background = "Black";
}
document.getElementsByTagName ("div class="planet"")[0].appendChild (M) ;

const V = document.createElement("div class="planetV"");
function planetV() {
  document.body.style.background = "Blue";
}
document.getElementsByTagName ("div class="planetV"")[1].appendChild (V) ;

const T = document.createElement("div class="planetT"");
function planetT() {
  document.body.style.background = "Brown";
}
document.getElementsByTagName ("div class="planetT"")[2].appendChild (T) ;

const M2 = document.createElement("div class="planetM2"");
function planetM2() {
  document.body.style.background = "Grey";
}document.getElementsByTagName ("div class="planetM2)[3].appendChild (M2) ;

const J = document.createElement("div class="planetJ"");
function planetJ() {
  document.body.style.background = "Yellow";
}
document.getElementsByTagName ("div class="planetJ"")[4].appendChild (J) ;

const S = document.createElement("div class="planetS"");
function planetS() {
  document.body.style.background = "Pink";
}
document.getElementsByTagName ("div class="planetS"")[5].appendChild (S) ;

const U = document.createElement("div class="planetU"");
function planetU() {
  document.body.style.background = "White";
}
document.getElementsByTagName ("div class="planetU"")[6].appendChild (U) ;

const N = document.createElement("div class="planetN"");
function planetN() {
  document.body.style.background = "Green";
}
document.getElementsByTagName ("div class="planetN"")[7].appendChild (N) ;

