function ButtonAdd() {
      const newButton = document.createElement("button");
      newButton.textContent = "Button created by javascript";

      const container = document.getElementById("button1");
      container.appendChild(newButton);
    }



    