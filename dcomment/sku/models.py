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

    @property
    def tone_is_positive(self):
        
        if self.tone:

            tone = json.loads(self.tone)
            tone_categories = tone['document_tone']['tone_categories']
            joy = 0.0

            for tone_category in tone_categories:
                if tone_category['category_id'] == 'emotion_tone':
                    for tone_category_tone in tone_category['tones']:
                        if tone_category_tone['tone_id'] == 'joy':
                            joy = tone_category_tone['score']
        
            return joy >= 0.5
            
        return None


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
