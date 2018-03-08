window.gifts_to_add = [];
window.gifts_to_remove = [];
window.removed_gifts = []
var new_gifts_id = window.gifts_id.slice()

function hide_button(button_id){
  var bye_button = document.getElementById(button_id);
  bye_button.classList.add("hidden");
}

function toggle_cover (id) {
  var cover = document.getElementById(id);
  cover.classList.toggle("added")
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
  toggle_cover("cover_" + gift_id)
  //gifts_to_add.push(gift_id);
  //gifts_to_remove.pop(gift_id);
  if (!new_gifts_id.includes(gift_id)) {
    gifts_to_add.push(gift_id)
    new_gifts_id.push(gift_id)
  }
}

function remove_gift(gift_id){
  var hi_button = "add_" + gift_id;
  var bye_button = "rmv_" + gift_id;
  hide_button(bye_button);
  show_button(hi_button);
  toggle_cover("cover_" + gift_id)

  if (new_gifts_id.includes(gift_id)) {
    new_gifts_id = new_gifts_id.filter(id => id !== gift_id)
    if (gifts_to_add.includes(gift_id)) {
        gifts_to_add = gifts_to_add.filter(id => id !== gift_id)
    } else {
      gifts_to_remove.push(gift_id);
    }
  }
}

function confirm_gifts(guest_id){
  // confirm("Confirmars " + gifts_to_remove);
  console.log('id list', new_gifts_id)
  console.log('to remove', gifts_to_remove)
  console.log('to add', gifts_to_add)
  if (new_gifts_id.length  > 0) {
    alert('you can add')
  } else {
    alert('nope')
  }
  /*
  alert(removed_gifts);
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
  })*/
}
