const paragraph = document.createElement("p");
    const text = document.createTextNode("This is added by JavaScript");
    paragraph.appendChild(text);
    document.body.appendChild(paragraph);

    const h2 = document.createElement("h2");
    h2.innerText = "Welcome!";
    const welcomeDiv = document.getElementById("welcome-container");
    welcomeDiv.appendChild(h2);

    const blueDiv = document.createElement("div");
    blueDiv.style.backgroundColor = "blue";
    blueDiv.style.color = "white";
    blueDiv.style.padding = "10px";
    blueDiv.innerText = "This is a blue box";
    document.body.appendChild(blueDiv);


    const button = document.createElement("button");
    button.innerText = "Click Me";
    const buttonContainer = document.getElementById("button-container");
    buttonContainer.appendChild(button);


    const span = document.createElement("span");
    span.innerText = " Important!";
    span.style.color = "red";

    const paragraph2 = document.createElement("p");
    paragraph2.innerText = "Notice:";
    paragraph2.appendChild(span);
    document.body.appendChild(paragraph2);