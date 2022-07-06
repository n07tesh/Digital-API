from django.urls import path
# from app.api.views import movie_list, movie_details
from app.api.views import (ReviewDetail, WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV,ReviewList)

urlpatterns = [
path('list/', WatchListAV.as_view(), name='movie_list'),
path('list/<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),
path('stream/', StreamPlatformAV.as_view(),name='streamplatofrm'),
path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='streamplatform-detail'),

# path('review/',ReviewList.as_view(),name='review-list'),
# path('review/<int:pk>',ReviewDetail.as_view(),name='review-list-detail')
path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-list'),

path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
path('stream/review/<int:pk',ReviewDetail.as_view(),name='review-list-detail')
]