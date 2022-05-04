

    var data = [
  {
    x: ['Bronx', 'Queens', 'Brooklyn','Staten Island','Manhattan'],
    y: [93, 7, 900, 3, 6],
    type: 'bar'
  }
];
    function barGraph() {
   
Plotly.newPlot('myDiv', data);
}
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            var mapParams = getMapParams(this.response);
            Plotly.plot('graph', mapParams.data, mapParams.layout);
        }
    };
    xhttp.open("GET","/tickets");
    xhttp.send();