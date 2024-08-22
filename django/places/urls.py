from django.urls import path

from .views import *

urlpatterns = [
    path("", AegaPlaceWholeView.as_view(), name="aegaplace_whole_view"),
    path("<str:main_category>/main/", AegaPlaceMainView.as_view(), name="aegaplace_main_view"),
    path("<int:place_pk>/", AegaPlaceView.as_view(), name="aegaplace_view"),
    path("<int:place_pk>/bookmark/", AegaPlaceMainBookmarkView.as_view(), name="aegaplace_main_bookmark_view"),
    path("<int:place_pk>/comments/", AegaPlaceCommentsAllView.as_view(), name="aegaplace_comments_all_view"),
    path("comments/<int:comment_pk>/", AegaPlaceCommentsView.as_view(), name="aegaplace_comments_view"),
    path("<int:place_pk>/comments/iamges/", AegaPlaceCommentImagesView.as_view(), name="aegaplace_Comment_Images_view"),
]
