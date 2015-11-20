function GenerateNumber(){
       var minVal = parseFloat(document.getElementById('minBox').value);
       var maxVal = parseFloat(document.getElementById('maxBox').value);
       var number = Math.floor(Math.random() *  (maxVal - minVal + 1)) + minVal;
       document.getElementById('outputDiv').innerHTML =
       'Your lucky number is ' + number;
     }

var button1 = document.getElementsByTagName('input')[2];

button1.onclick = GenerateNumber;
