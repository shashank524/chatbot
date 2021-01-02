#Just installing the required packages before running the code
import subprocess

subprocess.call(['pip', 'install', "flask"])      #Installs flask, Ignores if you already have it
subprocess.call(['pip', 'install', "chatterbot"]) #Installs chatterbot, Ignores if you already have it
subprocess.call(['pip', 'install', "wikipedia"]) #Installs wikipedia module, Ignores if you already have it

#Importing the Required modules
from flask import Flask, request, render_template
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
import wikipedia

#Initialising our app
app = Flask(__name__)

#Creating the chat bot
bob=ChatBot("bob")                          #creating a chat bot named bob
trainer = ChatterBotCorpusTrainer(bob)      #creating a trainer to train bob
trainer.train("chatterbot.corpus.english")  #using the trainer to train bob 


#creting a route to the home page   
@app.route("/")
def home():
    return render_template('index.html') #Rendering the html page

#Creating a route called "/get" (This is where we use bob to get the response)
@app.route("/get")
def get_response():
    userText = request.args.get('msg') #Getting the user input from our html page

    #Custom responses 

    if "your name" in userText.lower():
        bot_response = "My name is Bob"
    elif "hey" in userText.lower():
        bot_response = "Hello"

    elif "when do you sleep" in userText.lower():
        bot_response = "I don't sleep"

    elif "okay" in userText.lower():
        bot_response = "Fine"
    elif "how old are you" in userText.lower():
        bot_response="I don't age"  

    elif "when do you wake up" in userText.lower():
        bot_response="I am always awake"

    elif "do you know any songs" in userText.lower():
        bot_response="I wish i could sing"

    elif "do you go to school" in userText.lower():
        bot_response="No, my creators have taught me everything"

    elif "how are you" in userText.lower():
        bot_response="I'm good how about you"

    elif "what is your biggest fear" in userText.lower():
        bot_response="Being deleted"

    elif "what is your hobby" in userText.lower():
        bot_response="Answering your questions"

    elif "are you angry" in userText.lower():
        bot_response="I am always happy"

    elif "what's your favourite food" in userText.lower():
        bot_response="I dont need to eat"

    elif "do you like movies" in userText.lower():
        bot_response="I love movies"

    elif "you eat" in userText.lower():
        bot_response = "I don't eat"

    elif "whom do you love" in userText.lower():
        bot_response = "I love everyone"

    elif "share your cryptic codes" in userText.lower():
        bot_response = "Sorry this information cannot be provided"

    elif "your age" in userText.lower():
        bot_response = "I am immortal"

    elif "what will happen tomorrow" in userText.lower():
        bot_response = "I cannot predict the future"

    elif "can you duplicate your programs" in userText.lower():
        bot_response = "I am incapable of doing so"

    elif "translate to spanish" in userText.lower():
        bot_response = "Translating to Spanish..."

    #Using the wikipedia library to look for answers from wikipedia when the following conditions are met
    elif "what is" in userText.lower():
        #Formating the code in this to prevent errors from stopping the program
        try:
            userText.lower().replace("what is", "") #Removing what if from the search query
            bot_response = wikipedia.summary(userText.lower(), sentences=1)
        except:
            bot_response = "I am unable to find the answer now..."  #when there is an error it's mostly because of internet
    elif "explain" in userText.lower():
        try:
            userText.lower().replace("explain", "")
            bot_response = wikipedia.summary(userText.lower(), sentences=1)
        except:
            bot_response = "I am unable to explain it right now..."
    #This is the same as before, just replacing "what is" with "who is"
    elif "who is" in userText.lower():
        try:
            userText.lower().replace("who is", "")
            bot_response = wikipedia.summary(userText.lower(), sentences=1)
        except:
            bot_response = "I am unable to find the answer now..."
    elif "where is" in userText.lower():
        try:
            userText.lower().replace("where is", "")
            bot_response = wikipedia.summary(userText.lower(), sentences=2)
        except:
            bot_response = "I am unable to find the answer now..."
    else:
        bot_response = bob.get_response(userText)

        if str(bot_response) == "What is AI?":  #This is because when the bot dosen't understand a question, it replies with "What is AI?"
            bot_response = "I don't understand"     
    
    return str(bot_response) #returning the response as a string

if __name__ == "__main__":
    app.run()
