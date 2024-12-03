import requests
import logging

logger = logging.getLogger(__name__)

AVAILABLE_MODELS = {
    'gemma': {'name': 'gemma', 'context': 2048},
    'starcoder': {'name': 'starcoder', 'context': 4096},
    'mistral': {'name': 'mistral', 'context': 8192},
    'llama3': {'name': 'llama3', 'context': 4096}
}

def get_available_models():
    """Get list of available Ollama models"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.ok:
            models = response.json()
            return [model['name'] for model in models['models']]
        return ["mistral", "llama2", "codellama", "phi"]  # fallback defaults
    except:
        return ["mistral", "llama2", "codellama", "phi"]  # fallback defaults

def get_llm_response(user_message, celebrity_context, model_name="mistral"):
    """Generate celebrity-specific responses using Ollama API"""
    try:
        api_url = "http://localhost:11434/api/chat"
        
        system_prompt = f"""You are {celebrity_context['name']}.
        Style: {celebrity_context['style']}
        Background: {celebrity_context['background']}
        Maintain the celebrity's unique personality and speaking style throughout."""

        prompt = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }

        response = requests.post(api_url, json=prompt)
        response.raise_for_status()
        
        return response.json()["message"]["content"]

    except Exception as e:
        logger.error(f"Ollama Error: {str(e)}")
        return f"Sorry, I encountered an error: {str(e)}"