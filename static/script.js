function handleSubmission(selectElement, command) {
    document.getElementById("cmd").value = command;
    selectElement.form.submit();
}