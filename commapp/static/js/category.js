function option(e) {
    const talk = document.getElementById("talk");
    const issue = document.getElementById("issue");
    const project = document.getElementById("project");
    const connent = document.getElementById("connent");

    if (e.target.id == "T") {
      talk.style.display = "block";
      issue.style.display = "none";
      project.style.display = "none";
      connent.style.display = "none";
    } else if (e.target.id == "I") {
      talk.style.display = "none";
      issue.style.display = "block";
      project.style.display = "none";
      connent.style.display = "none";
    } else if (e.target.id == "P") {
      talk.style.display = "none";
      issue.style.display = "none";
      project.style.display = "block";
      connent.style.display = "none";
    } else if (e.target.id == "C") {
      talk.style.display = "none";
      issue.style.display = "none";
      project.style.display = "none";
      connent.style.display = "block";
    }
  }