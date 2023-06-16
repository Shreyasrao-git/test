from django.db import models

from wagtail.models import Page
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class Values(models.Model):
    lastname = models.CharField(max_length=100, default="")
    class Meta:
        db_table="user"


