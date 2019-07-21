$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var MAX_POINTS = 15;
    var MAX_DATA = 1;
    var numbers_received = [];

    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: [],
            datasets: [{
                label: 'Temperatures',
                backgroundColor: 'rgba(9, 132, 227,0.22)',
                borderColor: 'rgba(9, 132, 227,0.90)',
                borderWidth: 1,
                data: []
            }]
        },

        // Configuration options go here
        options: {
            responsive: true,
            title: {
                display: false
            },
            legend: {
                display: false
            },
            scales: {
                xAxes: [{
                    gridLines: {
                        display:false
                    },
                    ticks: {
                      fontColor: "rgba(9, 132, 227,0.9)",
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display:false
                    },
                    ticks: {
                      fontColor: "rgba(9, 132, 227,0.9)",
                    }
                }]
            }
        }
    });

    var numPoints = 0;

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number: " + msg.number);
        numPoints++;
        //maintain a list of ten numbers
        if (numbers_received.length >= MAX_DATA){
            numbers_received.shift()
        }
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = numbers_received.length - 1; i >= 0; i--){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }

        //add the data to number stream
        $('#data').html(numbers_string);
        //add the data to chart
        addData(chart, numPoints, numbers_received[numbers_received.length - 1])
        if(numPoints > MAX_POINTS){
            removeData(chart);
        }
    });
});

function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.shift();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
    chart.update();
}