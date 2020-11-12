let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// Exercise 1
// Remove the Banana from the array.
fruits.shift()
console.log(fruits)
// Exercise 2
// Sort the array in order.
fruits.sort()
console.log(fruits)
// Exercise 3
// Put “Kiwi” at the end of the array.
fruits.push("Kiwi");
console.log(fruits)
// Exercise 4
// Remove “Apples” from the array. Don’t use the same method as in the 
fruits.splice(0,1)
console.log(fruits)
// Exercise5
// Sort the array in reverse order. (Not alphabetical, 
fruits.reverse()
console.log(fruits)

// Exercise 6
// Access the item “Oranges”.
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
moreFruits[1][1][0]