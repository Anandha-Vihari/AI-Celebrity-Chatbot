document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const chatMessages = document.getElementById('chat-messages');
    const settingsButton = document.getElementById('settings-button');
    const settingsPanel = document.getElementById('settings-panel');
    const saveSettingsButton = document.getElementById('save-settings');
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    // Initialize chat settings with mistral as default model
    let chatSettings = {
        responseStyle: 'casual',
        traits: {
            humorous: true,
            serious: false,
            detailed: false,
            concise: true
        },
        model: 'mistral'  // Set default model that matches your Ollama installation
    };

    // Initialize model select with default value
    const modelSelect = document.getElementById('model-select');
    if (modelSelect) {
        modelSelect.value = chatSettings.model;
    }

    // Settings panel toggle
    settingsButton.addEventListener('click', () => {
        settingsPanel.classList.toggle('show');
    });

    // Close settings panel when clicking outside
    document.addEventListener('click', (event) => {
        if (!settingsPanel.contains(event.target) && 
            !settingsButton.contains(event.target) && 
            settingsPanel.classList.contains('show')) {
            settingsPanel.classList.remove('show');
        }
    });

    // Save settings
    saveSettingsButton.addEventListener('click', () => {
        chatSettings.responseStyle = document.getElementById('response-style').value;
        chatSettings.traits = {
            humorous: document.getElementById('trait-humorous').checked,
            serious: document.getElementById('trait-serious').checked,
            detailed: document.getElementById('trait-detailed').checked,
            concise: document.getElementById('trait-concise').checked
        };
        chatSettings.model = document.getElementById('model-select').value;
        
        settingsPanel.classList.remove('show');
        addMessage('Settings updated! My responses will reflect your preferences.', 'celebrity');
    });

    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('show');
    });

    document.addEventListener('click', (event) => {
        if (!mobileMenu.contains(event.target) && 
            !mobileMenuButton.contains(event.target)) {
            mobileMenu.classList.remove('show');
        }
    });

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');
        messageInput.value = '';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                    message,
                    celebrity_name: document.querySelector('.chat-header h2').textContent,
                    settings: chatSettings
                }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            addMessage(data.response, 'celebrity');
        } catch (error) {
            console.error('Error:', error);
            addMessage('Sorry, I encountered an error. Please try again.', 'celebrity');
        }
    });

    function addMessage(content, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = content;
        
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});