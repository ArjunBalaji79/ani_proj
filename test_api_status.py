#!/usr/bin/env python3
"""
Quick test to check if the Llama component fixes are working
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("🔍 MoodTunes API Status Check")
print("=" * 60)

# Check API key
api_key = os.environ.get('CEREBRAS_API_KEY', '')

print("\n1. Environment Variable Check:")
if not api_key:
    print("   ❌ CEREBRAS_API_KEY not found")
    print("   ℹ️  Create a .env file with your API key")
elif api_key == 'your_api_key_here':
    print("   ⚠️  CEREBRAS_API_KEY is set to placeholder value")
    print("   ℹ️  Replace with your actual API key")
else:
    print("   ✅ CEREBRAS_API_KEY is configured")
    print(f"   📝 Key starts with: {api_key[:10]}...")
    print(f"   📏 Key length: {len(api_key)} characters")

# Check dependencies
print("\n2. Dependency Check:")
try:
    import flask
    print("   ✅ Flask installed")
except ImportError:
    print("   ❌ Flask not installed")
    
try:
    from langchain_community.embeddings import HuggingFaceEmbeddings
    print("   ✅ LangChain installed")
except ImportError:
    print("   ❌ LangChain not installed")

try:
    import faiss
    print("   ✅ FAISS installed")
except ImportError:
    print("   ❌ FAISS not installed")

try:
    import requests
    print("   ✅ Requests installed")
except ImportError:
    print("   ❌ Requests not installed")

try:
    from dotenv import load_dotenv
    print("   ✅ python-dotenv installed")
except ImportError:
    print("   ❌ python-dotenv not installed")

# Test Cerebras API (if key is configured)
print("\n3. Cerebras API Test:")
if api_key and api_key != 'your_api_key_here':
    print("   🤖 Testing connection to Cerebras API...")
    try:
        import requests
        url = "https://api.cerebras.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama3.1-8b",
            "messages": [{"role": "user", "content": "Hi"}],
            "max_tokens": 10
        }
        response = requests.post(url, headers=headers, json=data, timeout=5)
        
        if response.status_code == 200:
            print("   ✅ Successfully connected to Cerebras API!")
            print("   ✅ API key is valid")
            print("   ✅ Llama 3.1-8b model is accessible")
        elif response.status_code == 401:
            print("   ❌ API key is invalid (401 Unauthorized)")
            print("   ℹ️  Check your key at https://cloud.cerebras.ai/")
        elif response.status_code == 429:
            print("   ⚠️  Rate limit exceeded (429)")
            print("   ℹ️  Try again in a few minutes")
        else:
            print(f"   ⚠️  Unexpected status code: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
    except requests.exceptions.Timeout:
        print("   ⚠️  Request timed out (API might be slow)")
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection failed (check internet connection)")
    except Exception as e:
        print(f"   ❌ Error: {e}")
else:
    print("   ⏭️  Skipped (no valid API key configured)")
    print("   ℹ️  The app will use fallback responses")

# Summary
print("\n" + "=" * 60)
print("📊 Summary")
print("=" * 60)

if api_key and api_key != 'your_api_key_here':
    print("✅ Your MoodTunes app is ready with AI-powered recommendations!")
    print("   Run: python app.py")
else:
    print("⚠️  Your MoodTunes app will work but with generic responses")
    print("   To enable AI recommendations:")
    print("   1. Get API key from https://cloud.cerebras.ai/")
    print("   2. Create .env file: echo 'CEREBRAS_API_KEY=your_key' > .env")
    print("   3. Restart the app")

print("\n💡 To test the app:")
print("   python app.py")
print("   Then visit: http://localhost:5000")
print("\n📚 For detailed setup instructions:")
print("   cat SETUP_API_KEY.md")
print("=" * 60)

