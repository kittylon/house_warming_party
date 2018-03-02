
function add_gift(gift_id, guest_id){
  axios.post('/invitation/' + guest_id + '/', {
    'gift_id' : gift_id,
    'guest_id': guest_id
  })
  .then(function (response) {
    console.log(response.data.message);
    alert(response.data.message);
  })
  .catch(function (error) {  
    alert("Something went wrong :'('");
    console.log("Something went wrong");
  });
}
