// static/js/home.js
document.addEventListener('DOMContentLoaded', () => {
    const chatButtons = document.querySelectorAll('.chat-button');
    
    chatButtons.forEach(button => {
        button.addEventListener('click', () => {
            const celebrityName = button.parentElement.querySelector('h3').textContent;
            window.location.href = `/chat/${encodeURIComponent(celebrityName)}`;
        });
    });
});