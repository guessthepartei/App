var score = 0
var scoreML = 0
var actualState
var mlState


changeState()

function checkResult(str) {
  var correct = (actualState == str)
  var correctML = (mlState == str)
  if (correct) score++
  if (correctML) scoreML++
  document.getElementById("answer").innerHTML = str+ ":" + mlState
  document.getElementById("score").innerHTML = score+ ":" + scoreML
  document.getElementById("plus").innerHTML = correct + ":" + correctML
  if (score > scoreML) document.getElementById("motivation").innerHTML = "Mommy is proud of you."
  else document.getElementById("motivation").innerHTML = "You are looser."
  changeState()
}

function changeState() {
  const Http = new XMLHttpRequest();
  const url='http://127.0.0.1:5000/main';
  Http.open("GET", url);
  Http.send();
  var obj
  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
    obj = JSON.parse(Http.responseText);
    document.getElementById("losung").innerHTML = obj.text
    actualState = obj.party
    mlState = obj.predict

  }

}
