const renderChart = (data, endMonth, endDay, endYear) => {
  document.getElementById("chart-container").innerHTML = "&nbsp;";
  document.getElementById("chart-container").innerHTML =
    '<canvas id="line-chart"></canvas>';

  const vals = JSON.parse(data.text);

  var xyValues = [];

  const start = new Date("01/01/2020");
  //const end = new Date(endMonth + "/" + endDay + "/" + endYear);
  let loop = new Date(start);

  for (var i = 0; i < vals.Results.output1.length; i = i + 1) {
    var month = loop.getMonth() + 1;
    var day = loop.getDate();
    month = month < 10 ? "0" + month : month;
    day = day < 10 ? "0" + day : day;

    xyValues.push({
      x: month + "/" + day + "/" + loop.getFullYear(),
      y: vals.Results.output1[i].column,
    });
    let newDate = loop.setDate(loop.getDate() + 1);
    loop = new Date(newDate);
  }
  new Chart(document.getElementById("line-chart"), {
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
