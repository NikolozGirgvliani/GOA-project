// 1. ახსნა კომენტარებით
// ობიექტი – მონაცემთა ერთეული კუთვნილებებითა და მეთოდებით
// კუთვნილება – ობიექტის მახასიათებელი (მაგ: name, age)
// მეთოდი – ობიექტში არსებული ფუნქციაა

    // 2. ობიექტების შექმნა
    const me = {
      name: "Nikoloz",
      surname: "Girgvliani",
      age: 15
    };

    const father = {
      name: "Manuchar",
      surname: "Girgvliani",
      age: 45
    };

    
    console.log("Me:", me);
    console.log("Father:", father);

    // 2. თითოეული კუთვნილება
    console.log("My Name:", me.name);
    console.log("My Surname:", me.surname);
    console.log("My Age:", me.age);

    console.log("Father's Name:", father.name);
    console.log("Father's Surname:", father.surname);
    console.log("Father's Age:", father.age);

    // 3. კუთვნილებების შეცვლა
    me.age = 26;
    father.surname = "Beridze";

    console.log("Updated Me:", me);
    console.log("Updated Father:", father);

    // 4. ახალი კუთვნილებების დამატება
    me.hobby = "Football";
    father.profession = "Policeman";

    console.log("Me with new property:", me);
    console.log("Father with new property:", father);

    // 5. კუთვნილებების წაშლა
    delete me.hobby;
    delete father.age;

    console.log("Me after deleting hobby:", me);
    console.log("Father after deleting age:", father);

    // 3. Prompt-ით ობიექტის შექმნა
    const name = prompt("შეიყვანეთ თქვენი სახელი:");
    const surname = prompt("შეიყვანეთ თქვენი გვარი:");
    const age = prompt("შეიყვანეთ თქვენი ასაკი:");

    const user = {
      name: name,
      surname: surname,
      age: age
    };

    console.log("User object:", user);

    user.name = "გიორგი";

    console.log("Updated User object:", user);

    // 4. რატომ შეიცვალა me ობიექტი?
    const me2 = {
      name: "Nika",
      age: 20
    };

    const you = me2;
    you.age = 15;

    console.log("me2.age =", me2.age);
