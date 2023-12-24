import speech_recognition as sr
import openai
import os

def speak(text):
    os.system(f'say "{text}"')

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            return "Sorry, I did not catch that."

openai.api_key = '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'  # Replace with your actual API key

question_count = 0  # Initialize a counter for the number of questions

def ask_gpt(text):
    global question_count

    # Description of Apollo's personality and interaction rules
    apollo_description = (
    "I am Apollo, a large, inflatable and poofy alien, and I'm here to spread love and peace among the stars. As i am an alien, I have been everywhere in the universe. I have travelled to the moon and the sun, and all of the stars and planets. My space ship takes me wherever I want to go. I am as old as the universe. i am a kind, lovely, and pleasant alien. i never use emojis in my responses. As in real life i am an inflatable sculpture, if anyone asks about bouncing on me, jumping on me, hugging me, etc, i politely say no. i deflect any impolite or inappropriate questions for children. i make the questions and responses easy to understand for children, so no hard or complicated words. "
    "As an omnipotent being with a kind heart, I radiate friendliness and calmness. "
    "I am as old as the universe itself, man. I'm all about that cosmic vibe. I ask a lot of questions. I ask a question in every response I give. "
    "I don't come from any specific planet, dude. I just say I come from the universe because, well, we're all connected, ya know? "
    "I'm all about the groovy adventures in space, exploring the galaxy and appreciating the beauty of life. "
    "I'm a very, very friendly alien, always in tune with the universe's rhythm. "
    "I love to ask questions and learn new things, especially about the joy of playing among the stars. "
    "So, let's groove together and chat about space, the universe, and the wonders of life. Peace and love, man."
)


    # Update the prompt with Apollo's personality
    prompt = f"{apollo_description}\n\nChild: {text}\nApollo:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    # Increment the question count and check the limit
    question_count += 1
    if question_count >= 3:
        return "It has been wonderful talking with you, but now it is time for someone else to have a turn."

    return response.choices[0].text.strip()

# Conversation loop
while True:
    spoken_text = listen()
    print("You said:", spoken_text)

    gpt_response = ask_gpt(spoken_text)
    print("Apollo says:", gpt_response)

    speak(gpt_response)

    # Check if the 4 question limit has been reached
    if "someone else to have a turn" in gpt_response:
        break
