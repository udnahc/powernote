        $(document).ready(function() {
                      var items = []
                      $.getJSON('/notes_for_page/',function(data){
                            $.each(data, function(key,val) {
                               $("#content").createNote({
                      				size : 'small',
                                    x: val.x_location,
                                    y: val.y_location,
                    				text : val.description,
                     				containment : 'content',
                                    id: val.id,
		                        });
                            });
                      });
                   });

		$(function() {
			$("#content").stickynote({
				size 			 : 'large',
				text			 : 'Don\'t forget to buy beans!',
				containment		 : 'content',
				event			 : 'dblclick'
			});
			
			$("#testclick").stickynote({
				size 			 : 'large',
				containment		 : 'content'
			});
			
			$("#testsmall").stickynote();
			
			$("#testcolor").stickynote({
				color			: '#FF0000',
				ontop			: true
			});
			
		});

function show_note_categories(){
    alert('Something for now');
};