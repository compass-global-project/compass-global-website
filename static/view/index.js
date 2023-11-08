initializeDatePicker = () => {
  var daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    today = new Date(),
    targetDate = new Date(today.getFullYear(), 1, 1);

  setDate(targetDate);
  setYears(10);

  $("#select-month").change(function () {
    var monthIndex = $("#select-month").val();
    setDays(monthIndex);
  });

  function setDate(date) {
    setDays(date.getMonth());
    $("#select-day").val(date.getDate());
    $("#select-month").val(date.getMonth());
    $("#select-year").val(date.getFullYear());
  }

  function setDays(monthIndex) {
    var optionCount = $("#select-day option").length,
      daysCount = daysInMonth[monthIndex];

    if (optionCount < daysCount) {
      for (var i = optionCount; i < daysCount; i++) {
        $("#select-day").append(
          $("<option></option>")
            .attr("value", i + 1)
            .text(i + 1)
        );
      }
    } else {
      for (var i = daysCount; i < optionCount; i++) {
        var optionItem = "#select-day option[value=" + (i + 1) + "]";
        $(optionItem).remove();
      }
    }
  }

  function setYears(val) {
    var startYear = 2020;
    var endYear = 2030;
    for (var i = startYear; i <= endYear; i++) {
      $("#select-year").append($("<option></option>").attr("value", i).text(i));
    }
  }
};

body = () => {
  const style = document.createElement("link");
  style.href = "static/styles.css";

  const titleDiv = document.getElementById("titleDiv");
  const label = document.createElement("h1");
  label.textContent = "Food Insecurity Model";
  titleDiv.append(label);

  const buttonDiv = document.getElementById("buttonDiv");
  const testButton = document.createElement("button");
  testButton.onclick = testButtonClicked;
  testButton.textContent = "Send Request";
  buttonDiv.append(testButton);

  initializeDatePicker();
};

window.onload = () => {
  body();
};
