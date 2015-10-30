from django.views.generic import DetailView

from .models import MockObject


class MockDetailView(DetailView):
    model = MockObject
    template_name = 'detailview.html'
