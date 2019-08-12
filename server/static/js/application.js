$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    var MAX_POINTS = 20;
    var MAX_DATA = 1;
    var measuredTemps = [];
    var theoryTemps = [];

    var units = {
        "time_stamp": "",
        "elapsed_time": "",
        "elapsed_time_formatted": "",
        "theory_tempC": "°C",
        "theory_remaining_time": "",
        "tempC_probe": "°C",
        "tempF_probe": "°F",
        "tempC_amb": "°C",
        "tempF_amb": "°F",
        "humidity": "%"
      };

    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: [],
            datasets: [{
                label: 'Measured Temp °C',
                backgroundColor: 'rgba(9, 132, 227,0.22)',
                borderColor: 'rgba(9, 132, 227,0.90)',
                borderWidth: 1,
                data: []
            },{
                label: 'Theory Temp °C',
                backgroundColor: 'rgba(85, 239, 196,0.22)',
                borderColor: 'rgba(85, 239, 196,0.9)',
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
                display: true
            },
            scales: {
                xAxes: [{
                    gridLines: {
                        display:false
                    },
                    ticks: {
                      fontColor: "#ecf0f1",
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display:false
                    },
                    ticks: {
                      fontColor: "#ecf0f1",
                    }
                }]
            }
        }
    });

    var numPoints = 0;

    //receive details from server
    socket.on('data', function(data) {
        console.log("Received data: " + data);
        numPoints++;
        
        if (measuredTemps.length >= MAX_DATA){
            measuredTemps.shift()
        }
        measuredTemps.push(data.tempC_probe);

        if (theoryTemps.length >= MAX_DATA){
            theoryTemps.shift()
        }
        theoryTemps.push(data.theory_tempC);
        
        //populate data section
        numbers_string = '';
        for (var key in data) {
            if (data.hasOwnProperty(key)) {
                for (var i = measuredTemps.length - 1; i >= 0; i--){
                    if(key.toUpperCase() == "ELAPSED_TIME"){
                        continue;
                    }
                    var dataHeader = '<h4>' + key.toUpperCase() +  '</h4>'
                    var dataBody = '<p>' + data[key].toString() + units[key] + '</p>'
                    numbers_string = numbers_string + dataHeader + dataBody;
                }
            }
        }

        //add the data to number stream
        $('#data').html(numbers_string);

        //add the data to chart
        addData(chart, numPoints, measuredTemps[measuredTemps.length - 1], theoryTemps[theoryTemps.length - 1]);
        if(numPoints > MAX_POINTS){
            removeData(chart);
        }
    });

    socket.on('connect', function(socket){
        console.log("I'm connected");
        $('#connectButton').html("CONNECTED");
        $('#connectButton').addClass('connected').removeClass('disconnected');
    });

    socket.on('disconnect', function () {
        console.log("I'm disconnected");
        $('#connectButton').html("DISCONNECTED");
        $('#connectButton').addClass('disconnected').removeClass('connected');
    });
});

function addData(chart, label, measured, theory) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        if(dataset.label == "Measured Temp °C"){
            dataset.data.push(measured);
        }else{
            dataset.data.push(theory); 
        }
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