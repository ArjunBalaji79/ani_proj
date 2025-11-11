#!/usr/bin/env python3
"""
Test the Llama component directly
"""

import os
import sys
from dotenv import load_dotenv

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Load environment variables
load_dotenv()

print("=" * 60)
print("🧪 Testing Llama Component")
print("=" * 60)

# Import the query function
from app import query_cerebras

# Test context
test_mood = "feeling happy and energetic"
test_context = """- Happy by Pharrell Williams (Mood: happy, joyful, energetic, Genre: Pop): An upbeat song that makes you want to dance and smile

- Don't Stop Me Now by Queen (Mood: happy, excited, euphoric, Genre: Rock): A high-energy anthem about feeling unstoppable

- Can't Stop the Feeling by Justin Timberlake (Mood: happy, energetic, excited, Genre: Pop): An irresistible dance song that lifts your spirits"""

print("\n📝 Test Input:")
print(f"   Mood: {test_mood}")
print(f"   Context: {len(test_context)} characters")

print("\n🤖 Calling query_cerebras()...")
print("-" * 60)

try:
    response = query_cerebras(test_mood, test_context)
    
    print("\n✅ Response Received:")
    print("-" * 60)
    print(response)
    print("-" * 60)
    
    # Check if it's a fallback response
    if "Based on your mood" in response and len(response) < 100:
        print("\n⚠️  This looks like a fallback response")
        print("   The API key might not be working properly")
    else:
        print("\n✅ SUCCESS! Llama component is working!")
        print(f"   Response length: {len(response)} characters")
        print("   This appears to be a genuine AI response")
        
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)

