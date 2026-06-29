function CharacterFrequency(sentence) {
    sentence = prompt("Enter a sentence:");
    if(!sentence) return;
    const frequency = {};
    for(let i=0;i<sentence.length;i++){
        const char=sentence[i];
        if(frequency[char]){
            frequency[char]++;
        }
        else{
            frequency[char]=1;
        }
    }
    alert("Character Frequency: " + JSON.stringify(frequency))
}