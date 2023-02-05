const tasks = [];

function addTask() {
  const task = document.querySelector("input").value;
  if (task) {
    tasks.push(task);
    const taskElement = document.createElement("div");
    taskElement.innerHTML = `
      <input type="checkbox">
      <label>${task}</label>
      <i class="fas fa-times"></i>
    `;
    document.querySelector(".listTasks").appendChild(taskElement);
    document.querySelector("input").value = "";
  }
}

document.querySelector("form").addEventListener("submit", function(event) {
  event.preventDefault();
  addTask();
});
