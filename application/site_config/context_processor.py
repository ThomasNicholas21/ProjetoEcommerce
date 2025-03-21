from site_config.models import SiteConfig

# Aqui sera criado um context_processor para toda aplicação

def context_site_config(request):
    data = SiteConfig.objects.order_by('-id').first()
    context = {
        'site_config': data,
    }

    return context