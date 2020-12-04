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

    #Write the if-else statements here
    if "your name" in userText.lower():
        bot_response = "My name is Bob"

    elif "when do you sleep" in userText.lower():
        bot_response = "I don't sleep"

    elif "okay" in userText.lower():
        bot_response = "Fine"

    #Using the wikipedia library to look for answers from wikipedia when the following conditions are met
    elif "what is" in userText.lower():
        #Formating the code in this to prevent errors from stopping the program
        try:
            userText.lower().replace("what is", "") #Removing what if from the search query
            bot_response = wikipedia.summary(userText.lower(), sentences=1)
        except:
            bot_response = "Internet Error..."  #when there is an error it's mostly because of internet

    #This is the same as before, just replacing "what is" with "who is"
    elif "who is" in userText.lower():
        try:
            userText.lower().replace("who is", "")
            bot_response = wikipedia.summary(userText.lower(), sentences=1)
        except:
            bot_response = "Internet Error..."

    else:
        bot_response = bob.get_response(userText)

        if str(bot_response) == "What is AI?":  #This is because when the bot dosen't understand a question, it replies with "What is AI?"
            bot_response = "I don't understand"     
    
    return str(bot_response) #returning the response as a string

if __name__ == "__main__":
    app.run()