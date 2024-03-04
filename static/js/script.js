SendButton.addEventListner("click", ()=>{
    alert("hey! you clicked")
    questionInput = document.getElementById("questionInput").value;
    question = document.getElementById("question").value;
    document.getElementById("question").value = "";
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"

    question1.innerHTML = questionInput;
    question2.innerHTML = questionInput;
})