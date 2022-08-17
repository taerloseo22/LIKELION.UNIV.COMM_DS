var btn = document.querySelector(".rebtn")
var section = document.querySelector(".resection")
function recomment(){
    if(btn.style.display==="flex"){
    section.style.display="block";
    btn.style.display="none";
    }
    else{
        section.style.display="none";
        btn.style.display="flex"; 
    }
}