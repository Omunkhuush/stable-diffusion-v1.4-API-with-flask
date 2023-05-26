function addFeature(btnId) {
  var feature = document.getElementById(btnId).textContent;
  var inputValue = document.getElementById("name").value;
  var backgroundColor = window.getComputedStyle(
    document.getElementById(btnId)
  ).backgroundColor;
  if (backgroundColor === "rgb(247, 247, 247)") {
    if (inputValue.length === 0) {
      var updateValue = feature;
    } else {
      var updateValue = inputValue + " " + feature;
    }
    document.getElementById("name").value = updateValue;
    document.getElementById(btnId).style.backgroundColor = "rgb(18, 165, 133)";
    document.getElementById(btnId).style.color = "#f7f7f7";
  } else {
    var updateValue = inputValue.replace(feature, "");
    document.getElementById("name").value = updateValue;
    document.getElementById(btnId).style.color = "black";
    document.getElementById(btnId).style.backgroundColor = "#f7f7f7";
  }
}

function showLoadingIcon() {
  var loadingWindow = window.getComputedStyle(
    document.getElementById("loadingSpinner")
  ).display;
  var imageShow = window.getComputedStyle(
    document.getElementById("genImage")
  ).display;
  //console.log("imageDisplay", imageShow);
  //console.log("loadingWindow:", loadingWindow);
  document.getElementById("mainTextDiv").style.display = "none";
  if (loadingWindow === "none") {
    document.getElementById("loadingSpinner").style.display = "block";
  }
  if (imageShow === "block") {
    document.getElementById("genImage").style.display = "none";
  }
}
function putPrompt() {
  var promptValue = document.getElementById("prompt").innerText;
  str = promptValue.split("PROMPT: ")[1];
  console.log("prompt:", str);
  document.getElementById("name").value = str;
}

function showModal(id) {
  var modal = window.getComputedStyle(document.getElementById(id));
  if (modal.visibility == "hidden") {
    document.getElementById(id).classList.add("show-modal");
  }
}
function hideModal(id) {
  document.getElementById(id).classList.remove("show-modal");
}
function sendEmail() {
  var email = document.getElementById("emailInput").value;
  console.log(email);
  if (email === "") {
    alert("please type email!");
  }
  changeSending();
  //hideModal("modalContainer");
}
function changeSending() {
  console.log("mail=", document.getElementById("mailformDiv").style.display);
  document.getElementById("mailformDiv").style.display = "none";
  console.log("sending=", document.getElementById("sendingDiv").style.display);
  console.log(document.getElementById("mailformDiv").style.display);
  document.getElementById("sendingDiv").style.display = "block";
  console.log(document.getElementById("sendingDiv").style.display);
}
