# config/sitemaps.py (или где удобно)
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'feedback','psychologists']    # имена url'ов

    def location(self, item):
        return reverse(item)
