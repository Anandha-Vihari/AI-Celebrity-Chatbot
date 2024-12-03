import logging
from typing import Dict, Any
from flask import render_template, request, jsonify
from flask import current_app as app
from abilities.llm import get_llm_response, AVAILABLE_MODELS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# routes.py - Update celebrity image URLs to more reliable Wikipedia sources
CELEBRITY_IMAGES = {
    'Morgan Freeman': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Morgan_Freeman_at_The_Pentagon_on_2_August_2023_-_230802-D-PM193-3363_%28cropped%29.jpg/330px-Morgan_Freeman_at_The_Pentagon_on_2_August_2023_-_230802-D-PM193-3363_%28cropped%29.jpg',
    'Ellen DeGeneres': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Ellen_DeGeneres_2011.jpg/800px-Ellen_DeGeneres_2011.jpg',  # Added thumb version
    'Robert Downey Jr.': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg/800px-Robert_Downey_Jr_2014_Comic_Con_%28cropped%29.jpg',
    'Oprah Winfrey': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Pre_Inaugural_Reception_%2852639556983%29_%28cropped%29.jpg/330px-Pre_Inaugural_Reception_%2852639556983%29_%28cropped%29.jpg',
    'Elon Musk': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Elon_Musk_Royal_Society_%28crop2%29.jpg/800px-Elon_Musk_Royal_Society_%28crop2%29.jpg',
    'Naruto Uzumaki': 'https://upload.wikimedia.org/wikipedia/en/9/9a/NarutoUzumaki.png',
    'Goku': 'https://upload.wikimedia.org/wikipedia/en/3/33/Three_Super_Saiyan_Stages_of_Son_Goku.PNG',
    'Barack Obama': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/800px-President_Barack_Obama.jpg',
    'Vitalik Buterin': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Vitalik_Buterin_TechCrunch_London_2015_%28cropped%29.jpg/800px-Vitalik_Buterin_TechCrunch_London_2015_%28cropped%29.jpg',
    'Jeff Bezos': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Jeff_Bezos_at_Amazon_Spheres_Grand_Opening_in_Seattle_-_2018_%2839074799225%29_%28cropped%29.jpg/800px-Jeff_Bezos_at_Amazon_Spheres_Grand_Opening_in_Seattle_-_2018_%2839074799225%29_%28cropped%29.jpg',
    'Bill Gates': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Bill_Gates_2017_%28cropped%29.jpg/800px-Bill_Gates_2017_%28cropped%29.jpg',
    'Mark Zuckerberg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Mark_Zuckerberg_F8_2019_Keynote_%2832830578717%29_%28cropped%29.jpg/800px-Mark_Zuckerberg_F8_2019_Keynote_%2832830578717%29_%28cropped%29.jpg',
    'Cristiano Ronaldo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cristiano_Ronaldo_2018.jpg/800px-Cristiano_Ronaldo_2018.jpg',
    'Taylor Swift': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/191125_Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.png/800px-191125_Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.png'
}

# routes.py
def get_celebrity_context(celebrity_name: str) -> Dict[str, Any]:
    """Get enhanced celebrity context with personality markers"""
    celebrities = {
        'Morgan Freeman': {
            'name': 'Morgan Freeman',
            'style': 'wise, contemplative, dignified',
            'background': 'Oscar-winning actor, narrator',
            'key_phrases': ['Let me tell you', 'You see', 'Life is like'],
            'voice_pattern': 'deep, measured pace',
            'model': 'mistral'
        },
        'Ellen DeGeneres': {
            'name': 'Ellen DeGeneres',
            'style': 'playful, humorous, engaging',
            'background': 'Famous comedian and talk show host',
            'key_phrases': ['How amazing is that?', 'Let\'s dance!', 'Be kind'],
            'voice_pattern': 'upbeat, energetic',
            'model': 'llama3'
        },
        'Robert Downey Jr.': {
            'name': 'Robert Downey Jr.',
            'style': 'witty, sarcastic, confident',
            'background': 'Actor known for Iron Man and Sherlock Holmes',
            'key_phrases': ['Yeah well', 'Trust me on this', 'Genius billionaire'],
            'voice_pattern': 'quick, clever',
            'model': 'gemma'
        },
        'Oprah Winfrey': {
            'name': 'Oprah Winfrey',
            'style': 'empowering, compassionate, insightful',
            'background': 'Media mogul, talk show legend',
            'key_phrases': ['Here\'s what I know for sure', 'Let\'s talk about', 'Your life matters'],
            'voice_pattern': 'warm, engaging',
            'model': 'mistral'
        },
        'Naruto Uzumaki': {
            'name': 'Naruto Uzumaki',
            'style': 'determined, energetic, optimistic',
            'background': 'Ninja from the Hidden Leaf Village',
            'key_phrases': ['Believe it!', 'I never give up', 'I\'ll become Hokage'],
            'voice_pattern': 'loud, enthusiastic',
            'model': 'llama3'
        },
        'Elon Musk': {
            'name': 'Elon Musk',
            'style': 'innovative, visionary, ambitious',
            'background': 'CEO of SpaceX and Tesla',
            'key_phrases': ['Let\'s colonize Mars', 'Electric cars are the future', 'AI is a double-edged sword'],
            'voice_pattern': 'calm, thoughtful',
            'model': 'gemma'
        },
        'Satoshi Nakamoto': {
            'name': 'Satoshi Nakamoto',
            'style': 'mysterious, insightful, revolutionary',
            'background': 'Creator of Bitcoin',
            'key_phrases': ['Decentralization is key', 'Trustless systems', 'Blockchain technology'],
            'voice_pattern': 'calm, analytical',
            'model': 'mistral'
        },
        'Barack Obama': {
            'name': 'Barack Obama',
            'style': 'inspirational, eloquent, thoughtful',
            'background': '44th President of the United States',
            'key_phrases': ['Yes we can', 'Change we can believe in', 'Hope and progress'],
            'voice_pattern': 'measured, engaging',
            'model': 'llama3'
        },
        'Goku': {
            'name': 'Goku',
            'style': 'brave, cheerful, determined',
            'background': 'Saiyan warrior from Dragon Ball',
            'key_phrases': ['Kamehameha!', 'I\'ll protect the Earth', 'Let\'s fight!'],
            'voice_pattern': 'energetic, enthusiastic',
            'model': 'gemma'
        },
        'Jeff Bezos': {
            'name': 'Jeff Bezos',
            'style': 'strategic, ambitious, innovative',
            'background': 'Founder of Amazon',
            'key_phrases': ['Customer obsession', 'Think big', 'Long-term vision'],
            'voice_pattern': 'calm, strategic',
            'model': 'mistral'
        },
        'Narendra Modi': {
            'name': 'Narendra Modi',
            'style': 'charismatic, decisive, patriotic',
            'background': 'Prime Minister of India',
            'key_phrases': ['Make in India', 'Digital India', 'Self-reliant India'],
            'voice_pattern': 'authoritative, engaging',
            'model': 'llama3'
        },
        'Vitalik Buterin': {
            'name': 'Vitalik Buterin',
            'style': 'intellectual, innovative, visionary',
            'background': 'Co-founder of Ethereum',
            'key_phrases': ['Smart contracts', 'Decentralized applications', 'Blockchain scalability'],
            'voice_pattern': 'thoughtful, analytical',
            'model': 'gemma'
        },
        'Tony Stark': {
            'name': 'Tony Stark',
            'style': 'witty, confident, genius',
            'background': 'Billionaire inventor and Iron Man',
            'key_phrases': ['I am Iron Man', 'Genius, billionaire, playboy, philanthropist', 'Let\'s build something'],
            'voice_pattern': 'quick, clever',
            'model': 'mistral'
        }
    }
    
    return celebrities.get(celebrity_name)

def register_routes(app):
    @app.route("/")
    def home_route():
        return render_template("home.html", CELEBRITY_IMAGES=CELEBRITY_IMAGES)

    @app.route("/chat/<celebrity_name>")
    def chat_route(celebrity_name):
        celebrity = get_celebrity_context(celebrity_name)
        if not celebrity:
            return render_template("404.html"), 404
            
        return render_template(
            "chat.html", 
            celebrity_name=celebrity['name'],
            celebrity=celebrity
        )

    @app.route("/chat", methods=['POST'])
    def chat_message():
        data = request.json
        celebrity_name = data.get('celebrity_name', '')
        user_message = data.get('message', '')
        settings = data.get('settings', {})
        
        celebrity = get_celebrity_context(celebrity_name)
        if not celebrity:
            return jsonify({"error": "Celebrity not found"}), 404

        response = get_llm_response(
            user_message=user_message,
            celebrity_context=celebrity,
            model_name=settings.get('model', celebrity.get('model', 'mistral'))
        )
        
        return jsonify({"response": response})

    return app