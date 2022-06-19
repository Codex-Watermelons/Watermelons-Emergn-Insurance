from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from pymongo import MongoClient
import smtplib

app = Flask(__name__)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
con = open('Chat.txt','r',encoding="utf8").readlines()
english_bot.set_trainer(ListTrainer)
english_bot.train(con)
fo = open("data.txt","w")
userText = ''
botResp = ''

def send_email(name, receiver, feedback):
    subject = 'Insurance App: Our Customer Service will get back to you'
    to = receiver
    sender = 'insuranceappcodex@gmail.com'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    user = 'insuranceappcodex@gmail.com'
    password = 'jhzlzcvattnzaebe'
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(user, password)
    header = 'To:' + to + '\n' + 'From: ' + sender + '\n' + 'Subject:' + subject + '\n'
    message = header + '\n' + 'Hi, ' + name + ',\n\nThanks for your message: \n\"' + feedback + '\"\n\nWe will get back to you soon!\n'
    smtpserver.sendmail(sender, to, message)
    smtpserver.close()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['buttonOutput'] == 'Not Satisfied with the Answer?':
            return render_template('problem.html')
    else:
        return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botResp = str(english_bot.get_response(userText))
    fo.write(userText + "\n")
    fo.write(botResp + "\n")
    return str(english_bot.get_response(userText))

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       name = request.form['name']
       email = request.form['email']
       message = request.form['message']

       '''
       client = MongoClient()
       db = client.chat_db  # use a database
       coll2 = db.chatfeedback   # and inside that DB, a collection

       text_file_doc2 = {"name": name, "email" : email, "message" : message}
       coll2.insert(text_file_doc2)
       '''

       send_email(name, email, message)
       return render_template("index.html")

if __name__ == "__main__":
    app.run()

fo.close()
client = MongoClient()
db = client.chat_db  # use a database
coll = db.chatcoll   # and inside that DB, a collection

f = open('data.txt')  # open a file
text = f.read()    # read the entire contents

# build a document to be inserted
text_file_doc = {"file_name": "data.txt", "contents" : text }
# insert the contents into the collection
coll.insert(text_file_doc)

f.close()
