let str = "The weather is not bad today";
let str1 = str.indexOf("not");
let str2 = str.indexOf("bad");

if (str1 == -1 || str2 == -1){
    console.log(str)
} else if(str1 < str2){
   console.log(str.replace(str.slice(str1, str2+ ((str.length - str2))), "good"))
 
}else{
 
    console.log("The weather is not bad today")
}

// another way
let str = "The weather is not bad today";
let arr = str.split(' ')
let not = arr.indexOf("not");
let bad = arr.indexOf("bad");
if(not !== -1 && bad !== -1 && not < bad){
    arr.splice(not, (bad-not)+1, 'good')
    console.log('2', arr)
}
console.log(arr.join(' '))