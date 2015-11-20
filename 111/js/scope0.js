//define a function with a local variable
function hi() {
    var hello = "hello"
};

//call the function
hi();

//error-- no access to local variable outside the function
alert(hello);