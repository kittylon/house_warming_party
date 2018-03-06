window.gifts_to_add = [];
window.gifts_to_remove = [];

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
  gifts_to_add.push(gift_id);
  gifts_to_remove.pop(gift_id);
}

function remove_gift(gift_id){
  var hi_button = "add_" + gift_id;
  var bye_button = "rmv_" + gift_id;
  hide_button(bye_button);
  show_button(hi_button);
  gifts_to_add.pop(gift_id);
  gifts_to_remove.push(gift_id);
}

function confirm_gifts(guest_id){
  // confirm("Confirmars " + gifts_to_remove);
  alert(gifts_to_add);
  alert(gifts_to_remove);
  axios.post('/invitation/' + guest_id + '/', {
    'guest_id': guest_id,
    'gifts_to_add' : gifts_to_add,
    'gifts_to_remove': gifts_to_remove
  })
  .then(function (response) {
    console.log(response.data.url);
    window.location = response.data.url;
  })
}
