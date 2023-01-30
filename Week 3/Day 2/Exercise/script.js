// Exercise 1
document.getElementById("red").onclick = function red() {
  document.body.style.backgroundColor = "red";
};

document.getElementById("blue").onclick = function blue() {
  document.body.style.backgroundColor = "blue";
};

// Exercise 2
const colors = ["blue", "yellow", "green", "pink"];

for (let i = 0; i < colors.length; i++) {
  let button = document.createElement("button");
  button.innerText = `Click here to change to ${colors[i]}`;
  button.addEventListener("click", changeColor);
  button.style.padding = "20px";
  function changeColor() {
    document.body.style.backgroundColor = `${colors[i]}`;
  }
  const container = document.getElementById("container");
  container.appendChild(button);
}

// Exercise 1 - basic addEventListener
// Create two buttons - id of "red", id of "blue"
// When we click on the red button -> Change the backgroundcolor of the page to red
// When we click on the blue button -> Change the backgroundcolor of the page to blue

// Exercise 2 - using the event object
// const colors = ["blue", "yellow", "green", "pink"];

// Add inside the HTML file a div of id "container" (do it directly in the HTML)
// Using a loop, add one button per color inside the div container (do it directly in the JS)
// Each button should have an "click" event listener that changes the background color of the document, to the color of the button (do it directly in the JS
