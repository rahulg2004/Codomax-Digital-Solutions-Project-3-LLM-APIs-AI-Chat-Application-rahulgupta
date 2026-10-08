# 🤖 AI Chat Assistant using Google Gemini API

An intelligent conversational AI web application built with **Python, Google Gemini API, and Streamlit**. The application provides a user-friendly chat interface with conversational memory, custom system instructions, model parameter controls, secure API authentication, error handling, and basic API usage management.

This project was developed as part of **Module 3: LLM APIs & Application Development**, focusing on practical implementation of Large Language Model APIs and building a complete AI-powered application.

---

## 📌 Project Overview

The AI Chat Assistant is a web-based conversational application that connects to Google's Gemini Large Language Model through the Gemini API.

Users can interact with the AI through a simple chat interface while maintaining conversation context across multiple messages. The application also provides controls for modifying the AI's behaviour through system instructions, temperature, and maximum output tokens.

The project demonstrates how an LLM API can be integrated into a real-world Python application while following basic security, error handling, conversation management, and API usage practices.

---

## ✨ Key Features

### 💬 Conversational AI

- Real-time interaction with Google Gemini.
- Natural language question and answer system.
- User-friendly chat interface.
- Supports multiple consecutive conversations.

### 🧠 Conversation Memory

- Maintains previous messages during the active session.
- Sends relevant conversation history to the Gemini model.
- Allows the AI to understand context from previous messages.
- Supports multi-turn conversations.

### ⚙️ Custom System Instructions

Users can define how the AI should behave by entering a custom system instruction.

Examples:

- "You are a Python programming teacher."
- "Explain everything in simple language."
- "Act as a professional financial analyst."
- "Answer using concise bullet points."

### 🎛️ Model Parameter Controls

The application provides controls for:

- Temperature
- Maximum output tokens

Temperature can be adjusted to control the creativity and variation of responses.

Maximum output tokens can be adjusted to control the approximate response length and help manage API usage.

### 🔐 Secure API Authentication

The Gemini API key is not hardcoded into the application.

The project uses Streamlit Secrets for securely storing the API key.

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
````

The secrets file is excluded from Git using `.gitignore`.

### 🛡️ Error Handling

The application includes error handling for problems such as:

* Missing API key
* Invalid API credentials
* Gemini API errors
* Connection failures
* Unexpected model responses

Instead of crashing, the application displays a user-friendly error message.

### 🗑️ Clear Chat

Users can clear the current conversation and start a new session using the **Clear Chat** button.

### 📊 Basic API Usage Management

The application provides basic mechanisms for responsible API usage through:

* Maximum output token control
* Conversation history management
* Limited recent message context
* Clear chat functionality
* Controlled response generation

These features help prevent unnecessarily large requests and responses.

---

## 🛠️ Technologies Used

| Technology                | Purpose                            |
| ------------------------- | ---------------------------------- |
| Python                    | Core application development       |
| Google Gemini API         | Large Language Model integration   |
| Google GenAI SDK          | Communication with Gemini API      |
| Streamlit                 | Web application and user interface |
| Git                       | Version control                    |
| GitHub                    | Source code hosting                |
| Streamlit Community Cloud | Application deployment             |

---

## 🏗️ Application Architecture

The application follows a simple architecture:

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Streamlit UI      │
                    │                     │
                    │ Chat Input          │
                    │ Settings            │
                    │ Chat History        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Conversation        │
                    │ Management           │
                    │                     │
                    │ User Messages      │
                    │ Assistant Messages │
                    │ Chat History       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Google Gemini API   │
                    │                     │
                    │ System Instruction  │
                    │ Temperature         │
                    │ Max Tokens          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ AI Generated        │
                    │ Response            │
                    └─────────────────────┘
```

---

## 📂 Project Structure

```text
AI-Chat-Application/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
├── .streamlit/
│   └── secrets.toml
│
└── venv/
```

### File Description

#### `app.py`

Main Python application containing:

* Streamlit interface
* Gemini API connection
* Chat functionality
* Conversation management
* System instructions
* Model parameters
* Error handling

#### `requirements.txt`

Contains the Python dependencies required to run the application.

#### `README.md`

Project documentation, installation instructions, features, architecture, and usage information.

#### `.gitignore`

Prevents sensitive and unnecessary files from being uploaded to GitHub.

Important ignored files include:

```text
venv/
.streamlit/secrets.toml
.env
__pycache__/
*.pyc
```

#### `.streamlit/secrets.toml`

Stores the Gemini API key securely during local development.

This file must **never be uploaded to GitHub**.

---

# 🚀 Getting Started

## 1. Clone the Repository

Clone the project using Git:

```bash
git clone https://github.com/YOUR-USERNAME/AI-Chat-Application-Gemini-API.git
```

Move into the project directory:

```bash
cd AI-Chat-Application-Gemini-API
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

### Windows

Activate the environment:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# 🔑 API Key Configuration

This project requires a **Google Gemini API key**.

Create your API key through **Google AI Studio**.

After obtaining the API key, create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace:

```text
YOUR_GEMINI_API_KEY
```

with your actual API key.

### ⚠️ Security Warning

Never upload your API key to GitHub.

The following file is intentionally excluded through `.gitignore`:

```text
.streamlit/secrets.toml
```

Do not write the API key directly inside `app.py`.

---

# ▶️ Running the Application

After configuring the API key, run:

```bash
streamlit run app.py
```

Streamlit will start the application locally.

Open the displayed local URL in your browser.

The application will provide an interface similar to:

```text
🤖 AI Chat Assistant

Powered by Google Gemini API

-------------------------------------

Chat with the AI...

[ Type your message here ]

-------------------------------------

Sidebar:

⚙️ Settings

System Instruction
Temperature
Maximum Output Tokens

🗑️ Clear Chat
```

---

# 💬 How to Use

## Step 1: Enter a Message

Type a question or instruction into the chat input.

Example:

```text
Explain artificial intelligence in simple words.
```

The Gemini model will generate a response.

---

## Step 2: Continue the Conversation

Ask a follow-up question.

Example:

```text
Give me a real-world example.
```

The application maintains the previous messages, allowing the AI to understand the conversation context.

---

## Step 3: Customize AI Behaviour

Use the **System Instruction** field to change the AI's behaviour.

Example:

```text
You are an expert Python programming teacher.
Explain concepts using simple examples.
```

Then ask:

```text
Explain object-oriented programming.
```

The response will follow the provided instructions.

---

## Step 4: Adjust Temperature

Temperature controls the randomness and creativity of the generated response.

For example:

```text
0.1 → More predictable
0.7 → Balanced
1.2 → More creative
```

The exact behaviour can vary depending on the model and prompt.

---

## Step 5: Adjust Maximum Output Tokens

Maximum output tokens control the maximum amount of content the model can generate for a response.

Lower values can help keep responses short and reduce unnecessary API usage.

Higher values allow longer responses.

---

## Step 6: Clear the Conversation

Click:

```text
🗑️ Clear Chat
```

to remove the current conversation history and start a new session.

---

# 🧠 Conversation Management

The application stores messages during the active Streamlit session.

Messages are represented using roles such as:

```text
user
assistant
```

For example:

```text
User:
What is machine learning?

Assistant:
Machine learning is a branch of AI...
```

The conversation history is then provided to the model so that follow-up questions can be understood in context.

---

# ⚙️ Model Configuration

The application allows users to control important generation parameters.

### Temperature

Controls response randomness and creativity.

```text
Temperature = 0.0
```

Generally produces more deterministic responses.

```text
Temperature = 1.0
```

Allows more variation.

### Maximum Output Tokens

Controls the maximum length of the generated response.

Example:

```text
Maximum Output Tokens = 800
```

This helps control response size and API usage.

---

# 🛡️ Error Handling

The application uses exception handling to prevent the application from unexpectedly crashing.

Potential problems include:

### Missing API Key

The application displays an error when the Gemini API key is unavailable.

### Invalid API Key

Authentication errors are handled and displayed to the user.

### API Failure

If the Gemini service cannot be reached, the application displays an appropriate error message.

### Unexpected Response

Unexpected model or API behaviour is handled using error handling logic.

---

# 💰 Basic API Cost Management

LLM APIs can generate costs depending on usage and token consumption.

This project implements basic API usage management through:

* Maximum output token configuration
* Conversation history control
* Limiting unnecessary context
* Clear conversation functionality
* Controlled response generation

The application is designed to avoid sending unnecessary amounts of conversation history whenever possible.

> Note: Actual API pricing depends on the selected Gemini model, usage, account configuration, and Google's current pricing policies.

---

# 🔒 Security Practices

The project follows basic API security practices.

### API key is stored outside the source code

```text
.streamlit/secrets.toml
```

### Secret file is ignored by Git

```gitignore
.streamlit/secrets.toml
```

### Environment files are ignored

```gitignore
.env
```

### Virtual environment is ignored

```gitignore
venv/
```

### API credentials are never displayed in the application

Only the application uses the secret value to authenticate API requests.

---

# 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

## Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the repository.
5. Select the `main` branch.
6. Select `app.py`.
7. Deploy the application.
8. Add the Gemini API key under the application's Secrets settings.

Use:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Do not upload the API key to GitHub.

---

# 🧪 Testing

The application should be tested using different types of prompts.

### Test 1: General Question

```text
What is artificial intelligence?
```

### Test 2: Conversation Memory

```text
My favourite programming language is Python.
```

Followed by:

```text
What is my favourite programming language?
```

### Test 3: Custom System Instruction

System instruction:

```text
You are a programming teacher who explains concepts to beginners.
```

Prompt:

```text
Explain recursion.
```

### Test 4: Creative Response

Change temperature and ask:

```text
Write a short story about an AI robot.
```

### Test 5: Long Response

Increase maximum output tokens and ask:

```text
Explain machine learning in detail.
```

### Test 6: Error Handling

Test the application with an unavailable or invalid API configuration and verify that an appropriate error message is displayed.

---

# 📸 Screenshots

Add screenshots of the completed application here.

Recommended screenshots:

### Main Chat Interface

```text
![AI Chat Assistant](screenshots/main-interface.png)
```

### Settings Panel

```text
![AI Settings](screenshots/settings-panel.png)
```

### Conversation Memory

```text
![Conversation Memory](screenshots/conversation-memory.png)
```

### Live Application

```text
![Live Application](screenshots/live-application.png)
```

If you create a `screenshots` folder, your project structure can become:

```text
AI-Chat-Application/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── main-interface.png
│   ├── settings-panel.png
│   ├── conversation-memory.png
│   └── live-application.png
│
└── .streamlit/
    └── secrets.toml
```

---

# 📈 Future Improvements

The project can be extended with additional functionality such as:

* Multiple conversation sessions
* Conversation export
* Download chat history
* Markdown file upload
* PDF document analysis
* Image input
* Voice input
* Text-to-speech responses
* Streaming responses
* Authentication system
* Persistent database-based chat history
* User profiles
* Conversation search
* Model selection
* Token usage dashboard
* Advanced API usage monitoring
* Custom prompt templates
* RAG-based document question answering

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Large Language Model APIs
* Gemini API integration
* Python API development
* API authentication
* Secure secret management
* Conversational AI
* Prompt and system instruction design
* Conversation history management
* Model parameter configuration
* Token management
* Error handling
* Streamlit application development
* Git and GitHub
* Cloud deployment
* Debugging and testing
* AI application development

---

# 📚 Module Requirements Covered

This project addresses the major requirements of **Module 3: LLM APIs & Application Development**.

| Module Requirement              | Implementation                  |
| ------------------------------- | ------------------------------- |
| Understand LLM APIs             | Google Gemini API               |
| Authentication                  | Gemini API key                  |
| Environment Variables / Secrets | Streamlit Secrets               |
| Connect LLM using Python        | Google GenAI SDK                |
| Manage Conversations            | Streamlit session state         |
| Chat History                    | Stored conversation messages    |
| System Messages                 | Custom system instruction       |
| User Messages                   | Chat input                      |
| Assistant Messages              | Gemini generated responses      |
| Model Parameters                | Temperature and maximum tokens  |
| Token Usage                     | Maximum output token control    |
| Structured Responses            | Role-based message structure    |
| Error Handling                  | Exception handling              |
| API Cost Management             | Token and context control       |
| AI Chat Application             | Streamlit web application       |
| Basic UI                        | Interactive Streamlit interface |

---

# 📊 Skills Demonstrated

```text
Python
Google Gemini API
Large Language Models
Generative AI
Prompt Engineering
API Integration
Streamlit
Conversational AI
Conversation Memory
API Authentication
Secret Management
Error Handling
Token Management
Git
GitHub
Cloud Deployment
Problem Solving
Application Development
```

---

# 👨‍💻 Author

## Rahul Gupta

B.Sc. (Hons) Computer Science

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Financial Analytics
* Python Development
* Data Analytics
* Software Development

---

# 🔗 Project Links

### GitHub Repository

```text
https://github.com/YOUR-USERNAME/AI-Chat-Application-Gemini-API
```

### Live Application

```text
YOUR_STREAMLIT_APP_URL
```

### LinkedIn Post

```text
YOUR_LINKEDIN_POST_URL
```

---

# 📄 Project Information

**Project:** AI Chat Assistant using Google Gemini API

**Module:** Module 3 - LLM APIs & Application Development

**Level:** Intermediate

**Technology:** Python + Google Gemini API + Streamlit

**Application Type:** Generative AI / Conversational AI

**Deployment:** Streamlit Community Cloud

---

## ⭐ Acknowledgement

This project was developed as part of an internship/project-based learning module focused on practical implementation of Large Language Models, API integration, and AI application development.

---

## ⭐ If You Found This Project Useful

Feel free to explore the repository, try the live application, and connect with me on LinkedIn.