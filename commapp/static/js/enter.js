// document.addEventListener('keydown', function(event) {
//     if (event.keyCode === 13) {
//       event.preventDefault();
//       this.textContent.value + "\n*"
//     };
//   }, true);

  var str = document.getElementById("textarea").value;
  str = str.replace(/(?:\r\n|\r|\n)/g, '<br/>');
  document.getElementById("textarea").value = str;