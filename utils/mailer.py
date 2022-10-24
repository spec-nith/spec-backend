from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_mail(html_template: str, subject: str, recipient_list: list):
    html_message = render_to_string(html_template)
    email_from = settings.EMAIL_HOST_USER
    message = EmailMessage(subject, html_message, email_from, recipient_list)
    message.content_subtype = "html"
    message.send()
