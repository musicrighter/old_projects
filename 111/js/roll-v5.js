function RollUntilDoubles(){
   var roll1, roll2, count;
  
   count = 0;
   document.getElementById('diceDiv').innerHTML = ""

   do {            
     roll1 = RandomInt(1, 6);       // ROLL AGAIN AND DISPLAY AT
     roll2 = RandomInt(1, 6);       // THE END OF THE PAGE DIVISION
     document.getElementById('diceDiv').innerHTML += '<img src=../images/die' + roll1 + ".gif>" + 
                                                     '<img src=../images/die' + roll2 + ".gif>" + '<br>';
     count += 1;
   }
   while (roll1 != roll2)

   document.getElementById('outputDiv').innerHTML = "<br>DOUBLES!";
   document.getElementById("counterDiv").innerHTML = '<br>Doubles in ' + count + ' rolls!';
}
   

function RandomInt(low, high){
    return Math.floor(Math.random()*(high-low+1)) + low;
}


var button1 = document.getElementById('btn1');

button1.onclick = RollUntilDoubles;