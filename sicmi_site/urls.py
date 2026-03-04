from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(86400)  # Cache 24h
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        "Sitemap: https://www.sicmisarl.com/sitemap.xml",
        "",
        "Disallow: /admin/",
        "Disallow: /debug/",
    ]
    return HttpResponse("\\n".join(lines), content_type="text/plain")


@cache_page(86400)
def sitemap_xml(request):
    urls = [
        ("https://www.sicmisarl.com/", "1.0", "weekly"),
        ("https://www.sicmisarl.com/services/", "0.9", "weekly"),
        ("https://www.sicmisarl.com/projets/", "0.8", "weekly"),
        ("https://www.sicmisarl.com/a-propos/", "0.8", "monthly"),
        ("https://www.sicmisarl.com/equipe/", "0.7", "monthly"),
        ("https://www.sicmisarl.com/ateliers/", "0.7", "monthly"),
        ("https://www.sicmisarl.com/politique-qhse/", "0.6", "monthly"),
        ("https://www.sicmisarl.com/contact/", "0.7", "monthly"),
    ]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
    for loc, priority, changefreq in urls:
        xml += f'  <url>\\n    <loc>{loc}</loc>\\n    <priority>{priority}</priority>\\n    <changefreq>{changefreq}</changefreq>\\n  </url>\\n'
    xml += '</urlset>'
    return HttpResponse(xml, content_type="application/xml")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
]

urlpatterns += i18n_patterns(
    path('', include('sicmi_app.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
