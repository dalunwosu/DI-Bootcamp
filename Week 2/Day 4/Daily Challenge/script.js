let words = prompt("Give me any amount of words separated by commas").split(",")
let longestWord = words [0]
for(i=0; i<words.length; i++){
    if(words[i].length>longestWord.length){
        longestWord = words[i]
    }
}

console.log("*".repeat(longestWord.length + 4));
for (let i = 0; i < words.length; i++) {
    console.log(`* ${words[i]}${" ".repeat(longestWord.length - words[i].length)} *`);
}
console.log("*".repeat(longestWord.length + 4));
