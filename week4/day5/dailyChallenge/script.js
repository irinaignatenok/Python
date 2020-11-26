let containerDiv = document.getElementById('root')
let song = containerDiv.innerHTML
let input = document.getElementById('number')
let str = "bottles of beer on the wall "
// let lyrics = str.repeat(2)
let beers = parseInt(prompt("enter rhe number"))

function lyricsToTheSong(){
    // let p = document.createElement('p');
    // p.appendChild(document.createTextNode(input.value))
    // p2 = document.createElement('p');
    // p2.appendChild(document.createTextNode(`${str}`))
    // containerDiv.appendChild(p);
    // containerDiv.appendChild(p2);
    // containerDiv.inner = `${p}${p2}`
   
    for(let i=99; i >= 1; i--){
        if(i == 1){
            bottles = 'bottle';
        }else{
            bottles = 'bottles'
        }
        song = i + ' ' + bottles+ ' of beer on the wall.'
        if(i < 99) {
            let p1 = document.createElement('p');
            p1.appendChild(document.createTextNode(`${i}  ${bottles} of beer on the wall.
            ${i} ${bottles} of beer.
            Take one down.
            Pass it around.`))
            containerDiv.appendChild(p1)
        }

        if(i == 1){
            song = "No bottles of beer on the wall."
        }
    }
}

input.addEventListener("change", lyricsToTheSong)