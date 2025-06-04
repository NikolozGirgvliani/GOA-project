function Movie(name, genre, year, imdb) {
    this.name = name;
    this.genre = genre;
    this.year = year;
    this.imdb = imdb;

    this.review = function() {
        console.log(`This movie named ${this.name} is entertaining and enjoyable, genre is ${this.genre}, it was released in ${this.year}, rating is ${this.imdb}`);
    };
}

const Movie1 = new Movie('Spider-Man: No Way Home', 'Science-Fiction', 2018, 4.7);
Movie1.review();
