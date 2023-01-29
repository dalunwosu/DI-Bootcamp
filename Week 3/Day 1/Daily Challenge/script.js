const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

const planetColors = ["rgb(255, 153, 153)", "rgb(255, 255, 102)", "rgb(153, 255, 153)", "rgb(204, 153, 255)", "rgb(255, 102, 153)", "rgb(255, 204, 153)", "rgb(102, 153, 255)", "rgb(102, 255, 153)"];

const listPlanets = document.getElementsByClassName("listPlanets")[0];

for (let i = 0; i < planets.length; i++) {
  let planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.style.backgroundColor = planetColors[i];
  planetDiv.innerHTML = planets[i];
  listPlanets.appendChild(planetDiv);
}
