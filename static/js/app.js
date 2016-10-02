$(document).foundation()

$(document).ready(function() {
  $('button').click(function() {
    var text = $('#emoji').val();

    $.ajax({
      url: '/word',
      data: $('form').serialize(),
      type: 'POST',
      success: function(response) {
        console.log(response);
      },
      error: function(error) {
        console.log(error)
      }
    });

  }); 
});
