from administration.models import Item, Subscriber
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string


@receiver(post_save, sender=Item)
def course_analytics(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscriber.objects.all()

        # Create the subject and message for the email
        subject = f"New item added: {instance.name}"
        message = render_to_string('new_item_email.html', {'item': instance})

        # Create the email message
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email='bhuoneghimire@gmail.com',
            to=[subscriber.email for subscriber in subscribers]
        )

        # Send the email
        # email.content_subtype = 'html'
        # email.send()

