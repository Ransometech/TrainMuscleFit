document.addEventListener('DOMContentLoaded', function() {
    const alertButton = document.createElement('button');
    alertButton.innerText = 'Click me for a surprise!';
    alertButton.className = 'btn btn-primary';
    document.body.appendChild(alertButton);

    alertButton.addEventListener('click', function() {
        alert('Hello! Welcome to my homepage.');
    });
});
