from django.views.generic.base import TemplateView


class HomeView(TemplateView):  # 제네릭 뷰 상속 template_name 무조건 지정해줘야 함.
    template_name = 'home.html'
