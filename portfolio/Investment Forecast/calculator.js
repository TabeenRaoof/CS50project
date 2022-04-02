function calc() {

    var tSP = parseFloat(document.querySelector("#tdaySPrice").value);
    var oSP = parseFloat(document.querySelector("#oldSPrice").value);
    var cDiv = (parseFloat(document.querySelector("#curDiv").value))/100;
    var iAm = parseFloat(document.querySelector("#invAmount").value);
    var fVYr = parseFloat(document.querySelector("#selector").value);
    const form = document.getElementById("calculator");
    var calculate;


        // Annual Growth Rate
        aGrowthRate = (((tSP - oSP) / oSP) / 10);
        // Annual Return including dividends
        anROI = aGrowthRate + cDiv
        // investment value in X years
        calculate = iAm + (iAm * (anROI * fVYr));


    const numFormat = new Intl.NumberFormat("en",{
        style: "currency",
        currency: "USD"
    });
    var rslt = numFormat.format(calculate);

    document.querySelector("#result").innerHTML = rslt;

    //change color of result based on return (if negative = red; positive = green)
    if (calculate > iAm) {

    document.querySelector("#result").style.cssText = "color: #5adb5a; font-weight: bold; font-size: 20px;";
    } else if (calculate < iAm) {

    document.querySelector("#result").style.cssText = "color: #ff4d4d; font-weight: bold; font-size: 20px;";
    } else if (calculate == iAm) {

    document.querySelector("#result").style.cssText = "color: white; font-weight: bold; font-size: 20px;";
    }

    form.addEventListener('submit', (e) => {
        e.preventDefault()
    })
}


