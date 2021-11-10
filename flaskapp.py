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
        try:
          server.sendmail(sender, recipients, msg)
          server.quit()
          message = 'Success!'
          return flask.render_template('index.html', message=message)
        except smtplib.SMTPException as error:  
          message = 'Error - {err}'.format(err=error)
          return flask.render_template('index.html', message=message)
      
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
