let input = document.getElementById("input")
let inputtxt = document.createElement('div');
document.body.appendChild(inputtxt)
input.addEventListener("keyup", addLettersAfterKeyPress);

function addLettersAfterKeyPress(event){
    let key = event.keyCode
    console.log(key)
    if(key<65 || key> 90){
        input.value = input.value.replace(event.key, '')
    }else{
        inputtxt.innerHTML = input.value
    }
}