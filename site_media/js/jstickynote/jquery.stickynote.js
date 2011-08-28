(function($) {
	
	$.fn.stickynote = function(options) {
		var opts = $.extend({}, $.fn.stickynote.defaults, options);
		return this.each(function() {
			$this = $(this);
			var o = $.meta ? $.extend({}, opts, $this.data()) : opts;
			switch(o.event){
				case 'dblclick':
					$this.dblclick(function(e){$.fn.stickynote.createNote(o,e);})
					break;
				case 'click':
					$this.click(function(e){$.fn.stickynote.createNote(o,e);})
					break;
			}		
		});
	};
	$.fn.stickynote.defaults = {
		size 	: 'small',
		event	: 'click',
		color	: '#000000'
	};


	$.fn.stickynote.createNote = function(o,e) {

        x_location = e.pageX;
        y_location = e.pageY;
        
		var _note_content = $(document.createElement('textarea')).attr('id','description');
		var _div_note 	= 	$(document.createElement('div'))
							.addClass('jStickyNote')
                            .css('cursor','move');

        var _save_button = $(document.createElement('button')).attr('id', 'save').attr('class','btn small primary');
        _save_button.text('Save')
        _div_note.append(_save_button);

        var _properties_button = $(document.createElement('button')).attr('id','properties').attr('class', 'btn small primary');
        _properties_button.text('Properties')
        _div_note.append(_properties_button)

        var _hide_button = $(document.createElement('button')).attr('id','hide').attr('class','btn small primary');
        _hide_button.text('Hide')
        _div_note.append(_hide_button)

        _save_button.click(function(e) 
                        { 
                            div_to_be_saved = $(e.target).parent().parent();
                            
                            $.ajax({
                                    type: "POST",
                                        url:'/save_note/',
                                data: {'x-location':e.pageX, 'y-location':e.pageY , 'note_id': 'new', 'description': $(div_to_be_saved).find('#description').val()},


                                        success: function(return_value){
                                            $("<div class='alert-message success'><a class='close' onClick='close_message();' href='#'>x</a><p>Note has been created successfully</p></div>").appendTo("#navigation") 
                                        }
                                        });
                        });

        _properties_button.click(function(e) 
                        { 
                            centerPopup();
                            loadPopup();
                        });

        _hide_button.click(function(e) 
                        { 
                            $(this).parent().hide();
                            $(this).parent().parent().hide();
                        });


		if(!o.text){
			_div_note.append(_note_content);
			var _div_create = $(document.createElement('div'))
						.addClass('jSticky-create')
                .attr('title','Create Sticky Note');
		
			_div_create.click(function(e){
				var _p_note_text = 	$(document.createElement('p'))
									.css('color',o.color)
									.html	(
											$(this)
											.parent()
											.find('textarea')
											.val()
											);
				$(this)
				.parent()
				.find('textarea')
				.before(_p_note_text)
				.remove(); 
				
				$(this).remove();						
			})
		}	
		else
            //			_div_note.append('<p style="color:'+o.color+'">'+o.text+'</p>');  
          _div_note.append(_note_content);
		
		var _div_delete = 	$(document.createElement('div'))
							.addClass('jSticky-delete');
		
		_div_delete.click(function(e){
			$(this).parent().remove();
		})
		
		var _div_wrap 	= 	$(document.createElement('div'))
                .attr("note_id", 'new' )       
                .css({'position':'absolute','left':x_location, 'top':y_location})
				.append(_div_note)
				.append(_div_delete)
				.append(_div_create);	
        
		switch(o.size){
			case 'large':
				_div_wrap.addClass('jSticky-medium');
				break;
			case 'small':
				_div_wrap.addClass('jSticky-medium');
				break;
		}		
		if(o.containment){
			_div_wrap.draggable({ containment: '#'+o.containment , scroll: false ,start: function(event, ui) {
				if(o.ontop)
					$(this).parent().append($(this));
			}});	
		}	
		else{
			_div_wrap.draggable({ scroll: false ,start: function(event, ui) {
				if(o.ontop)
					$(this).parent().append($(this));
			}});	
		}
		$('body').append(_div_wrap);
	};


    // Have to remove this DANGEROUS !!!!
	$.fn.createNote = function(o) {
        
        x_location = o.x;
        y_location = o.y;
        note_text = o.text;
        note_id = o.id;
        

		var _note_content = $(document.createElement('textarea')).attr('id', 'text-' + note_id).html(note_text);
		var _div_note 	= 	$(document.createElement('div'))
							.addClass('jStickyNote')
                            .css('cursor','move');

        var _save_button = $(document.createElement('button')).attr('id', 'save').attr('class','btn small primary');
        _save_button.text('Save')
        _div_note.append(_save_button);

        var _properties_button = $(document.createElement('button')).attr('id','properties').attr('class', 'btn small primary');
        _properties_button.text('Properties')
        _div_note.append(_properties_button)

        var _hide_button = $(document.createElement('button')).attr('id','hide').attr('class','btn small primary');
        _hide_button.text('Hide')
        _div_note.append(_hide_button)
        
        _save_button.click(function(e) 
                        { 
                            div_to_be_saved = $(e.target).parent().parent();
                            note_id_to_be_saved = div_to_be_saved.attr('note_id');
                        
                            $.ajax({
                                    type: "POST",
                                        url:'/save_note/',
                                data: {'x-location':e.pageX, 'y-location':e.pageY, 'note_id': note_id_to_be_saved, 'description' : $('#text-' + note_id_to_be_saved).val() },
                                        success: function(return_value){ 
                                            $("<div class='alert-message success'><a class='close' onClick='close_message();' href='#'>x</a><p>Note has been created successfully</p></div>").appendTo("#navigation")
                                        },
                                        });
                        });

        _properties_button.click(function(e) 
                        { 
                            div_to_be_saved = $(e.target).parent().parent();
                            note_id_to_be_saved = div_to_be_saved.attr('note_id');
                            $.ajax({
                                    type: "GET",
                                        url:'/properties/',
                                data: {'note_id': note_id_to_be_saved },
                                success: function(return_value){ 
                                    $("#popupContact").html(return_value);
                                                                 processPopup(note_id_to_be_saved, return_value);},
                                        });
                            

                        });

        _hide_button.click(function(e) 
                        { 
                            $(this).parent().hide();
                            $(this).parent().parent().hide();
                        });


		if(!o.text){
			_div_note.append(_note_content);
			var _div_create = $(document.createElement('div'))
						.addClass('jSticky-create')
                .attr('title','Create Sticky Note');
		
			_div_create.click(function(e){
				var _p_note_text = 	$(document.createElement('p'))
									.css('color',o.color)
									.html	(
											$(this)
											.parent()
											.find('textarea')
											.val()
											);
				$(this)
				.parent()
				.find('textarea')
				.before(_p_note_text)
				.remove(); 
				
				$(this).remove();						
			})
		}	
		else
			_div_note.append(_note_content);
			// _div_note.append('<p style="color:'+o.color+'">'+o.text+'</p>');
					
		
		var _div_delete = 	$(document.createElement('div'))
							.addClass('jSticky-delete');
		
		_div_delete.click(function(e){
			$(this).parent().remove();
		})
		
		var _div_wrap 	= 	$(document.createElement('div'))
            .attr("note_id", note_id)
        .css({'position':'absolute','left':x_location, 'top':y_location})
							.append(_div_note)
							.append(_div_delete)
							.append(_div_create);	
		switch(o.size){
			case 'large':
				_div_wrap.addClass('jSticky-large');
				break;
			case 'small':
				_div_wrap.addClass('jSticky-medium');
				break;
		}		
		if(o.containment){
			_div_wrap.draggable({ containment: '#'+o.containment , scroll: false ,start: function(event, ui) {
				if(o.ontop)
					$(this).parent().append($(this));
			}});	
		}	
		else{
			_div_wrap.draggable({ scroll: false ,start: function(event, ui) {
				if(o.ontop)
					$(this).parent().append($(this));
			}});	
		}
		$('body').append(_div_wrap);
	};
})(jQuery);


function change_property() {
    $.ajax({
        type: "POST",
        url:'/test_ajax/',
        // data: {'x-location':e.pageX, 'y-location':e.pageY , 'note_id': 'new', 'description': $(div_to_be_saved).find('#description').val()},

        success: function(return_value){
                    $("<div class='alert-message success'><a class='close' onClick='close_message();' href='#'>x</a><p>Note has been updated successfully</p></div>").prependTo("#change_property") 
        }
     });
}


