$(document).foundation()

// When the form is submitted, process the input.
// Returns an object containing emojis and their relative weights.
$(document).ready(function() {

  $('button').click(function() {
    $.ajax({
      url: '/wordUp',
      data: $('form').serialize(),
      type: 'POST',
      dataType: 'json',
      success: function(response) {
        renderWordCloud(response.weighted_emojis);
        $('button').fadeOut('fast');
     },
      error: function(error) {
        console.log(error)
      }
    });
  });

  // Pass the emoijs over to the jQCloud plugin.
  // Hide the text area.
  var renderWordCloud = function(emojis) {
    $('#emoji textarea').fadeOut('slow', function() {
      $('#cloud').jQCloud(emojis);
    }); 
  }
 
});
