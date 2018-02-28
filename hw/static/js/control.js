function check_mail(){
  var mail = document.getElementById('input_mail').value;

  axios.post('/control/', {
    'mail' : mail,
  })
  .then(function (response) {
    console.log(response);
    alert("Welcome mother foca")
  })
  .catch(function (error) {
    const $error = document.getElementById("message_error")
    if ($error) {
      $error.textContent = "No estas invitado :("
    }
    console.log("Ich bin eine schöne error");
  });
}
