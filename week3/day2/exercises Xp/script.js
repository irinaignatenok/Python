// Exercise XP
// Exercise1
// Create 2 variables, x and y. Each of them has a different numeric value.
// Write an if/else statement that checks the biggest number.
 let x = 5;
 let y = 7;

 if(x > y){
     console.log("x is the biggest number")
 }else{
    console.log("y is the biggest number")
 }
 // Exercise2
//  Create a variable newDog that is equal to the string “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just use 2 console.log).

let newDog = "Chihuahua";
console.log(newDog.length)

console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())
// Check if the variable newDog equals to “Chihuahua”
// if it does, display ‘I love Chihuahua, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats

if (newDog == 'Chihuahua'){
    console.log('I love Chihuahua, it’s my favorite dog breed')
}else{
    console.log('I dont care, I prefer cats')
}
