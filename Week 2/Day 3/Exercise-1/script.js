let number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
for (let counter = 0; counter < number.length; counter++){
if(number[counter] %2===0){
    console.log(`${number[counter]} is an even number`)
}
else{
    console.log(`${number[counter]} is an odd number`)
}
}

const prices = [23, 15, 34, 10];

let sum = 0;

for (let i = 0; i < prices.length; i++){
    sum = sum + prices[i]
}

console.log(sum);

const colors = ["blue", "red"]