// Load customer data
fetch('/get-data')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector("#customerTable tbody");
        tableBody.innerHTML = data.map(row => `
            <tr>
                <td>${row.CustomerID}</td>
                <td>${row.Recency}</td>
                <td>${row.Frequency}</td>
                <td>${row.Revenue}</td>
                <td>${row.Segment}</td>
            </tr>
        `).join('');
    });

// Load stats for the chart
fetch('/get-stats')
    .then(response => response.json())
    .then(stats => {
        const data = [{
            x: Object.keys(stats.Recency),
            y: Object.values(stats.Recency),
            type: 'bar',
            name: 'Recency'
        }, {
            x: Object.keys(stats.Frequency),
            y: Object.values(stats.Frequency),
            type: 'bar',
            name: 'Frequency'
        }, {
            x: Object.keys(stats.Revenue),
            y: Object.values(stats.Revenue),
            type: 'bar',
            name: 'Revenue'
        }];
        
        Plotly.newPlot('chart', data);
    });
