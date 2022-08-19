function option(e) {
    const talk = document.getElementById("talk");
    const issue = document.getElementById("issue");
    const project = document.getElementById("project");
    const connect = document.getElementById("connect");

    if (e.target.id == "T") {
      // talk.style.color = "black";
      talk.style.display = "block";
      issue.style.display = "none";
      project.style.display = "none";
      connect.style.display = "none";
    } else if (e.target.id == "I") {
      talk.style.display = "none";
      issue.style.display = "block";
      issue.style.color = "black";
      project.style.display = "none";
      connect.style.display = "none";
    } else if (e.target.id == "P") {
      talk.style.display = "none";
      issue.style.display = "none";
      project.style.display = "block";
      project.style.color = "black";
      connect.style.display = "none";
    } else if (e.target.id == "C") {
      talk.style.display = "none";
      issue.style.display = "none";
      project.style.display = "none";
      connect.style.display = "block";
      connect.style.color = "black";
    }
  }