// Mobile menu toggle
function toggleMobileMenu() {
  var menu = document.getElementById('mobileMenu');
  var hamburger = document.getElementById('hamburger');
  var overlay = document.getElementById('mobileOverlay');
  if (menu) {
    menu.classList.toggle('open');
    hamburger.classList.toggle('active');
    if (overlay) overlay.classList.toggle('show');
    document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : '';
  }
}

// Close mobile menu when a link is clicked
document.addEventListener('DOMContentLoaded', function() {
  var mobileMenu = document.getElementById('mobileMenu');
  if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        var menu = document.getElementById('mobileMenu');
        var hamburger = document.getElementById('hamburger');
        var overlay = document.getElementById('mobileOverlay');
        if (menu && menu.classList.contains('open')) {
          menu.classList.remove('open');
          hamburger.classList.remove('active');
          if (overlay) overlay.classList.remove('show');
          document.body.style.overflow = '';
        }
      });
    });
  }
});

// Blueprint tab switching
function switchBPTab(tab) {
  document.querySelectorAll('.bp-tab').forEach(btn => {
    btn.classList.toggle('active', btn.textContent.toLowerCase().includes(tab) || (tab === 'robotic' && btn.textContent.includes('Robotic')) || (tab === 'aeroponic' && btn.textContent.includes('Atomization')));
  });
  document.querySelectorAll('.bp-panel').forEach(panel => {
    panel.classList.toggle('active', panel.id === 'bp-' + tab);
  });
}

// Chart instances
var importChart, substitutionChart, projectionChart;

// Chart data (trilingual)
var chartLabels = {
  en: {
    years: ['2017','2018','2019','2020','2021E','2022E','2023E','2024E','2025E','2026E'],
    volume: 'Import Volume (tons)',
    value: 'Import Value ($M)',
    substitution: 'Napell Supply (tons)',
    totalImport: 'Total Import (tons)',
    revenue: 'Revenue ($M)',
    ebitda: 'EBITDA ($M)',
    yAxisVol: 'Volume (tons)',
    yAxisVal: 'Value ($M)',
  },
  zh: {
    years: ['2021','2022','2023','2024','2025E','2026E','2027E','2028E','2029E','2030E'],
    volume: '进口量（吨）',
    value: '进口额（百万美元）',
    substitution: 'Napell供应（吨）',
    totalImport: '总进口（吨）',
    revenue: '收入（百万美元）',
    ebitda: 'EBITDA（百万美元）',
    yAxisVol: '数量（吨）',
    yAxisVal: '价值（百万美元）',
  },
  ar: {
    years: ['2021','2022','2023','2024','2025E','2026E','2027E','2028E','2029E','2030E'],
    volume: 'حجم الاستيراد (طن)',
    value: 'قيمة الاستيراد (مليون $)',
    substitution: 'إمداد Napell (طن)',
    totalImport: 'إجمالي الاستيراد (طن)',
    revenue: 'الإيرادات (مليون $)',
    ebitda: 'EBITDA (مليون $)',
    yAxisVol: 'الحجم (طن)',
    yAxisVal: 'القيمة (مليون $)',
  }
};

function getChartLang() {
  return localStorage.getItem('lang') || 'en';
}

// Chart default colors
var chartColors = {
  accent: '#1d9bf0',
  green: '#22c55e',
  orange: '#f59e0b',
  purple: '#a855f7',
  red: '#ef4444',
  textSec: '#94a3b8',
  grid: 'rgba(30,41,59,0.5)',
};

function makeImportChart() {
  var canvas = document.getElementById('importChart');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var lang = getChartLang();
  var L = chartLabels[lang];
  importChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['2022','2023','2024','2025E'],
      datasets: [
        {
          label: L.volume,
          data: [155000, 172000, 188000, 205000],
          backgroundColor: chartColors.accent + '80',
          borderColor: chartColors.accent,
          borderWidth: 2,
          yAxisID: 'y',
        },
        {
          label: L.value,
          data: [280, 350, 420, 480],
          type: 'line',
          borderColor: chartColors.green,
          backgroundColor: chartColors.green + '20',
          borderWidth: 3,
          tension: 0.3,
          yAxisID: 'y1',
          pointRadius: 5,
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: chartColors.textSec, font: { size: 12 } } },
      },
      scales: {
        x: { ticks: { color: chartColors.textSec }, grid: { color: chartColors.grid } },
        y: { position: 'left', ticks: { color: chartColors.textSec }, grid: { color: chartColors.grid }, title: { display: true, text: L.yAxisVol, color: chartColors.textSec } },
        y1: { position: 'right', ticks: { color: chartColors.textSec }, grid: { drawOnChartArea: false }, title: { display: true, text: L.yAxisVal, color: chartColors.textSec } },
      }
    }
  });
}

function makeSubstitutionChart() {
  var canvas = document.getElementById('substitutionChart');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var lang = getChartLang();
  var L = chartLabels[lang];
  substitutionChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Yr 1','Yr 2','Yr 3','Yr 4','Yr 5','Yr 6','Yr 7','Yr 8','Yr 9','Yr 10'],
      datasets: [
        {
          label: L.totalImport,
          data: [190000,195000,200000,205000,210000,215000,220000,225000,232000,240000],
          backgroundColor: chartColors.textSec + '40',
          borderColor: chartColors.textSec,
          borderWidth: 1,
          yAxisID: 'y',
        },
        {
          label: L.substitution,
          data: [0,0,1200,2400,4800,8000,14000,21000,28000,36000],
          type: 'line',
          borderColor: chartColors.accent,
          backgroundColor: chartColors.accent + '20',
          borderWidth: 3,
          tension: 0.3,
          fill: true,
          yAxisID: 'y1',
          pointRadius: 4,
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: chartColors.textSec, font: { size: 12 } } },
      },
      scales: {
        x: { ticks: { color: chartColors.textSec }, grid: { color: chartColors.grid } },
        y: { position: 'left', ticks: { color: chartColors.textSec }, grid: { color: chartColors.grid } },
        y1: { position: 'right', ticks: { color: chartColors.textSec }, grid: { drawOnChartArea: false } },
      }
    }
  });
}

function makeProjectionChart() {
  var canvas = document.getElementById('projectionChart');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var lang = getChartLang();
  var L = chartLabels[lang];
  projectionChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: L.years,
      datasets: [
        {
          label: L.revenue,
          data: [0, 0, 2, 8, 25, 55, 86, 120, 165, 210],
          borderColor: chartColors.accent,
          backgroundColor: chartColors.accent + '20',
          borderWidth: 3,
          tension: 0.3,
          fill: true,
          pointRadius: 4,
        },
        {
          label: L.ebitda,
          data: [-5, -8, -3, 5, 15, 31, 45, 62, 82, 105],
          borderColor: chartColors.green,
          backgroundColor: 'transparent',
          borderWidth: 3,
          tension: 0.3,
          pointRadius: 4,
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: chartColors.textSec, font: { size: 12 } } },
      },
      scales: {
        x: { ticks: { color: chartColors.textSec }, grid: { color: chartColors.grid } },
        y: { ticks: { color: chartColors.textSec, callback: function(v) { return '$' + v + 'M'; } }, grid: { color: chartColors.grid } },
      }
    }
  });
}

// Update chart labels on language switch
function updateChartLabels(lang) {
  var L = chartLabels[lang] || chartLabels.en;
  if (importChart) {
    importChart.data.datasets[0].label = L.volume;
    importChart.data.datasets[1].label = L.value;
    importChart.options.scales.y.title.text = L.yAxisVol;
    importChart.options.scales.y1.title.text = L.yAxisVal;
    importChart.update();
  }
  if (substitutionChart) {
    substitutionChart.data.datasets[0].label = L.totalImport;
    substitutionChart.data.datasets[1].label = L.substitution;
    substitutionChart.update();
  }
  if (projectionChart) {
    projectionChart.data.labels = L.years;
    projectionChart.data.datasets[0].label = L.revenue;
    projectionChart.data.datasets[1].label = L.ebitda;
    projectionChart.update();
  }
}

// Init charts on load
document.addEventListener('DOMContentLoaded', function() {
  makeImportChart();
  makeSubstitutionChart();
  makeProjectionChart();
});
