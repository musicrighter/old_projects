//define global function
function fullName(){
	//define local variable
    var firstName = "Hugo";

    //define local function
    function alertFullName() {
        var lastName = "Reyes";
        //reference to firstName is OK here
        //firstName is defined in containing scope
        alert("Full name: " + firstName + " " + lastName);
    }
    
    //call local function
    alertFullName();
}

//call global function
fullName();

//reference to firstName is !OK here
//not defined in current scope
alert(firstName);