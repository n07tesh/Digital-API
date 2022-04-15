from django.urls import path
# from app.api.views import movie_list, movie_details
from app.api.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV

urlpatterns = [
path('list/', WatchListAV.as_view(), name='movie_list'),
path('list/<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),
path('stream/', StreamPlatformAV.as_view(),name='streamplatofrm'),
path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='streamplatform-detail')
]