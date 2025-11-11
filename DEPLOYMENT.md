# Deployment Guide

## Quick Deploy to Vercel

### Option 1: Deploy from GitHub (Recommended)

1. **Push your code to GitHub**:
```bash
git init
git add .
git commit -m "Initial commit - MoodTunes RAG system"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. **Deploy on Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`
   - Click "Deploy"

3. **Add Environment Variable** (Optional but recommended):
   - Go to your project settings on Vercel
   - Navigate to "Environment Variables"
   - Add: `CEREBRAS_API_KEY` = `your_api_key_here`
   - Redeploy the project

### Option 2: Deploy with Vercel CLI

1. **Install Vercel CLI**:
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy**:
```bash
vercel
```

4. **Add environment variable**:
```bash
vercel env add CEREBRAS_API_KEY
```

## Getting Cerebras API Key

1. Go to [cerebras.ai](https://cerebras.ai)
2. Sign up for an account
3. Navigate to API settings
4. Generate a new API key
5. Add it to your Vercel environment variables

## Important Notes

- **First Load**: The first request might be slow due to cold start and model loading
- **Subsequent Requests**: Will be much faster
- **Without API Key**: The app will still work but with generic responses
- **With API Key**: You'll get personalized, AI-generated song recommendations

## Testing Locally

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Open http://localhost:5000
```

## Troubleshooting

### Build fails on Vercel
- Check that all dependencies are in `requirements.txt`
- Ensure Python version compatibility

### App is slow
- This is expected on first load (cold start)
- Consider upgrading to Vercel Pro for better performance

### Environment variables not working
- Make sure to redeploy after adding environment variables
- Check that the variable name matches exactly: `CEREBRAS_API_KEY`

## Alternative Deployment Options

If Vercel doesn't work well:

### Render.com
1. Go to [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`

### Railway.app
1. Go to [railway.app](https://railway.app)
2. Create a new project from GitHub repo
3. Railway will auto-detect Flask
4. Add environment variables in settings

### Heroku
1. Install Heroku CLI
2. Create `Procfile` with: `web: python app.py`
3. Deploy:
```bash
heroku create
git push heroku main
```

