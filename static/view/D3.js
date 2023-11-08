document.addEventListener("DOMContentLoaded", function () {
  let dataType = "price_usd";
  let currency = "bitcoin";
  let data = null;
  let rawData = null;
  let range = [0, 0];

  const dataTypeCaptions = {
    price_usd: "US Dollar",
    market_cap: "Market capitalization",
    "24h_vol": "Trading Volume",
  };

  const margin = { left: 80, right: 100, top: 50, bottom: 100 };
  const totalHeight = 500;
  const totalWidth = 800;
  const height = totalHeight - margin.top - margin.bottom;
  const width = totalWidth - margin.left - margin.right;

  const svg = d3
    .create("svg")
    .attr("width", totalWidth)
    .attr("height", totalHeight);

  document.getElementById("chart-area").appendChild(svg.node());

  const g = svg
    .append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // Time parser for x-scale
  const parseTime = d3.timeParse("%Y-%m-%d");

  // For tooltip
  const bisectDate = d3.bisector((d) => d.year).left;

  // Scales
  const x = d3.scaleTime().range([0, width]);
  const y = d3.scaleLinear().range([height, 0]);

  const formatSi = d3.format(".2s");
  function formatAbbreviation(x) {
    const s = formatSi(x);
    switch (s[s.length - 1]) {
      case "G":
        return s.slice(0, -1) + "B";
      case "k":
        return s.slice(0, -1) + "K";
      default:
        return s;
    }
  }

  // Axis generators
  const xAxisCall = d3.axisBottom(x).ticks(4);
  const yAxisCall = d3
    .axisLeft(y)
    .ticks(6)
    .tickFormat((d) => formatAbbreviation(d));

  // Axis groups
  const xAxis = g
    .append("g")
    .attr("class", "x axis")
    .attr("transform", `translate(0,${height})`);

  const yAxis = g.append("g").attr("class", "y axis");

  // Y-Axis label
  const yLabel = yAxis
    .append("text")
    .attr("class", "axis-title")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .attr("text-anchor", "end")
    .attr("fill", "#5D6971");

  // Line path generator
  const line = d3
    .line()
    .x((d) => x(d.year))
    .y((d) => y(d.value));

  const dataUrl =
    "https://raw.githubusercontent.com/adamjanes/udemy-d3/master/06/6.10.1/data/coins.json";

  const graphLine = g
    .append("path")
    .attr("class", "line")
    .attr("fill", "none")
    .attr("stroke", "grey")
    .attr("stroke-width", "3px");

  document
    .getElementById("coin-select")
    .addEventListener("change", function () {
      currency = this.value;
      update();
    });

  document.getElementById("var-select").addEventListener("change", function () {
    dataType = this.value;
    update();
  });

  const $dateLabel1 = document.getElementById("dateLabel1");
  const $dateLabel2 = document.getElementById("dateLabel2");

  const getSelectedData = () => rawData[currency];

  const update = () => {
    const allSelectedData = getSelectedData();
    data = allSelectedData
      .filter((d, i) => i >= range[0] && i <= range[1])
      .map((d) => ({
        year: parseTime(d.date),
        value: +d[dataType],
      }));

    $dateLabel1.textContent = allSelectedData[range[0]].date;
    $dateLabel2.textContent = allSelectedData[range[1]].date;

    // Set scale domains
    x.domain(d3.extent(data, (d) => d.year));
    y.domain([
      d3.min(data, (d) => d.value) / 1.005,
      d3.max(data, (d) => d.value) * 1.005,
    ]);

    // Generate axes once scales have been set
    xAxis.transition().call(xAxisCall);
    yAxis.transition().call(yAxisCall);

    yLabel.text(dataTypeCaptions[dataType]);

    graphLine
      .transition()
      .ease(d3.easeLinear)
      .duration(100)
      .attr("d", line(data));
  };

  function mousemove(event) {
    const x0 = x.invert(d3.pointer(event)[0]);
    const i = bisectDate(data, x0, 1);
    const d0 = data[i - 1];
    const d1 = data[i];
    const d = x0 - d0.year > d1.year - x0 ? d1 : d0;
    focus.attr("transform", `translate(${x(d.year)},${y(d.value)})`);
    focus.select("text").text(d.value);
    focus.select(".x-hover-line").attr("y2", height - y(d.value));
    focus.select(".y-hover-line").attr("x2", -x(d.year));
  }

  /******************************** Tooltip Code ********************************/
  const focus = g.append("g").attr("class", "focus").style("display", "none");

  const xHoverLine = focus
    .append("line")
    .attr("class", "x-hover-line hover-line")
    .attr("y1", 0)
    .attr("y2", height);

  const yHoverLine = focus
    .append("line")
    .attr("class", "y-hover-line hover-line")
    .attr("x1", 0)
    .attr("x2", width);

  const circle = focus.append("circle").attr("r", 7.5);

  const text = focus.append("text").attr("x", 15).attr("dy", ".31em");

  const overlay = svg
    .append("rect")
    .attr("class", "overlay")
    .attr("width", width)
    .attr("height", height);

  overlay.on("mouseover", function () {
    focus.style("display", null);
  });

  overlay.on("mouseout", function () {
    focus.style("display", "none");
  });

  overlay.on("mousemove", mousemove);

  /******************************** Tooltip Code ********************************/

  d3.json(dataUrl)
    .then(function (response) {
      rawData = response;
      const data = getSelectedData();
      range = [0, data.length - 1];
      update();
    })
    .catch(function (error) {
      console.error("Error loading data: " + error.message);
    });
});
