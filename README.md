# 🏠 AI Real Estate Customer Support Agent

An intelligent customer support chatbot for real estate businesses, built using **Python**, **LangChain**, and **Google Gemini AI**. This project demonstrates how to build a production-ready AI assistant with conversation memory, knowledge base integration, and context-aware responses.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 🎯 Features

- ✅ **Conversational AI** - Natural language understanding with context retention
- ✅ **Knowledge Base Integration** - Answers from structured JSON data
- ✅ **Memory Management** - Remembers conversation history for contextual responses
- ✅ **Hybrid Response Mode** - Strict knowledge base answers for critical info, flexible for general queries
- ✅ **Multi-language Support** - Handles both English and Hindi queries
- ✅ **Error Handling** - Graceful fallbacks and informative error messages
- ✅ **Customizable** - Easy to adapt for any business domain

---

## 🏗️ Architecture
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│                  (Console / Streamlit)                   │
└─────────────────────┬───────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────┐
│                 LangChain Components                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │  Prompt      │  │  Memory      │  │  Chain       │ │
│  │  Template    │  │  Buffer      │  │  Logic       │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────┬───────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────┐
│              Google Gemini AI (LLM)                      │
└─────────────────────┬───────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────┐
│              Knowledge Base (JSON)                       │
│   • Company Info  • Projects  • Pricing  • FAQs         │
└─────────────────────────────────────────────────────────┘


---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Google Gemini API Key ([Get it here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/ai-real-estate-chatbot.git
   cd ai-real-estate-chatbot

2. Install dependencies

bash   pip install langchain langchain-google-genai google-generativeai

3. Configure API Key
Open agent/config.py and add your Gemini API key:

python   GEMINI_API_KEY = "your_api_key_here"

4. Run the chatbot

bash   cd agent
   python chatbot.py

💡 Usage Examples
Example 1: Property Inquiry
You: Tell me about 3BHK apartments
AI: Skyline Heights offers 3BHK apartments ranging from ₹85 Lakhs to ₹1.05 Crores. 
    The sizes range from 1650-1850 sq.ft, located in Sector 137, Noida Expressway.

🎨 Customization
Adding Your Own Knowledge Base
Edit agent/knowledge_base.json:
json{
  "company_info": {
    "name": "Your Company",
    "tagline": "Your Tagline"
  },
  "projects": [
    {
      "name": "Your Project",
      "type": "Apartments",
      "price_range": {...}
    }
  ],
  "faqs": [...]
}


🔮 Future Enhancements

 Streamlit UI - Web-based interface
 RAG (Retrieval Augmented Generation) - Vector database integration
 Multi-language - Full Hindi support
 Voice Integration - Speech-to-text capabilities
 Analytics Dashboard - Query tracking and insights
 CRM Integration - Lead management
 WhatsApp Bot - Deploy on messaging platforms
