# Flask-Mail Sender

## Overview

Flask-Mail Sender is a simple Python program that leverages Flask-Mail to send emails. This program is designed to be easy to use and integrate into your Flask applications for sending emails seamlessly.

## Features

- **Email Sending:** Easily send emails using Flask-Mail.
- **Styling:** Styling Mail, using html tags and css styles.
- **Minimal Setup:** Quickly integrate into your Flask projects.

## Getting Started

Follow these steps to integrate Flask-Mail Sender into your Flask project.

### Prerequisites

- Python installed (version 3.6 or later)
- Flask installed (`pip install Flask`)
- Flask-Mail installed (`pip install Flask-Mail`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/745talha/Flask-Mail-Sender.git
    ```

2. Change into the project directory:

    ```bash
    cd flask-mail-sender
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```


### Usage

1. Configure settings and call the "/send_email"


2. User can pass the data also but it need some changes in api calling



### Configuration

1. Open the `app.py` file.
2. Update the email configuration parameters such as `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USE_SSL`, `MAIL_USERNAME`, and `MAIL_PASSWORD` to match your email provider's settings.
3. For Gmail users, since two-factor authentication is enabled, you need to generate an "App Password." Follow these steps:
    - Go to [https://myaccount.google.com/](https://myaccount.google.com/).
    - Turn on Two-Factor Authentication.
    - In the "Security" section, find "App Passwords" and generate a new app password for your application.
    - Use the generated app password as the value for `MAIL_PASSWORD` in your `app.py` file.
  
   
## Example

Check out the `app.py` file for a simple example of how to use Flask-Mail Sender in a Flask application.

## Acknowledgments

- Flask-Mail: [https://pythonhosted.org/Flask-Mail/](https://pythonhosted.org/flask-mail/)
