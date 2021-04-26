from django.views.generic import TemplateView
from datetime import timedelta, datetime, timezone

class StatView(TemplateView):

    template_name = "stat/stat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = []
        context['time'].append((datetime.now(timezone.utc) - self.request.user.last_login).days)
        context['time'].append(((datetime.now(timezone.utc) - self.request.user.last_login).seconds)//3600)
        context['time'].append(((datetime.now(timezone.utc) - self.request.user.last_login).seconds//60)%60)
        return context