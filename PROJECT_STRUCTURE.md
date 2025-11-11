# Project Structure

```
ani_proj/
│
├── api/                          # Vercel serverless functions
│   ├── __init__.py              # Python package marker
│   └── index.py                 # Main API handler for Vercel
│
├── templates/                    # Flask HTML templates
│   └── index.html               # Frontend UI
│
├── static/                       # Static files (CSS, JS, images)
│
├── app.py                        # Main Flask application (for local dev)
├── requirements.txt              # Python dependencies
├── vercel.json                   # Vercel deployment config
├── start.sh                      # Quick start script
│
├── README.md                     # Main documentation
├── DEPLOYMENT.md                 # Deployment guide
├── PROJECT_STRUCTURE.md          # This file
│
├── .gitignore                    # Git ignore rules
└── .env.example                  # Environment variable template

```

## File Descriptions

### Core Application Files

- **`app.py`**: Main Flask application for local development
  - Initializes Flask server
  - Sets up RAG system with vector store
  - Defines API endpoints
  - Handles song recommendations

- **`api/index.py`**: Vercel-optimized version of app.py
  - Same functionality as app.py
  - Configured for serverless deployment
  - Used by Vercel in production

### Frontend

- **`templates/index.html`**: Single-page web interface
  - Clean, modern UI with gradient design
  - Mood input textarea
  - Example mood buttons
  - Results display with song cards
  - Fully responsive

### Configuration

- **`requirements.txt`**: Python package dependencies
  - Flask (web framework)
  - LangChain (RAG orchestration)
  - sentence-transformers (embeddings)
  - FAISS (vector store)
  - requests (API calls)

- **`vercel.json`**: Vercel deployment configuration
  - Specifies Python runtime
  - Routes all requests to api/index.py
  - Serverless function settings

- **`.gitignore`**: Files to exclude from Git
  - Python cache files
  - Virtual environments
  - Environment variables
  - IDE files

## Key Components

### RAG System Architecture

1. **Song Database** (in-memory)
   - 25 curated songs with metadata
   - Each song has: title, artist, mood tags, genre, description

2. **Vector Store** (FAISS)
   - Converts songs to vector embeddings
   - Enables semantic similarity search
   - Fast retrieval of relevant songs

3. **Embeddings Model** (sentence-transformers)
   - Model: all-MiniLM-L6-v2
   - Lightweight and fast
   - Good balance of accuracy and performance

4. **LLM Integration** (Cerebras API)
   - Uses Llama 3.1-8b model
   - Generates personalized explanations
   - Falls back gracefully without API key

### API Endpoints

- `GET /`: Serve the main web interface
- `POST /api/recommend`: Get song recommendations
  - Input: `{"mood": "user mood description"}`
  - Output: `{"recommendations": [...], "explanation": "..."}`
- `GET /api/health`: Health check endpoint

## Data Flow

```
User Input (Mood Description)
    ↓
Vector Embedding
    ↓
Similarity Search in FAISS
    ↓
Retrieve Top 5 Songs
    ↓
Send to Cerebras LLM (optional)
    ↓
Generate Personalized Explanation
    ↓
Return Results to User
```

## Development vs Production

### Local Development
- Uses `app.py`
- Run with `python app.py`
- Full logging and debug mode
- Hot reload enabled

### Production (Vercel)
- Uses `api/index.py`
- Serverless deployment
- Automatic scaling
- Cold start optimization

## Extending the System

### Add More Songs
Edit the `SONGS_DATA` list in `app.py` or `api/index.py`:
```python
{"title": "Song Name", "artist": "Artist Name", 
 "mood": "mood tags", "genre": "Genre", 
 "description": "Description"}
```

### Change Embedding Model
Modify the `HuggingFaceEmbeddings` initialization:
```python
embeddings = HuggingFaceEmbeddings(
    model_name="your-model-name"
)
```

### Adjust Number of Recommendations
Change the `k` parameter in similarity search:
```python
relevant_docs = vectorstore.similarity_search(mood_input, k=10)
```

### Customize UI
Edit `templates/index.html` - all styling is inline CSS.

