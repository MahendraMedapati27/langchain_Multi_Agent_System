# API Keys Setup Guide

## Quick Answer: What API Keys Do You Need?

### ✅ **Minimum Setup (Recommended for Free Tier)**
**Only ONE API key needed:**
- `GROQ_API_KEY` - **REQUIRED** ✅

**That's it!** The app will run with just the Groq API key.

### 📋 Full API Keys Overview

| API Key | Required? | Used By | Purpose |
|---------|-----------|---------|---------|
| `GROQ_API_KEY` | ✅ **YES** | All agents by default | Primary LLM provider (Free tier available) |
| `GOOGLE_API_KEY` | ❌ No | Optional (if you want Google models) | Alternative fast model provider |
| `ANTHROPIC_API_KEY` | ❌ No | Not used by default | Not needed for basic functionality |

## Setup Instructions

### Minimum Setup (Groq Only)

1. **Get your free Groq API key:**
   - Visit: https://console.groq.com
   - Sign up (free)
   - Create an API key
   - Copy the key

2. **Create `.env` file:**
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

That's all you need! ✅

### Full Setup (Optional - Multiple Providers)

If you want to use Google models for faster responses:

1. **Get Google API key** (optional):
   - Visit: https://makersuite.google.com/app/apikey
   - Create an API key

2. **Update `.env` file:**
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here  # Optional
   ```

3. **Update agents to use Google** (if desired):
   - Edit `agents/research_agents.py`, `agents/analysis_agents.py`
   - Change `use_google=False` to `use_google=True`

## Current Configuration

All agents are now configured to use **Groq by default**:
- ✅ ResearchAgent → Uses Groq
- ✅ DataCollectorAgent → Uses Groq
- ✅ AnalystAgent → Uses Groq
- ✅ WriterAgent → Uses Groq
- ✅ EditorAgent → Uses Groq
- ✅ SentimentAnalyzer → Uses Groq
- ✅ Single Agent Workflow → Uses Groq

## Model Information

### Groq Models (Free Tier)
- **Default**: `llama-3.3-70b-versatile` (high quality)
- **Fast**: `llama-3.1-8b-instant` (quick responses)

### Google Models (Optional)
- **Fast**: `gemini-2.0-flash-exp` (if GOOGLE_API_KEY is provided)

## FAQ

### Q: Do I need Google API key?
**A:** No! The app runs perfectly with just `GROQ_API_KEY`. Google API key is optional and only needed if you want to use Google's models.

### Q: Do I need Anthropic API key?
**A:** No! It's not used by any agents in the current setup.

### Q: Why is only Groq required?
**A:** All agents have been configured to use Groq by default (`use_google=False`). Groq offers a generous free tier, making it perfect for development and testing.

### Q: Can I use only Google API key?
**A:** No. The app requires `GROQ_API_KEY` as it's the primary provider. If you want to use Google, you'd need both keys and then configure agents to use Google.

### Q: How do I switch back to Google for some agents?
**A:** Edit the agent files and change `use_google=False` to `use_google=True`, then add `GOOGLE_API_KEY` to your `.env` file.

## Summary

**Minimum Required:**
```
GROQ_API_KEY=your_key_here
```

**That's it!** The app is ready to run. 🚀

---

**Last Updated**: After migration to Groq
**Status**: ✅ All agents use Groq by default

