
var generateButton = document.getElementById("generate_button");

// Thêm sự kiện click
generateButton.addEventListener("click", function () {
    var vietnameseText = document.getElementsByClassName('scroll-hide').value;
    alert(vietnameseText)
    // Call the translate_text function
    var englishText = translate_text(vietnameseText);
    console.log("English Text:", englishText);

    // Call the generate_image function
    generate_image();
});