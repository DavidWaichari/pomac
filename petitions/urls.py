from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views


urlpatterns = [
    # urls for PetitionForm
    path('petitionform/', login_required(views.PetitionFormListView.as_view()), name='petitionform_list'),
    path('', login_required(views.PetitionFormListView.as_view()), name='petitionform_list'),
    path('petitionform/create/', views.PetitionFormCreateView.as_view(),name='petitionform_create'),
    path('petitionform/detail/<int:pk>/', views.PetitionFormDetailView.as_view(),name='petitionform_detail'),
    path('petitionform/update/<int:pk>/', views.PetitionFormUpdateView.as_view(),name='petitionform_update'),
    path('petitionform/ineligible', views.PetitionFormIneligibleListView.as_view(), name='petitionform_ineligible'),
    path('petitionform/eligible', views.PetitionFormEligibleListView.as_view(), name='petitionform_eligible'),
    path('petitionform/print/<int:pk>/', views.GeneratePetitionForm,name='petitionform_print'),

    path('admissibilityform/', views.AdmissibilityFormListView.as_view(), name='admissibilityform_list'),
    path('admissibilityform/admissible', views.AdmissibilityFormAdmissibleListView.as_view(), name='admissibilityformadmissible_list'),
    path('admissibilityform/inadmissible', views.AdmissibilityFormInAdmissibleListView.as_view(), name='admissibilityformaindmissible_list'),
    path('admissibilityform/create/', views.AdmissibilityFormCreateView.as_view(), name='admissibilityform_create'),
    path('admissibilityform/detail/<int:pk>/', views.AdmissibilityFormDetailView.as_view(), name='admissibilityform_detail'),
    path('admissibilityform/update/<int:pk>/', views.AdmissibilityFormUpdateView.as_view(), name='admissibilityform_update'),
    path('admissibilityform/print/<int:pk>/', views.GenerateAdmissibilityForm, name='admissibilityform_print'),

    # urls for PetitionSummary
    path('petitions/petitionsummary/', views.PetitionSummaryListView.as_view(), name='petitionsummary_list'),
    path('petitions/petitionsummary/create/', views.PetitionSummaryCreateView.as_view(), name='petitionsummary_create'),
    path('petitions/petitionsummary/detail/<int:pk>/', views.PetitionSummaryDetailView.as_view(), name='petitionsummary_detail'),
    path('petitions/petitionsummary/update/<int:pk>/', views.PetitionSummaryUpdateView.as_view(), name='petitionsummary_update'),
    path('petitions/petitionsummary/print/<int:pk>/', views.GeneratePetitionSummary, name='petitionsummary_print'),

    # urls for HearingSummary
    path('hearingsummary/', views.HearingSummaryListView.as_view(), name='hearingsummary_list'),
    path('hearingsummary/deferred', views.HearingSummaryDeferredListView.as_view(), name='hearingsummary_deferred'),
    path('hearingsummary/declined', views.HearingSummaryDeclinedListView.as_view(), name='hearingsummary_declined'),
    path('hearingsummary/scheduled-for-interview', views.HearingSummaryScheduledforInterviewListView.as_view(), name='hearingsummary_scheduledforinterview'),
    path('hearingsummary/awaiting-schedule-for-interview', views.HearingSummaryAwaitingScheduleforInterviewListView.as_view(), name='hearingsummary_awaitingscheduleforinterview'),
    path('hearingsummary/create/', views.HearingSummaryCreateView.as_view(),name='hearingsummary_create'),
    path('hearingsummary/detail/<int:pk>/', views.HearingSummaryDetailView.as_view(),name='hearingsummary_detail'),
    path('hearingsummary/update/<int:pk>/', views.HearingSummaryUpdateView.as_view(),name='hearingsummary_update'),
    path('hearingsummary/print/<int:pk>/', views.GenerateHearingForm,name='hearingsummary_print'),

    # urls for InterviewSummary
    path('interviewsummary/', views.InterviewSummaryListView.as_view(),name='interviewsummary_list'),
    path('interviewsummary/recommended', views.InterviewSummaryRecommendedListView.as_view(),name='interviewsummary_recommended'),
    path('interviewsummary/notrecommended', views.InterviewSummaryNotRecommendedListView.as_view(),name='interviewsummary_notrecommended'),
    path('interviewsummary/create/', views.InterviewSummaryCreateView.as_view(),name='interviewsummary_create'),
    path('interviewsummary/detail/<int:pk>/', views.InterviewSummaryDetailView.as_view(),name='interviewsummary_detail'),
    path('interviewsummary/update/<int:pk>/', views.InterviewSummaryUpdateView.as_view(),name='interviewsummary_update'),
    path('interviewsummary/print/<int:pk>/', views.GenerateInterviewSummary,name='interviewsummary_print'),

# urls for RecommendationForm
    path('recommendationform/', views.RecommendationFormListView.as_view(), name='recommendationform_list'),
    path('recommendationform/create/', views.RecommendationFormCreateView.as_view(), name='recommendationform_create'),
    path('recommendationform/detail/<int:pk>/', views.RecommendationFormDetailView.as_view(), name='recommendationform_detail'),
    path('recommendationform/update/<int:pk>/', views.RecommendationFormUpdateView.as_view(), name='recommendationform_update'),
    path('recommendationform/print/<int:pk>/', views.GenerateRecommendationForm, name='recommendationform_print'),

    # urls for County
    path('petitions/county/', views.CountyListView.as_view(), name='petitions_county_list'),
    path('petitions/county/create/', views.CountyCreateView.as_view(), name='petitions_county_create'),
    path('petitions/county/detail/<int:pk>/', views.CountyDetailView.as_view(), name='petitions_county_detail'),
    path('petitions/county/update/<int:pk>/', views.CountyUpdateView.as_view(), name='petitions_county_update'),

    # urls for SubCounty
    path('petitions/subcounty/', views.SubCountyListView.as_view(), name='petitions_subcounty_list'),
    path('petitions/subcounty/create/', views.SubCountyCreateView.as_view(), name='petitions_subcounty_create'),
    path('petitions/subcounty/detail/<int:pk>/', views.SubCountyDetailView.as_view(),name='petitions_subcounty_detail'),
    path('petitions/subcounty/update/<int:pk>/', views.SubCountyUpdateView.as_view(),name='petitions_subcounty_update'),
    path('ajax/load-subcounties/', views.load_subcounties, name='ajax_load_subcounties'),  # <-- this one here
]

