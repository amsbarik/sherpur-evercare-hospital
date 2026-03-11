from .models import SiteSetting

def site_data(request):
    return {
        'site_setting': SiteSetting.objects.first(),
    }
