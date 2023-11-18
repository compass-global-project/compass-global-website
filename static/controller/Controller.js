const testButtonClicked = () => {

  const startDate = "2020-01-01";

  var rawEndDate = new Date(document.getElementById('dateSlider').value * 1000);

  var year = rawEndDate.getFullYear();
  var month = rawEndDate.getMonth() + 1; // Adding 1 because getMonth() returns 0-11
  var day = rawEndDate.getDate();

  month = month < 10 ? '0' + month : month;
  day = day < 10 ? '0' + day : day;

  var endDate = `${year}-${month}-${day}`;


  const body = JSON.stringify({
    Inputs: {
      input1: [
        { Date: startDate + "T00:00:00Z" },
        {
          Date: endDate + "T00:00:00Z",
        },
      ],
    },
    GlobalParameters: {},
  });

  console.log(body);

  fetch("/send-date", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: body,
  })
    .then((response) => {
      console.log(response);
      return response.json();
    })
    .then((data) => {
      renderChart(data);
      console.log("Success:", data);
      var lineChartDiv = document.getElementById('lineChart-container');
        lineChartDiv.style.display = 'block';
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};
