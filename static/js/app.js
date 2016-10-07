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
        console.log(response);

          // var words = response.weighted_emojis; // doesn't work

          // this one works -- diff is no quotes on the object property names
          var words = [{weight: 19, text: "\ud83c\udfaa"}, {weight: 19, text: "\ud83c\udfac"}, {weight: 45, text: "\ud83c\udf89"}, {weight: 19, text: "\ud83c\udfab"}];

          // @todo the array from python has properties like "weight" and "text" 
          // instead of just weight and text (no quotes). Seems to be the issue here. Could fix in JS or Python...
          renderWordCloud(words);
      },
      error: function(error) {
        console.log(error) // @todo clearer error for the user
      }
    });

    $(this).fadeOut('fast');

  });

  // Pass the emoijs over to the jQCloud plugin.
  // Hide the text area.
  var renderWordCloud = function(emojis) {
    $textarea.fadeOut('slow', function() {
      $('#cloud').jQCloud(emojis);
    }); 
  }
 
});
