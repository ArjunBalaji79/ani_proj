# 🎵 MoodTunes - AI-Powered Music Recommendations

A RAG (Retrieval Augmented Generation) system that recommends songs based on your mood using AI.

## ✨ Features

- 🎯 **Smart Mood Analysis**: Understands natural language descriptions of your mood
- 🔍 **RAG System**: Uses vector embeddings and semantic search to find relevant songs
- 🤖 **AI-Powered**: Leverages Cerebras API with Llama 3.1 for personalized recommendations
- ⚡ **Fast & Smooth**: Optimized for quick responses
- 🎨 **Clean UI**: Simple, modern interface
- 📱 **Responsive**: Works on all devices

## 🛠 Tech Stack

- **Backend**: Flask (Python web framework)
- **RAG System**: LangChain + FAISS vector store
- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
- **LLM**: Cerebras API (Llama 3.1-8b - ultra fast!)
- **Deployment**: Vercel (serverless)
- **Database**: In-memory vector store with 25 curated songs

## 🚀 Quick Start

### Option 1: Using the start script (Recommended)
```bash
chmod +x start.sh
./start.sh
```

### Option 2: Manual setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

### Option 3: Direct run
```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 in your browser! 🎉

## 🔑 Optional: Add Cerebras API Key

For best AI-powered recommendations:

1. Get your API key from [cerebras.ai](https://cerebras.ai)
2. Set environment variable:
```bash
export CEREBRAS_API_KEY="your_key_here"
```
3. Or create a `.env` file:
```
CEREBRAS_API_KEY=your_key_here
```

**Note**: App works without API key but recommendations are more generic.

## Deploy to Vercel

1. Push your code to GitHub

2. Go to [Vercel](https://vercel.com) and import your repository

3. Add environment variable (optional):
   - Key: `CEREBRAS_API_KEY`
   - Value: Your Cerebras API key

4. Deploy!

## How It Works

1. **User Input**: User describes their mood in natural language
2. **Vector Search**: System uses embeddings to find semantically similar songs from the database
3. **LLM Enhancement**: Cerebras API generates personalized explanations
4. **Results**: User receives curated song recommendations with explanations

## Song Database

The system includes 25 songs across different moods:
- Happy & Energetic
- Sad & Melancholic
- Motivated & Powerful
- Nostalgic
- Anxious & Stressed
- And more...

## API Endpoints

- `GET /`: Main web interface
- `POST /api/recommend`: Get song recommendations
  - Body: `{"mood": "your mood description"}`
  - Response: `{"recommendations": [...], "explanation": "..."}`
- `GET /api/health`: Health check

## Notes

- The app works without Cerebras API key (uses fallback responses)
- For best results, add your Cerebras API key
- Song database can be easily expanded in `app.py`

## License

MIT

