'''
Created on 27 mar 2019

@author: mpasteri

https://www.tutorialspoint.com/flask/flask_sessions.htm
'''
#from flask import Flask, session, request,redirect,url_for,render_template
from flask import Flask, session, request,redirect,url_for,escape,render_template


app = Flask(__name__)
#-------------------------------------------------------------

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"


@app.route('/login', methods = ['GET', 'POST'])
def login():
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    if request.method == 'POST':
        session['username'] = request.form['username']        
        return redirect(url_for('index'))
    
    if request.method == 'GET':
        print('Ciaoooooooooooo')
        return render_template('login.html')
    
    return "   <form action = "'/'" method = "+ 'post' "> + \
      <p>username <input type = text name = username/></p> + \
      <p<input type = submit value = Login/></p> + \
   </form>"    
   
@app.route('/logout')
def logout():    
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

#-------------------------------------------------------------
#-------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
    #app.secret_key = 'any random string'.encode(encoding='utf_8', errors='strict')
    
    
