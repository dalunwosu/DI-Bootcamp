let user = document.getElementById("container")
console.log(user)
let label = document.getElementsByClassName("list")[0]
console.log(label)
let richard = label.children[1]
console.log(richard)
richard.textContent = "Richard"
console.log(richard)
let list = document.getElementsByClassName("list") [0]
console.log (list)
let kids = list.children[0]
kids.textContent = "Dalu"
let chart = document.getElementsByClassName("list") [1]
console.log(chart)
let child = chart.children[0]
child.textContent = "Dalu"
let remove = document.getElementsByClassName("list") [1]
let sarahGone = remove.children[1]
console.log(sarahGone)
let gone = remove.removeChild(sarahGone)
