function CountULDS(){
    let str = prompt("Enter a string:")
    let U=L=D=S=Spaces=0
    for(let i=0;i<str.length;i++){
        let char = str[i]
        if(char>='A' && char<='Z'){
            U++
        }
        else if(char>='a' && char<='z'){
            L++
        }
        else if(char>='0' && char<='9'){
            D++
        }
        else if(char!==' '){
            S++
        }
        else{
            Spaces++
        }
    }
    alert("UPPERCASE: "+U)
    alert("LOWERCASE: "+L)
    alert("DIGITS: "+D)
    alert("SPECIAL CHARACTERS: "+S)
    alert("SPACES: "+Spaces)
}