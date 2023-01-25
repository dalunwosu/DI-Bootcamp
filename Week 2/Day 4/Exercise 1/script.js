function myAge (age){
    let mumAge = 2 * age
    console.log(`my mum is ${mumAge} and my dad is ${1.2*mumAge}`)
}
myAge(17)


function checkQuantityOrder (quantity,name="Client"){
    if (quantity>5 && quantity<= 10){
        console.log (`Dear ${name}, you won a bouquet of flowers`)
    }
    else if(quantity>10 && quantity<=20){
        console.log (`Dear ${name}, you won a bottle of wine`)
    }
    else if(quantity>=20){
        console.log (`Dear ${name}, you won a trip to Paris`)
    }
}

checkQuantityOrder(8,"John");
checkQuantityOrder(15);
checkQuantityOrder(30, "David");

const prices = [20,30,10,4];
function calculateTotal(){
let sum =0;
for (let i = 0; i<prices.length; i++){
    sum = sum + prices[i];
}
console.log(sum)
}
calculateTotal()