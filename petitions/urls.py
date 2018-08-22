from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views


urlpatterns = [
    # urls for PetitionForm
    path('petitionform/', login_required(views.PetitionFormListView.as_view()), name='petitionform_list'),
    path('', login_required(views.PetitionFormListView.as_view()), name='petitionform_list'),
    path('petitionform/create/',login_required(views.PetitionFormCreateView.as_view()),name='petitionform_create'),
    path('petitionform/detail/<int:pk>/', login_required(views.PetitionFormDetailView.as_view()),name='petitionform_detail'),
    path('petitionform/update/<int:pk>/', login_required(views.PetitionFormUpdateView.as_view()),name='petitionform_update'),
    path('petitionform/ineligible', login_required(views.PetitionFormIneligibleListView.as_view()), name='petitionform_ineligible'),
    path('petitionform/eligible', login_required(views.PetitionFormEligibleListView.as_view()), name='petitionform_eligible'),
    path('petitionform/print/<int:pk>/', login_required(views.GeneratePetitionForm),name='petitionform_print'),

    path('admissibilityform/', login_required(views.AdmissibilityFormListView.as_view()), name='admissibilityform_list'),
    path('admissibilityform/awaiting-admissibility', login_required(views.AwaitingAdmissibilityFormListView.as_view()), name='awaitingadmissibility'),
    path('admissibilityform/admissible', login_required(views.AdmissibilityFormAdmissibleListView.as_view()), name='admissibilityformadmissible_list'),
    path('admissibilityform/inadmissible', login_required(views.AdmissibilityFormInAdmissibleListView.as_view()), name='admissibilityformaindmissible_list'),
    path('admissibilityform/create/', login_required(views.AdmissibilityFormCreateView.as_view()), name='admissibilityform_create'),
    path('admissibilityform/detail/<int:pk>/', login_required(views.AdmissibilityFormDetailView.as_view()), name='admissibilityform_detail'),
    path('admissibilityform/update/<int:pk>/', login_required(views.AdmissibilityFormUpdateView.as_view()), name='admissibilityform_update'),
    path('admissibilityform/print/<int:pk>/', login_required(views.GenerateAdmissibilityForm), name='admissibilityform_print'),

    # urls for PetitionSummary
    path('petitionsummary/', login_required(views.PetitionSummaryListView.as_view()), name='petitionsummary_list'),
    path('petitionsummary/awating-summaries', login_required(views.AwaitingPetitionSummaryListView.as_view()), name='awaitingsummary'),
    path('petitionsummary/create/', login_required(views.PetitionSummaryCreateView.as_view()), name='petitionsummary_create'),
    path('petitionsummary/detail/<int:pk>/', login_required(views.PetitionSummaryDetailView.as_view()), name='petitionsummary_detail'),
    path('petitionsummary/update/<int:pk>/', login_required(views.PetitionSummaryUpdateView.as_view()), name='petitionsummary_update'),
    path('petitionsummary/print/<int:pk>/', login_required(views.GeneratePetitionSummary), name='petitionsummary_print'),

    # urls for HearingSummary
    path('hearingsummary/', login_required(views.HearingSummaryListView.as_view()), name='hearingsummary_list'),
    path('hearingsummary/awaiting-hearing', login_required(views.AwaitingHearingSummaryListView.as_view()), name='awaitinghearing'),
    path('hearingsummary/deferred', login_required(views.HearingSummaryDeferredListView.as_view()), name='hearingsummary_deferred'),
    path('hearingsummary/declined', login_required(views.HearingSummaryDeclinedListView.as_view()), name='hearingsummary_declined'),
    path('hearingsummary/scheduled-for-interview', login_required(views.HearingSummaryScheduledforInterviewListView.as_view()), name='hearingsummary_scheduledforinterview'),
    path('hearingsummary/awaiting-schedule-for-interview', login_required(views.HearingSummaryAwaitingScheduleforInterviewListView.as_view()), name='hearingsummary_awaitingscheduleforinterview'),
    path('hearingsummary/create/', login_required(views.HearingSummaryCreateView.as_view()),name='hearingsummary_create'),
    path('hearingsummary/detail/<int:pk>/', login_required(views.HearingSummaryDetailView.as_view()),name='hearingsummary_detail'),
    path('hearingsummary/update/<int:pk>/', login_required(views.HearingSummaryUpdateView.as_view()),name='hearingsummary_update'),
    path('hearingsummary/print/<int:pk>/', login_required(views.GenerateHearingForm),name='hearingsummary_print'),

    # urls for InterviewSummary
    path('interviewsummary/', login_required(views.InterviewSummaryListView.as_view()),name='interviewsummary_list'),
    path('interviewsummary/awaiting-interviews', login_required(views.AwaitingInterviewFormListView.as_view()),name='awaitinginterviws'),
    path('interviewsummary/recommended', login_required(views.InterviewSummaryRecommendedListView.as_view()),name='interviewsummary_recommended'),
    path('interviewsummary/notrecommended', login_required(views.InterviewSummaryNotRecommendedListView.as_view()),name='interviewsummary_notrecommended'),
    path('interviewsummary/create/', login_required(views.InterviewSummaryCreateView.as_view()),name='interviewsummary_create'),
    path('interviewsummary/detail/<int:pk>/', login_required(views.InterviewSummaryDetailView.as_view()),name='interviewsummary_detail'),
    path('interviewsummary/update/<int:pk>/', login_required(views.InterviewSummaryUpdateView.as_view()),name='interviewsummary_update'),
    path('interviewsummary/print/<int:pk>/', login_required(views.GenerateInterviewSummary),name='interviewsummary_print'),

# urls for RecommendationForm
    path('recommendationform/', login_required(views.RecommendationFormListView.as_view()), name='recommendationform_list'),
    path('recommendationform/awaiting-recommendation', login_required(views.AwaitingRecommendationFormListView.as_view()), name='awaitingrecommendations'),
    path('recommendationform/create/', login_required(views.RecommendationFormCreateView.as_view()), name='recommendationform_create'),
    path('recommendationform/detail/<int:pk>/', login_required(views.RecommendationFormDetailView.as_view()), name='recommendationform_detail'),
    path('recommendationform/update/<int:pk>/', login_required(views.RecommendationFormUpdateView.as_view()), name='recommendationform_update'),
    path('recommendationform/print/<int:pk>/', login_required(views.GenerateRecommendationForm), name='recommendationform_print'),

    # urls for County
    path('petitions/county/', login_required(views.CountyListView.as_view()), name='petitions_county_list'),
    path('petitions/county/create/', login_required(views.CountyCreateView.as_view()), name='petitions_county_create'),
    path('petitions/county/detail/<int:pk>/', login_required(views.CountyDetailView.as_view()), name='petitions_county_detail'),
    path('petitions/county/update/<int:pk>/', login_required(views.CountyUpdateView.as_view()), name='petitions_county_update'),

    # urls for SubCounty
    path('petitions/subcounty/', login_required(views.SubCountyListView.as_view()), name='petitions_subcounty_list'),
    path('petitions/subcounty/create/', login_required(views.SubCountyCreateView.as_view()), name='petitions_subcounty_create'),
    path('petitions/subcounty/detail/<int:pk>/', login_required(views.SubCountyDetailView.as_view()),name='petitions_subcounty_detail'),
    path('petitions/subcounty/update/<int:pk>/', login_required(views.SubCountyUpdateView.as_view()),name='petitions_subcounty_update'),
    path('ajax/load-subcounties/', login_required(views.load_subcounties), name='ajax_load_subcounties'),  # <-- this one here

    #url for the
    path('petitions/dashboard/', login_required(views.dashboard), name='petitions_dashboard'),
]

