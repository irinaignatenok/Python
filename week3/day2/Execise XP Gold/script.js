// Exercise 1
let language = prompt('What language do you speak?');
switch (language) {
    case 'French':
        console.log('Bonjour');
        break;
    case 'English':
        console.log('Hello');
        break;
    case 'Hebrew':
        console.log('Shalom');
        break;
        default:
            console.log('01110011 01101111 01110010 01110010 01111001')
}
// Exercise 2 
let grade = parseFloat(prompt("What's yourgrade?"));
if(grade > 90){
    console.log('A')
}else if(grade > 80 && grade <= 90){
    console.log('B')
}else if(grade >= 70 && grade <= 80){
    console.log('C')
}
else{
    console.log('D')
}

// Exercise 3
let verb = "sleep";

let verbLength = verb.length;
let checkVerb = verb.slice(-3);
let newState = verb.includes(checkVerb) != 'ing';
if(verbLength >= 3 && newState == false){
    console.log(verb + 'ing')
}else if(verb.includes(checkVerb)) {
    console.log(verb + 'ly')
}else{
    console.log(verb)
}