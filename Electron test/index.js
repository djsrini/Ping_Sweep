var input1 = document.getElementById('input1');
var input2 = document.getElementById('input2');
var btn = document.getElementById('btn');
var ul = document.getElementById("list");


strike();
getInput();
removeInput();

function getInput() {
    btn.addEventListener('click', function () {
        var li = document.createElement("li");
        li.innerHTML = "<li class='lis'><span class='sp'>x</span> " + input1.value + " "+input2.value+ "</li>";
        var element = document.getElementById("list").appendChild(li);
        input.value = "";
    });
}


function removeInput() {
    ul.addEventListener('click', function (e) {
        if (e.target.matches("span")) {
            e.target.parentNode.remove();
        }
    });
}
function strike() {
    ul.addEventListener('click', function (e) {
        if (e.target.matches("li")) {
            e.target.style.textDecoration = "line-through";
        }
    });
}
