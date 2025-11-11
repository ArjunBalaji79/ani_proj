from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)

# Initialize embeddings model (lightweight)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
)

# Song database with mood tags
SONGS_DATA = [
    {"title": "Happy", "artist": "Pharrell Williams", "mood": "happy, joyful, energetic", "genre": "Pop", "description": "An upbeat song that makes you want to dance and smile"},
    {"title": "Someone Like You", "artist": "Adele", "mood": "sad, melancholic, heartbroken", "genre": "Pop/Soul", "description": "A powerful ballad about lost love and moving on"},
    {"title": "Shake It Off", "artist": "Taylor Swift", "mood": "happy, carefree, confident", "genre": "Pop", "description": "An anthem about not letting negativity bring you down"},
    {"title": "The Night We Met", "artist": "Lord Huron", "mood": "nostalgic, sad, longing", "genre": "Indie Folk", "description": "A hauntingly beautiful song about missing someone"},
    {"title": "Eye of the Tiger", "artist": "Survivor", "mood": "motivated, powerful, energetic", "genre": "Rock", "description": "The ultimate pump-up song for motivation and determination"},
    {"title": "Stressed Out", "artist": "Twenty One Pilots", "mood": "anxious, nostalgic, stressed", "genre": "Alternative", "description": "About the pressures of adulthood and longing for simpler times"},
    {"title": "Don't Stop Me Now", "artist": "Queen", "mood": "happy, excited, euphoric", "genre": "Rock", "description": "A high-energy anthem about feeling unstoppable"},
    {"title": "Mad World", "artist": "Gary Jules", "mood": "sad, depressed, melancholic", "genre": "Alternative", "description": "A haunting cover about feeling disconnected from the world"},
    {"title": "Good Vibrations", "artist": "The Beach Boys", "mood": "happy, relaxed, positive", "genre": "Pop Rock", "description": "Classic feel-good song with positive energy"},
    {"title": "Hurt", "artist": "Johnny Cash", "mood": "sad, reflective, regretful", "genre": "Alternative Country", "description": "A powerful song about pain, regret, and redemption"},
    {"title": "Walking on Sunshine", "artist": "Katrina and the Waves", "mood": "happy, joyful, optimistic", "genre": "Pop", "description": "An infectious song about pure happiness and excitement"},
    {"title": "Creep", "artist": "Radiohead", "mood": "sad, lonely, insecure", "genre": "Alternative Rock", "description": "About feeling like an outsider and not belonging"},
    {"title": "Lovely Day", "artist": "Bill Withers", "mood": "happy, peaceful, content", "genre": "Soul", "description": "A soothing song that makes everything feel better"},
    {"title": "Boulevard of Broken Dreams", "artist": "Green Day", "mood": "lonely, sad, isolated", "genre": "Rock", "description": "About walking alone and feeling disconnected"},
    {"title": "Can't Stop the Feeling", "artist": "Justin Timberlake", "mood": "happy, energetic, excited", "genre": "Pop", "description": "An irresistible dance song that lifts your spirits"},
    {"title": "Skinny Love", "artist": "Bon Iver", "mood": "sad, heartbroken, vulnerable", "genre": "Indie Folk", "description": "A raw, emotional song about a failing relationship"},
    {"title": "Best Day of My Life", "artist": "American Authors", "mood": "happy, optimistic, celebratory", "genre": "Indie Pop", "description": "An uplifting anthem about enjoying life"},
    {"title": "Everybody Hurts", "artist": "R.E.M.", "mood": "sad, comforting, empathetic", "genre": "Rock", "description": "A comforting reminder that everyone struggles sometimes"},
    {"title": "September", "artist": "Earth, Wind & Fire", "mood": "happy, nostalgic, groovy", "genre": "Funk/Soul", "description": "A timeless party song that never fails to lift spirits"},
    {"title": "Fix You", "artist": "Coldplay", "mood": "sad, hopeful, comforting", "genre": "Alternative Rock", "description": "A beautiful song about supporting someone through difficult times"},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "mood": "happy, confident, funky", "genre": "Funk/Pop", "description": "A groovy, feel-good song that makes you want to move"},
    {"title": "Numb", "artist": "Linkin Park", "mood": "angry, frustrated, pressured", "genre": "Rock", "description": "About feeling overwhelmed by expectations"},
    {"title": "Three Little Birds", "artist": "Bob Marley", "mood": "relaxed, peaceful, reassuring", "genre": "Reggae", "description": "A calming reminder that everything will be alright"},
    {"title": "The Sound of Silence", "artist": "Simon & Garfunkel", "mood": "melancholic, contemplative, isolated", "genre": "Folk", "description": "A profound meditation on loneliness and disconnection"},
    {"title": "I Gotta Feeling", "artist": "Black Eyed Peas", "mood": "happy, excited, party", "genre": "Pop", "description": "The ultimate party anthem about good times ahead"},
]

# Create vector store
def create_vector_store():
    documents = []
    for song in SONGS_DATA:
        content = f"Song: {song['title']} by {song['artist']}. Mood: {song['mood']}. Genre: {song['genre']}. {song['description']}"
        documents.append(Document(page_content=content, metadata=song))
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(documents)
    
    vectorstore = FAISS.from_documents(splits, embeddings)
    return vectorstore

# Initialize vector store
print("Initializing vector store...")
vectorstore = create_vector_store()
print("Vector store ready!")

def query_cerebras(prompt, context):
    """Query Cerebras API for song recommendations"""
    api_key = os.environ.get('CEREBRAS_API_KEY', '')
    
    if not api_key or api_key == 'your_api_key_here':
        # Fallback response if no API key
        print("⚠️  WARNING: No valid CEREBRAS_API_KEY found. Using fallback response.")
        print("   To enable AI recommendations, get a key from: https://cloud.cerebras.ai/")
        print("   Then add it to Vercel environment variables: CEREBRAS_API_KEY=your_key")
        return "Based on your mood, I'd recommend checking out the songs I found for you!"
    
    try:
        url = "https://api.cerebras.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        system_prompt = """You are a music recommendation assistant. Based on the user's mood and the songs provided, 
        give personalized recommendations. Be friendly, empathetic, and explain why each song matches their mood.
        Keep your response concise but warm."""
        
        user_prompt = f"""User's mood: {prompt}

Relevant songs from database:
{context}

Provide 3-5 song recommendations from the list above that best match the user's mood. 
Explain briefly why each song fits their current emotional state."""

        data = {
            "model": "llama3.1-8b",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        print(f"🤖 Querying Cerebras API with model: llama3.1-8b")
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        # Check for HTTP errors
        if response.status_code == 401:
            print(f"❌ ERROR: Invalid API key (401 Unauthorized)")
            print(f"   Please check your CEREBRAS_API_KEY is correct")
            return "Unable to generate AI recommendations. Please check your API key configuration."
        elif response.status_code == 429:
            print(f"❌ ERROR: Rate limit exceeded (429)")
            return "Too many requests. Please try again in a moment."
        elif response.status_code >= 500:
            print(f"❌ ERROR: Cerebras API server error ({response.status_code})")
            return "AI service temporarily unavailable. Here are some great song recommendations!"
        
        response.raise_for_status()
        
        result = response.json()
        print(f"✅ Successfully received AI response from Cerebras")
        return result['choices'][0]['message']['content']
    
    except requests.exceptions.Timeout:
        print(f"❌ ERROR: Request timeout after 10 seconds")
        return "Request took too long. Here are some great song recommendations from my collection!"
    except requests.exceptions.ConnectionError as e:
        print(f"❌ ERROR: Connection failed - {str(e)}")
        return "Unable to connect to AI service. Here are some great song recommendations!"
    except KeyError as e:
        print(f"❌ ERROR: Unexpected API response format - missing key: {e}")
        print(f"   Response: {response.text if 'response' in locals() else 'No response'}")
        return "Received unexpected response from AI. Here are some great song recommendations!"
    except Exception as e:
        print(f"❌ ERROR: Unexpected error querying Cerebras: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return "Based on your mood, here are some great song recommendations from my collection!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        mood_input = data.get('mood', '')
        
        if not mood_input:
            return jsonify({'error': 'Please describe your mood'}), 400
        
        print(f"\n📝 Processing mood: '{mood_input}'")
        
        # Retrieve relevant songs using RAG
        relevant_docs = vectorstore.similarity_search(mood_input, k=5)
        print(f"🔍 Found {len(relevant_docs)} relevant songs")
        
        # Prepare context for LLM
        context = "\n\n".join([
            f"- {doc.metadata['title']} by {doc.metadata['artist']} (Mood: {doc.metadata['mood']}, Genre: {doc.metadata['genre']}): {doc.metadata['description']}"
            for doc in relevant_docs
        ])
        
        # Get LLM response
        llm_response = query_cerebras(mood_input, context)
        
        # Prepare song recommendations
        recommendations = [
            {
                'title': doc.metadata['title'],
                'artist': doc.metadata['artist'],
                'mood': doc.metadata['mood'],
                'genre': doc.metadata['genre'],
                'description': doc.metadata['description']
            }
            for doc in relevant_docs
        ]
        
        return jsonify({
            'recommendations': recommendations,
            'explanation': llm_response
        })
    
    except Exception as e:
        print(f"❌ Error in recommend endpoint: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    api_key = os.environ.get('CEREBRAS_API_KEY', '')
    api_key_status = 'configured' if api_key and api_key != 'your_api_key_here' else 'not_configured'
    
    return jsonify({
        'status': 'healthy',
        'cerebras_api': api_key_status,
        'message': 'AI recommendations enabled' if api_key_status == 'configured' else 'Using fallback responses (set CEREBRAS_API_KEY for AI recommendations)'
    })

# Vercel serverless function handler
def handler(request):
    with app.request_context(request.environ):
        return app.full_dispatch_request()
