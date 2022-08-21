function registration_js() {
    var username = $("#name").val(); // Кладем текст из поля "name" в переменную
    var email = $("#e_mail").val();
    var password = $("#password").val();
    var second_password = $("#second_password").val();
    $.get("/send_reg_credentials", { "username" : username, "email" : email, "password": password, "second_password": second_password});
}