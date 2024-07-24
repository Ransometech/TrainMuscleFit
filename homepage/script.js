// JavaScript to add interactivity on page load
document.addEventListener('DOMContentLoaded', function() {
    // Create a button element for the alert
    const alertButton = document.createElement('button');
    alertButton.innerText = 'Click me for a surprise!';
    alertButton.className = 'btn btn-primary';
    document.body.appendChild(alertButton);

    // Add an event listener to the button to show an alert
    alertButton.addEventListener('click', function() {
        alert('Hello! Welcome to my homepage.');
    });
});
