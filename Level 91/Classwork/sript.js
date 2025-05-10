let weight = Number(prompt('Enter your weight: '))
let height = Number(prompt('Enter your height: '))

height = height / 100
let BMI = weight / (height * height)


if (BMI < 18.5) {
    console.log('Underweight')

} else if (BMI >= 18.5 && BMI < 24.9) {
    console.log('Normal')

} else if (BMI >= 25 && BMI < 29.9) { 
    console.log('Overweight')

} else if (BMI >= 30 && BMI < 34.9) {
    console.log('Little Obese')

} else {
    console.log('Unhealthy Obese')
}
