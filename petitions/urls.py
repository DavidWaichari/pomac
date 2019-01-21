from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views


urlpatterns = [
    # urls for PetitionForm
    path('petitionform/', login_required(views.PetitionFormListView.as_view()), name='petitionform_list'),
    path('', login_required(views.dashboard), name='petitions_dashboard'),
    path('petitionform/create/',login_required(views.PetitionFormCreateView.as_view()),name='petitionform_create'),
    path('petitionform/detail/<int:pk>/', login_required(views.PetitionFormDetailView.as_view()),name='petitionform_detail'),
    path('petitionform/update/<int:pk>/', login_required(views.PetitionFormUpdateView.as_view()),name='petitionform_update'),
    path('petitionform/ineligible', login_required(views.PetitionFormIneligibleListView.as_view()), name='petitionform_ineligible'),
    path('petitionform/eligible', login_required(views.PetitionFormEligibleListView.as_view()), name='petitionform_eligible'),
    path('petitionform/print/<int:pk>/', login_required(views.GeneratePetitionForm),name='petitionform_print'),
    path('petitionform/my-petitions', login_required(views.MyPetitionFormListView.as_view()), name='mypetitionform_list'),
    path('petitionform/my-eligible-petitions', login_required(views.MyEligiblePetitionFormListView.as_view()), name='myeligiblepetitionform_list'),
    path('petitionform/my-ineligle-petitions', login_required(views.MyInEligiblePetitionFormListView.as_view()), name='myineligiblepetitionform_list'),
    path('petitionform/delete/<int:pk>/', login_required(views.DeletePetitionForm),name='petitionform_delete'),
    path('petitionform/status', login_required(views.PetitionFormStatusListView.as_view()), name='petitionformstatus_list'),
    path('petitionform/duplicates-finder', login_required(views.PetitionFormDuplicatesFinderView), name='duplicates_finder'),

    # urls for Admissibility Form
    path('admissibilityform/', login_required(views.AdmissibilityFormListView.as_view()), name='admissibilityform_list'),
    path('admissibilityform/awaiting-admissibility', login_required(views.AwaitingAdmissibilityFormListView.as_view()), name='awaitingadmissibility'),
    path('admissibilityform/admissible', login_required(views.AdmissibilityFormAdmissibleListView.as_view()), name='admissibilityformadmissible_list'),
    path('admissibilityform/inadmissible', login_required(views.AdmissibilityFormInAdmissibleListView.as_view()), name='admissibilityformaindmissible_list'),
    path('admissibilityform/create/', login_required(views.AdmissibilityFormCreateView.as_view()), name='admissibilityform_create'),
    path('admissibilityform/detail/<int:pk>/', login_required(views.AdmissibilityFormDetailView.as_view()), name='admissibilityform_detail'),
    path('admissibilityform/update/<int:pk>/', login_required(views.AdmissibilityFormUpdateView.as_view()), name='admissibilityform_update'),
    path('admissibilityform/print/<int:pk>/', login_required(views.GenerateAdmissibilityForm), name='admissibilityform_print'),
    path('admissibilityform/my-admissibilities', login_required(views.MyAdmissibilityFormListView.as_view()), name='myadmissibilityform_list'),
    path('admissibilityform/my-admissible-admissibilities', login_required(views.MyAdmissibleAdmissibilityFormListView.as_view()), name='myadmissibleadmissibilityform_list'),
    path('admissibilityform/my-inadmissible-admissibilities', login_required(views.MyInAdmissibleAdmissibilityFormListView.as_view()), name='myinadmissibleadmissibilityform_list'),
    path('admissibilityform/my-awaiting-admissibility', login_required(views.MyAwaitingAdmissibilityFormListView.as_view()), name='myawaitingadmissibility'),
    path('admissibilityform/delete/<int:pk>/', login_required(views.DeleteAdmissibility), name='admissibilityform_delete'),

    # urls for PetitionSummary
    path('petitionsummary/', login_required(views.PetitionSummaryListView.as_view()), name='petitionsummary_list'),
    path('petitionsummary/awaiting-summaries', login_required(views.AwaitingPetitionSummaryListView.as_view()), name='awaitingsummary'),
    path('petitionsummary/create/', login_required(views.PetitionSummaryCreateView.as_view()), name='petitionsummary_create'),
    path('petitionsummary/detail/<int:pk>/', login_required(views.PetitionSummaryDetailView.as_view()), name='petitionsummary_detail'),
    path('petitionsummary/update/<int:pk>/', login_required(views.PetitionSummaryUpdateView.as_view()), name='petitionsummary_update'),
    path('petitionsummary/print/<int:pk>/', login_required(views.GeneratePetitionSummary), name='petitionsummary_print'),
    path('petitionsummary/my-summaries', login_required(views.MyPetitionSummaryListView.as_view()), name='mypetitionsummary_list'),
    path('petitionsummary/my-awaiting-summaries', login_required(views.MyAwaitingPetitionSummaryListView.as_view()), name='myawaitingsummary'),
    path('petitionsummary/delete/<int:pk>/', login_required(views.DeletePetitionSummary), name='petitionsummary_delete'),

    # urls for HearingSummary
    path('hearingsummary/', login_required(views.HearingSummaryListView.as_view()), name='hearingsummary_list'),
    path('hearingsummary/awaiting-schedule-for-hearing', login_required(views.AwaitingScheduleforHearingSummaryListView.as_view()), name='awaitingscheduleforhearing'),
    path('hearingsummary/awaiting-hearing', login_required(views.AwaitingHearingSummaryListView.as_view()), name='awaitinghearing'),
    path('hearingsummary/deferred', login_required(views.HearingSummaryDeferredListView.as_view()), name='hearingsummary_deferred'),
    path('hearingsummary/declined', login_required(views.HearingSummaryDeclinedListView.as_view()), name='hearingsummary_declined'),
    path('hearingsummary/scheduled-for-interview', login_required(views.HearingSummaryScheduledforInterviewListView.as_view()), name='hearingsummary_scheduledforinterview'),
    path('hearingsummary/awaiting-schedule-for-interview', login_required(views.HearingSummaryAwaitingScheduleforInterviewListView.as_view()), name='hearingsummary_awaitingscheduleforinterview'),
    path('hearingsummary/create/', login_required(views.HearingSummaryCreateView.as_view()),name='hearingsummary_create'),
    path('hearingsummary/detail/<int:pk>/', login_required(views.HearingSummaryDetailView.as_view()),name='hearingsummary_detail'),
    path('hearingsummary/update/<int:pk>/', login_required(views.HearingSummaryUpdateView.as_view()),name='hearingsummary_update'),
    path('hearingsummary/print/<int:pk>/', login_required(views.GenerateHearingForm),name='hearingsummary_print'),
    path('hearingsummary/my-hearing-summary', login_required(views.MyHearingSummaryListView.as_view()), name='myhearingsummary_list'),
    path('hearingsummary/my-schedule-for-interview', login_required(views.MyHearingSummaryScheduledforInterviewListView.as_view()), name='myhearingsummary_scheduledforinterview'),
    path('hearingsummary/myawaiting-schedule-for-interview', login_required(views.MyHearingSummaryAwaitingScheduleforInterviewListView.as_view()), name='myhearingsummary_awaitingscheduleforinterview'),
    path('hearingsummary/my-awaiting-hearing', login_required(views.MyAwaitingHearingSummaryListView.as_view()), name='myawaitinghearing'),
    path('hearingsummary/my-deferred-hearings', login_required(views.MyHearingSummaryDeferredListView.as_view()), name='myhearingsummary_deferred'),
    path('hearingsummary/my-declined-hearings', login_required(views.MyHearingSummaryDeclinedListView.as_view()), name='myhearingsummary_declined'),
    path('hearingsummary/delete/<int:pk>/', login_required(views.DeleteHearing),name='hearingsummary_delete'),

    # urls for InterviewSummary
    path('interviewsummary/', login_required(views.InterviewSummaryListView.as_view()),name='interviewsummary_list'),
    path('interviewsummary/filtered-by-date', login_required(views.FilterInterviewsByDate),name='interviewsummary_filterbydatelist'),
    path('interviewsummary/filtered-master-by-date', login_required(views.FilterMasterInteviewsByDate),name='interviewsummary_filtermasterbydatelist'),
    path('interviewsummary/master-recommendations', login_required(views.MasterInterviewsListView.as_view()),name='interviewsummary_master_list'),
    path('interviewsummary/awaiting-interviews', login_required(views.AwaitingInterviewFormListView.as_view()),name='awaitinginterviws'),
    path('interviewsummary/recommended', login_required(views.InterviewSummaryRecommendedListView.as_view()),name='interviewsummary_recommended'),
    path('interviewsummary/notrecommended', login_required(views.InterviewSummaryNotRecommendedListView.as_view()),name='interviewsummary_notrecommended'),
    path('interviewsummary/create/', login_required(views.InterviewSummaryCreateView.as_view()),name='interviewsummary_create'),
    path('interviewsummary/detail/<int:pk>/', login_required(views.InterviewSummaryDetailView.as_view()),name='interviewsummary_detail'),
    path('interviewsummary/update/<int:pk>/', login_required(views.InterviewSummaryUpdateView.as_view()),name='interviewsummary_update'),
    path('interviewsummary/print/<int:pk>/', login_required(views.GenerateInterviewSummary),name='interviewsummary_print'),
    path('interviewsummary/my-interviews', login_required(views.MyInterviewSummaryListView.as_view()),name='myinterviewsummary_list'),
    path('interviewsummary/my-petitions-awaiting-interview', login_required(views.MyAwaitingInterviewFormListView.as_view()),name='myawaitinginterviws'),
    path('interviewsummary/my-recommendations', login_required(views.MyInterviewSummaryRecommendedListView.as_view()),name='myinterviewsummary_recommended'),
    path('interviewsummary/my-not-recommended', login_required(views.myInterviewSummaryNotRecommendedListView.as_view()),name='myinterviewsummary_notrecommended'),
    path('interviewsummary/delete/<int:pk>/', login_required(views.DeleteInterviewSummary),name='interviewsummary_delete'),

    # urls for RecommendationForm
    path('recommendationform/', login_required(views.RecommendationFormListView.as_view()), name='recommendationform_list'),
    path('recommendationform/awaiting-recommendation', login_required(views.AwaitingRecommendationFormListView.as_view()), name='awaitingrecommendations'),
    path('recommendationform/create/', login_required(views.RecommendationFormCreateView.as_view()), name='recommendationform_create'),
    path('recommendationform/detail/<int:pk>/', login_required(views.RecommendationFormDetailView.as_view()), name='recommendationform_detail'),
    path('recommendationform/update/<int:pk>/', login_required(views.RecommendationFormUpdateView.as_view()), name='recommendationform_update'),
    path('recommendationform/print/<int:pk>/', login_required(views.GenerateRecommendationForm), name='recommendationform_print'),
    path('recommendationform/my-recommendations', login_required(views.MyRecommendationFormListView.as_view()), name='myrecommendationform_list'),
    path('recommendationform/my-awaiting-recommendation', login_required(views.MyAwaitingRecommendationFormListView.as_view()), name='myawaitingrecommendations'),
    path('recommendationform/delete/<int:pk>/', login_required(views.DeleteRecommendationForm), name='recommendationform_delete'),
    path('recommendationform/master', login_required(views.MasterRecommendationFormListView.as_view()),name='master_recommendationform_list'),
    path('ajax/get-circumstance-from-summary/', login_required(views.get_circumstance_from_summary), name='getcircumstance'),

    # urls for County
    path('county/', login_required(views.CountyListView.as_view()), name='petitions_county_list'),
    path('county/create/', login_required(views.CountyCreateView.as_view()), name='petitions_county_create'),
    path('county/detail/<int:pk>/', login_required(views.CountyDetailView.as_view()), name='petitions_county_detail'),
    path('county/update/<int:pk>/', login_required(views.CountyUpdateView.as_view()), name='petitions_county_update'),
    path('county/petitioners/<int:pk>/', login_required(views.CountyPetitionersListView), name='countypetitioners'),

    # urls for SubCounty
    path('subcounty/', login_required(views.SubCountyListView.as_view()), name='petitions_subcounty_list'),
    path('subcounty/create/', login_required(views.SubCountyCreateView.as_view()), name='petitions_subcounty_create'),
    path('subcounty/detail/<int:pk>/', login_required(views.SubCountyDetailView.as_view()),name='petitions_subcounty_detail'),
    path('subcounty/update/<int:pk>/', login_required(views.SubCountyUpdateView.as_view()),name='petitions_subcounty_update'),
    path('ajax/load-subcounties/', login_required(views.load_subcounties), name='ajax_load_subcounties'),  # <-- this one here

    # urls for Exit
    path('exit/', login_required(views.ExitListView.as_view()), name='petitions_exit_list'),
    path('exit/create/', login_required(views.ExitCreateView.as_view()), name='petitions_exit_create'),
    path('exit/detail/<int:pk>/', login_required(views.ExitDetailView.as_view()), name='petitions_exit_detail'),
    path('exit/update/<int:pk>/', login_required(views.ExitUpdateView.as_view()), name='petitions_exit_update'),
    path('exit/ecapes', login_required(views.ExitEscapeListView.as_view()), name='petitions_exitescape_list'),
    path('exit/deaths', login_required(views.ExitDeathsListView.as_view()), name='petitions_exitdeaths_list'),
    path('exit/pomac', login_required(views.ExitReleasedUnderPomacListView.as_view()), name='petitions_exitpomac_list'),
    path('exit/served-term', login_required(views.ExitServedTermListView.as_view()), name='petitions_exitservedterm_list'),
    path('exit/resentencing', login_required(views.ExitAfterResentencingListView.as_view()), name='petitions_exitresentencing_list'),
    path('exit/delete/<int:pk>/', login_required(views.DeleteExit), name='petitions_exit_delete'),

    # urls for Prison
    path('petitions/prison/', login_required(views.PrisonListView.as_view()), name='petitions_prison_list'),
    path('petitions/prison/create/', login_required(views.PrisonCreateView.as_view()), name='petitions_prison_create'),
    path('petitions/prison/detail/<int:pk>/', login_required(views.PrisonDetailView.as_view()), name='petitions_prison_detail'),
    path('petitions/prison/update/<int:pk>/', login_required(views.PrisonUpdateView.as_view()), name='petitions_prison_update'),
    path('petitions/prison/petitioners/<int:pk>/', login_required(views.PrisonPetitionersListView), name='prisonpetitioners'),
    path('petitions/prison/current-petitioners/<int:pk>/', login_required(views.CurrentPrisonPetitionersListView), name='current_prisonpetitioners'),
    path('petitions/prison/delete/<int:pk>/', login_required(views.DeletePrison), name='petitions_prison_delete'),

    # urls for Court
    path('petitions/court/', login_required(views.CourtListView.as_view()), name='petitions_court_list'),
    path('petitions/court/create/', login_required(views.CourtCreateView.as_view()), name='petitions_court_create'),
    path('petitions/court/detail/<int:pk>/', login_required(views.CourtDetailView.as_view()), name='petitions_court_detail'),
    path('petitions/court/update/<int:pk>/', login_required(views.CourtUpdateView.as_view()), name='petitions_court_update'),
    path('petitions/court/delete/<int:pk>/', login_required(views.DeleteCourt),name='petitions_court_delete'),
    path('petitions/court/petitions/<int:pk>/', login_required(views.CourtPetitionersListView),name='court_petitioners_list'),

    # urls for Offence
    path('petitions/offence/', login_required(views.OffenceListView.as_view()), name='petitions_offence_list'),
    path('petitions/offence/create/', login_required(views.OffenceCreateView.as_view()), name='petitions_offence_create'),
    path('petitions/offence/detail/<int:pk>/', login_required(views.OffenceDetailView.as_view()), name='petitions_offence_detail'),
    path('petitions/offence/update/<int:pk>/', login_required(views.OffenceUpdateView.as_view()), name='petitions_offence_update'),
    path('petitions/offence/petitioners/<int:pk>/', login_required(views.OffencePetitioners), name='offencepetitioners'),
    path('petitions/offence/delete/<int:pk>/', login_required(views.DeleteOffence), name='petitions_offence_delete'),

    # urls for Grant
    path('petitions/grant/', views.GrantListView.as_view(), name='petitions_grant_list'),
    path('petitions/grant/create/', views.GrantCreateView.as_view(), name='petitions_grant_create'),
    path('petitions/grant/detail/<int:pk>/', views.GrantDetailView.as_view(), name='petitions_grant_detail'),
    path('petitions/grant/delete/<int:pk>/', views.DeleteGrant, name='petitions_grant_delete'),
    path('petitions/grant/awaiting-grant', views.AwaitingGrantListView.as_view(), name='petitions_awaiting_grant_list'),
    path('petitions/grant/print/<int:pk>/', login_required(views.GenerateGrant), name='grantpetition_print'),
    path('petitions/grant/my-grants', login_required(views.MyGrantListView.as_view()), name='mypetitions_grant_list'),
    path('petitions/grant/my-awaiting-grant', views.MyAwaitingGrantListView.as_view(), name='mypetitions_awaiting_grant_list'),
    #url for the
    path('dashboard/', login_required(views.dashboard), name='petitions_dashboard'),
    path('my-dashboard/', login_required(views.mydashboard), name='mypetitions_dashboard'),
    path('petitionform/trustees', login_required(views.TrusteesListView.as_view()), name='trustees'),
    path('petitionform/special-condition', login_required(views.SpecialConditionListView.as_view()), name='specialcondition'),
    path('petitionform/appealed-against-conviction', login_required(views.AppealedAgainstConvictionView.as_view()), name='appealedagainstconviction'),
    path('petitionform/petitioners-with-skills', login_required(views.PetitionersWithSkillsView.as_view()), name='specialattributesorskills'),
    path('petitionform/foreigners', login_required(views.ForeignersListView.as_view()), name='foreigners_list'),
    path('petitionform/pp-mental', login_required(views.PPMentalListView.as_view()), name='ppmental_list'),
    path('petitionform/pp-underage', login_required(views.PPUnderAgelListView.as_view()), name='ppunderage_list'),
    path('petitionform/filter-petitions-by-date', login_required(views.FilterPetitionsByDate), name='filterpetitionsbydate'),
    path('admissibilityform/filter-admissibilities-by-date', login_required(views.FilterAdmissibilitiesByDate), name='filteradmissibilitiesbydate'),
    path('petitionsummary/filter-summaries-by-date', login_required(views.SummariesByDate), name='filtersummariesbydate'),
    path('petitionshearings/filter-hearings-by-date', login_required(views.FilterHearingsByDate), name='filterhearingsbydate'),

]

