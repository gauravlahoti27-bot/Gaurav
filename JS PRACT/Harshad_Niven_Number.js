function HNN(){
    let num = parseInt(prompt("Enter a number:"))
    let originalNum = num
    let sum = 0
    while(num > 0){
        let digit = num%10
        sum += digit
        num = Math.floor(num/10)
    }
    if(originalNum % sum == 0){
         alert(originalNum + " is a Harshad/Niven Number")
    }
    else{
        alert(originalNum + " is not a Harshad/Niven Number")
    }
}