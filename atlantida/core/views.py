from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)

class ServicesView(View):
    template_name = 'service.html'

    def get(self, request):
        return render(request, self.template_name)

class ProductsView(View):
    template_name = 'products.html'

    def get(self, request):
        return render(request, self.template_name)


class CareerView(View):
    template_name = 'career.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

class audio_visual(View):
    template_name = 'audio_visual.html'

    def get(self, request):
        return render(request, self.template_name)
class security(View):
    template_name = 'security.html'

    def get(self, request):
        return render(request, self.template_name)
class POE(View):
    template_name = 'POE.html'

    def get(self, request):
        return render(request, self.template_name)
class structured_cabling(View):
    template_name = 'structured_cabling.html'

    def get(self, request):
        return render(request, self.template_name)

class wireless(View):
    template_name = 'wireless.html'

    def get(self, request):
        return render(request, self.template_name)
