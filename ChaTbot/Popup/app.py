from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    if form.validate_on_submit():
        if request.form['submit_button'] == 'Do Something':
            print("here2")
            return render_template('index2.html')
        elif request.form['submit_button'] == 'Do Something Else':
            print("here3")
            return render_template('index3.html')
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
 

@app.route('/page2', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            return render_template('index2.html')
        elif request.form['submit_button'] == 'Do Something Else':
            return render_template('index3.html')
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')

'''
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


       client = MongoClient()
       db = client.chat_db  # use a database
       coll2 = db.chatfeedback   # and inside that DB, a collection

       text_file_doc2 = {"name": name, "email" : email, "message" : message}
       coll2.insert(text_file_doc2)

       send_email(name, email, message)
       return render_template("index.html")
'''

if __name__ == "__main__":
    app.run()

#fo.close()
#client = MongoClient()
#db = client.chat_db  # use a database
#coll = db.chatcoll   # and inside that DB, a collection

#f = open('data.txt')  # open a file
#text = f.read()    # read the entire contents

# build a document to be inserted
#text_file_doc = {"file_name": "data.txt", "contents" : text }
# insert the contents into the collection
#coll.insert(text_file_doc)

#f.close()
