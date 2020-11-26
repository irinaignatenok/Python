function my_f(arg){
    document.getElementById('display').value += arg
    if(arg == 'reset'){
        document.getElementById('display').value = '';
    }
}

function solve(){
    let inputValue = document.getElementById('display').value;
    let calculate = eval(inputValue)
    document.getElementById('display').value = calculate
}

// function clear(){
//     let elem = document.getElementById('display').value
//     document.getElementById('display').value= elem.substring(0, elem.length-1)
// }

