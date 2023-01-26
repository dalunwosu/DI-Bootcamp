// Exercise 1
function infoAboutMe(){
    console.log(`My name is Dalu, I am 17 years old, I enjoy reading, gaming and sports.`)
}
infoAboutMe()

function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`)
}
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

// Exercise 2
function calculateTip(){
let  bill = prompt("How much is your bill?")
    if(bill<50){
        console.log(`You are to give a $${bill*0.2} tip and your bill is $${bill *1.2}`)
    }
    else if (bill>50 && bill<200){
        console.log(`You are to give a $${bill*0.15} tip and your bill is $${bill *1.15}`)
    }
    else if (bill>200){
        console.log(`You are to give a $${bill*0.1} tip and your bill is $${bill *1.1}`)
    }
}
calculateTip()

// Exercise 3 
function isDivisible(){
     let sum = 0;
    for (let i= 0; i<=500; i++){
    if(i % 23 ==0){
        console.log(`${i}`);
        sum+=i
        
    }
    
    }
    console.log(sum)
}
isDivisible()

// Bonus
function isDividible(divisor){
    let sum = 0;
   for (let i= 0; i<=500; i++){
   if(i % divisor ==0){
       console.log(`${i}`);
       sum+=i
       
   }
   
   }
   console.log(sum)
}
isDividible(3)
isDividible(45)

// Exercise 4
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = ["banana", "orange", "apple"];
function myBill(){
    let total = 0
    for(let f= 0; f<shoppingList.length; f++){
        let item = shoppingList[f];
        if(item in stock && stock[item]>0){
            total+= prices[item];
        }
        else{
            console.log(`${item} is out of stock`)
        }
    }
    console.log(`total bill:$${total}`)
}
myBill()

// Exercise 5
function changeEnough(itemPrice, amountOfChange){
    let totalChange= amountOfChange[0]*0.25 + amountOfChange[1]*0.10 + amountOfChange[2]*0.05 + amountOfChange[3]*0.01;
    if (totalChange>=itemPrice){
        console.log("true")
        return true;
    }
    else if(itemPrice>=totalChange){
        console.log("false")
        return false;
    }
}
changeEnough(4.25, [25, 20, 5, 0])
changeEnough(14.11, [2,100,0,0])
changeEnough(0.75, [0,0,20,5])

// Execrise 6
function hotelCost(){
    let hotel = prompt("How many nights are you staying?")
    while(isNaN(hotel) || hotel === null){
        hotel = prompt("Please enter a valid number of nights")
    }
    console.log(`Your total is $${hotel*140} for ${hotel} nights `)
    return hotel*140
}

function planeRideCost(){
let plane = prompt("What is your Destination?").toLowerCase
while(typeof plane !== "string" || plane === null|| !isNaN(plane)){
    plane = prompt("Please enter a valid destination")
}
if (plane === "london"){
    console.log(`your flight is $183` )
    return 183
}
else if (plane === "paris"){
    console.log(`your flight is $220`)
    return 220
}
else if (plane !== "london" || plane !== "paris"){
    console.log(`your flight is $300`)
    return 300
}

}

function rentalCarCost(){
    let car = prompt("How many days would you like to rent a car?")
    while(isNaN(car) || car === null)(
        car = prompt("Please enter a valid number of days")
    )
    let cost = car * 40 
    if(car>10){
        cost = cost - cost*0.05
    }
    console.log(`The cost of your car for ${car} days is $${cost}`)
    return cost
}

function totalVacationCost(){
    let hotel = hotelCost();
    let plane = planeRideCost();
    let car = rentalCarCost();
    let total = hotel + plane + car
    console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}.`)
    console.log(`Your total is $${total}`)
    return total
}
totalVacationCost()