// Exercise1
for(let i of document.getElementsByTagName('p')){
    i.setAttribute("class", "para_article" )  
}
// Exercise2
let article = document.getElementsByTagName('article')[0]
article.removeChild(article.childNodes[5])

// Exercise 3 
// Add an event listener so that when you click on the h2, 
// it is removed from the DOM.

let h2 = document.getElementsByTagName('h2')[0]
h2.addEventListener('click', removeH)

function removeH(){
    article.removeChild(h2)
}
// Exercise 4
// Set the font size of the h1 to be a random pixel size from 0 to 100.
let h1 = document.getElementsByTagName('h1')[0]
let random = Math.floor(Math.random()* 100)
h1.setAttribute("style", `font-size:${random}px`)

// Exercise 5
// Hide the 1st paragraph, when it’s clicked. (use the display property )
let p = document.getElementsByTagName('p')[0]
p.addEventListener("click", hidePara)

function hidePara(){
p.setAttribute("style", "display: none;")
}

// Exercise 6
// Get the values from the inputs and append 
// them to the end of the html, inside a table.
let input1 = document.getElementsByTagName('input')[0]
let input2 = document.getElementsByTagName('input')[1]
input1.addEventListener("change", addInputValue)
input2.addEventListener("change", addInputValue)
function addInputValue(){
    let table = document.createElement('table')
    document.body.appendChild(table)
    let row = document.createElement('tr')
    table.appendChild(row)
        let data1 = document.createElement('td')
        let data2 = document.createElement('td')
        data1.appendChild(document.createTextNode(input1.value))
        data2.appendChild(document.createTextNode(input2.value))
        row.appendChild(data1)
        row.appendChild(data2)
}


// Part2
function getBold_items(){
    let boldText = document.getElementsByTagName('strong')
    for(let i of boldText){
        console.log(i)
    }
}
getBold_items()

// Create a function called : highlight() that 
// changes the color of each bold item to blue.
function highlight(){
    let boldText = document.getElementsByTagName('strong')
    for(let i of boldText){
        i.setAttribute("style", "color:blue;")
    }
}
highlight()
// return_normal() that changes the color of each bold item to black.
function return_normal(){
    let boldText = document.getElementsByTagName('strong')
    for(let i of boldText){
        i.removeAttribute("style")
    }
}
return_normal()

let boldText = document.getElementsByTagName('strong')
for(let i of boldText){
i.addEventListener("mouseover",highlight)
i.addEventListener("mouseout",return_normal)
}

// Exercise3

let form = document.forms[0]
console.log(form)
function calculate(){
    let radius = document.getElementById("radius").value;
    let area = 4 * Math.PI * Math.pow(radius, 2);
    document.getElementById("volume").value = area;
}