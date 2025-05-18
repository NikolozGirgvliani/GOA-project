function Person(name, surname, color) {
    this.name = name
    this.surname = surname
    this.color = color
}

const Person1 = new Person('Nikoloz', 'Girgvliani', 'White')
const Person2 = new Person('Lebron', 'James', 'Black')
const Person3 = new Person('SpongeBob', 'SquarePants', 'Yellow')

console.log(Person1, Person2, Person3)