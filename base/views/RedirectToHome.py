from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

class RedirectToHome(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('base')