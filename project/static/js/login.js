var registeredUsers = JSON.parse(localStorage.getItem('registered-Users')) || [];
var registeredAdmins = JSON.parse(localStorage.getItem('registeredUsers')) || [];
function displayErrorMessage(message, duration,container) {
    var errorMessage = document.createElement('div');
    var errorMessageContainer = document.getElementById(container);
    errorMessage.textContent = message;
    errorMessage.classList.add('error-message');
    errorMessageContainer.appendChild(errorMessage);
    setTimeout(function() {
        errorMessageContainer.removeChild(errorMessage);
    }, duration);
}
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var user = document.getElementById('option1');
    var admin = document.getElementById('option2');
   
    if(user.checked){
        var isUsernameTaken = registeredUsers.some(function(user) {
            return user.username == username;
        });
        var isPasswordTaken = registeredUsers.some(function(user) {
            return user.password == password;
        });
        if (isUsernameTaken && isPasswordTaken) {
            alert('login Successfully!!');
            window.location.href='userPage.html';
        }
        else{
            displayErrorMessage('There is no user with this Data.',2000,'error-message-1');
            return;
        }
    }
    else if(admin.checked){
        var isUsernameTaken = registeredAdmins.some(function(user) {
            return user.username == username;
        });
        var isPasswordTaken = registeredAdmins.some(function(user) {
            return user.password == password;
        });
        if (isUsernameTaken && isPasswordTaken) {
            alert('login Successfully!!');
            window.location.href='adminPage.html';
        }
        else{
            displayErrorMessage('There is no Admin with this Data.',2000,'error-message-1');
            return;
        }
    }
});