// Exercise 1
let language = prompt("Which Language do you speak?").toLowerCase();
if (language == 'english'){
    console.log('Hello');
}
else if (language == 'french'){
    console.log('Bonjour');
}
else if (language == 'hebrew'){
    console.log ('Shalom');
}
else{
    console.log('01110011 01101111 01110010 01110010 01111001');
}

// Exercise 2
let grade = prompt("Enter your grade:");

if (grade > 90) 
{
  console.log("A");
} else if (80 < grade && grade <= 90)
{
  console.log("B");
} else if (70 <= grade && grade <= 80) 
{
  console.log("C");
} else if (grade < 70) 
{
  console.log("D");
}

// Exercise 3
let statement = prompt("Enter a verb")
if (statement.length>= 3 &&  !statement.endsWith("ing")) {
    console.log(statement + "ing");
}
else if (statement.length>= 3 && statement.endsWith("ing")) {
    console.log(statement + "ly");
}
else if (statement.length<3){
    console.log(statement);
}