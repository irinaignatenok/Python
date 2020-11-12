let str = "The weather is not bad today";
let str1 = str.indexOf("not");

let str2 = str.indexOf("bad");

if (str1 == -1 || str2 == -1){
    console.log(str)
} else if(str1 < str2){
   console.log(str.replace(str.slice(str1, str2 +(str.length - str2)), "good"))
 
}else{
 
    console.log("The weather is not bad today")
}