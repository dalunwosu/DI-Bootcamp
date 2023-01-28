function bottles(){
var num = prompt("Enter a number so we can start counting bottles");

for (var i = num; i>= 0; i--){
    let minus = num -i
    if (i>1){
        console.log (`${i} bottles of beer on the wall `);
        console.log(`${i} bottles of beer`);
        if (minus === 1) {
            console.log(`Take ${minus + 1}  down, pass it around`);
          } else {
            console.log(`Take ${minus + 1} down, pass them around`);
          }
    }
    else if (i === 1){
        console.log (`${i} bottle of beer on the wall `);
        console.log(`${i} bottle of beer`);
        console.log(`Take ${minus + 1} down, pass it around`);
    }
    else if (i === 0){
        console.log(`No bottles on the wall`)
    }
}
}

bottles()