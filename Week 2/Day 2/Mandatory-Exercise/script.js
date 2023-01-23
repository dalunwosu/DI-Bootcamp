// Exercise 1
let x = 5;
let y = 2;
 if (x>y){
    console.log("x is bigger number")

 } 
 else if (y>x){
    console.log("y is bigger number")
 }

// Exercise 2
let newDog= "Chihuahua"
console.log(newDog.length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())

if (newDog="Chihuahua"){
    console.log("I love Chihuahuas, it\'s my favorite dog breed")
}
else if (newDog !=Chihuahua){
    console.log("I dont care, I prefer cats")
}

// Exercise 3
let question = prompt("Pick a number")
if (question % 2 == 0){
    console.log(`${question} is an even number`)
}
else if (question % 2 !== 0){
    console.log(`${question} is an odd number`)
}

// Exercise 4 
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let number = users.length
console.log(number)
if (number==0){
    console.log(`no one is online`)
}
else if(number==1){
    console.log(`${users[0]} is online`)
}
else if (number==2){
    console.log(`${users[0]} and ${users[1]} are online`)
}
else if (number>2){
    console.log(`${users[0]}, ${users[1]} and ${number-2} more are online`)
}