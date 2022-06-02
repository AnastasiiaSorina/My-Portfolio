
<<<<<<< Updated upstream
var operationButtons = document.getElementsByClassName("operation-button");
var input1 = document.getElementById("number1");
var input2 = document.getElementById("number2");

function makeOperation(operationeCode) {
    var number1 = Number(input1.value);
    var number2 = Number(input2.value);

    if (operationeCode === "+") {
        var result = number1 + number2;
    } else if (operationeCode === "-") {
        var result = number1 - number2;
    } else if (operationeCode === "*") {
        var result = number1 * number2;
    } else if (operationeCode === "/") {
        var result = number1 / number2;
    } else {
        window.alert("operation is onknow");
    }
    window.alert(result);
}
function onOperationButtonClick(eventObject) {
    var clicedElement = eventObject.currentTarget;
    var operation = clicedElement.innerHTML;
    makeOperation(operation);
}
for (var i = 0; i < operationButtons.length; i++) {
    var button = operationButtons[i];
    button.addEventListener('click', onOperationButtonClick);

=======
var input1 = document.getElementById("number1");
var input2 = document.getElementById("number2");

function makeOperation(operationeCode){
    var number1 = Number(input1.value);
    var number2 = Number(input2.value);

    if (operationeCode === "+"){
        var result = number1 + number2;
    } else if (operationeCode === "-") {
        var result = number1 - number2;
    } else if (operationeCode === "*") {
        var result = number1 * number2;
    } else if (operationeCode === "/") {
        var result = number1 / number2;
    } else {
        window.alert("operation is onknow");
    }
    window.alert(result);
    }
    function onOperationButtonClick(eventObject) {
        var clicedElement = eventObject.currentTarget;
        var operation = clicedElement.innerHTML;
        makeOperation(operation);
    }

var operationsButtons = [buttonPlus, buttonMinus, buttonMultiply, buttonDevide];
for (var i = 0; i < operationsButtons.length; i++) {
    var buttons = operationsButtons[i];
    buttons.addEventListener('click', onOperationButtonClick);
>>>>>>> Stashed changes
}