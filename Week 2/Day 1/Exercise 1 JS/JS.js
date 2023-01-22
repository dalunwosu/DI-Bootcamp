let addressNumber = 7;
let addressStreet = "Jam Street";
let country = "Nigeria";
let globalAddress = `I live in ${addressStreet} ${addressNumber}, in ${country}`;

console.log(globalAddress)

const birthYear = 2005
let futureYear = 2074
const futureAge= futureYear - birthYear
let sentence = ` I will be ${futureAge} in ${futureYear}`;
console.log(sentence)

let pets = ['cat','dog','fish','rabbit','cow'];
let dog = pets[1]
console.log(dog)
pets[3] = 'horse'
console.log(pets)

console.log(pets.length)

alert("wubalubbadubdub");

let age = prompt('How old are you?', 0);
alert(`You are ${age} years old!`); 

let isBoss = confirm("Are you the boss?");
alert(isBoss);
console.log('To be or not to be'.indexOf('To'));
console.log('To be or not to be'.indexOf(' '));
console.log('To be or not to be'.indexOf('o', 2));
console.log('To be or not to be'.indexOf('be', 4));
console.log('To be or not to be'.indexOf('to'));
console.log('To be or not to be'.indexOf('B'));
console.log('To be or not to be'.indexOf('', 9));
