from django.contrib.sessions.models import Session
from django.shortcuts import render
class HitCountMixin():

    def dispatch(self, request, *args, **kwargs):
        hit = self.request.session.get('hit', {})
        try:
            hit[self.request.path] += 1
            self.request.session['hit'] = hit
        except KeyError:
            hit[self.request.path] = 1
            self.request.session['hit'] = hit
        return super(HitCountMixin, self).dispatch(request, *args, **kwargs)