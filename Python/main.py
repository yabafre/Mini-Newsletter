# Extremely simple flask application, will display 'Hello World!' on the screen when you run it
# Access it by running it, then going to whatever port its running on (It'll say which port it's running on).
from flask import Flask
from Newsletter import app
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    app.run(debug=True, port=5000)
