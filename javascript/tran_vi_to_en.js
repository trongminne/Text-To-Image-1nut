document.getElementById('generate_button').addEventListener('click', function() {
    var vietnameseText = document.getElementById('positive_prompt').value;
    
    // Call the translate_text function
    var englishText = translate_text(vietnameseText);
    console.log("English Text:", englishText);

    // Call the generate_image function
    generate_image();
});
alert('sbdjjsdbj')