# AI-Powered Chatbot

A simple web-based chatbot built with Python, Flask, and HTML/CSS. The chatbot responds to user inputs based on predefined responses stored in a JSON file. This project is beginner-friendly and can be extended with advanced AI features like NLP or external APIs.

## Features
- Web interface for chatting with the bot.
- Predefined responses for common user inputs.
- Easy to extend with additional responses or AI integration.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DropPlan-at13/first-intelligent-project.git
   cd first-intelligent-project
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate



3. Install dependencies:

pip install -r requirements.txt



4. Run the application:

python app.py



5. Open http://localhost:5000 in your browser.

Usage





Type a message in the input box and press "Send."



The chatbot responds based on keywords in your message.



Edit responses.json to add more responses.

Future Enhancements





Integrate an AI API (e.g., OpenAI) for dynamic responses.



Add user authentication for personalized chats.



Implement a database to store chat history.

Contributing

Feel free to fork this repository, make changes, and submit a pull request. See CONTRIBUTING.md for guidelines.

License

MIT License


### requirements.txt
```text
Flask==3.0.3

User Stories





As a user, I want to type a message and receive a response from the chatbot.



As a user, I want the chat interface to be clean and easy to use.



As a developer, I want to easily add new responses to the chatbot.



As a developer, I want the project to be well-documented for collaboration.

Bonus Features (Optional)





AI Integration: Integrate an API like OpenAI’s GPT for more intelligent responses (requires an API key).



Chat History: Store conversations in a database like SQLite.



Styling: Enhance the UI with animations or a more modern design using Tailwind CSS.



Deployment: Deploy the app to a platform like Heroku or Render for public access.

Resources





Flask Documentation



GitHub Pages for Hosting (for static files, if you choose to host the front-end separately)



Python JSON Handling
