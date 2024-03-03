from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect

from user.models import UserRelationModel, UserProfileModel
from content.models import (
    MediaModel, MentionModel, PostModel, StoryModel
)
from tag.models import TagModel

# Create an instance of user model
User = get_user_model()


def get_followers(current_user):
    # Get the IDs of users who are following the current user
    follower_ids = (UserRelationModel.objects.filter(related_with=current_user, relation_type='follower').
                    values_list('user_id', flat=True))
    # Get the users who are following the current user
    followers = User.objects.filter(id__in=follower_ids)
    return followers


def get_following_users(current_user):
    # Get the IDs of users who are following the current user
    followings_ids = (UserRelationModel.objects.filter(related_with=current_user, relation_type='following').
                      values_list('user_id', flat=True))
    # Get the users who are following the current user
    followings = User.objects.filter(id__in=followings_ids)
    return followings


def get_public_users():
    # Get the IDs of users who are following the current user
    public_user_ids = (UserProfileModel.objects.filter(public=True).values_list('user_id', flat=True))
    # Get the users who are following the current user
    public_users = User.objects.filter(id__in=public_user_ids)
    return public_users


def add_posts_stories(preferred_users, posts, stories):
    for users in preferred_users:
        user_posts = PostModel.objects.filter(user=users).order_by('-created_date')
        user_stories = StoryModel.objects.filter(user=users).order_by('-created_date')
        for post in user_posts:
            # Get all media associated with the current post
            media = post.media.all()
            comment = post.comment.all()
            posts.append({'content': post, 'media': media, 'comment': comment})
        for story in user_stories:
            # Get all media associated with the current post
            media = story.media.all()
            comment = story.comment.all()
            stories.append({'content': story, 'media': media, 'comment': comment})


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
