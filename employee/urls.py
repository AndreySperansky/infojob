from django.urls import path
from .views import *


app_name = 'employee'

urlpatterns = [
	path('', HomepageView.as_view(), name='employee'),
	path('cv/<int:pk>/', CollectionDetailView.as_view(), name='cv_detail'),
    path('cv/create/', CollectionCreate.as_view(), name='cv_create'),
    path('cv/update/<int:pk>/', CollectionUpdate.as_view(), name='cv_update'),
    path('cv/delete/<int:pk>/', CollectionDelete.as_view(), name='cv_delete'),


    path('vacancy/', SearchView.as_view(), name='vacancies'),
    path('vacancy/list/', vacancies, name='job_list'),
    path('vacancy/bookmark/', BookmarkView.as_view(), name='bookmarks'),
    path('vacancy/bookmark/list/', job_bookmarks, name='bookmark_list'),
    path('vacancy/bookmark/<int:pk>', add_remove_bookmark, name='job_bookmark'),
    path('vacancy/delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete_bookmark'),
    path('vacancy/read/<int:pk>', JobDetailView.as_view(), name='job_read'),
    path('vacancy/filter/', JobFilter.as_view(), name='job_filter'),


    path('response/<int:pk>/', ResponseCreate.as_view(), name='response'),
    path('response/', ResponseView.as_view(), name='responses'),
    path('response/list/', responses, name='response_list'),
    path('response/delete/<int:pk>', ResponseDelete.as_view(), name='delete_response'),
]
