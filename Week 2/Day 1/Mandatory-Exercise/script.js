// Exercise 1
let favouriteFood = "Chicken";
let favouriteMeal = "Dinner";
console.log(`I eat ${favouriteFood} at every ${favouriteMeal}`);

// Exercise 2
const myWatchedSeries = ["The Big Bang Theory","Better Call Saul",  "Rick and Morty"];
const myWatchedSeriesLength = myWatchedSeries.length
const myWatchedSeriesSentence = [myWatchedSeries[0], myWatchedSeries[1], "and"  ,myWatchedSeries[2]]
console.log(`I watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}`)
myWatchedSeries[2]= "Bojack Horseman"
myWatchedSeries.push("Avatar the Last Airbender")
myWatchedSeries.unshift("Breaking Bad")
myWatchedSeries.splice(1,1)
console.log(myWatchedSeries[1][3])
console.log(myWatchedSeries)

// Exercise 3
const temperatureCelsius = [100]
const temperatureFahrenheit = (temperatureCelsius*9/5) +32
console.log(`${temperatureCelsius}°C is ${temperatureFahrenheit}°F`)

// Exercise 4
let c;
let a = 34;
let b = 21;

console.log(a+b); //first expression
    // Prediction: It will ouput 55 because both 34 and 21 are numbers
    // Actual: 55

    a = 2;

console.log(a+b); //second expression
    // Prediction: It will output 23 because the value of a is changed to 2 and 2 and 21 are both numbers
    // Actual: 23

console.log(c);
    // C is undefined

console.log(3 + 4 + '5');
    // Prediction: It will output 75 because 3+4=7 and since '5' is a string it will settle next to the 7
    // Actual: 75

    // Exercise 5
    console.log(typeof(15))
// Prediction:number
// Actual: number

console.log(typeof(5.5))
// Prediction: number
// Actual: number 

console.log(typeof(NaN))
// Prediction: number
// Actual: number

console.log(typeof("hello"))
// Prediction:string
// Actual: string 

console.log(typeof(true))
// Prediction: boolean
// Actual: boolean

console.log(typeof(1 != 2))
// Prediction: boolean
// Actual: boolean

console.log("hamburger" + "s")
// Prediction:it gives an output of hamburgers because they are both strings so they just slide next together
// Actual: hamburgers

console.log("hamburgers" - "s")
// Prediction: It gives an output of NaN because they are not numbers so the function cannot be executed
// Actual: NaN

console.log("1" + "3")
// Prediction: It gives an output of 13 because they are both strings so they just slide next to each other
// Actual: 13 

console.log("1" - "3")
// Prediction: It gives an output of -2 because even though they are strings they are both numbers so subtraction can be executed
// Actual: -2

console.log("johnny" + 5)
// Prediction: It gives an output of johnny5 because "johnny" is a string so it slides next to the 5
// Actual: johnny5

console.log("johnny" - 5)
// Prediction: It gives an output of NaN because "johnny" is a string and subtraction cannot be executed between aa string and number
// Actual: NaN

console.log(99 * "hello")
// Prediction:It gives and output of NaN because the function cannot be executed with a string that has words
// Actual: NaN

console.log(1 != 1)
// Prediction: it gives an output of false because it is true, but due to the exclamation mark which means "not" it becomes false
// Actual: false

console.log(1 == "1")
// Prediction: It gives an output of true because since there only two equal to signs it only checks the value and the values are equal
// Actual: true

console.log(1 === "1")
// Prediction: It gives an output of false because there are 3 equal to signs so it checks the value and data type, which in this case are not equal
// Actual: false

// Exercise 6
console.log(5 + "34")
// Prediction: It gives an output of 534 because 5 is a number while "34" is a string so it just slides next to the 5
// Actual:

console.log(5 - "4")
// Prediction: it gives an output of 1
// Actual:

console.log(10 % 5)
// Prediction: It gives an output of 0 becasue the remainder is 0
// Actual:

console.log(5 % 10)
// Prediction: It gives an output of 5 because the remainder is 5
// Actual:

console.log("Java" + "Script")
// Prediction: The output is JavaScript because they are both strings    
// Actual:

console.log(" " + " ")
// Prediction: undefined because the strings are both empty
// Actual: (there was nothing there the line was blank)

console.log(" " + 0)
// Prediction: It gives an output of 0 because the string is empty
// Actual: 0

console.log(true + true)
// Prediction: the output is 2 because the value of true=1 so 1+1 =2
// Actual:2

console.log(true + false)
// Prediction: The output is 1 because the value of true=1 and false =0 so 1+0=1
// Actual:
1
console.log(false + true)
// Prediction: The output is 1 because the value of true=1 and false =0 so 0+1=1
// Actual:1

console.log(false - true)
// Prediction:The output is -1 because the value of true=1 and false =0 so 0-1=-1
// Actual:-1

console.log(!true)
// Prediction: false
// Actual: false

console.log(3 - 4)
// Prediction: -1
// Actual: -1

console.log("Bob" - "bill")
// Prediction: It gives an output of NaN because subtraction does not work with strings with words
// Actual: NaN







    