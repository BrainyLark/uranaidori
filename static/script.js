function handleSubmission(selectElement, change_level) {
    if (selectElement.value == '') {
        alert("You messed up.")
    } else {
        document.getElementById("id_level").value = change_level;
        selectElement.form.submit();
    }
}