// Exercise XP
// Exercise 1
let arr = ['blue', 'red', 'white', 'black'];
for (let i = 0; i< arr.length; i++){
        console.log('My #', i+1, 'choice is', arr[i])
    }
   
// Bonus
// doesn't work properly

let arr = ['blue', 'red', 'white', 'black'];
let suffix = ['st', 'nd', 'rd', 'th'];
for (let i = 0; i < arr.length; i++){
for(let  j=i;j< suffix.length; j++){
    if(arr[i] == suffix[j]){
        // let temp = arr[i]
        // arr[i]= suffix[j]
        // suffix[j] = temp
        let temp = suffix[j]
        suffix[j]= arr[i]
        arr[i] = temp
    }
    console.log('My #', (i+1 )+ suffix[j], 'choice is', arr[i])
}

}
// second try
let arr = ['blue', 'red', 'white', 'black'];
for (let i = 0; i < arr.length; i++){
    let num = i+1;
    let suffix;
    if( num ==1){
        suffix = 'st'
    }else if(num == 2){
        suffix = 'nd'
    }else if(num == 3){
        suffix = 'rd'
    }else {
        suffix = 'th'
    }
    console.log('My ', num + suffix, 'choice is', arr[i])
}
// Exercise 2 

// A group of friends have decided to start a secret 
// society. The society’s name will be the first letter of each of their firstnames,
//  sorted in alphabetical order.
// Console.log the name of their secret society.
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
for(let i in names){
let secretName = names[i][0]
console.log(secretName)
    }
    
    // Exercise 3
 let number = parseFloat(prompt('Please a number'))
while(number < 10){
    number = prompt('The number is smaller than 10. Give me another numer')
}

// Exercise 4

let people = ["Greg", "Mary", "Devon", "James"]
// 1. Using a loop, iterate through this array and console.log all of the people.
for (let i in people){
    console.log(people[i])
}
// 2.Write the command to remove “Greg” from the array.
let people = ["Greg", "Mary", "Devon", "James"]
people.shift()
console.log(people)

// 3.Write the command to replace “James” by “Jason” in the array.
let people = ["Greg", "Mary", "Devon", "James"]
people.splice(3,1,'Jason')
console.log(people)
// 4.Write the command to add your name to the end of the array.
let people = ["Greg", "Mary", "Devon", "James"]
people.push('Irina')
console.log(people)
// 5.Using a loop, iterate through this array and after console.log-ing “Mary”, exit from the loop.
let people = ["Greg", "Mary", "Devon", "James"]
for (let i= 0; i< people.length; i++){
    if(people[i] == 'Mary'){
        console.log('Bye Mary')
        break;
    }
}
// 6.Write the command to make a copy of the array using slice. The copy should NOT include “Mary” or your name.
let people = ["Greg", "Mary", "Devon", "James"]
let arr = people.slice()
console.log(arr)
arr.splice(1,1)
console.log(arr)

