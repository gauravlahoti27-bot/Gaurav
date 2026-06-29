function NumberToWords(number) {
    
    const units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
    const teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
        "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
        const tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", 
            "Sixty", "Seventy", "Eighty", "Ninety"];
    const hundreds = ["", "One Hundred", "Two Hundred", "Three Hundred", 
                      "Four Hundred", "Five Hundred", "Six Hundred", 
                      "Seven Hundred", "Eight Hundred", "Nine Hundred"];

    if (number === 0) return "Zero";

    if (number < 10) 
        return units[number];

    else if (number < 20) 
        return teens[number - 10];

    else if (number < 100) 
        return tens[Math.floor(number / 10)] +
               (number % 10 ? " " + units[number % 10] : "");

    else if (number < 1000) 
        return hundreds[Math.floor(number / 100)] +
               (number % 100 ? " " + NumberToWords(number % 100) : "");

    else 
        return "Number out of range";
}
function NumberConverter(){
let num = parseInt(prompt("Enter a number:"));

if (!isNaN(num) && num >= 0 && num < 1000) {
    alert(NumberToWords(num));
} else {
    alert("Invalid input or number out of range.");
}
}