document.addEventListener('keydown', function(event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      this.textContent.value + "\n*"
    };
  }, true);