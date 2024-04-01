
from django.shortcuts import render
from django.views.generic import TemplateView

# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Thread, Post
from .forms import ThreadForm, PostForm
from .models import Thread
from .forms import TweetForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ThreadPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from .models import Thread
from django.views.generic import ListView
from .models import Tweet
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = ThreadPostForm
    template_name = 'index.html'
    success_url = reverse_lazy('app:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'index.html', {'threads': threads})

def come_list(request):
    tweet = Tweet.objects.all()
    return render(request, 'a.html', {'threads': tweet})

def view_thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    posts = thread.posts.all()

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            user_name = post_form.cleaned_data['user_name']
            email = post_form.cleaned_data['email']
            comment = post_form.cleaned_data['comment']

            Post.objects.create(thread=thread, user_name=user_name, email=email, comment=comment)
            return redirect('view_thread', thread_id=thread_id)
    else:
        post_form = PostForm()

    return render(request, 'a.html', {'thread': thread, 'posts': posts, 'post_form': post_form})


class IndexView(TemplateView):
    template_name = 'index.html'

# この関数を追加
def post(request):

    message = request.POST['text']  # フォームのフィールド名を正確に指定
    thread = Thread(title=message)
    thread.save()
    return HttpResponseRedirect(reverse_lazy('app:index'))


class IndexView(ListView):
    template_name = 'index.html'
    queryset = Thread.objects.order_by('-created_at')  # 'created_at'に変更
    paginate_by = 9

def come_post(request,thread_id):
    comment = request.POST.get('comment')
    thread = Thread.objects.get(id=thread_id)
    message = Post(thread=thread,comment=comment)
    message.save()
    return HttpResponseRedirect('..')
