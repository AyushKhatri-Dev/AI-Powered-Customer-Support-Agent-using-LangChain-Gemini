import json
import os
import sys

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from config import *


def load_knowledge_base():
    """
    Load knowledge base from JSON file

    Returns:
       dict: Knowledge base as Python dictionary
       None: If file not found or error
    """

    try:
        if not os.path.exists(KNOWLEDGE_BASE_PATH):
            print(ERROR_MESSAGES["knowledge_base_not_found"])
            return None

        with open(KNOWLEDGE_BASE_PATH, 'r', encoding='utf-8') as file:
            knowledge_base = json.load(file)

        if not knowledge_base:
            print("⚠️ Warning: Knowledge base is empty!")
            return None

        print("✅ Knowledge base loaded successfully!")
        return knowledge_base

    except json.JSONDecodeError as e:
        print(ERROR_MESSAGES["json_parse_error"])
        print(f"Error details: {e}")
        return None

    except Exception as e:
        print(f"❌ Unexpected error loading knowledge base: {e}")
        return None


def format_knowledge_base(kb):
    """
    Convert knowledge base dict to readable text format
    
    Args:
        kb (dict): Knowledge base dictionary
    
    Returns:
        str: Formatted text for LLM context
    """
    
    context = "SKYLINE RESIDENCES - KNOWLEDGE BASE\n\n"
    
    # Company Info Section
    if "company_info" in kb:
        context += "=== COMPANY INFORMATION ===\n"
        company = kb["company_info"]
        context += f"Name: {company.get('name', 'N/A')}\n"
        context += f"Tagline: {company.get('tagline', 'N/A')}\n"
        context += f"Experience: {company.get('years_of_experience', 'N/A')} years\n"
        context += f"About: {company.get('about', 'N/A')}\n\n"
    
    # Projects Section
    if "projects" in kb:
        context += "=== AVAILABLE PROJECTS ===\n"
        for project in kb["projects"]:
            context += f"\nProject: {project.get('name', 'N/A')}\n"
            context += f"Type: {project.get('type', 'N/A')}\n"
            context += f"Location: {project.get('location', 'N/A')}\n"
            context += f"Configurations: {', '.join(project.get('configurations', []))}\n"
            
            # Pricing
            if "price_range" in project:
                context += "Pricing:\n"
                for config, price in project["price_range"].items():
                    context += f"  {config}: {price}\n"
            
            # Sizes
            if "sizes" in project:
                context += "Sizes:\n"
                for config, size in project["sizes"].items():
                    context += f"  {config}: {size}\n"
            
            context += f"RERA: {project.get('rera_number', 'N/A')}\n"
            context += f"Possession: {project.get('possession_date', 'N/A')}\n"
            context += f"Status: {project.get('status', 'N/A')}\n"
    
    # Amenities Section
    if "amenities" in kb:
        context += "\n=== AMENITIES ===\n"
        if "common" in kb["amenities"]:
            context += "Common Amenities: " + ", ".join(kb["amenities"]["common"]) + "\n"
        if "premium_villas_only" in kb["amenities"]:
            context += "Premium (Villas Only): " + ", ".join(kb["amenities"]["premium_villas_only"]) + "\n"
    
    # Pricing Info
    if "pricing_info" in kb:
        context += "\n=== PRICING & PAYMENT ===\n"
        pricing = kb["pricing_info"]
        context += f"Booking Amount: {pricing.get('booking_amount', 'N/A')}\n"
        context += f"Home Loan: {pricing.get('home_loan_assistance', 'N/A')}\n"
        context += f"Special Offers: {pricing.get('special_offers', 'N/A')}\n"
    
    # FAQs Section
    if "faqs" in kb:
        context += "\n=== FREQUENTLY ASKED QUESTIONS ===\n"
        for faq in kb["faqs"]:
            context += f"\nQ: {faq.get('question', 'N/A')}\n"
            context += f"A: {faq.get('answer', 'N/A')}\n"
    
    # Contact Info
    if "contact_info" in kb:
        context += "\n=== CONTACT INFORMATION ===\n"
        contact = kb["contact_info"]
        context += f"Phone: {contact.get('phone', 'N/A')}\n"
        context += f"Email: {contact.get('email', 'N/A')}\n"
        context += f"Office: {contact.get('office_address', 'N/A')}\n"
        context += f"Hours: {contact.get('working_hours', 'N/A')}\n"
    
    return context


def initialize_chatbot(knowledge_base_text):
    """
    Initialize LangChain components:
    - LLM (Gemini)
    - Memory (Conversation history)
    - Prompt Template
    - Chain (Everything connected)
    
    Args:
        knowledge_base_text (str): Formatted knowledge base
    
    Returns:
        ConversationChain: Ready chatbot chain
    """

    print("\n🔧 Initializing chatbot components...")

    # Step 1: Initialize Gemini LLM
    print("  ↳ Setting up Gemini AI...")
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=GEMINI_API_KEY,
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUT_TOKENS,
        top_p=TOP_P,
        top_k=TOP_K
    )

    # Step 2: Create Conversation Memory
    print("  ↳ Creating conversation memory...")
    memory = ConversationBufferMemory(
        memory_key=MEMORY_KEY,
        return_messages=MEMORY_RETURN_MESSAGES,
        ai_prefix="AI Assistant",
        human_prefix="Customer"
    )

    # Step 3: Create Prompt Template
    print("  ↳ Building prompt template...")
    
    # Insert knowledge base into template
    full_prompt = PROMPT_TEMPLATE.replace("{context}", knowledge_base_text)

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=full_prompt
    )

    # Step 4: Create the Conversation Chain
    print("  ↳ Connecting all components...")
    chain = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt,
        verbose=VERBOSE
    )

    print("✅ Chatbot initialized successfully!\n")
    return chain

    
def chat_loop(chain):
    """
    Main interactive chat loop
    
    Args:
        chain: LangChain ConversationChain
    """
    
    print(GREETING_MESSAGE)
    print("=" * 60)
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Check for exit keywords
            if user_input.lower() in EXIT_KEYWORDS:
                print("\n👋 Thank you for contacting Skyline Residences! Have a great day!")
                break
            
            # Skip empty input
            if not user_input:
                print("⚠️ Please enter a question!")
                continue
            
            # Show typing indicator (optional)
            if SHOW_TYPING_INDICATOR:
                print("\n🤖 AI Assistant is typing...")
            
            # Get response from chain
            response = chain.predict(input=user_input)
            
            # Display response
            print(f"\n🤖 AI Assistant: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print(FALLBACK_RESPONSE)
            if VERBOSE:
                import traceback
                traceback.print_exc()


def main():
    """
    Main function to run the chatbot
    """
    
    print("\n" + "=" * 60)
    print("  SKYLINE RESIDENCES - AI CUSTOMER SUPPORT")
    print("=" * 60)
    
    # Step 1: Load knowledge base
    print("\n📂 Loading knowledge base...")
    knowledge_base = load_knowledge_base()
    
    if knowledge_base is None:
        print("❌ Cannot start chatbot without knowledge base. Exiting...")
        sys.exit(1)
    
    # Step 2: Format knowledge base for LLM
    print("📝 Formatting knowledge base for AI...")
    kb_text = format_knowledge_base(knowledge_base)
    
    # Step 3: Initialize chatbot
    chatbot_chain = initialize_chatbot(kb_text)
    
    # Step 4: Start chat loop
    chat_loop(chatbot_chain)
    
    print("\n" + "=" * 60)
    print("  Session ended. Thank you!")
    print("=" * 60)


# Run the chatbot
if __name__ == "__main__":
    main()