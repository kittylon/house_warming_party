function check_mail(){
  var mail = document.getElementById('input').value;

  axios.post('/control/', {
    'mail' : mail,
  })
  .then(function (response) {
    window.location = response.data.url;
  })
  .catch(function (error) {
    const $error = document.getElementById("message_error")
    if ($error) {
      $error.textContent = "No estas invitado :("
    }
  });
}

function start () {
  const $input = document.getElementById('input')
  $input.addEventListener('keypress', e => {
    if (e.keyCode === 13) {
      check_mail()
    }
  })
}

start()
