document.addEventListener("DOMContentLoaded", function () {
    const closeButtons = document.querySelectorAll(".message-close");

    closeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const message = button.closest(".message");
            if (message) {
                message.remove();
            }
        });
    });
});