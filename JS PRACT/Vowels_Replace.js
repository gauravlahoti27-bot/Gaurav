function VR(){
    let char = prompt("Enter a sentence: ");
    let charr = char.toString()
    let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    let r = "";
    for(let i=0;i<charr.length;i++){
        if(vowels.includes(charr[i])){
            r+="*"
        }
        else{
            r+=charr[i]
        }
    }
    alert("String after replacing vowels with '*': " + r)
}