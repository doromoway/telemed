document.addEventListener("DOMContentLoaded", function () {
    let num1 = document.getElementById("num1");
    let num2 = document.getElementById("num2");
    let num3 = document.getElementById("num3");
    let num4 = document.getElementById("num4");
    let num5 = document.getElementById("num5");
    let num6 = document.getElementById("num6");
    let but = document.getElementById("but");
    let result = document.getElementById("result");
    let results1 = document.getElementById("results1")

    but.addEventListener("click", () => {
        let value1 = parseFloat(num1.value); 
        let value2 = parseFloat(num2.value);
        let value3 = parseFloat(num3.value); 
        let value4 = parseFloat(num4.value);
        let value5 = parseFloat(num5.value); 
        let value6 = parseFloat(num6.value); 
        let sum = value1 + value2 + value3 + value4 + value5 + value6 ;
        
        if (sum === 100) {
            console.log("Сумма равна '100' =", sum);
        } else if (sum < 10.75) {
            console.log("Сумма меньше '100' =", sum);
        } else {
            console.log("Сумма больше '100' =", sum);
        }
        if (sum === 100) {
            results1.innerHTML= "<strong>Сумма равна '100' =" + sum + "</strong>";
        } else if (sum < 100) {
            results1.innerHTML = "<strong>Сумма меньше '100' =" + sum + "</strong>";
        } else {
            results1.innerHTML = "<strong>Сумма больше '100' =" + sum + "</strong>";
        }
        result.innerHTML = "<strong>Сумма: " + sum + "</strong>";
        console.log("Сумма:", sum);
    });
});