// 1. შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე, while loop-ის გამოყენებით.
let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

// 2. შექმენით პროგრამა, რომელიც ბეჭდავს ყველა ლუწ რიცხვს 1-დან 20-მდე, while loop-ის გამოყენებით.
i = 1;
while (i <= 20) {
    if (i % 2 === 0) {
        console.log(i);
    }
    i++;
}

// 3. შექმენით პროგრამა, რომელიც იყენებს while ციკლს, რათა გამოთვალოს 1-იდან 10-მდე ყველა რიცხვის
//  ჯამი და გამოიტანოს შედეგი კონსოლში.
i = 1;
let sum = 0;
while (i <= 10) {
    sum += i;
    i++;
}
console.log("Sum of numbers from 1 to 10:", sum);

// 4. შექმენით პროგრამა, რომელიც ბეჭდავს 10-დან 1-მდე რიცხვებს კონსოლში, while loop-ის გამოყენებით.
i = 10;
while (i >= 1) {
    console.log(i);
    i--;
}

// 5. შექმენით პროგრამა, ცვლადში შეინახეთ random რიცხვი 1-დან 50-მდე. შემდეგ,
//  while loop-ის გამოყენებით, სთხოვეთ მომხმარებელს გამოიცნოს რიცხვი prompt()-ის გამოყენებით.
//  ყოველი გამოცნობის შემდეგ, აჩვენეთ შეტყობინება alert()-ის გამოყენებით, რომელიც ეუბნება მომხმარებელს,
//  მათი ვარაუდი რეალურზე მეტია, ნაკლები, თუ ტოლი. პროგრამამ უნდა გააგრძელოს ციკლი მანამ,
//  სანამ მომხმარებელი არ გამოიცნობს სწორ რიცხვს.
let randomNumber = Math.floor(Math.random() * 50) + 1;
let guess;
while (guess !== randomNumber) {
    guess = parseInt(prompt("Guess the number between 1 and 50:"));
    if (guess < randomNumber) {
        alert("Your guess is too low!");
    } else if (guess > randomNumber) {
        alert("Your guess is too high!");
    } else {
        alert("Congratulations! You've guessed the correct number!");
    }
}
