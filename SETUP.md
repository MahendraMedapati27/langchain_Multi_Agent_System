# Setup Instructions

## Prerequisites
- Python 3.9 or higher
- pip package manager
- Groq API key (required, free tier available at https://console.groq.com)
- Optionally Google AI API key

## Installation Steps

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd langgraph-multi-agent-system
```

### 2. Create Virtual Environment
```bash
# On Linux/Mac
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your API keys
# REQUIRED: GROQ_API_KEY (get free API key at https://console.groq.com)
# OPTIONAL: GOOGLE_API_KEY, ANTHROPIC_API_KEY
```

### 5. Run the Application
```bash
# Linux/Mac
chmod +x run.sh
./run.sh

# Windows
run.bat

# Or directly
streamlit run app.py
```

### 6. Access the Application
Open your browser and navigate to:
http://localhost:8501

## Testing

Run tests to verify installation:
```bash
pytest tests/ -v
```

## Troubleshooting

### API Key Issues
- Ensure .env file is in project root
- Get your free Groq API key at https://console.groq.com
- Check that GROQ_API_KEY is set correctly
- Verify no extra spaces in .env file

### Import Errors
- Verify all dependencies are installed
- Check Python version (3.9+)
- Try reinstalling requirements

### Streamlit Issues
- Clear cache: streamlit cache clear
- Update Streamlit: pip install --upgrade streamlit
- Check port 8501 is not in use

## Need Help?
- Check logs in logs/ directory
- Enable verbose logging in sidebar
- Review error messages in terminal

