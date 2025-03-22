from django.views import generic
from .models import Post
from .forms import PostCreateForm  # forms.py で作ったクラスをimport
from django.urls import reverse_lazy


class PostListView(generic.ListView):  # generic の ListViewクラスを継承
    model = Post  # 一覧表示させたいモデルを呼び出し


class PostCreateView(generic.CreateView):  # 追加
    model = Post  # 作成したい model を指定
    form_class = PostCreateForm  # 作成した form クラスを指定
    success_url = reverse_lazy("blog:post_list")  # 記事作成に成功した時のリダイレクト先を指定


class PostDetailView(generic.DetailView):  # 追加
    model = Post  # pk(primary key)はurls.pyで指定しているのでここではmodelを呼び出すだけで済む


class PostUpdateView(generic.UpdateView):  # 追加
    model = Post
    form_class = PostCreateForm  # PostCreateFormをほぼそのまま活用できる

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(generic.DeleteView):  # 追加
    model = Post
    success_url = reverse_lazy("blog:post_list")
