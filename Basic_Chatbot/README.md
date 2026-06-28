# Simple Rule-Based Chatbot

This is a beginner-friendly command-line chatbot built with Python. Unlike complex AI models, this chatbot operates on clear, predefined rules. It listens for specific keywords or phrases and immediately replies with matching, hardcoded answers. 

---

## How it Works (In Simple Words)

This project breaks down into three core steps: cleaning the text, checking the rules, and running the conversation loop.

### 1. Cleaning the Text (`.lower().strip()`)
Humans type in chaotic ways. Someone might type `"HI "`, `"Hi"`, or `"hi"`. To keep the chatbot from getting confused, the program uses two built-in Python tools the moment you type your message:
* `.lower()` turns every letter lowercase.
* `.strip()` cuts off any accidental spaces left at the beginning or end of your text.

This ensures that `"  Hello   "` cleanly becomes `"hello"` before the chatbot looks at it.

### 2. The Choice Matrix (If / Elif / Else)
At the top of the code, all the chatbot's "intelligence" lives inside the `chatbot_response()` function. It acts like a giant matching game:
* **If** you say a greeting $\rightarrow$ it says "Hello!"
* **Else If (Elif)** you ask who it is $\rightarrow$ it proudly reveals it was created by Engineer 9.0.
* **Else (The Catch-All)** if you type anything it doesn't recognize, it politely lets you know it doesn't understand yet instead of breaking.

### 3. The Continuous Chat Loop (While Loop)
To keep you from having to restart the script after every single sentence, a `while True` loop keeps the conversation going seamlessly. The chat stays active until you explicitly type `q` at the end-of-turn prompt, which stops the program cleanly.

---

## How to Use It

1. Run the script in your terminal.
2. The chatbot will display a menu of topics it knows how to discuss.
3. Type your message at the `You:` prompt and hit Enter.
4. Read the chatbot's response!
5. Press `q` when asked if you want to exit, or press any other key to keep chatting.

---

## Example Conversation

```text
I am a simple chatbot, which responses only these pre-defined messages:
1. Greetings(Hi, Hello, etc...)
2. How are you? or How are you
3. Who are you? or Who are you or Who? or Who
4. What is your favorite Programming Language?

You:  HELLO 
Chatbot: Hello!
To end the chat press 'q' and to continue press any key: 

You: who are you
Chatbot: I am a basic Chatbot - created by Sahito Pirih
To end the chat press 'q' and to continue press any key: q
Thank You for using Chatbot! Goodbye! Have a good day