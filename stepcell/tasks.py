from background_task import background
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


@background(schedule=10)
def contact_mail(name,email):
    ctx = {
        'user': name
    }

    subject, from_email, to = 'Contact Mail!',"Choreography Club<settings.EMAIL_HOST_USER>", [email,]
    text_content = 'This is an Contact message.'
    html_content = get_template('contact_mail.html').render(ctx)
    msg = EmailMultiAlternatives(subject, text_content,from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print(name + " contacted us")

@background(schedule=15)
def self_contact_mail(name,query):
    subject, from_email, to = 'Contact', "Choreography Club<settings.EMAIL_HOST_USER>", 'choreographycell@gmail.com'
    text_content = 'This is an Contact message.'
    html_content = '<h3>Name:</h3>' + name +  '<h3>Query:</h3>'+ query
    msg = EmailMultiAlternatives(subject, text_content,from_email, [to,])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("Self contact mail " + name)


@background(schedule=10)
def ongoing_event_mail(name,email):
    ctx = {
        'user': name
    }

    subject, from_email, to = 'Confirmation Mail!',"Choreography Club<settings.EMAIL_HOST_USER>", [email,]
    text_content = 'This is an Contact message.'
    html_content = get_template('ongoing_event_mail.html').render(ctx)
    msg = EmailMultiAlternatives(subject, text_content,from_email, to)
    msg.attach_alternative(html_content, "text/html")
    # msg.attach_file('Challenge.pdf')
    msg.send()
    print(name + " registered for Namaskaram")

@background(schedule=10)
def sending_mail(name,email):
    ctx = {
        'user': name
    }

    subject, from_email, to = 'Reminder Mail!',"Choreography Club<settings.EMAIL_HOST_USER>", [email,]
    text_content = 'This is an Contact message.'
    html_content = get_template('sendingEmail.html').render(ctx)
    msg = EmailMultiAlternatives(subject, text_content,from_email, to)
    msg.attach_alternative(html_content, "text/html")
    # msg.attach_file('Challenge.pdf')
    msg.send()
    print("mail sent to " + name)