from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, createpost
from .models import Post


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register/register_done.html', {new_user: new_user})
        else:
            user_form = RegisterForm()
    user_form = RegisterForm()
    return render(request, 'register/register_final.html', {'user_form': user_form})


def see_all_posts(request):
    allposts = Post.objects.all()
    context = {"object_list": allposts}
    template_name = 'account/postboard.html'
    return render(request, template_name, context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # add a new view of the post bulletin board here
                    return see_all_posts(request)
                else:
                    return HttpResponse('User Cannot be Authenticated')
            else:
                return render(request, 'account/login_failed.html')
        else:
            form = LoginForm()
    form = LoginForm()
    return render(request, 'login/login_final.html', {'form': form})

'''def post(request):

    if request.method == 'POST':
        post = createpost(request.POST)
        return render(request, 'create/create_post.html', {'post': post})
    else:
        form = LoginForm()
        return render(request, 'login/login_final.html', {'form': form})

        deprecated function needed to be resorted

        '''
def post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = createpost(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(see_all_posts)
        else:
            print(form.errors)
    else:
        form = createpost()
    form = createpost()

    post = createpost(request.POST)
    return render(request, 'create/create_post.html', {'post': post})
