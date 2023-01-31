let idInterval;
function appear() {
    let container = document.getElementById("container")
  let banner = document.createElement("p");
  banner.setAttribute ("id","banner")
  container.appendChild(banner);
  idInterval = setInterval(changeNumber, 1000,banner);
}

appear()

let counter = 10;

function changeNumber(bannerP){
    if (counter === 0){
clearInterval(idInterval)
bannerP.textContent = `The sales is over`
    }
    else{
  bannerP.textContent = `The sales end in ${counter} sec`
    }
    counter --
}