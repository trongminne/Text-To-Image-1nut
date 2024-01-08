document.addEventListener("DOMContentLoaded", function() {
    var generateButton = document.getElementById("generate_button");

    if (generateButton) {
        generateButton.addEventListener("click", function () {
            var vietnameseText = document.querySelector('.scroll-hide').value;
            alert(vietnameseText);

            // Kiểm tra xem các hàm có được định nghĩa đúng không
            console.log("Calling translate_text...");
            var englishText = translate_text(vietnameseText);
            console.log("English Text:", englishText);

            console.log("Calling generate_image...");
            generate_image();
        });
    } else {
        console.error("Element with id 'generate_button' not found.");
    }
});
