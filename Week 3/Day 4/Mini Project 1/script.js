const colors = ["red","orangered","orange","yellow","green","forestgreen", "darkgreen" ,"lightblue","blue","darkblue","purple","violet","indigo","pink","brown","grey","black","white"];
let sidebar = document.getElementById("sidebar")
let grid = document.getElementById("grid")
let button = document.getElementById("clear")
var bg;
function pallete(){
for(let color of colors){
 let hue = document.createElement("div")
  console.log(color);
  hue.style.backgroundColor = `${color}`
  hue.setAttribute("class", "color")
  hue.addEventListener("click",retrieveColor)
  sidebar.appendChild(hue)
}
function retrieveColor(event){
  bg = event.target.style.backgroundColor
 }
}
pallete()

function body (){
for (let i=0; i<=1440; i++){
    let main = document.createElement("div")
    main.setAttribute("class","lines")
    main.addEventListener("click",addColor)
  main.addEventListener("mousedown", coloring);
  main.addEventListener("mouseover", coloring);
  main.addEventListener("mouseup", coloring);
    grid.appendChild(main)
    button.addEventListener("click", function (){
      main.style.backgroundColor = "white"
      })
}
}
function addColor(event){
  event.target.style.backgroundColor = bg
  }
body()
let checkIfMouseDown = false
function coloring(event){
 switch (event.type){
  case "mousedown":
    checkIfMouseDown = true
    addColor(event)
    break
    case  "mouseover":
      if (checkIfMouseDown) {
        addColor(event);
      }
      break;
    case "mouseup":
      checkIfMouseDown = false;
      break;
    default:
      break;
  }
 }

















// # HTML
// - 2 sections
// - In the 1st section : button
// ​
// # JS
// ​
// ## Creation Part
// ​
// - Pallet section
//     - array of 21 colors
//     - loop through the array of color, and for each color create a div
//     - for each div add background color
//     - make each div clickable by adding an eventlistener of `click` that will call the function `retrieveColor`
//     (you could also give a value attribute to each div)
//     - append them the section
// ​
// ​
// - Grid section
//     - loop a lot of times (24 rows*60 colums) and create div
//     - make each div clickable by adding an eventlistener of `click` that will call the function `addColor`
//     - make each div mouseover, mousedown, mouseup by adding an eventlistener of `mouseover, mousedown, mouseup`
//     - append them to the 2nd section
// ​
// ​
// ## retrieveColor
// - evt target and find the background color
// - store the color in a variable
// ​
// ## addColor
// - use the variable that stores the color, to add the color as a background color
// of the div I click
// ​
// ## coloring
// Events
//     mousedown 
//     mouseover
//     mouseup
// ​
// variable flag checkIfMouseDown will start as false, as soon as the mouse is down
// this variable will change to true
// as soon as the mouse is up this variable will change to false
// ​
// In the mouseover, we check, if the variable is true we can color
// if not we don't
// ​
// ## ClearButton
// add an event listener to the button that when clicked on, loop over the grid to hange the background color to white
// ​
// # CSS
// - display the 2 section - display flex, direction row
// - For the pallet section
//     - use grid : 8 rows, each 1 fr
//                 3 colums, each 1fr
// - For the grid section
//     - use grid : 24 rows, each 1 fr
//                 60 colums, each 1fr