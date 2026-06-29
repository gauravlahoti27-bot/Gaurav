function AdamNumber(){
    let num = parseInt(prompt("Enter a number:"));
    let square = num* num;
    let reverse = parseInt(num.toString().split("").reverse().join(""))
    let reverseSquare = reverse*reverse
    let rstring = (reverseSquare.toString().split("").reverse().join(""))

    if(square==rstring){
        alert(num + " is a Adam Number")
    }
    else{
        alert(num + " is not a Adam Number")
    }
}