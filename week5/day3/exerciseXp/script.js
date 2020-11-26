let container = document.getElementById("container");
let animate = document.getElementById("animate")
let square3 = document.getElementById("box")
let pos = 0
let id = setInterval(() => {
    if(pos == 350){
        clearInterval(id)
    }else{
        pos++
        animate.style.top = pos + 'px';
        animate.style.left = pos + 'px';
    }
}, 5);

animate.addEventListener("dragstart", dragStart)

square3.addEventListener("dragover", dragOver)
square3.addEventListener("drop", drop)
square3.addEventListener("dragenter", allowEnter)
square3.addEventListener("dragleave", allowLeave)
function allowDrop(event){
    event.preventDefault()
}

allowEnter = (event) =>{
event.target.classList.add('over')
}

allowLeave = (event) => {
    event.target.classList.remove('over') 
}

dragStart = (event) => {
    console.log("target: ", event.target)
    console.log("id: ", event.target.id)
    event.dataTransfer.setData("text", event.target.id)
}

dragDrop = (event) => {
    event.preventDefault()
    let data = event.dataTransfer.getData("text")
    console.log("data: ", data)
    let box = document.getElementById('data')
event.target.appendChild(box);
}