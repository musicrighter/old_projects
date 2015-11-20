function compare(choice1, choice2){
    if (choice1 === choice2)
        return "The result is a tie!";
        
    else if (choice1 === 'rock'){
        if (choice2 === 'scissors')
            return 'You Win!';
        else 
            return 'Paper Wins!';
    }
    else if (choice1 === 'paper'){
        if (choice2 === 'rock')
            return 'You Win!';
        else 
            return 'Scissors win!';
    } 
     else if (choice1 === 'scissors'){
        if (choice2 === 'rock')
            return 'Rock Wins!';
        else 
            return 'You Win!';
    }    
}

function uChoice(){
    var radios = document.getElementsByName('userChoice')
    size = radios.length

    for (var i = 0; i < size; i++) {
        if (radios[i].checked == true) 
            return radios[i].value
    }
}
 
function cChoice(){
    var computerChoice = Math.random();

    if (computerChoice < 0.34) {
        return "rock";
    } 
    else if(computerChoice <= 0.67) {
        return "paper";
    } 
    else return "scissors";
}

var button1 = document.getElementById('btn1');
var player = 0
var opponent = 0


/*button1.onclick = function(){
    var comp = cChoice();
    var user = uChoice();
    var winner = compare(user, comp)
    if (winner === 'You Win!')
        player += 1
    else if (winner != "The result is a tie!")
        opponent += 1
    document.getElementById("outputDiv").innerHTML =
    'Your choice: <b>' + user + '</b><br>' +
    "Opponent's choice: <b>" + comp + '</b><br><br><b>' +
    winner.fontsize(5) + '</b><br><br>' +
    'Your score: <b>' + player + '</b><br>' + 
    'Opponent score: <b>' + opponent + '</b><br>';
};*/

button1.onclick = function(){
    var comp = cChoice();
    var user = uChoice();
    var winner = compare(user, comp);
    var userPic = new Image();
    var userWidth = '100'
    var compWidth = '100'
    var vs = 'Vs.'
    if (user == 'paper'){
        var userWidth = '80'
    }
    if (comp == 'paper'){
        var compWidth = '80'
    }
    userPic.src = document.getElementById(user + 'Img').src;
    var compPic = new Image();
    compPic.src = document.getElementById(comp + 'Img').src;
    if (winner === 'You Win!')
        player += 1
    else if (winner != "The result is a tie!")
        opponent += 1
    document.getElementById("outputDiv").innerHTML =
    '<img src=' + userPic.src + ' height="100" width=' + userWidth + '>' + 
    '&nbsp;&nbsp;&nbsp;&nbsp;' + vs.fontsize(12) + '&nbsp;&nbsp;&nbsp;&nbsp;' +
    '<img src=' + compPic.src + ' height="100" width=' + compWidth + '>' + '<br><br><b>' +
    winner.fontsize(5) + '</b><br><br>' +
    'Your score: <b>' + player + '</b><br>' + 
    'Opponent score: <b>' + opponent + '</b><br>';
};