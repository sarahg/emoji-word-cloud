$(document).foundation()

$(document).ready(function() {
  
  $textarea = $('#emoji textarea');

  // When the form is submitted, process the input.
  // Returns an object containing emojis and their relative weights.
  $('button').click(function() {
    var text = $textarea.val();

    $.ajax({
      url: '/wordUp',
      data: $('form').serialize(),
      type: 'POST',
      success: function(response) {
        //console.log(response);
        renderWordCloud(response.weighted_emojis);
      },
      error: function(error) {
        console.log(error) // @todo clearer error for the user
      }
    });

  });

  // Pass the emoijs over to the jQCloud plugin.
  // Hide the text area.
  var renderWordCloud = function(emojis) {
    $textarea.fadeOut('slow', function() {
      $('#cloud').jQCloud(emojis);
    }); 
  }
 
});
