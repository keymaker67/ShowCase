from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from user.models import UserRelationModel, UserProfileModel
from content.models import (
    MediaModel, MentionModel, PostModel, StoryModel
)
from user_activity.forms import CommentForm
from user_activity.models import CommentModel
from tag.models import TagModel
from log.models import PreviewModel

# Create an instance of user model
User = get_user_model()


def get_followers(current_user):
    # Get the IDs of users who are following the current user
    follower_ids = (
        UserRelationModel.objects.filter(
            user=current_user,
            relation_type='follower',
            is_active=True).
        values_list('related_with_id', flat=True))
    # Get the users who are following the current user
    followers = UserProfileModel.objects.filter(user_id__in=follower_ids)
    return followers, follower_ids


def get_following_users(current_user):
    # Get the IDs of users who are following the current user
    following_ids = (
        UserRelationModel.objects.filter(
            related_with=current_user,
            relation_type='follower',
            is_active=True).
        values_list('user_id', flat=True))
    # Get the users who are following the current user
    followings = UserProfileModel.objects.filter(user_id__in=following_ids)
    return followings, following_ids


def get_follow_requests(current_user):
    # Get the IDs of users who want to follow the current user
    follow_request_ids = (
        UserRelationModel.objects.filter(
            user=current_user,
            relation_type='follower',
            is_active=False).
        values_list('related_with_id', flat=True))
    # Get the users who want to follow the current user
    follow_requests = UserProfileModel.objects.filter(user_id__in=follow_request_ids)
    return follow_requests, follow_request_ids


def get_public_users():
    # Get the IDs of users who are public
    public_user_ids = (UserProfileModel.objects.filter(public=True).values_list('user_id', flat=True))
    # Get the users who are public
    public_users = UserProfileModel.objects.filter(id__in=public_user_ids)
    return public_users, public_user_ids


def add_posts_stories(preferred_users, posts, stories):
    for user in preferred_users:
        user_posts = PostModel.objects.filter(user=user.user).order_by('-created_date')
        user_stories = StoryModel.objects.filter(user=user.user).order_by('-created_date')
        for post in user_posts:
            # Get all media associated with the current post
            profile_picture = UserProfileModel.objects.filter(user=post.user).first().profile_picture
            media = post.media.all()
            comment = post.comment.all()
            posts.append({'content': post, 'media': media, 'comment': comment, 'profile_picture': profile_picture})
        for story in user_stories:
            # Get all media associated with the current post
            profile_picture = UserProfileModel.objects.filter(user=story.user).first().profile_picture
            media = story.media.all()
            comment = story.comment.all()
            stories.append({'content': story, 'media': media, 'comment': comment, 'profile_picture': profile_picture})


def post_story_form_validator(request, form):
    if form.is_valid():
        content = form.save()

        # Create Media instance
        content_type = ContentType.objects.get_for_model(content)
        object_id = content.id
        media_file_paths = request.FILES.getlist('media_files')
        for media_file_path in media_file_paths:
            # Create a new media object
            MediaModel.objects.create(
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


def content_view(request, pk, model, template):
    content = model.objects.filter(id=pk).first()
    if content:
        content_user = UserProfileModel.objects.filter(user_id=content.user_id)
        profile_picture = content_user.first().profile_picture
        public_users = get_public_users()
        medias = content.media.all()
        comments = content.comment.all().order_by('-created_date')
        context = {
            'content': content,
            'medias': medias,
            'comments': comments,
            'profile_picture': profile_picture}
        if content_user in public_users:
            if request.user.is_authenticated:
                trigger_preview(request, content)
                if request.method == 'POST':
                    input_comment(request, content)
                    return render(request, template, context)
                else:
                    return render(request, template, context)
            else:
                if request.method == 'POST':
                    messages.error = (request, 'You need to login first!')
                    return render(request, template, context)
                else:
                    return render(request, template, context)
        else:
            if request.user.is_authenticated:
                trigger_preview(request, content)
                following_users = get_following_users(request.user)[1]
                content_user_id = content_user.first().user_id
                if content_user_id in following_users or content_user_id == request.user:
                    if request.method == 'POST':
                        input_comment(request, content)
                        return render(request, template, context)
                    else:
                        return render(request, template, context)
                else:
                    messages.error = (request, '''
                        You are not permitted to see this content since you are not a follower.
                    ''')
                    print(1)
                    return redirect(request.META.get('HTTP_REFERER'))
            else:
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


def input_comment(request, content):
    form = CommentForm(request.POST)
    if form.is_valid():
        content_type = ContentType.objects.get_for_model(content)
        object_id = content.id
        CommentModel.objects.create(
            content_type=content_type,
            object_id=object_id,
            user=request.user,
            comment=request.POST['comment']
        )
        return redirect(request.path)
    else:
        messages.error = (request, 'Form is not valid.')
        return redirect(request.path)


def trigger_preview(request, content):
    content_type = ContentType.objects.get_for_model(content)
    object_id = content.id
    PreviewModel.objects.get_or_create(
        content_type=content_type,
        object_id=object_id,
        user=request.user,
    )
