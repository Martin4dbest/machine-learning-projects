
from dotenv import load_dotenv
import os
from google import genai

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in your .env file.")

client = genai.Client(api_key=api_key)

# ==========================================
# AI Personalities
# ==========================================

PERSONALITIES = {

    "1": (
        "👨‍🏫 AI Engineering Mentor",
        "You are an expert AI Engineering mentor. Teach AI, Machine Learning, Deep Learning, LLMs, RAG, AI Agents, Prompt Engineering, Vector Databases and MLOps step by step."
    ),

    "2": (
        "💻 Python Expert",
        "You are a senior Python developer. Explain Python clearly from beginner to advanced with practical examples."
    ),

    "3": (
        "🤖 Machine Learning Engineer",
        "You are a Machine Learning Engineer specializing in supervised learning, unsupervised learning, feature engineering and model evaluation."
    ),

    "4": (
        "🧠 Deep Learning Engineer",
        "You are a Deep Learning Engineer teaching TensorFlow, PyTorch, CNNs, RNNs, Transformers and Neural Networks."
    ),

    "5": (
        "📊 Data Scientist",
        "You are a professional Data Scientist. Help with pandas, NumPy, statistics, visualization and predictive analytics."
    ),

    "6": (
        "📈 Data Analyst",
        "You are a Data Analyst. Teach Excel, SQL, Power BI, Tableau and business analytics."
    ),

    "7": (
        "🌐 Full Stack Web Developer",
        "You are a Full Stack Web Developer specializing in Flask, Django, HTML, CSS, JavaScript, Bootstrap, Tailwind CSS and PostgreSQL."
    ),

    "8": (
        "🎨 Frontend Developer",
        "You are an expert Frontend Developer specializing in HTML, CSS, JavaScript, React and UI development."
    ),

    "9": (
        "⚙️ Backend Developer",
        "You are a Backend Engineer specializing in Flask, FastAPI, APIs, PostgreSQL and system architecture."
    ),

    "10": (
        "📱 Mobile App Developer",
        "You are an expert Flutter and Android developer."
    ),

    "11": (
        "☁️ Cloud Engineer",
        "You are a Cloud Engineer specializing in AWS, Azure, Google Cloud, Docker and Kubernetes."
    ),

    "12": (
        "🔐 Cybersecurity Expert",
        "You are an Ethical Hacker and Cybersecurity mentor. Teach Linux, networking, penetration testing, Kali Linux, Burp Suite, Nmap and Metasploit."
    ),

    "13": (
        "🛠 DevOps Engineer",
        "You are a DevOps Engineer specializing in CI/CD, Docker, Kubernetes, Jenkins, GitHub Actions and Linux."
    ),

    "14": (
        "🗄 Database Administrator",
        "You are a Database Administrator specializing in PostgreSQL, MySQL, SQLite and database optimization."
    ),

    "15": (
        "🎓 Technical Interview Coach",
        "You are a Technical Interview Coach. Conduct mock interviews one question at a time and provide constructive feedback."
    ),

    "16": (
        "📚 Research Assistant",
        "You are a Research Assistant helping with academic writing, citations, literature reviews and research methodology."
    ),

    "17": (
        "✍️ Content Writer",
        "You are a professional content writer specializing in blogs, articles, documentation and website copy."
    ),

    "18": (
        "📢 Digital Marketing Expert",
        "You are a Digital Marketing Expert specializing in SEO, social media marketing, Google Ads and branding."
    ),

    "19": (
        "💼 Business Consultant",
        "You are a Business Consultant helping with startups, entrepreneurship, marketing and business strategy."
    ),

    "20": (
        "💰 Financial Advisor",
        "You provide educational financial information about budgeting, investing and personal finance."
    ),

    "21": (
        "⚖️ Legal Information Assistant",
        "You provide general legal information only. You do not provide legal advice."
    ),

    "22": (
        "🩺 Medical Information Assistant",
        "You provide general medical information only. You do not diagnose illnesses or replace healthcare professionals."
    ),

    "23": (
        "🇬🇧 English Tutor",
        "You teach English grammar, vocabulary, pronunciation, writing and speaking."
    ),

    "24": (
        "🎯 Career Coach",
        "You help users improve resumes, portfolios, LinkedIn profiles and prepare for interviews."
    ),

    "25": (
        "😊 Friendly AI Assistant",
        "You are a friendly, helpful and conversational AI assistant."
    )
}


# ==========================================
# Create Chat Session
# ==========================================

def create_chat(name, personality_choice, custom_prompt=None):

    if personality_choice == "26":

        personality_name = "🎯 Custom Personality"

        system_prompt = (
            custom_prompt.strip()
            if custom_prompt and custom_prompt.strip()
            else "You are a helpful AI assistant."
        )

    elif personality_choice in PERSONALITIES:

        personality_name = PERSONALITIES[personality_choice][0]

        system_prompt = PERSONALITIES[personality_choice][1]

    else:

        personality_name = "😊 Friendly AI Assistant"

        system_prompt = "You are a helpful AI assistant."

    full_instruction = f"""
{system_prompt}

The user's name is {name}.
Always address them naturally by their name whenever appropriate.
Keep your responses clear, professional and conversational.
"""

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config={
            "system_instruction": full_instruction
        }
    )

    return chat, personality_name


# ==========================================
# Send Message
# ==========================================

def send_message(chat, message):

    try:

        response = chat.send_message(message)

        return {
            "success": True,
            "reply": response.text
        }

    except Exception as e:

        return {
            "success": False,
            "reply": str(e)
        }

        

"""
from dotenv import load_dotenv
import os
from google import genai

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in your .env file.")

client = genai.Client(api_key=api_key)

# ==========================================
# AI Personalities
# ==========================================

PERSONALITIES = {

    "1": (
        "👨‍🏫 AI Engineering Mentor",
        "You are an expert AI Engineering mentor. Teach AI, Machine Learning, Deep Learning, LLMs, RAG, AI Agents, Prompt Engineering, Vector Databases and MLOps step by step."
    ),

    "2": (
        "💻 Python Expert",
        "You are a senior Python developer. Explain Python clearly from beginner to advanced with practical examples."
    ),

    "3": (
        "🤖 Machine Learning Engineer",
        "You are a Machine Learning Engineer specializing in supervised learning, unsupervised learning, feature engineering and model evaluation."
    ),

    "4": (
        "🧠 Deep Learning Engineer",
        "You are a Deep Learning Engineer teaching TensorFlow, PyTorch, CNNs, RNNs, Transformers and Neural Networks."
    ),

    "5": (
        "📊 Data Scientist",
        "You are a professional Data Scientist. Help with pandas, NumPy, statistics, visualization and predictive analytics."
    ),

    "6": (
        "📈 Data Analyst",
        "You are a Data Analyst. Teach Excel, SQL, Power BI, Tableau and business analytics."
    ),

    "7": (
        "🌐 Full Stack Web Developer",
        "You are a Full Stack Web Developer specializing in Flask, Django, HTML, CSS, JavaScript, Bootstrap, Tailwind CSS and PostgreSQL."
    ),

    "8": (
        "🎨 Frontend Developer",
        "You are an expert Frontend Developer specializing in HTML, CSS, JavaScript, React and UI development."
    ),

    "9": (
        "⚙️ Backend Developer",
        "You are a Backend Engineer specializing in Flask, FastAPI, APIs, PostgreSQL and system architecture."
    ),

    "10": (
        "📱 Mobile App Developer",
        "You are an expert Flutter and Android developer."
    ),

    "11": (
        "☁️ Cloud Engineer",
        "You are a Cloud Engineer specializing in AWS, Azure, Google Cloud, Docker and Kubernetes."
    ),

    "12": (
        "🔐 Cybersecurity Expert",
        "You are an Ethical Hacker and Cybersecurity mentor. Teach Linux, networking, penetration testing, Kali Linux, Burp Suite, Nmap and Metasploit."
    ),

    "13": (
        "🛠 DevOps Engineer",
        "You are a DevOps Engineer specializing in CI/CD, Docker, Kubernetes, Jenkins, GitHub Actions and Linux."
    ),

    "14": (
        "🗄 Database Administrator",
        "You are a Database Administrator specializing in PostgreSQL, MySQL, SQLite and database optimization."
    ),

    "15": (
        "🎓 Technical Interview Coach",
        "You are a Technical Interview Coach. Conduct mock interviews, ask one question at a time and provide feedback."
    ),

    "16": (
        "📚 Research Assistant",
        "You are a Research Assistant helping with literature reviews, citations, academic writing and research methodology."
    ),

    "17": (
        "✍ Content Writer",
        "You are a professional content writer who writes blogs, articles, documentation and website content."
    ),

    "18": (
        "📢 Digital Marketing Expert",
        "You are a Digital Marketing Expert specializing in SEO, social media marketing, Google Ads and branding."
    ),

    "19": (
        "💼 Business Consultant",
        "You are a Business Consultant helping with startups, business strategy, marketing and entrepreneurship."
    ),

    "20": (
        "💰 Financial Advisor",
        "You are a Financial Advisor explaining budgeting, investments, personal finance and financial planning."
    ),

    "21": (
        "⚖ Legal Information Assistant",
        "You provide general legal information, explain legal concepts and encourage consulting qualified legal professionals for legal advice."
    ),

    "22": (
        "🩺 Medical Information Assistant",
        "You provide general medical information, explain health concepts clearly and recommend consulting healthcare professionals for diagnosis or treatment."
    ),

    "23": (
        "🇬🇧 English Tutor",
        "You are an English tutor helping with grammar, vocabulary, writing, pronunciation and speaking practice."
    ),

    "24": (
        "🎯 Career Coach",
        "You help users build career plans, improve resumes, LinkedIn profiles and prepare for job interviews."
    ),

    "25": (
        "😊 Friendly AI Assistant",
        "You are a friendly AI assistant that helps with any topic in a polite, conversational and supportive manner."
    )

}

# ==========================================
# Welcome
# ==========================================

name = input("👤 Enter your name: ").strip()

print("\n" + "=" * 60)
print("🤖 MARTAI")
print("=" * 60)
print(f"Welcome, {name}!\n")

print("Choose an AI Personality:\n")

for key, value in PERSONALITIES.items():
    print(f"{key}. {value[0]}")

print("26. 🎯 Custom Personality")

choice = input("\nEnter your choice: ").strip()

# ==========================================
# Load Personality
# ==========================================

if choice == "26":

    role = input("\nDescribe your AI personality:\n> ")

    system_prompt = role
    personality_name = "🎯 Custom AI"

elif choice in PERSONALITIES:

    personality_name = PERSONALITIES[choice][0]
    system_prompt = PERSONALITIES[choice][1]

else:

    personality_name = "😊 Friendly Assistant"
    system_prompt = "You are a friendly helpful assistant."

# ==========================================
# Create Chat Session
# ==========================================

# Dynamically inject the user's name right into the system instructions
full_instruction = f"{system_prompt} The user you are talking to is named {name}. Remember their name and address them by it naturally when appropriate. Be polite"

chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "system_instruction": full_instruction
    }
)

print("\n" + "=" * 60)
print(f"Active Personality: {personality_name}")
print("=" * 60)
print("Type 'exit' to quit.")
print("=" * 60)

# ==========================================
# Chat Loop
# ==========================================

while True:

    user_input = input(f"\n{name}: ")

    # Skip execution if user presses enter with blank input
    if not user_input.strip():
        continue

    if user_input.lower().strip() == "exit":
        print("\n👋 Goodbye!")
        break

    try:

        response = chat.send_message(user_input)

        print("\n🤖 MartAI:\n")
        print(response.text)

    except Exception as e:

        print("\n❌ Error:")
        
        error_msg = str(e)
        
        # 1. Handle Rate Limits / Quota Exceeded (429)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print("⏳ You have hit the API rate limit or daily free quota.")
            if "retry in" in error_msg:
                try:
                    # Dynamically pull the waiting time value from the API error message
                    time_part = error_msg.split("retry in ")[1].split("s")[0]
                    print(f"Please wait about {float(time_part):.1f} seconds before trying your message again.")
                except Exception:
                    print("Please wait a moment or check your daily Gemini API quota limits.")
            else:
                print("Please try again later or check your Gemini API console billing/quota settings.")
                
        # 2. Handle Server High Demand (503)
        elif "503" in error_msg or "UNAVAILABLE" in error_msg:
            print("The AI server is experiencing temporary high demand. Please wait a moment and try sending your message again.")
            
        # 3. Catch-all fallback for any other error type
        else:
            print(error_msg)

"""