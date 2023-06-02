# pylint: disable=C0114, W0311, C0301
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message

class MailManager(object):
    """
    This is a utility class for managing Mail connections and mail
    """

    def __init__(self, app):
        """
        Initializes the MailManager object.
        """
        load_dotenv()
        self.mail = Mail(app)

        app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
        app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
        app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS').lower() == 'true'
        app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
        app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
        app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
        self.mail = Mail(app)

    def send_email(self, recipient, subject, body):
        """
        Sends an email.
        """
        with self.mail.app.app_context():
            msg = Message(subject, recipients=[recipient])
            msg.body = body
            self.mail.send(msg)
