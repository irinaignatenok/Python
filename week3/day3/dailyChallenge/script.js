// 1.Using the .toString() method, convert the array to a string.
const numbers = [5,0,9,1,7,4,2,6,3,8];
let newNumbers = numbers.toString()

// 2.Using the .join(), convert the array to a string. Try passing different values into the join.
// Eg .join(“+”), .join(” “), .join(“”)
let numbers = [5,0,9,1,7,4,2,6,3,8];
let newNumbers = numbers.join('=');
numbers.join('');
console.log(typeof(newNumbers))

// Bonus : Sort the array numbers in descending order using for loops 
// (Not using built-in sort methods).
let numbers = [5,0,9,1,7,4,2,6,3,8];
for(let i = numbers.length -1; i>=0; i--){
    console.log(i)
    for(let j=i; j>=0; j--){ /*Looping through the first loop*/
        console.log('j', j)
        if (numbers[i] > numbers[j]){
            let arr = numbers[i];
            numbers[i]= numbers[j]
            numbers[j] = arr
           
        }
    }
}

console.log(numbers)
  