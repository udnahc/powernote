        $(document).ready(function() {
                      var items = []
                      $.getJSON('/notes_for_page/',function(data){
                            $.each(data, function(key,val) {
                               $("body").createNote({
                      				size : 'small',
                                    x: val.x_location,
                                    y: val.y_location,
                    				text : val.description,
                     				containment : '',
                                    id: val.id,
		                        });
                            });
                      });
        });

		$(function() {
			$("body").stickynote({
				size 			 : 'large',
				text			 : '',
				containment		 : '',
				event			 : 'dblclick'
			});
		});

function show_note_categories(){
    alert('Something for now');
};


function close_message() {
    $('.alert-message').remove()
};