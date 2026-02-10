const API_URL = "http://127.0.0.1:5000/live";

// UI elements
const signalBox = document.getElementById("signalBox");
const imbalanceEl = document.getElementById("imbalance");
const lag1El = document.getElementById("lag1");
const avg5El = document.getElementById("avg5");
const changeEl = document.getElementById("change");
const lastUpdateEl = document.getElementById("lastUpdate");

const statusText = document.getElementById("statusText");
const dot = document.getElementById("dot");

const historyTable = document.getElementById("historyTable");

// imbalance graph store
let imbalanceData = [];
let imbalanceLabels = [];

// Chart.js setup
const ctx = document.getElementById("imbalanceChart").getContext("2d");

const imbalanceChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: imbalanceLabels,
    datasets: [{
      label: "Imbalance",
      data: imbalanceData,
      borderWidth: 2,
      tension: 0.3
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        labels: {
          color: "white"
        }
      }
    },
    scales: {
      x: {
        ticks: { color: "white" }
      },
      y: {
        ticks: { color: "white" }
      }
    }
  }
});

// TradingView chart init
function initTradingView() {
  new TradingView.widget({
    container_id: "tv_chart_container",
    autosize: true,
    symbol: "BINANCE:BTCUSDT",
    interval: "1",
    timezone: "Asia/Kolkata",
    theme: "dark",
    style: "1",
    locale: "en",
    toolbar_bg: "#0b1025",
    enable_publishing: false,
    allow_symbol_change: false,
    hide_side_toolbar: true,
    withdateranges: true
  });
}

initTradingView();

// Update UI
async function fetchPrediction() {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();

    statusText.innerText = "Connected";
    dot.style.background = "#22c55e";

    if (!data.features || Object.keys(data.features).length === 0) {
      signalBox.innerText = "WAITING";
      signalBox.className = "signal neutral";
      return;
    }

    const signal = data.signal;

    // Update signal box
    signalBox.innerText = signal;

    if (signal === "UP") {
      signalBox.className = "signal up";
    } else {
      signalBox.className = "signal down";
    }

    // Update features
    imbalanceEl.innerText = data.features.imbalance.toFixed(6);
    lag1El.innerText = data.features.imbalance_lag1.toFixed(6);
    avg5El.innerText = data.features.imbalance_avg_5.toFixed(6);
    changeEl.innerText = data.features.imbalance_change.toFixed(6);

    // Update last update time
    lastUpdateEl.innerText = data.time;

    // Update imbalance chart
    const timeLabel = new Date().toLocaleTimeString();

    imbalanceLabels.push(timeLabel);
    imbalanceData.push(data.features.imbalance);

    if (imbalanceLabels.length > 20) {
      imbalanceLabels.shift();
      imbalanceData.shift();
    }

    imbalanceChart.update();

    // Update history table
    const row = `
      <tr>
        <td>${new Date().toLocaleTimeString()}</td>
        <td style="font-weight:900;">${signal}</td>
        <td>${data.features.imbalance.toFixed(6)}</td>
      </tr>
    `;

    if (historyTable.innerText.includes("Waiting")) {
      historyTable.innerHTML = row;
    } else {
      historyTable.innerHTML = row + historyTable.innerHTML;
    }

    // Keep only 15 rows
    const rows = historyTable.querySelectorAll("tr");
    if (rows.length > 15) {
      rows[rows.length - 1].remove();
    }

  } catch (err) {
    statusText.innerText = "Disconnected";
    dot.style.background = "red";

    signalBox.innerText = "NO API";
    signalBox.className = "signal neutral";
  }
}

// Refresh every 3 seconds
setInterval(fetchPrediction, 60000);
fetchPrediction();
