# 💊 Medication Reminder App

Simple medication reminder app I built to help my grandma remember her pills. She was always forgetting when to take what, so I made this voice-enabled reminder system.

## What it does

- Ask questions like "what's my morning medicine?" 
- Speaks the medication list out loud
- Easy dropdown if you don't want to type
- Shows all your meds organized by time

## Setup

You'll need Python 3.7 or newer. Then:

```bash
pip install streamlit gtts pygame
streamlit run app.py
```

## How to use

1. Type a question or pick a time from dropdown
2. Click "Get My Medications" 
3. Listen to the voice reminder

The app understands questions like:
- "What should I take in the morning?"
- "What's my night medicine?"
- "Show me afternoon meds"

## Customizing medications

Edit the `medications.json` file to add your own medications:

```json
{
  "morning": [
    "Your morning medication",
    "Another morning med"
  ],
  "afternoon": [
    "Afternoon medication"
  ],
  "night": [
    "Evening medication"
  ]
}
```

## Tech stuff

- Built with Streamlit for the web interface
- Google Text-to-Speech for voice announcements  
- Pygame for audio playback
- JSON file for easy medication data management

## Note

This is just a reminder tool - always follow your doctor's instructions and don't use this as medical advice!