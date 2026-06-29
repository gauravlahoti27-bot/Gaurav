 function LWS() {
    let sentence = prompt("Enter a sentence:");
    const words = sentence.split(" ");
    let long = '';

    for (let i = 0; i < words.length; i++) {
        if (words[i].length > long.length) {
            long = words[i];
        }
    }

    alert("Longest word is:" +long);
}