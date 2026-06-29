function FRD(){
    let num = prompt("Enter  number: ")
    let nnum = num.toString()
    let freq = {}
    for (let i=0;i<nnum.length;i++){
        let d=nnum[i]
        if(freq[d]){
            alert("First Repeating Digit: " + d)
            return;
        }
        else{
            freq[d]=1
        }
    }
    alert("No Repeating Digit")
}    