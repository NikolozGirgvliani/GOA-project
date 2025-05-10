// 1. Person ობიექტი
const person = {
  name: "Nika",
  age: 15,
  hobby: "Judo",
  city: "tbilisi",
  profession: "Pupil"
};

// ობიექტის თვისებების გამოტანა კონსოლში
console.log("სახელი:", person.name);
console.log("ასაკი:", person.age);
console.log("ჰობი:", person.hobby);
console.log("ქალაქი:", person.city);
console.log("პროფესია:", person.profession);


// 2. Car ობიექტი + BONUS ამოცანა
const car = {
  brand: "Lamborgini",
  model: "Aventador",
  color: "Orange",
  makeYear: 2000
};

// if-else შემოწმება გამოშვების წლის მიხედვით
if (car.makeYear > 1990) {
  console.log("pass");
} else {
  console.log("Not pass");
}
