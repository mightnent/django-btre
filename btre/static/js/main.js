const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#msg').fadeOut('slow');
},3000);