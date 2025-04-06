function checkCheckboxes() {
    let opt1 = document.getElementById("option1").checked;
    let opt2 = document.getElementById("option2").checked;

    let result = (opt1 && opt2);

    console.log("Result of the operation is " + result);
    document.getElementById("resultText").textContent = "Result of the operation is " + result;
  }