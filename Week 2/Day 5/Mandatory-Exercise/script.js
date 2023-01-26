function playTheGame(){
    let yes = confirm("Would you like to play game? ");
if (yes === false){
alert("No problem, Goodbye");
return;
}
   let answer = prompt("Pick a number between 0 and 10");
    while(isNaN(answer)) {
        answer = prompt("Sorry, not a valid number. Please enter a number between 0 and 10"); //Bonus Change made
    }
   while (answer < 0 || answer > 10){
        answer = prompt("Sorry, not a valid number. Please enter a number between 0 and 10"); //Bonus Change made
    }
let computerNumber = Math.round(Math.random() * 8) + 1;
compareNumbers(answer,computerNumber);
}



function compareNumbers(answer,computerNumber){
    let count = 0;
    while(answer !== computerNumber && count< 2){
        if (answer>computerNumber ){
            alert("Your number is bigger than the computer's, guess again");
            answer = prompt("Give a new number");
        }
        else{
        alert("Your number is smaller than the computer's, guess again");
            answer = prompt("Give a new number");
        }
        count++;
 }
    
    if (answer == computerNumber){
        alert("WINNER")
    }
    else{
        alert("out of chances")
    }
}
