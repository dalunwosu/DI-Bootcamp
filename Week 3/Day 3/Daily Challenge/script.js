const inputText = document.getElementById("inputText");
inputText.addEventListener("input", function (event) {
  const value = event.target.value;
  const onlyLetters = value.replace(/[^a-zA-Z]/g, "");
  if (onlyLetters !== value) {
    event.target.value = onlyLetters;
  }
});
