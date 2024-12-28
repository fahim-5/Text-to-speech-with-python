import pyttsx3

def text_to_speech():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Get input from the user
    text = input("Enter the text you want me to speak: ")
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()
    

if __name__ == "__main__":
    text_to_speech()
