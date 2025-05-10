function calculateBMI() {
    let weight = document.getElementById('weight').value;
    let height = document.getElementById('height').value;
    let result = document.getElementById('bmi');
    let classificationEl = document.getElementById('classification');

    weight = parseFloat(weight);
    height = parseFloat(height);


    height = height / 100;
    let bmi = weight / (height * height);

    let classification = "";

    if (bmi < 18.5) {
        classification = "Underweight";
    } else if (bmi < 24.9) {
        classification = "Normal";
    } else if (bmi < 29.9) {
        classification = "Overweight";
    } else if (bmi < 34.9) {
        classification = "Little Obese";
    } else {
        classification = "Unhealthy Obese";
    }

    result.textContent = `Your BMI is: ${bmi.toFixed(1)}`;
    classificationEl.textContent = classification;
}
