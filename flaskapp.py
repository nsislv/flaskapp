import flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# A simple Flask App which takes
# a user's name as input and responds
# with "Hello {name}!"

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
    
        # Create message container - the correct MIME type is multipart/alternative here!
        sender = flask.request.form['from']
        recipients = flask.request.form['to']
        msg = flask.request.form['message']
    
        # Create SMTP object
        server = smtplib.SMTP(host='localhost')
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()
        return flask.render_template('index.html')
      
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
