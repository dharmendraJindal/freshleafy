from django.shortcuts import render_to_response
from django.template.context import RequestContext


def handle_page_not_found_404(request):
    page_title='Page Not Found'
    return render_to_response('404.html',locals(),context_instance=RequestContext(request))