const SALES_TAX_RATE = 0.07;

var mealAmt = prompt('Enter cost of meal');
var tipPct = prompt('Enter the tip percentage "0.xx"');
mealAmt = parseFloat(mealAmt)
tipPct = parseFloat(tipPct)
var tipAmt = mealAmt * tipPct;
var salesTaxAmt = mealAmt * SALES_TAX_RATE;
var mealTotal = mealAmt + tipAmt + salesTaxAmt;

alert('The correct amount to tip is $' + tipAmt.toFixed(2));
alert('The sales tax at a rate of 7% is $' + salesTaxAmt.toFixed(2));
alert('The total cost with tip and tax is $' + mealTotal.toFixed(2));

document.write("For a meal that costs $" + mealAmt.toFixed(2) + ', with a ' + parseInt(tipPct * 100) + '% tip, the correct amount to tip is $' + tipAmt.toFixed(2));
document.write("<br>");
document.write("and the total bill with an added sales tax of " + salesTaxAmt.toFixed(2) + "% is <b> $" + mealTotal.toFixed(2)) + '</b>';