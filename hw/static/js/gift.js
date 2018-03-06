var gifts = [];

function hide_button(button_id){
  var bye_button = document.getElementById(button_id);
  bye_button.classList.add("hidden");
}

function show_button(button_id){
  var hi_button = document.getElementById(button_id);
  hi_button.classList.remove("hidden");
}

function add_gift(gift_id){
  var hi_button = "rmv_" + gift_id;
  var bye_button = "add_" + gift_id;
  hide_button(bye_button);
  show_button(hi_button);
  gifts.push(gift_id);
}

function remove_gift(gift_id){
  var hi_button = "add_" + gift_id;
  var bye_button = "rmv_" + gift_id;
  hide_button(bye_button);
  show_button(hi_button);
  gifts.pop(gift_id);
}

function confirm_gifts(guest_id){
  confirm("Confirmars " + gifts);

  axios.post('/invitation/' + guest_id + '/', {
    'guest_id': guest_id,
    'gifts' : gifts
  })
  .then(function (response) {
    console.log(response.data.url);
    window.location = response.data.url;
  })
}
