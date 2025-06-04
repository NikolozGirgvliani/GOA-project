function addText() {
    const parent = document.getElementById('Parent');

    const para = document.createElement('p');
    para.textContent = 'new text in paragraph';

    const Button = document.createElement('button');
    Button.textContent = 'new button in paragraph';

    parent.appendChild(para);
    parent.appendChild(Button);
}
