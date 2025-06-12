let button = document.getElementById("button1");

    function printRemove() {
        console.log(5);
        button.removeEventListener("click", printRemove);
    }

    button.addEventListener("click", printRemove);



    