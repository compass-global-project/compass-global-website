body = () => {
  const style = document.createElement("link");
  style.href = "static/styles.css";

  const main = document.getElementById("main");
  const centerContainer = document.createElement("div");
  const label = document.createElement("h1");

  label.textContent = "Food Insecurity Model";

  const testButton = document.createElement("button");
  testButton.onclick = testButtonClicked();
  testButton.textContent("Click");

  centerContainer.append(label, testButton);
  main.append(centerContainer);
};

window.onload = () => {
  body();
};
