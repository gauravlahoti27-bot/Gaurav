function FP(){
    let n = parseInt(prompt("Enter the no. of lines for the Fibonacci Pyramid:"));
    let a=0,b=1,c;
    let fibo = "";
    for(let i=1;i<=n;i++){
    for(let j=1;j<=i;j++){
        fibo += a + " ";
        let c = a + b;
        a = b;
        b = c;
    }
    fibo += "\n";
}
    
alert(fibo)
}


