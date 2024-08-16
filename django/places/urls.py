from django.urls import path

from .views import *

urlpatterns = [
    path("", AegaPlaceWholeView.as_view(), name="aegaplace_whole_view"),
    path("main/", AegaPlaceMainView.as_view(), name="aegaplace_main_view"),
    path("main/banner/<int:banner_pk>/", AegaPlaceBannerView.as_view(), name="aegaplace_banner_view"),
    path(
        "main/recommendation/<int:recommendation_pk>/",
        AegaPlaceRecommendationView.as_view(),
        name="aegaplace_recommendation_view",
    ),
    path("<int:place_pk>/", AegaPlaceView.as_view(), name="aegaplace_view"),
    path("region/<int:region_pk>/", AegaPlaceRegionView.as_view(), name="aegaplace_region_view"),
    path("subcategory/<int:subcategory_pk>/", AegaPlaceSubcategoryView.as_view(), name="aegaplace_subcategory_view"),
    path("<int:place_pk>/share/", AegaPlaceMainShareView.as_view(), name="aegaplace_main_share_view"),
    path("<int:place_pk>/bookmark/", AegaPlaceMainBookmarkView.as_view(), name="aegaplace_main_bookmark_view"),
    path("<int:place_pk>/commets/", AegaPlaceCommentsView.as_view(), name="aegaplace_Comments_view"),
    path(
        "<int:place_pk>/commets/update/", AegaPlaceCommentsUpdateView.as_view(), name="aegaplace_Comments_update_view"
    ),
    path(
        "<int:place_pk>/commets/delete/", AegaPlaceCommentsDeleteView.as_view(), name="aegaplace_Comments_delete_view"
    ),
    path("<int:place_pk>/commet/iamges/", AegaPlaceCommentImagesView.as_view(), name="aegaplace_Comment_Images_view"),
]
