const testButtonClicked = () => {
  console.log("?");
  var request = new XMLHttpRequest();
  request.open("POST", "/api/connect", true);
  request.send();
};
