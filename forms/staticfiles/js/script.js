var counter = 0;
    //var  oForm = document.forms[counter];
jQuery(function(){
    jQuery('a.add-field').click(function(event){
        event.preventDefault();
        //var name = oForm.elements["name"].value;
        counter=counter+1;
        var row = '<input type = "text"'+'id=question'+counter+' class = "question" name="array[]" placeholder = "type your question here" required>&nbsp;<select name="opt[]" class = "dropdown"><option value="1" class="list">Text</option><option value="2" class="list">Number</option><option value="3" class="list">Date</option></select><br>';
        var newRow = jQuery(row);
        jQuery('div.main1').append(newRow);
    });
});
