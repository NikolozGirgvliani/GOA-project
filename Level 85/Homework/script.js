let count = 0;
const value = document.getElementById('value');

function increase() {
  count += 1;
  value.textContent = count;
}

function decrease() {
  count -= 1;
  value.textContent = count;
}

function reset() {
  count = 0;
  value.textContent = count;
}
