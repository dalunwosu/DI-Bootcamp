let newName = document.getElementById("navBar")
newName.setAttribute("navbar","socialNetworkNavigation")
console.log(newName)
let newList = document.createElement("li")
console.log (newList)
let writing = document.createTextNode("Logout")
let link = document.createElement("a")
link.href = "#"
link.append(writing)
newList.appendChild(link);
let finish = document.getElementById("navBar").children[0]
console.log(finish)
finish.appendChild(newList)

// bonus
let bonus = document.getElementById("navBar").children[0]
let kid = bonus.firstElementChild
let kidText = kid.textContent
let child = bonus.lastElementChild
let childText = child.textContent

console.log(`The text content of the first element is ${kidText}`)
console.log(`The text content of the last element is ${childText}`)