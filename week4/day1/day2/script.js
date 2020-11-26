let planets = [
    {
        planet:'Mercury',
        moon: 0
    }, {
        planet:'Venus',
        moon: 0
    },{
        planet:'Venus',
        moon: 0
    }

    , , 'Earth','Mars','Jupiter',
'Saturn', 'Uranus', 'Neptune'];


for(let planet of planets){
    let newElement = document.createElement('div');
    newElement.className = 'planet';
    newElement.innerHTML = planet
    let randomColor = Math.floor(Math.random()*  16777215).toString(16)
    newElement.setAttribute('style', 'background-color : #' + randomColor)
   document.body.appendChild(newElement)
}

let moonOfEarth = document.getElementsByTagName('div')[3]

let moonOfMars = document.getElementsByTagName('div')[4]
console.log(moonOfMars)

let moonOfJupiter = document.getElementsByTagName('div')[5]
console.log(moonOfJupiter)

let moonOfSaturn = document.getElementsByTagName('div')[6]
console.log(moonOfSaturn)

let moonOfUranus = document.getElementsByTagName('div')[7]
console.log(moonOfUranus)

let moonOfNeptun = document.getElementsByTagName('div')[8]
console.log(moonOfNeptun)

let moons = ['Earth - 1', 'Mars - 1', 'Jupiter -79', 'Saturn - 82', 'Uranus - 27', 'Neptun - 14']


for(let i in moons){
    let satellite = document.createElement('p')
    satellite.className = 'moon';
    satellite.innerHTML = moons[i]
    satellite.setAttribute('style', 'background-color: yellow')
    demo.appendChild(satellite)
}


// for(let color in newclasses){
//     let newColor = document.getElementsByTagName('div');
//     newColor.className = newclasses[color]

// }

// let allPlanets = document.getElementsByClassName('demo')[0]
// let mercury = document.createElement('div')
// mercury.className = 'planet';
// let venus = document.createElement('div')
// mercury.className = 'planet';
// let earth = document.createElement('div')
// console.log(earth)
// earth.className = 'planet';
// let venus = document.createElement('div')
// mercury.className = 'planet';

// for(let planet of planets){
// planet.createElement('div')
//  planet.className = 'planet';
// }
// let planet = document.getElementsByClassName('planet')