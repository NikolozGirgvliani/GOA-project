// 1. შექმენი პროგრამა, რომელიც დაბეჭდავს რიცხვებს 1-დან 10-მდე while loop-ის გამოყენებით, თუმცა თითოეული რიცხვი უნდა იყოს დაბეჭდილი ახალ ხაზზე console.log()-ის გამოყენებით.
console.log("Numbers From 1 to 10:");
let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

// 2. შექმენი პროგრამა, რომელიც ბეჭდავს ყველა კენტ რიცხვს 1-დან 20-მდე while loop-ის გამოყენებით.
console.log(" Odd Numbers From 1 to 10:");
i = 1;
while (i <= 20) {
    if (i % 2 !== 0) {
        console.log(i);
    }
    i++;
}

// 3. შექმენი პროგრამა, რომელიც იყენებს while loop-ს 1-დან 20-მდე ყველა რიცხვის ჯამის გამოსათვლელად და შედეგი კონსოლში გამოაქვს.
console.log("1 to 10 numbers sum:");
i = 1;
let sum = 0;
while (i <= 20) {
    sum += i;
    i++;
}
console.log("sum:", sum);

// 4. შექმენი პროგრამა, რომელიც დაბეჭდავს ციფრებს 5-დან 25-მდე 5-იანი გამოტოვებით, while loop-ის გამოყენებით.
console.log("numbers from 5 to 25 skipping 5:");
i = 5;
while (i <= 25) {
    console.log(i);
    i += 5;
}

// 5. შექმენი პროგრამა, რომელიც დაბეჭდავს 7-ს კონსოლში, while loop-ის გამოყენებით, მხოლოდ ერთხელ უნდა გაეშვას ციკლი.

console.log("print 7 one time:");
i = 0;
while (i < 1) {
    console.log(7);
    i++;
}
