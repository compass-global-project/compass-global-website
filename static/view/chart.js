const renderChart = (data) => {
  const vals = JSON.parse(data.text);

  var xyValues = [];

  for (var i = 0; i < vals.Results.output1.length; i = i + 2) {
    xyValues.push({
      x: vals.Results.output1[i].column,
      y: vals.Results.output1[i + 1].column,
    });
  }

  new Chart(document.getElementById("lineChart"), {
    type: "line",
    data: {
      labels: xyValues.map((row) => row.x),
      datasets: [
        {
          pointBackgroundColor: "rgba(0,0,255,1)",
          label: "Price of Rice",
          data: xyValues.map((row) => row.y),
          borderColor: "rgb(75, 192, 192)",
        },
      ],
    },
  });
};
