// Exercise 1
const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift()
fruits.sort()
fruits.push("Kiwi")
fruits.splice(0,1)
fruits.reverse()
console.log(fruits)

// Exercise 2
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0])