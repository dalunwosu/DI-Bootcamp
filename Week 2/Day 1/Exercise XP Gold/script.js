let sentence = ["my","favorite","color","is","blue"];
let joinedSentence = sentence.join(" ");
console.log(joinedSentence);

let str1 = "mix";
let str2 = "pod";

let str1First= str1.slice(0,2);
let str2First= str2.slice(0,2);
let str3 = str1First + str2.slice(2);
let str4 = str2First + str1.slice(2);
let newWord= str4 + " "+ str3;
console.log(newWord)
