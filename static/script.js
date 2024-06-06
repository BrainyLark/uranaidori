function send(field, cmd) {
    document.getElementById('cmd').value=cmd;
    field.form.submit();
}