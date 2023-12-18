from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '745talha@gmail.com'
app.config['MAIL_PASSWORD'] = 'rrvq fjig jtrm sbew'
app.config['MAIL_USE_TLS']=False

mail = Mail(app)



from flask_mail import Message

@app.route('/send_email')
def send_email():
    html_body = """
    <p>This is a <b>styled</b> email with <span style="color: green; font-size: 30px;">custom styling</span>.</p>
    """
    msg = Message('Subject2', sender='745talha@gmail.com', recipients=['1261sherzaman@gmail.com'])

    # Attach both plain text and HTML versions of the email
    # msg.body = 'This is the plain text version of the email.'
    msg.html = html_body

    mail.send(msg)
    print("1")
    return 'Email sent Sucessfully!'

@app.route('/')
def hello():
    return 'Hello Testing Mail'


if __name__=='__main__':
    app.run()
