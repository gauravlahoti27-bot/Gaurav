function TechNumber(){
    let num = parseInt(prompt("Enter a number:"));
    let len = num.toString().length
    if(len % 2 !== 0){
        alert("Not a Tech Number (digits not even)");
        return;
    }
    let mid = num.toString().length / 2
    let midNum1 = num.toString().slice(0,mid)
    let midNum2 = num.toString().slice(mid)
    let square = (Number(midNum1)+Number(midNum2))**2
    if(num==square){
        alert(num + " is a Tech Number")
    }
    else{
        alert(num + " is not a Tech Number")
    }
}