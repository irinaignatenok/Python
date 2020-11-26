



function rectangularText(str){
    let words = prompt('Please say a few words (separated by commas)')
    words = words.split(',').map(i => i.trim())
    console.log(words);
    let longestWord = '';
    for(word of words){
        if(word.length > longestWord.length){
            longestWord = word /*we will assigh to the variable longestWord which one is the longest*/
        }
    }
    console.log(words)
    console.log('*'.repeat(longestWord.length + 4))

    for(w of words){
        // to create space for each word that has letters of longest word
        let space = (' '.repeat(longestWord.length - w.length))
        // we'll print the space that created with 2 sides if frame
        console.log('* '+ w + space+ ' *')
    }
    console.log('*'.repeat(longestWord.length + 4))
}




