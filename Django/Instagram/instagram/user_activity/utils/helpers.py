from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from content.models import PostModel, StoryModel
from user_activity.models import CommentModel, LikeModel


def like_view(request, pk, my_model):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            content = get_object_or_404(my_model, id=pk)
            content_type = ContentType.objects.get_for_model(content)
            liked, created = LikeModel.objects.get_or_create(
                content_type=content_type, object_id=pk, user=user)
            if not created:
                LikeModel.objects.filter(
                    content_type=content_type,
                    object_id=pk,
                    user=user
                ).delete()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, 'You need to login first!')
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))
