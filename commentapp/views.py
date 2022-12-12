from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect


# Create your views here.
from .forms import CommentForm
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_detail(request):
    template_name = 'commentapp/post_detail.html'
    post = get_object_or_404(Post)
    comments = post.comments.filter(active=True)
    new_comment =  None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form.save()
        return redirect('/post_detail/')  
    
    else:
        comment_form = CommentForm()
    response=redirect('post_detail')

    return render(request, template_name, {
        'post': post,
                                        'comments': comments,
                                        'new_comment': new_comment,
                                        'comment_form': comment_form,
                                        'hello':response
                                           })

