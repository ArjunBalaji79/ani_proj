# ⚡ Quick Start Guide

## For the Impatient

```bash
# Clone the repo
git clone <your-repo-url>
cd ani_proj

# Run it
chmod +x start.sh
./start.sh
```

Open http://localhost:5000 and you're done! 🎉

## What Just Happened?

The `start.sh` script:
1. ✅ Created a Python virtual environment
2. ✅ Installed all dependencies
3. ✅ Started the Flask server
4. ✅ Opened your app at localhost:5000

## Deploy to Vercel in 2 Minutes

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "MoodTunes RAG system"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 2: Deploy on Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repo
4. Click "Deploy"

Done! ✨

### Step 3 (Optional): Add API Key
1. In Vercel project settings
2. Environment Variables
3. Add: `CEREBRAS_API_KEY` = `your_key`
4. Redeploy

## Testing the App

### Try These Moods:

**Happy vibes** 😊
```
"I'm feeling super happy and want to dance!"
```

**Sad feels** 😢
```
"Feeling down and need some comfort music"
```

**Workout mode** 💪
```
"Need motivation for my workout!"
```

**Chill time** 😌
```
"Just want to relax and unwind"
```

**Party mode** 🎉
```
"Getting ready to party all night!"
```

## Common Issues

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Port 5000 already in use"
Edit `app.py` and change:
```python
app.run(debug=True, port=5001)  # Use different port
```

### "Import error: sentence-transformers"
```bash
pip install sentence-transformers
```

### Slow first load
This is normal! The app needs to:
- Load the embedding model
- Create the vector store
- Initialize everything

Subsequent requests will be fast ⚡

## File Structure (The Important Bits)

```
ani_proj/
├── app.py              ← Main app (run this)
├── api/index.py        ← For Vercel
├── templates/index.html ← The UI
├── requirements.txt    ← Dependencies
└── vercel.json         ← Deploy config
```

## Customize It

### Add More Songs
Edit `app.py`, find `SONGS_DATA = [...]`, add your songs:
```python
{"title": "Your Song", "artist": "Artist Name", 
 "mood": "happy, energetic", "genre": "Pop",
 "description": "Why this song is great"}
```

### Change Colors
Edit `templates/index.html`, find the `<style>` section:
```css
background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
```

### Get More Recommendations
Edit `app.py`, change `k=5` to `k=10`:
```python
relevant_docs = vectorstore.similarity_search(mood_input, k=10)
```

## Need Help?

Check out:
- `README.md` - Full documentation
- `FEATURES.md` - Feature details
- `DEPLOYMENT.md` - Deployment guide
- `PROJECT_STRUCTURE.md` - Code structure

## Pro Tips

1. **Faster Development**: Use `Flask-Cors` for API testing
2. **Better Recommendations**: Get a Cerebras API key (it's free!)
3. **More Songs**: The more songs in the database, the better the matches
4. **Test Locally**: Always test before deploying
5. **Check Logs**: Use `print()` statements to debug

## Next Steps

1. ✅ Get it running locally
2. ✅ Test with different moods
3. ✅ Deploy to Vercel
4. ✅ Share with friends!
5. 🎯 Add more songs
6. 🎯 Get Cerebras API key
7. 🎯 Customize the UI
8. 🎯 Add new features

## One-Liners

**Install everything:**
```bash
pip install Flask flask-cors langchain langchain-community sentence-transformers faiss-cpu requests
```

**Run the app:**
```bash
python app.py
```

**Deploy to Vercel:**
```bash
vercel
```

That's it! Happy coding! 🚀

