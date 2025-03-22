from django.views import generic
from .models import Post


class IndexView(generic.TemplateView):
    template_name = "blog/index.html"
    model = Post  # 一覧表示させたいモデルを呼び出し


class PostListView(generic.ListView):  # generic の ListViewクラスを継承
    model = Post  # 一覧表示させたいモデルを呼び出し
