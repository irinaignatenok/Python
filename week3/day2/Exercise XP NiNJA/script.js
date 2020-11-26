// Exercise 1
// Given the birthday year of two people, find the date when the younger one is exactly half the age of the other.
// Notes: The dates are given in the format YYY

let currentYear = 2020

let year   = 1965;
let halfAge = 1990;
let olderAge = (currentYear - year)/2; /*28*/
let ageOfOlderAge = 1990 + olderAge;
console.log(ageOfOlderAge)

// Exercise2
// A valid zip code is as follows:
// Zip codes consist of 5 consecutive digits
// Must only contain numbers (no non-digits allowed).
// Must not contain any spaces.
// Must not be greater than 5 digits in length.
 
let zipCode = prompt('Please enter your zip code')

if(Number.isNaN(zipCode) == false && zipCode.includes(" ") == false
    && zipCode.length <= 5){
    console.log('good')
}else{
    console.log('error') 
}

// Exercise 3
// Ask the user for a word and save it in a variable.
// Delete all the vowels of the string and console.log the result
let word = prompt('Please enter a word');
let word1 = word.split('')
let arr = ['a','e','i','o','u']
word1 = word1.map(x=>x.replace(/[aeiou]/g, ''))
console.log(word1)
word1.split()


console.log(word1.map(x => x.replace(arr, "")))

console.log(word1)
if(word1){
    console.log(word.replace(word.slice(word1,word1 +(word.length - word1)), ""))
}else{
    console.log('error')
}
