const testButtonClicked = () => {
  const day = document.getElementById("select-day").value;
  const month = document.getElementById("select-month").value;
  const year = document.getElementById("select-year").value;

  const date = `${year}-${month}-${day}`;
  console.log(date);

  const startDate = "2020-01-01";
  const endDate = `${year}-${month}-${day}`;

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
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};
