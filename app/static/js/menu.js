/*<a class="waves-effect waves-light btn">button</a>
<a class="waves-effect waves-light btn"><i class="material-icons left">cloud</i>button</a>
<a class="waves-effect waves-light btn"><i class="material-icons right">cloud</i>button</a>*/

  var x=function(texto,h){
    var a=document.createElement("a");
    a.setAttribute("class","waves-effect waves-light btn collection-item");
    a.setAttribute("href","http://localhost:5000/getState/"+h);
    var i=document.createElement("i");
    i.setAttribute("class","material-icons right")
    a.innerText=texto;
    i.innerText="pageview";
    a.appendChild(i);

    return a;

  }

var xmlhttp = new XMLHttpRequest();
var url = "http://localhost:5000/getState/";
//http://localhost:5000/getState/

xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var myArr = JSON.parse(xmlhttp.responseText);
        myFunction(myArr);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();

function myFunction(arr) {
    var out = "";
    var i;
    for(key in arr){
      document.getElementById('divisor').appendChild(x(arr[key],key))
    }
}

  //document.getElementsByTagName('body')[0].appendChild(x("hola"))
