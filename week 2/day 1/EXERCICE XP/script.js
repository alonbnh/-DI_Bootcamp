//exercice 1: YOUR  FAVORITE FOOD

let f = "pastas"
let m = "dinner"
console.log (" i eat "+f+" at every "+m)

// exercice 2: SERIES

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"]
let myWatchedSeriesLength = console.log(myWatchedSeries.length)
let x = myWatchedSeries.slice(0,2)
let y = myWatchedSeries.slice(2,3)
let myWatchedSeriesSentence= console.log ("I watched 3 series : "+x+" and "+y )

// exercice 2: PART II

myWatchedSeries.pop()
myWatchedSeries.splice (2,2, "friends", " Vamprie Diaries")
let favorite = myWatchedSeries.slice (1)
console.log(favorite)
// i don'T understand the 5 
console.log(myWatchedSeries)

// exercice 3: THE TEMPERATURE CONVERTER 

x=32
d= x/5*9+32
console.log (x+" °C is "+ d +"°F")

// exercice 4: GUESS THE ANSWERS #1
    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:It will output 55, because 34 and 21 are numbers
    // Actual: 55

    a = 2;

    console.log (a+b) //second expression
    // Prediction: It will output 23, because 34 has changed into 2 and 21 are still numbers
    // Actual: 23

    // the value of c is undefined

    console.log(3 + 4 + '5');// The out come will be none because "5" is a string and not a number


// exercice 5: GUESS THE ANSWERS #2

typeof(15)
// Prediction: 15 is a number
// Actual: number
console.log(typeof(15))

typeof(5.5)
// Prediction: 5.5 is a number
// Actual:number
console.log(typeof(5.5))

typeof(NaN)
// Prediction: Nan is a number
// Actual:number
console.log(typeof(NaN))

typeof("hello")
// Prediction:"hello" is a string
// Actual:string
console.log(typeof("hello"))

typeof(true)
// Prediction: true is a boolean
// Actual:boolean
console.log(typeof(true))

typeof(1 != 2)
// Prediction: 1 !=2 is a boolean
// Actual:boolrean
console.log(typeof(1 != 2))

"hamburger" + "s"
// Prediction: It's a string, it will write " hamburgers"
// Actual:hamburgers
console.log("hamburger" + "s")

"hamburgers" - "s"
// Prediction: it won't work because it's a -
// Actual:NaN
console.log("hamburger" - "s")

"1" + "3"
// Prediction: it will write 13 because they are strings
// Actual:13
console.log("1" + "3")

"1" - "3"
// Prediction:it won't work because they are strings
// Actual:-2
console.log("1" - "3")

"johnny" + 5
// Prediction: it won't work because it's a string and a number
// Actual:johnny5
console.log("johnny" + 5)

"johnny" - 5
// Prediction: it will not work because it's a - and it's a string and a number
// Actual:NaN
console.log("johnny" - 5)

99 * "hello"
// Prediction:it won't work "NaN"
// Actual:NaN
console.log(99 * "hello")

1 != 1
// Prediction: it will write that it's false because the equation is false
// Actual:False
console.log(1 != 1)

1 == "1"
// Prediction: it's false because "1" is a string
// Actual:true
console.log(1 == "1")

1 === "1"
// Prediction: it's false because "1" is a string
// Actual:false
console.log(1 === "1")


// Exercise 6 : GUESS THE ANSWER #3

5 + "34"
// Prediction: 39
// Actual:539
console.log(5 + "34")

5 - "4"
// Prediction: 1
// Actual:1
console.log(5 - "4")

10 % 5
// Prediction: 0.5
// Actual: 0
console.log(10 % 5)

5 % 10
// Prediction:0.5
// Actual: 5
console.log(5 % 10)

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript
console.log("Java" + "Script")

" " + " "
// Prediction:"  "
// Actual:"  "
console.log(" " + " ")

" " + 0
// Prediction:" 0"
// Actual:" O"
console.log(" " + 0)

true + true
// Prediction: NaN
// Actual:2
console.log(true + true)

true + false
// Prediction: 0
// Actual:1
console.log(true + false)

false + true
// Prediction:1
// Actual:1
console.log(false + true)

false - true
// Prediction:-1
// Actual:-1
console.log(false - true)

!true
// Prediction:false
// Actual:false
console.log(!true)

3 - 4
// Prediction: -1
// Actual:-1
console.log(3 - 4)

"Bob" - "bill"
// Prediction: NaN
// Actual:NaN
console.log("Bob" - "bill")
