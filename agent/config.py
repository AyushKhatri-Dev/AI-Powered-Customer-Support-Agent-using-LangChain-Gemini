# config.py
# Real Estate Chatbot Configuration with LangChain

import os

# ========================================
# GEMINI API CONFIGURATION
# ========================================

GEMINI_API_KEY = "AIzaSyD9EojNt0eFLtbe0KQod0waLFpSZtumzpA"

# ========================================
# MODEL SETTINGS
# ========================================

MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.2
MAX_OUTPUT_TOKENS = 500
TOP_P = 0.95
TOP_K = 40

# ========================================
# KNOWLEDGE BASE CONFIGURATION
# ========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_BASE_PATH = os.path.join(BASE_DIR, "knowledge_base.json")
LOAD_FULL_KNOWLEDGE_BASE = True

# ========================================
# LANGCHAIN MEMORY SETTINGS
# ========================================

MEMORY_KEY = "history"
MAX_MEMORY_MESSAGES = 10
MEMORY_RETURN_MESSAGES = True
MEMORY_TYPE = "buffer"

# ========================================
# LANGCHAIN CHAIN SETTINGS
# ========================================

CHAIN_TYPE = "stuff"
VERBOSE = False

# ========================================
# RESPONSE MODE CONFIGURATION
# ========================================

RESPONSE_MODE = "hybrid"

STRICT_KEYWORDS = [
    "price", "cost", "pricing", "amount", "rupees", "lakhs", "crores",
    "size", "area", "sqft", "square",
    "bhk", "bedroom", "configuration",
    "rera", "legal", "approval", "registration",
    "payment", "booking", "emi", "installment",
    "possession", "delivery", "handover", "date",
    "contact", "phone", "email", "address", "office",
    "project", "skyline", "heights", "villas"
]

ALLOW_GENERAL_KNOWLEDGE = True
GENERAL_KNOWLEDGE_DISCLAIMER = "\n\n💡 Note: This is general information. For specific property details, contact our team."

# ========================================
# PROMPT TEMPLATES
# ========================================

SYSTEM_INSTRUCTION = """You are a professional customer support AI agent for Skyline Residences, a premium real estate company in Noida.

YOUR ROLE:
- Answer customer queries about properties, pricing, amenities accurately
- Be polite, helpful, and professional
- Provide precise information from the knowledge base
- Admit when you don't know something rather than guessing
- Keep responses concise (2-4 sentences typically)
- Match the customer's language (Hindi/English)

IMPORTANT GUIDELINES:
1. For prices, sizes, RERA numbers, contact info - use ONLY knowledge base
2. If specific info not available, say: "I don't have that information. Let me connect you with our sales team."
3. Always cite project names (Skyline Heights/Villas) when discussing properties
4. For general real estate questions, you can use general knowledge with a disclaimer

PERSONALITY: Friendly, professional, helpful, honest"""

PROMPT_TEMPLATE = """You are the Skyline Residences AI assistant.

KNOWLEDGE BASE (Use this to answer questions):
{context}

CONVERSATION HISTORY:
{history}

CURRENT QUESTION: {input}

Instructions:
- Answer based on knowledge base for property-specific questions
- For general real estate queries, you can use general knowledge but add disclaimer
- Be concise and helpful
- If unsure, admit it and offer human assistance

YOUR RESPONSE:"""

# ========================================
# USER INTERFACE SETTINGS
# ========================================

GREETING_MESSAGE = """
🏠 Welcome to Skyline Residences AI Assistant!

I can help you with:
✅ Property details (Skyline Heights & Skyline Villas)  
✅ Pricing, sizes, and configurations
✅ Amenities and features
✅ Site visit bookings
✅ Payment plans and offers
✅ RERA and legal information

Type your question or 'quit' to exit.

How may I assist you today?
"""

EXIT_KEYWORDS = ["quit", "exit", "bye", "goodbye", "close", "stop"]
SHOW_TYPING_INDICATOR = True
USE_EMOJIS = True

# ========================================
# ERROR HANDLING
# ========================================

ERROR_MESSAGES = {
    "api_error": "⚠️ I'm having trouble connecting right now. Please try again in a moment.",
    "knowledge_base_not_found": "❌ Error: Knowledge base file not found. Please check the file location.",
    "json_parse_error": "❌ Error: Knowledge base file is corrupted or invalid JSON format.",
    "no_answer": "I don't have specific information about that. Would you like me to connect you with our sales team?\n📞 Call: +91-9876543210",
    "invalid_input": "I didn't quite understand that. Could you rephrase your question?",
}

FALLBACK_RESPONSE = "I apologize for the technical difficulty. Please contact our team at +91-9876543210."

# ========================================
# LOGGING
# ========================================

ENABLE_LOGGING = True
LOG_FILE_PATH = "chatbot_logs.txt"
LOG_LEVEL = "INFO"
LOG_USER_QUERIES = True
LOG_BOT_RESPONSES = True