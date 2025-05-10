function calculatePrice() {
  const input = document.getElementById("ageInput").value;
  const age = parseInt(input);
  const result = document.getElementById("result");

  if (isNaN(age) || age < 0) {
    result.textContent = "Enter Valid Age.";
  } else if (age < 6) {
    result.textContent = "Ticket Is Free.";
  } else if (age >= 6 && age <= 17) {
    result.textContent = "Ticket Price: 5$.";
  } else if (age >= 18 && age <= 64) {
    result.textContent = "Ticket Price: 10$.";
  } else if (age >= 65) {
    result.textContent = "Ticket Price: 7$.";
  }
}
