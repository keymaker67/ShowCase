from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect

from user.models import UserRelationModel
from content.models import (
    MediaModel, MentionModel,
)
from tag.models import TagModel

# Create an instance of user model
User = get_user_model()


def get_followers(current_user):
    # Get the IDs of users who are following the current user
    follower_ids = UserRelationModel.objects.filter(related_with=current_user, relation_type='follower').values_list('user_id', flat=True)
    # Get the users who are following the current user
    followers = User.objects.filter(id__in=follower_ids)
    return followers


def post_story_form_validator(request, form):
    if form.is_valid():
        content = form.save()

        # Create Media instance
        content_type = ContentType.objects.get_for_model(content)
        object_id = content.id
        media_file_paths = request.FILES.getlist('media_files')
        for media_file_path in media_file_paths:
            # Create a new media object
            media_instance = MediaModel.objects.create(
                content_type=content_type,
                object_id=object_id,
                media_file=media_file_path,
                media_type=request.POST['media_type']
            )

        # Create a new tag object
        TagModel.objects.create(
            content_type=content_type,
            object_id=object_id,
            title=request.POST['tag'],
        )

        # Create a new mention object
        mentioned_username = request.POST['mention']
        mentioned_user = User.objects.get(username=mentioned_username)
        MentionModel.objects.create(
            content_type=content_type,
            object_id=object_id,
            user=mentioned_user,
        )

        # return redirect('post_detail', pk=post.pk)
        return redirect('home')
    else:
        print(form.errors)
