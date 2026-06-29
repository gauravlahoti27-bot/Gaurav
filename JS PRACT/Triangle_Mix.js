function TMP(){
    let n = parseInt(prompt("Enter the number of rows:"));

    console.log("*");

    // Increasing part
    for(let i = 1; i <= n; i++){
        let line = "";
        for(let j = 1; j <= i; j++){
            line += j + " ";
        }
        line += "*";
        console.log(line);
    }

    // Decreasing part
    for(let i = n-1; i >= 1; i--){
        let line = "";
        for(let j = 1; j <= i; j++){
            line += j + " ";
        }
        line += "*";
        console.log(line);
    }

    console.log("*");
}