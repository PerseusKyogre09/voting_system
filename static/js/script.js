// static/js/script.js
document.addEventListener("DOMContentLoaded", function () {
    const voteForm = document.getElementById("voteForm");
    const progressMessage = document.getElementById("progressMessage");

    voteForm.addEventListener("submit", function () {
        progressMessage.textContent = "Submitting your encrypted vote...";
    });
});
