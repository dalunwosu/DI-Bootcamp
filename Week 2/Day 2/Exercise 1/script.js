const userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

userCart["lastname"]= "Smith"
console.log(userCart)

userCart["username"]= "Tom"
console.log(userCart)

userCart["prices"]["pear"]*= 1.17
console.log(userCart)

const question = prompt("Pick between an apple, pear or Banana").toLowerCase();
const value= userCart["prices"][question]
console.log(`The price of ${question} is ${value} dollars`)


let grade = prompt("Enter your grade:");

if (grade > 90) {
  console.log("A");
} else if (grade >= 80 && grade <= 90) {
  console.log("B");
} else if (grade >= 70 && grade < 80) {
  console.log("C");
} else if (grade < 70) {
  console.log("D");
}



// 1. Add the lastname Smith to the object
// 2. Change the username from John to Tom
// 2. Change the price of the pear, so it will include the Taxes. (17% is 0.17)
// 3. Ask the user for the fruit he wants between Apple, Banana and Pear. Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA"
// 4. Console.log the price for the specific fruit the user wants