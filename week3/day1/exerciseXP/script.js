// Exercise XP Gold
let me = ["my","favorite","color","is","blue"]
me.toString()

// Exercise XP Gold Mixup
// Create two strings
// Create a variable which value is the concatenation of the 
// two strings (separated by a space) slicing out and swapping 
// the first 2 characters of each.

let str1 = "Hello";
let newStr1 = str1.slice(2)
let firstLetterOfStr1 = str1.slice(0,2)
let str2 = "Irina";
let newStr2 = str2.slice(2)
let firstLetterOfStr2 = str2.slice(0,2)
let newString = firstLetterOfStr2 + newStr1 +" " + firstLetterOfStr1 + newStr2
console.log(newString)

// Exercise XP GOLD Calculator
// Prompt the user for the first number.
// Store that first number
// Prompt the user for the second number.
// Store that second number
// Alert the result of the SUM of these two numbers.
// BONUS: Make a program that can subtract, multiply, and also divide!

let firstNumber = prompt('Please , Enter a number');
let num1 = parseInt(firstNumber)
let mode = prompt('Please enter a math operator +, -, /, *')
let secondNumber = prompt('Please, enter the second number')
let num2 = parseInt(secondNumber)
if(mode == '-'){
    num1-num2
} else if(mode == '+'){
    num1+num2
}else if(mode == '*'){
    num1*num2
}else{
    num1/num2
}
// Exercise XP Ninja
// 1.You’re given a string of words. You need to find the word “Nemo”, and 
// return a string like this: “I found Nemo at [the order of the 
// word you find nemo]!”.

let str = "I am finding Nemo!"
let word = str.includes("Nemo")
str.search("Nemo")
console.log(word)
let word1 = str.indexOf("Nemo")
let word2 = str.search("Nemo")

