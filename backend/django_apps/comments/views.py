from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Comment



@login_required
def comment_delete(request,id):
    """This is the view for deleting comments.
    Using user.auth we are able to make sure that users are only able to delete their own comments.

    Args:
        request: the http request
        id: integer that represents the ID of the comment

    Return:
        All information needed in order to delete comments.

        request:
        context: a dictionary that contains{
            obj: the comment that is being deleted
            }
        confirm_delete.html: the html template in which all of the context is being passed into
    """
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404

    if obj.user != request.user:
            reponse = HttpResponse("You do not have permission to do this.")
            response.status_code = 403
            return response

    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        message.success(request, "This has been deleted.")
        return HttpResponseRedirect(parent_obj_url)
    context = {
        "object":obj
    }

    return render(request, "confirm_delete.html", context)


def comment_thread (request, id):
    """This is the display for the comment thread. It allows for users to post new comments as well as reply to comments
    This entire system relies heavily on user.auth

    Args:
        request: html response
        id: an integer that represents the id of the comment

    Return:
        All the comments within a thread. All the comment responses to each of the comments.
        The reply button is also returned for users to reply to comments.
        All of this is passed toward the template "comment_thread.html"

    """
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404

    if not obj.is_parent:
        obj = obj.parent

    content_object = obj.content_object
    content_id = obj.content_object.id

    initial_data = {
        "content_type": obj.content_type,
        "object_id": obj.object_id
    }

    form = CommentForm(request.POST or None, intial = initial_data)
    if form.is_valid() and request.user.is_authenticated():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.object.get(model = c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        parent_obj = None

        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id = parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment , created = Comment.object.get_or_create(
                                user = request.user,
                                content_type = content_type,
                                object_id = obj_id
                                content = content_data,
                                parent = parent_obj,
                            )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    context = {
        "comment":obj,
        "form":form,
    }
    return(request,"comment_thread.html",context)
