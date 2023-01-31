let box = document.getElementById("box");
box.setAttribute("draggable", "true");
let target = document.getElementById("target");
target.addEventListener("drop", function (event) {
  event.preventDefault();
  let data = event.dataTransfer.getData("text");
  let box = document.getElementById(data);
  event.target.appendChild(box);
});

box.addEventListener("dragstart", function (event) {
  event.dataTransfer.setData("text", event.target.id);
});
target.addEventListener("dragenter", function (event) {
  event.target.classList.add("over");
});
target.addEventListener("dragover", function (event) {
  event.preventDefault();
});
target.addEventListener("dragleave", function (event) {
  event.target.classList.remove("over");
});
