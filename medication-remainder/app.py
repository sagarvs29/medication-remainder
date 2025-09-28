"""
Medication Reminder App

Simple app to help elderly folks remember their medications.
Built this for my grandma who keeps forgetting her pills.

Setup:
- Need Python 3.7+
- Run: pip install streamlit gtts pygame
- Start with: streamlit run app.py

Features:
- Ask questions like "what's my morning medicine?"
- Voice announcements 
- Easy dropdown selection
"""

import streamlit as st
import json
from gtts import gTTS
import pygame
import os
import tempfile

# App config
st.set_page_config(
    page_title="Medication Reminder",
    page_icon="💊"
)

# Load meds from file
@st.cache_data
def load_meds():
    """Load medication data from JSON"""
    try:
        with open('medications.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Can't find medications.json file")
        return {}
    except:
        st.error("Problem reading medications file")
        return {}

def find_time_in_question(text):
    """
    Figure out what time they're asking about
    """
    text = text.lower()
    
    # Check for time keywords
    morning_words = ['morning', 'breakfast', 'am', 'dawn', 'early']
    afternoon_words = ['afternoon', 'lunch', 'noon', 'pm', 'midday'] 
    night_words = ['night', 'evening', 'dinner', 'bed', 'sleep', 'bedtime']
    
    # Look for matches
    if any(word in text for word in morning_words):
        return 'morning'
    elif any(word in text for word in afternoon_words):
        return 'afternoon'
    elif any(word in text for word in night_words):
        return 'night'
    
    return None

def speak_meds(message):
    """
    Text to speech for medication reminders
    """
    audio_file = None
    try:
        # Start pygame
        pygame.mixer.init()
        
        # Make temp file for audio
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        audio_file = temp_file.name
        temp_file.close()
        
        # Generate speech
        tts = gTTS(text=message, lang='en')
        tts.save(audio_file)
        
        # Play the audio
        if os.path.exists(audio_file):
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            
            # Wait for it to finish
            while pygame.mixer.music.get_busy():
                pygame.time.wait(50)
        
    except Exception as e:
        st.error(f"Couldn't play audio: {e}")
    finally:
        # Clean up
        if audio_file and os.path.exists(audio_file):
            try:
                os.remove(audio_file)
            except:
                pass
        try:
            pygame.mixer.quit()
        except:
            pass


def main():
    """Run the app"""
    
    # Title
    st.title("💊 Medication Reminder")
    st.markdown("---")
    
    # Get medication data
    meds_data = load_meds()
    
    if not meds_data:
        st.stop()
    
    # Two columns for input
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Question input
        st.subheader("Ask about your meds:")
        question = st.text_input(
            "Type your question:",
            placeholder="What's my morning medicine?",
            help="Ask things like 'what should I take at night?'"
        )
    
    with col2:
        # Time picker
        st.subheader("Or pick time:")
        time_choices = ["Choose...", "morning", "afternoon", "night"]
        picked_time = st.selectbox(
            "Time:",
            time_choices
        )
    
    # Get meds button
    st.markdown("---")
    if st.button("Get My Medications", type="primary", use_container_width=True):
        
        # Figure out what time they want
        time_period = None
        
        # Check the question first
        if question:
            time_period = find_time_in_question(question)
        
        # If nothing found, use dropdown
        if not time_period and picked_time != "Choose...":
            time_period = picked_time
        
        # Show results
        if time_period and time_period in meds_data:
            meds = meds_data[time_period]
            
            # Show the medications
            st.success(f"📋 {time_period.title()} Medications:")
            
            # List them out
            for i, med in enumerate(meds, 1):
                st.write(f"{i}. **{med}**")
            
            # Create voice message
            voice_msg = f"Time for your {time_period} medications: "
            voice_msg += ", ".join(meds)
            voice_msg += ". Don't forget to take them!"
            
            # Play audio reminder
            st.markdown("---")
            st.info("🔊 Playing reminder...")
            speak_meds(voice_msg)
            st.success("Done!")
            
        elif time_period:
            st.error(f"No {time_period} meds found")
        else:
            st.warning("Please ask about a specific time or use the dropdown")
            st.info("Try: 'What's my morning medicine?' or pick from the dropdown")
    
    # Side panel info
    with st.sidebar:
        st.header("Your Meds")
        for time_slot in meds_data.keys():
            count = len(meds_data[time_slot])
            st.write(f"• {time_slot.title()}: {count} items")
        
        st.markdown("---")
        st.header("How to use")
        st.write("1. Ask a question or pick time")
        st.write("2. Click the button")
        st.write("3. Listen to reminder")
        
        st.markdown("---")
        st.caption("Always follow your doctor's instructions")

if __name__ == "__main__":
    main()