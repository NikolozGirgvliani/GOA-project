function Person(name, lastname, age) {
    this.name = name;
    this.lastname = lastname;
    this.age = age;
}

function Person12() {
    const person1 = new Person("Nikoloz", "Girgvliani", 15);
    console.log(person1);
}