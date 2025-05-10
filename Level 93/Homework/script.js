// 1. book ობიექტი და კონსოლში მისი თვისებების დაბეჭდვა
const book = {
    name: "Hitler Biography",
    author: "Unknown",
    pages: Unknown,
    genre: "Fiction",
    isAvailable: true
};

console.log("Book Name:", book.name);
console.log("Author:", book.author);
console.log("Pages:", book.pages);
console.log("Genre:", book.genre);
console.log("Is Available:", book.isAvailable);

// 2. student ობიექტი და if-else-ით შემოწმება
const student = {
    name: "nika",
    grade: "9",
    passed: true,
    year: 2025
};

if (student.passed) {
    console.log("Student passed the grade");
} else {
    console.log("Student failed the grade");
}

// 3. movie ობიექტი და წინადადების დაბეჭდვა
const movie = {
    title: "Interstellar",
    rating: "PG-13",
    duration: "169 minutes",
    yearReleased: 2014,
    isAnimated: false
};

console.log(`The movie ${movie.title} is rated ${movie.rating} and was released in ${movie.yearReleased}.`);

// 4. phone ობიექტი და 5G მხარდაჭერის შემოწმება
const phone = {
    brand: "IOS",
    model: "Iphone 12 Pro",
    storage: "128GB",
    batteryLife: "24h",
    is5G: true
};

if (phone.is5G) {
    console.log("Supports 5G");
} else {
    console.log("Doesn't support 5G");
}

// 5. game ობიექტი და მოთამაშეების რაოდენობის შემოწმება
const game = {
    name: "Ea Fc 25",
    players: 2,
    online: true,
    releaseYear: 2025,
    genre: "Sports"
};

if (game.players > 1) {
    console.log("Multiplayer game");
} else {
    console.log("Single player game");
}
