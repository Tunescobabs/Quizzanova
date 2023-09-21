function validateEmail(email) {
    var regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return regex.test(email);
}

document.getElementById('id_email').onchange = function() {
    if (!validateEmail(this.value)) {
        alert("Invalid email address");
    }
};
