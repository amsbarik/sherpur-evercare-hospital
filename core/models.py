from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['order']


class HeroOverview(BaseModel):
    heading = models.CharField(max_length=120)
    short_description = models.TextField()
    # visit_url = models.URLField(default='https://', blank=True, null=True)
    # button_name = models.CharField(max_length=50, default='Visit Now')
    calling_photo = models.ImageField(upload_to='slider/', blank=True)
    image = models.ImageField(upload_to='slider/')

    def __str__(self):
        return self.heading
    

class FAQ(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

# class HowItWork(BaseModel):
#     question = models.CharField(max_length=255)
#     answer = models.TextField()

#     def __str__(self):
#         return self.question
    


class SiteSetting(models.Model):
    # Branding
    header_logo = models.ImageField(upload_to='site/')
    footer_logo = models.ImageField(upload_to='site/')
    favicon = models.ImageField(upload_to='site/')

    # Contact info
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    working_hour = models.CharField(max_length=120)

    # Social links
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twiter_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    # SEO Meta
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.CharField(
        max_length=255,
        help_text="Comma-separated keywords (e.g. hospital, doctor)"
    )

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"



# class PromotionalOffer(BaseModel):
#     offer_name = models.CharField(max_length=120, default='Promotional Offer')
#     image = models.ImageField(upload_to='offer_popups/')

#     def __str__(self):
#         return "Promotional Offer Design"

#     class Meta:
#         verbose_name = "Promotional Offer Design"
#         verbose_name_plural = "Promotional Offer Design"
