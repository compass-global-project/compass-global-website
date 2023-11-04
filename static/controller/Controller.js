const testButtonClicked = () => {
  $.ajax({
    url: "/api/connect",
    type: "POST",
    contentType: "application/json;charset=utf-8",
    dataType: "json",
    success: function (response) {
      console.log("?");
      if (response.success) {
        var responseText = document.getElementById("responseText");
        console.log("Success");
        console.log(response);
        responseText.innerText = response.text;
        responseText.style.display = "block";
      } else {
        console.log("Failed to get text: " + response.message);
      }
    },
    error: function (error) {
      console.log("/");
      console.log(error);
    },
  });
};
