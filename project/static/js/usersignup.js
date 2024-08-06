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

document.getElementById('registration-form').addEventListener('submit', function(event) {
  event.preventDefault(); 

  var username = document.getElementById('name').value;
  var password = document.getElementById('password').value;
  var confirmPassword = document.getElementById('re-password').value;
  var talent = document.getElementsByName('ONE').value;

  var isUsernameTaken = registeredUsers.some(function(user) {
    return user.username == username;
  });

  if (isUsernameTaken) {
    displayErrorMessage('Username is taken',2000,'error-message-3');
    return;
  }

  if (password !== confirmPassword) {
    displayErrorMessage('Password is not match',2000,'error-message-4');
    return;
  }
  
  alert('Registration successful!');
  window.location.href = 'login.html';
});