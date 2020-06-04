from django.urls import path
from myapp import views


urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('/',views.PostListView.as_view(),name='post_name'),
    path('post/(?p<pk>\d+)',views.PostDetailView.as_view(),name='post_detail)'),
    path('post/new/)',views.CreatePostView.as_view(),name='post_new)'),
    path('post/(?p<pk>\d+)/edit/)',views.PostUpdateView.as_view(),name='post_edit)'),
    path('post/(?p<pk>\d+)/remove/)',views.PostDetailView.as_view(),name='post_remove)'),
    path('drafts/)',views.DraftListView.as_view(),name='post_draft_list)'),
    path('post/(?P<pk>\d+)/comment/', views.PostPublish.as_view(), name='add_comment_to_post'),
    path('comment/(?p<pk>\d+)/approve/)',views.PostAddComment.as_view(),name='comment_approve)'),
    path('comment/(?p<pk>\d+)/remove/)',views.PostApprove.as_view(),name='comment_remove)'),
    path('post/(?p<pk>\d+)/publish/)',views.PostCommentRemove.as_view(),name='post_publish)'),

]
