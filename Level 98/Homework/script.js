
    function Car(brand, model, year) {
      this.brand = brand;
      this.model = model;
      this.year = year;

      this.getDescription = function () {
        return `${this.year} ${this.brand} ${this.model}`;
      };

      this.age = function () {
        const currentYear = new Date().getFullYear();
        return currentYear - this.year;
      };
    }

    function Rectangle(width, height) {
      this.width = width;
      this.height = height;

      this.getArea = function () {
        return this.width * this.height;
      };

      this.getPerimeter = function () {
        return 2 * (this.width + this.height);
      };
    }

    function showCar() {
      const car1 = new Car("Toyota", "Corolla", 2015);
      const car2 = new Car("BMW", "X5", 2018);
      const car3 = new Car("Tesla", "Model 3", 2021);

      const output = `
        <p>${car1.getDescription()} — age: ${car1.age()} year</p>
        <p>${car2.getDescription()} — age: ${car2.age()} year</p>
        <p>${car3.getDescription()} — age: ${car3.age()} year</p>
      `;

      document.getElementById("car-output").innerHTML = output;
    }
