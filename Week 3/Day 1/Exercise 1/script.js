function exercise(){
    let div = document.body.firstChild
    let div1= document.body.firstElementChild
    let ul = div.nextSibling
    let ul1 = div1.nextElementSibling
    let pete = ul.firstChild
    let pete1 = ul1.lastElementChild
    console.log(div)
    console.log(div1)
    console.log(ul)
    console.log(ul1)
    console.log(pete)
    console.log(pete1)
}

//correction
function correction() {
const firstDiv = document.body.firstElementChild;
const firstDivSecondWay = document.body.children [0];
const list = document.body.children [1];
const listOtherWay = firstDiv.nextElementSibling
const secondLi = list.lastElementChild
const secondLiOtherWay = list.children[1]
console.log(firstDiv)
console.log(firstDivSecondWay)
console.log(list)
console.log(listOtherWay)
console.log(secondLi)
console.log(secondLiOtherWay)
}
correction()