from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # this is using for gmail 
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'abcd@examplemail.com' #set your email here
app.config['MAIL_PASSWORD'] = 'abcd efgh ijkl mnop' #it not working with gmail password, Enter Your app password here( if you don't have, follow instructions mentioned in Configuration in readme)
app.config['MAIL_USE_TLS']=False

mail = Mail(app)




@app.route('/send_email')
def send_email():
    msg = Message('Subject2', sender='abcd@examplemail.com', recipients=['abcd@examplemail.com']) #user can add multiple email addresses in recipients list

    # if user want styling in mail content this can be added as following 
    html_body = """
    <p>This is a <b>styled</b> email with <span style="color: green; font-size: 30px;">custom styling</span>.</p>
    """
    msg.html = html_body

    # the following line is to just send simple mail without any styling
    # msg.body = 'This is the plain text for mail. without any style'

    mail.send(msg)


if __name__=='__main__':
    app.run()
