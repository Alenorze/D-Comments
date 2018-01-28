import json

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver 
from django.conf import settings

from watson_developer_cloud import ToneAnalyzerV3



class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    tone = models.TextField(blank=True)

    class Meta:
        ordering = ('created',)


@receiver(pre_save, sender=Comment)
def provide_tone(sender, instance, *args, **kwargs):
    tone_analyzer = ToneAnalyzerV3(
        username=settings.WATSON_USERNAME,
        password=settings.WATSON_PASSWORD,
        version='2017-09-21' 
    )

    tone = tone_analyzer.tone(text=instance.content)

    instance.tone = json.dumps(tone)
    