from django.urls import path
from .views import *


urlpatterns = [
	path('', HomepageView.as_view(), name='employer'),

	path('company/<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    path('company/create/', CompanyCreate.as_view(), name='company_create'),
    path('company/update/<int:pk>/', CompanyUpdate.as_view(), name='company_update'),
    path('company/delete/<int:pk>/', CompanyDelete.as_view(), name='company_delete'),
    path('vacancy/<int:pk>/', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/create/', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>/', VacancyUpdate.as_view(), name='vacancy_update'),
    path('vacancy/delete/<int:pk>/', VacancyDelete.as_view(), name='vacancy_delete'),
    path('cv/', SearchView.as_view(), name='cvs'),
    path('cv/list/', cvs, name='cv_list'),
    path('cv/filter/', CvFilterView.as_view(), name='cv_filter'),
    path('cv/bookmark/<int:pk>', CvBookmarkView.as_view(), name='cv_bookmark'),
    path('cv/response/<int:pk>', CvResponseView.as_view(), name='cv_response'),
    path('cv/read/<int:pk>', CvReadView.as_view(), name='cv_read'),

]
app_name = 'employer'

