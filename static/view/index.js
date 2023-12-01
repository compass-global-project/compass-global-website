// initializeDatePicker = () => {
//   var daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
//     today = new Date(),
//     targetDate = new Date(today.getFullYear(), 1, 1);

//   setDate(targetDate);
//   setYears(10);

//   $("#select-month").change(function () {
//     var monthIndex = $("#select-month").val();
//     setDays(monthIndex);
//   });

//   function setDate(date) {
//     setDays(date.getMonth());
//     $("#select-day").val(date.getDate());
//     $("#select-month").val(date.getMonth());
//     $("#select-year").val(date.getFullYear());
//   }

//   function setDays(monthIndex) {
//     var optionCount = $("#select-day option").length,
//       daysCount = daysInMonth[monthIndex];

//     if (optionCount < daysCount) {
//       for (var i = optionCount; i < daysCount; i++) {
//         $("#select-day").append(
//           $("<option></option>")
//             .attr("value", i + 1)
//             .text(i + 1)
//         );
//       }
//     } else {
//       for (var i = daysCount; i < optionCount; i++) {
//         var optionItem = "#select-day option[value=" + (i + 1) + "]";
//         $(optionItem).remove();
//       }
//     }
//   }

//   function setYears(val) {
//     var startYear = 2020;
//     var endYear = 2030;
//     for (var i = startYear; i <= endYear; i++) {
//       $("#select-year").append($("<option></option>").attr("value", i).text(i));
//     }
//   }

// };

function toggleSwitchOff(){
  toggle_display(false);
}

function toggleSwitchOn(){
  toggle_display(true);
}

toggle_display = (show_chart) => {
    if(!show_chart){
        document.getElementById('chart-container').style.display = "none";
        document.getElementById('heatmap').style.display = 'block';
    }
    else {
        document.getElementById('chart-container').style.display = 'block';
        document.getElementById('heatmap').style.display = "none";
    }

}

initializeSlider = () => {
  const slider = document.getElementById('dateSlider');
  const dateDisplay = document.getElementById('dateLabel');

  const startDate = new Date("2020-01-02");
  const endDate = new Date("2030-12-31");
  const timeDifference = endDate - startDate;

  // Convert dates to UNIX timestamps in seconds
  slider.min = startDate.getTime() / 1000;
  slider.max = endDate.getTime() / 1000;
  slider.value = new Date("2023-01-01").getTime() / 1000;
  slider.step = 86400; // One day in seconds

    slider.oninput = function() {
        const selectedDate = new Date(this.value * 1000);
        const formattedDate = selectedDate.toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'long',
          day: 'numeric'
        });
        dateDisplay.textContent = formattedDate;
    };

  slider.onclick = testButtonClicked;
  const initialDate = new Date(slider.value * 1000);
  const formattedInitialDate = initialDate.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
  dateDisplay.textContent = formattedInitialDate;
};

body = () => {
  const style = document.createElement("link");
  style.href = "static/styles.css";

  const titleDiv = document.getElementById("titleDiv");
  const subTitleDiv = document.getElementById("subTitleDiv");
  const label = document.createElement("h1");
  const subLabel = document.createElement("a");


  subLabel.id = "subLabelId"; 
  subLabel.href = "https://www.compassinstitution.com/";
  label.textContent = "A Prediction of Rice Prices in India";
  subLabel.textContent = "COMPASS INSTITUTION AT UC SAN DIEGO"
  subLabel.style.textDecoration = "none";
  titleDiv.append(label);
  subTitleDiv.append(subLabel);

  //initializeDatePicker();
  initializeSlider();
  toggle_display(false);
};

window.onload = () => {
  body();
  testButtonClicked();
};
