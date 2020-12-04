#Just installing the required packages before running the code
import subprocess

subprocess.call(['pip', 'install', "flask"])      #Installs flask, Ignores if you already have it
subprocess.call(['pip', 'install', "chatterbot"]) #Installs chatterbot, Ignores if you already have it

#Importing the Required modules
from flask import Flask, request, render_template
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

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
    userText = request.args.get('msg') #Getting the user input from out html page

    #Custom responses 

    #Write the if-else statements here
    if "what is your name" in userText.lower():
        bot_response = "My name is Bob"

    elif "when do you sleep" in userText.lower():
        bot_response = "I don't sleep"

    elif "okay" in userText.lower():
        bot_response = "Fine"

    else:
        bot_response = bob.get_response(userText)
        if bot_response == "What is AI?":
            bot_response = "I don't understand"
    
    
    return str(bot_response) #returning the response 

if __name__ == "__main__":
    app.run()