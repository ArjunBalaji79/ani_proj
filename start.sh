#!/bin/bash

echo "🎵 Starting MoodTunes RAG System..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Starting Flask server..."
echo "Open http://localhost:5000 in your browser"
echo ""

# Run the app
python app.py

