from django.views.generic import TemplateView


class TestMiddlewareView(TemplateView):
    template_name = 'test_middleware_view.html'
