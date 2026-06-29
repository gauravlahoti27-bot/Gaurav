function LWSWS() {
    let sentence = prompt("Enter a sentence:");
    if (!sentence) return;

    let longest = "";
    let current = "";

    for (let i = 0; i < sentence.length; i++) {
        if (sentence[i] !== " ") {
            current += sentence[i];
        } else {
            if (current.length > longest.length) {
                longest = current;
            }
            current = "";
        }
    }

    if (current.length > longest.length) {
        longest = current;
    }

    alert("Longest word is: " + longest);
}