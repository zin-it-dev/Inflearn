const chartInstances = {}


document.addEventListener("DOMContentLoaded", function () {
    createChart("newUsersChart", "/charts/new-users", "line");
    createChart("userActivityChart", "/charts/user-activity", "line")
});


async function createChart(chartId, endpoint, chartType) {
    try {
        const res = await fetch(endpoint);
        if (!res.ok) throw new Error(`Error API: ${res.status}`);

        const data = await res.json()
        const ctx = document.getElementById(chartId).getContext("2d");

        if (chartInstances[chartId]) {
            chartInstances[chartId].destroy();
        }

        chartInstances[chartId] = new Chart(ctx, {
            type: chartType,
            data: {
                labels: data.data.labels,
                datasets: [{
                    label: data.data.datasets[0].label,
                    data: data.data.datasets[0].data,
                    backgroundColor: data.data.datasets[0].backgroundColor,
                    borderColor: data.data.datasets[0].borderColor,
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: data.title
                    }
                }
            }
        });
    } catch (error) {
        console.error(`Error loading data for ${chartId}:`, error);
    }
}