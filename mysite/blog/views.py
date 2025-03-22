from django.views import generic
from .models import Post
from .forms import PostCreateForm  # forms.py で作ったクラスをimport
from django.urls import reverse_lazy


class IndexView(generic.TemplateView):
    template_name = "blog/index.html"
    model = Post  # 一覧表示させたいモデルを呼び出し


class PostListView(generic.ListView):  # generic の ListViewクラスを継承
    model = Post  # 一覧表示させたいモデルを呼び出し


class PostCreateView(generic.CreateView):  # 追加
    model = Post  # 作成したい model を指定
    form_class = PostCreateForm  # 作成した form クラスを指定
    success_url = reverse_lazy("blog:post_list")  # 記事作成に成功した時のリダイレクト先を指定
