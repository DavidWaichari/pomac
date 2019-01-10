from datetime import date, datetime, timedelta

import sweetify
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, request, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.dateparse import parse_date
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

from users.models import CustomUser
from .models import PetitionForm, AdmissibilityForm, HearingSummary, InterviewSummary, RecommendationForm, \
    PetitionSummary, County, SubCounty, Exit, Prison, Court, Offence, Grant, Count
from .forms import PetitionFormForm, HearingSummaryForm, InterviewSummaryForm, InterviewSummaryEditForm, \
    RecommendationFormForm, \
    AdmissibilityCreateForm, AdmissibilityUpdateForm, HearingSummaryUpdateForm, RecommendationUpdateForm, \
    PetitionSummaryForm, PetitionSummaryEditForm, CountyForm, SubCountyForm, ExitForm, ExitFormUpdate, PrisonForm, \
    CourtForm, OffenceForm, GrantForm, PetitionsDateFilterForm, AdmissibilitiesDateFilterForm,SummariesDateFilterForm,HearingsDateFilterForm
from djangox.utils import render_to_pdf  # created in step 4


class CountyListView(ListView):
    template_name = 'petitions/counties/county_list.html'
    model = County
    def get_queryset(self):
        queryset = County.objects.order_by('name')
        return queryset

def CountyPetitionersListView(request, pk):
    county = County.objects.get(id=pk)
    object_list = PetitionForm.objects.filter(county_id=pk).filter(anypendingcourtmatter=False)
    return render(request,'petitions/counties/coutypetitioners_list.html',{'object_list':object_list, 'county':county})


class CountyCreateView(PermissionRequiredMixin,CreateView):
    template_name = 'petitions/counties/county_form.html'
    permission_required = 'petitions.add_county'
    model = County
    form_class = CountyForm
    success_message = "County added successfully."
    def form_valid(self, form):
         instance = form.save(commit=False)
         instance.added_by = CustomUser.objects.get(id=self.request.user.id)
         instance.save()
         messages.success(self.request, self.success_message)
         return  redirect ('petitions_county_detail', instance.id)

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_county'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(CountyCreateView, self).dispatch(request, *args, **kwargs)

class CountyDetailView(DetailView):
    template_name = 'petitions/counties/county_detail.html'
    model = County


class CountyUpdateView(UpdateView):
    template_name = 'petitions/counties/county_form.html'
    model = County
    form_class = CountyForm
    success_message = 'County details updated successfully'
    def form_valid(self, form):
        county = form.save(commit=False)
        county.save()
        messages.success(self.request, self.success_message)
        return redirect('petitions_county_detail', county.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.change_county'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(CountyUpdateView, self).dispatch(request, *args, **kwargs)


def load_subcounties(request):
    county_id = request.GET.get('county')
    subcounties = SubCounty.objects.filter(county_id=county_id).order_by('name')
    return render(request, 'petitions/subcounties/subcountiesdropdown.html', {'subcounties': subcounties})

class SubCountyListView(ListView):
    template_name = 'petitions/subcounties/subcounty_list.html'
    model = SubCounty
    def get_queryset(self):
        queryset = SubCounty.objects.order_by('name')
        return queryset


class SubCountyCreateView(CreateView):
    template_name = 'petitions/subcounties/subcounty_form.html'
    model = SubCounty
    form_class = SubCountyForm
    success_message = "Sub County added successfully."
    def form_valid(self, form):
         instance = form.save(commit=False)
         instance.added_by = CustomUser.objects.get(id=self.request.user.id)
         instance.save()
         messages.success(self.request, self.success_message)
         return  redirect ('petitions_subcounty_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_subcounty'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(SubCountyCreateView, self).dispatch(request, *args, **kwargs)


class SubCountyDetailView(DetailView):
    template_name = 'petitions/subcounties/subcounty_detail.html'
    model = SubCounty


class SubCountyUpdateView(UpdateView):
    template_name = 'petitions/subcounties/subcounty_form.html'
    model = SubCounty
    form_class = SubCountyForm
    success_message = "Sub County updated successfully."

    def form_valid(self, form):
        subcounty = form.save(commit=False)
        subcounty.save()
        messages.success(self.request, self.success_message)
        return redirect('petitions_subcounty_detail', subcounty.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.change_subcounty'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(SubCountyUpdateView, self).dispatch(request, *args, **kwargs)

class PrisonListView(ListView):
    template_name = 'petitions/prisons/prison_list.html'
    model = Prison
    def get_queryset(self):
        queryset = Prison.objects.order_by('name')
        return queryset


def PrisonPetitionersListView(request, pk):
    prison = Prison.objects.get(id=pk)
    object_list = PetitionForm.objects.filter(prison_id=pk).filter(anypendingcourtmatter=False)
    return render(request,'petitions/prisons/prisonpetitioners_list.html',{'object_list':object_list, 'prison':prison, 'today':date.today()})

def CurrentPrisonPetitionersListView(request, pk):
    prison = Prison.objects.get(id=pk)
    object_list = PetitionForm.objects.filter(prison_id=pk).filter(anypendingcourtmatter=False).filter(exit__isnull=True)
    return render(request,'petitions/prisons/prisonpetitioners_current_list.html',{'object_list':object_list, 'prison':prison, 'today':date.today()})


class PrisonCreateView(CreateView):
    template_name = 'petitions/prisons/prison_form.html'
    model = Prison
    form_class = PrisonForm

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_prison'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PrisonCreateView, self).dispatch(request, *args, **kwargs)


class PrisonDetailView(DetailView):
    template_name = 'petitions/prisons/prison_detail.html'
    model = Prison


class PrisonUpdateView(UpdateView):
    template_name = 'petitions/prisons/prison_form.html'
    model = Prison
    form_class = PrisonForm
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.change_prison'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PrisonUpdateView, self).dispatch(request, *args, **kwargs)

@permission_required ('petitions.delete_prison', raise_exception=True)
def DeletePrison(request,pk):
    Prison.objects.get(pk=pk).delete()
    sweetify.success(request, 'Prison Deleted Successfully', button=True, timer=15000)
    return redirect('petitions_prison_list')


class CourtListView(ListView):
    template_name = 'petitions/courts/court_list.html'
    model = Court
    def get_queryset(self):
        queryset = Court.objects.order_by('name')
        return queryset


class CourtCreateView(CreateView):
    template_name = 'petitions/courts/court_form.html'
    model = Court
    form_class = CourtForm
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_court'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(CourtCreateView, self).dispatch(request, *args, **kwargs)


class CourtDetailView(DetailView):
    template_name = 'petitions/courts/court_detail.html'
    model = Court


class CourtUpdateView(UpdateView):
    template_name = 'petitions/courts/court_form.html'
    model = Court
    form_class = CourtForm

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.change_court'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(CourtUpdateView, self).dispatch(request, *args, **kwargs)


def CourtPetitionersListView(request, pk):
    court = Court.objects.get(id=pk)
    object_list = PetitionForm.objects.filter(court_id=pk).filter(anypendingcourtmatter=False)
    return render(request,'petitions/courts/court_petitioners_list.html',{'object_list':object_list, 'court': court, 'today':date.today()})

@permission_required ('petitions.delete_court', raise_exception=True)
def DeleteCourt(request,pk):
    Court.objects.get(pk=pk).delete()
    sweetify.success(request, 'Court Deleted Successfully', button=True, timer=15000)
    return redirect('petitions_court_list')



class OffenceListView(ListView):
    template_name = 'petitions/offences/offence_list.html'
    model = Offence
    def get_queryset(self):
        queryset = Offence.objects.order_by('name')
        return queryset

def OffencePetitioners(request, pk):
    offence = Offence.objects.get(pk=pk)
    object_list = PetitionForm.objects.filter(offence_id=pk)
    data = {
        'offence':offence,
        'object_list':object_list,
        'today':date.today()
    }
    return  render(request, 'petitions/offences/offencepetitions_list.html', data)




class OffenceCreateView(CreateView):
    template_name = 'petitions/offences/offence_form.html'
    model = Offence
    form_class = OffenceForm

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_offence'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(OffenceCreateView, self).dispatch(request, *args, **kwargs)


class OffenceDetailView(DetailView):
    template_name = 'petitions/offences/offence_detail.html'
    model = Offence


class OffenceUpdateView(UpdateView):
    template_name = 'petitions/offences/offence_form.html'
    model = Offence
    form_class = OffenceForm

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.change_offence'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(OffenceUpdateView, self).dispatch(request, *args, **kwargs)

@permission_required ('petitions.delete_offence', raise_exception=True)
def DeleteOffence(request,pk):
    Offence.objects.get(pk=pk).delete()
    sweetify.success(request, 'Offence Deleted Successfully', button=True, timer=15000)
    return redirect('petitions_offence_list')



class PetitionFormListView(ListView):
    model = PetitionForm
    template_name = 'petitions/petition_form/petitionform_list.html'
    def get_context_data(self, **kwargs):
        context = super(PetitionFormListView, self).get_context_data(**kwargs)
        today = date.today()
        petitionsdatefilterform = PetitionsDateFilterForm
        context['today'] =today
        context['form'] = petitionsdatefilterform
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_petitionforms'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PetitionFormListView, self).dispatch(request, *args, **kwargs)

def FilterPetitionsByDate(request):
    if request.method == 'POST':
        form = PetitionsDateFilterForm(request.POST)
        if form.is_valid():
            filterdate = request.POST['reservation']
            daterange = filterdate.split("-")
            start = daterange[0]
            startdate = start.split("/")
            startfilterdate = datetime(int(startdate[2]),int(startdate[0]),int(startdate[1]))
            end = daterange[1]
            enddate = end.split("/")
            endfilterdatepassed = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))
            endfilterdate = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))+timedelta(days=1)

            object_list = PetitionForm.objects.filter(created__range=[startfilterdate.date(), endfilterdate.date()])

            context = {
                'startdate': startfilterdate.date(),
                'enddate': endfilterdatepassed.date(),
                'form':PetitionsDateFilterForm,
                'today': date.today(),
                'object_list' : object_list
            }
            return render(request, 'petitions/petition_form/filteredpetitionsbydate_list.html',context)
        return  redirect('petitionform_list')
    else:
        return redirect('petitionform_list')

class PetitionFormStatusListView(ListView):
    model = PetitionForm
    template_name = 'petitions/petitionstatus_list.html'
    def get_context_data(self, **kwargs):
        context = super(PetitionFormStatusListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] =today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_petitionformstatus'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PetitionFormStatusListView, self).dispatch(request, *args, **kwargs)

@permission_required ('petitions.can_view_duplicatesfinder', raise_exception=True)
def PetitionFormDuplicatesFinderView(request):
    duplicates = PetitionForm.objects.values('name').annotate(Count('id')) .order_by().filter(id__count__gt=1)
    duprecords = PetitionForm.objects.filter(name__in=[item['name'] for item in duplicates])
    data = {
        'today':date.today(),
        'object_list': duprecords
    }
    return render(request,'petitions/duplicatesfinder.html', data)


class MyPetitionFormListView(ListView):
    model = PetitionForm
    template_name = 'petitions/petition_form/mypetitionform_list.html'
    def get_context_data(self, **kwargs):
        context = super(MyPetitionFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] =today
        return context
    def get_queryset(self):
        queryset = super(MyPetitionFormListView, self).get_queryset()
        queryset = queryset.filter(added_by = self.request.user)
        return queryset

class MyEligiblePetitionFormListView(ListView):
    model = PetitionForm
    template_name = 'petitions/petition_form/myeligiblepetitionform_list.html'
    def get_context_data(self, **kwargs):
        context = super(MyEligiblePetitionFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] =today
        return context
    def get_queryset(self):
        queryset = super(MyEligiblePetitionFormListView, self).get_queryset()
        queryset = queryset.filter(anypendingcourtmatter=False).filter(added_by = self.request.user)
        return queryset

class MyInEligiblePetitionFormListView(ListView):
    model = PetitionForm
    template_name = 'petitions/petition_form/myineligiblepetitionform_list.html'
    def get_context_data(self, **kwargs):
        context = super(MyInEligiblePetitionFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] =today
        return context
    def get_queryset(self):
        queryset = super(MyInEligiblePetitionFormListView, self).get_queryset()
        queryset = queryset.filter(anypendingcourtmatter=True).filter(added_by = self.request.user)
        return queryset

class PetitionFormIneligibleListView(ListView):
    model = PetitionForm
    template_name = 'petitions/petition_form/petitionform_ineligible.html'
    def get_queryset(self):
        queryset = super(PetitionFormIneligibleListView, self).get_queryset()
        queryset = queryset.filter(anypendingcourtmatter=True)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(PetitionFormIneligibleListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_petitionforms'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PetitionFormIneligibleListView, self).dispatch(request, *args, **kwargs)


class PetitionFormEligibleListView(ListView):
    model = PetitionForm
    template_name = 'petitions/petition_form/petitionform_eligible.html'
    def get_queryset(self):
        queryset = super(PetitionFormEligibleListView, self).get_queryset()
        queryset = queryset.filter(anypendingcourtmatter=False)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(PetitionFormEligibleListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_petitionforms'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PetitionFormEligibleListView, self).dispatch(request, *args, **kwargs)

class TrusteesListView(ListView):
    model = PetitionForm
    template_name = 'petitions/trustees_list.html'
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).filter(areyouatrustee=True)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(TrusteesListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context

class SpecialConditionListView(ListView):
    model = PetitionForm
    template_name = 'petitions/specialcondition_list.html'
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialcondition=True)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(SpecialConditionListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context

class ForeignersListView(ListView):
    model = PetitionForm
    template_name = 'petitions/foreigners_list.html'
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).exclude(nationality='Kenyan')
        return queryset
    def get_context_data(self, **kwargs):
        context = super(ForeignersListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context

class PPMentalListView(ListView):
    model = PetitionForm
    template_name = 'petitions/ppmental_list.html'
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialcondition=True).filter(ageatconviction__gte=18).filter(prisonno__endswith='P')
        return queryset
    def get_context_data(self, **kwargs):
        context = super(PPMentalListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context

class PPUnderAgelListView(ListView):
    model = PetitionForm
    template_name = 'petitions/ppunderage_list.html'
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialcondition=True).filter(ageatconviction__lt=18).filter(prisonno__endswith='P')
        return queryset
    def get_context_data(self, **kwargs):
        context = super(PPUnderAgelListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context



class AppealedAgainstConvictionView(ListView):
    model = PetitionForm
    template_name = 'petitions/appealedagainstconviction_list.html'
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).filter(appealedagainsttheconviction=True)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(AppealedAgainstConvictionView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context

class PetitionersWithSkillsView(ListView):
    model = PetitionForm
    template_name = 'petitions/skilledpetitioners_list.html'
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialattributesorskills=True)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(PetitionersWithSkillsView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context



class PetitionFormCreateView(CreateView):
    template_name = 'petitions/petition_form/petitionform_form.html'
    model = PetitionForm
    form_class = PetitionFormForm
    def form_valid(self, form):
         instance = form.save(commit=False)
         instance.added_by = CustomUser.objects.get(id=self.request.user.id)
         instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
         instance.save()
         sweetify.success(self.request, 'Petition submitted successfully', button=True, timer=15000)
         return  redirect ('petitionform_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=self.request.user.id)
        if(user.first_name == '' and user.last_name == ''):
            sweetify.warning(self.request, 'Please update your profile to submit a petition. Provide the firstname and lastname as they appear In the ID Card/B.C/Passport', button=True, timer=15000)
            return redirect('updateprofile',self.request.user.id)
        return super(PetitionFormCreateView, self).dispatch(request, *args, **kwargs)


class PetitionFormDetailView(DetailView):
    template_name = 'petitions/petition_form/petitionform_detail.html'
    model = PetitionForm
    def get_context_data(self, **kwargs):
        context = super(PetitionFormDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context

class PetitionFormUpdateView(UpdateView):
    template_name = 'petitions/petition_form/petitionform_update.html'
    model = PetitionForm
    form_class = PetitionFormForm
    def form_valid(self, form):
         instance = form.save(commit=False)
         instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
         instance.save()
         sweetify.success(self.request, 'Petition details updated successfully', button=True, timer=15000)
         return  redirect ('petitionform_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        petititionformtoupdate = PetitionForm.objects.get(pk=self.kwargs.get('pk'))
        petitiondate = petititionformtoupdate.created.date()
        if not petitiondate == date.today():
            """ Permission check for this class """
            if not request.user.has_perm('petitions.change_petitionform'):
                raise PermissionDenied("You do not have permission to delete events")
        else:
            if not request.user.has_perm('petitions.change_petitionform'):
                if not petititionformtoupdate.added_by == self.request.user:
                    raise PermissionDenied("You do not have permission to delete events")
        return super(PetitionFormUpdateView, self).dispatch(request, *args, **kwargs)


@permission_required ('petitions.delete_petitionform', raise_exception=True)
def DeletePetitionForm(request,pk):
    PetitionForm.objects.get(pk=pk).delete()
    sweetify.success(request, 'Petitione deleted successfully and all its related information', button=True, timer=15000)
    return redirect('petitionform_list')

class AdmissibilityFormListView(ListView):
    template_name = 'petitions/admissibility_form/admissibilityform_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(AdmissibilityFormListView, self).get_context_data(**kwargs)
        today = date.today()
        admissibilitydatefilter = AdmissibilitiesDateFilterForm
        context['today'] = today
        context['form'] = admissibilitydatefilter
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_admissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AdmissibilityFormListView, self).dispatch(request, *args, **kwargs)

def FilterAdmissibilitiesByDate(request):
    if request.method == 'POST':
        form = AdmissibilitiesDateFilterForm(request.POST)
        if form.is_valid():
            filterdate = request.POST['reservation']
            daterange = filterdate.split("-")
            start = daterange[0]
            startdate = start.split("/")
            startfilterdate = datetime(int(startdate[2]),int(startdate[0]),int(startdate[1]))
            end = daterange[1]
            enddate = end.split("/")
            endfilterdatepassed = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))
            endfilterdate = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))+timedelta(days=1)

            object_list = AdmissibilityForm.objects.filter(created__range=[startfilterdate.date(), endfilterdate.date()])

            context = {
                'startdate': startfilterdate.date(),
                'enddate': endfilterdatepassed.date(),
                'form':AdmissibilitiesDateFilterForm,
                'today': date.today(),
                'object_list' : object_list
            }
            return render(request, 'petitions/admissibility_form/filteredadmissibilitiesbydate_list.html',context)
        return  redirect('admissibilityform_list')
    else:
        return redirect('admissibilityform_list')

class MyAdmissibilityFormListView(ListView):
    template_name = 'petitions/admissibility_form/myadmissibilityform_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(MyAdmissibilityFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset=AdmissibilityForm.objects.filter(added_by= self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myadmissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAdmissibilityFormListView, self).dispatch(request, *args, **kwargs)

class MyAdmissibleAdmissibilityFormListView(ListView):
    template_name = 'petitions/admissibility_form/myadmissibleadmissibilityform_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(MyAdmissibleAdmissibilityFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset=AdmissibilityForm.objects.filter(added_by= self.request.user).filter(admissability=True)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myadmissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAdmissibleAdmissibilityFormListView, self).dispatch(request, *args, **kwargs)

class MyInAdmissibleAdmissibilityFormListView(ListView):
    template_name = 'petitions/admissibility_form/myinadmissibleadmissibilityform_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(MyInAdmissibleAdmissibilityFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset=AdmissibilityForm.objects.filter(added_by= self.request.user).filter(admissability=False)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myadmissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyInAdmissibleAdmissibilityFormListView, self).dispatch(request, *args, **kwargs)

class AwaitingAdmissibilityFormListView(ListView):
    template_name = 'petitions/admissibility_form/awaitingadmissibilityform_list.html'
    model = PetitionForm
    def get_context_data(self, **kwargs):
        context = super(AwaitingAdmissibilityFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset= PetitionForm.objects.filter(anypendingcourtmatter=False).filter(admissibilityform__isnull=True).filter(exit__isnull=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_admissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AwaitingAdmissibilityFormListView, self).dispatch(request, *args, **kwargs)

class MyAwaitingAdmissibilityFormListView(ListView):
    template_name = 'petitions/admissibility_form/myawaitingadmissibilityform_list.html'
    model = PetitionForm
    def get_context_data(self, **kwargs):
        context = super(MyAwaitingAdmissibilityFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = PetitionForm.objects.filter(anypendingcourtmatter=False).filter(admissibilityform__isnull=True).filter(
            exit__isnull=True).filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myadmissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAwaitingAdmissibilityFormListView, self).dispatch(request, *args, **kwargs)


@permission_required ('petitions.delete_admissibilityform', raise_exception=True)
def DeleteAdmissibility(request,pk):
    AdmissibilityForm.objects.get(pk=pk).delete()
    sweetify.success(request, 'Admissibility form for the petitioner deleted successfully and all consequent information ', button=True, timer=15000)
    return redirect('admissibilityform_list')

def GeneratePetitionForm(request, pk):
    petitioner = PetitionForm.objects.get(pk=pk)
    today = date.today()
    if petitioner.nextofkin== '':
        nextofkin = None
        relationshipwithnextofkin = None
    else:
        nextofkin = petitioner.nextofkin
        relationshipwithnextofkin = petitioner.relationshipwithnextofkin
    if petitioner.contactperson == '':
        contactperson = None
        contactpersontelno = None
    else:
        contactperson = petitioner.contactperson
        contactpersontelno = petitioner.telnoofcontactperson
    if petitioner.homechief == '':
        nameofhomechief = None
    else:
        nameofhomechief = petitioner.homechief
    if petitioner.dateofconviction.year - petitioner.dateofcustody.year == '':
        yearsinremand = 0
    else:
        yearsinremand = petitioner.dateofconviction.year - petitioner.dateofcustody.year
    if petitioner.sentence==None:
        sentence = 'LIFE IMPRISONMENT'
    else:
        sentence = str(petitioner.sentence)+' '+'YEARS IMPRISONMENT'
    if petitioner.chargedalonefortheoffense==True:
        chargedalone = 'YES'
    else:
        chargedalone = 'NO'
    if petitioner.namesofcoaccused=='':
        coaccused = 'None'
    else:
        coaccused = petitioner.namesofcoaccused
    if petitioner.knowledgeofthevictim== True:
        knowledgeofvictim = 'YES'
    else:
        knowledgeofvictim = 'NO'
    if petitioner.nameofvictim== '':
        nameofvictim = 'None'
    else:
        nameofvictim = petitioner.nameofvictim
    if petitioner.areaofresidence== '':
        areaofresidence = 'None'
    else:
        areaofresidence = petitioner.areaofresidence
    if petitioner.previousconvictions== '':
        previousconvictions = 'None'
    else:
        previousconvictions = petitioner.previousconvictions
    if petitioner.previouspetition== True:
        previouspetition = 'YES'
    else:
        previouspetition = 'NO'
    if petitioner.reasonofdenialofpreviouspetition== '':
        reasonofdenial = 'None'
    else:
        reasonofdenial = petitioner.reasonofdenialofpreviouspetition
    if petitioner.anydisplinaryactioninprison== True:
        disciplinaryaction = 'YES'
    else:
        disciplinaryaction = 'NO'
    if petitioner.detailsofdisplinaryactioninprison== '':
        explanationofdisciplinaryaction = 'None'
    else:
        explanationofdisciplinaryaction = petitioner.detailsofdisplinaryactioninprison
    if petitioner.anyspecialcondition== True:
        anyspecialcondition = 'YES'
    else:
        anyspecialcondition = 'NO'
    if petitioner.detailsofspecialcondition== '':
        explanationofspecialcondition = 'None'
    else:
        explanationofspecialcondition = petitioner.detailsofspecialcondition
    if petitioner.areyouatrustee== True:
        trustee = 'YES'
    else:
        trustee = 'NO'
    if petitioner.dateofpromotiontotrustee== '':
        trustedate = 'None'
    else:
        trustedate = petitioner.dateofpromotiontotrustee
    if petitioner.anyspecialattributesorskills== True:
        anyskills = 'YES'
    else:
        anyskills = 'NO'
    if petitioner.explanationofspecialattributesorskills== '':
        skillsexplanation = 'None'
    else:
        skillsexplanation = petitioner.explanationofspecialattributesorskills
    if petitioner.appealedagainsttheconviction== True:
        appealed = 'YES'
    else:
        appealed = 'NO'
    if petitioner.appealoutcome== '':
        appealoutcome = 'None'
    else:
        appealoutcome = petitioner.appealoutcome
    if petitioner.appealcaseno== '':
        appealcaseno = 'None'
    else:
        appealcaseno = petitioner.appealcaseno
    if petitioner.anypendingcourtmatter== True:
        pendingcourtmatter = 'YES'
    else:
        pendingcourtmatter = 'NO'
    if petitioner.explanationofpendingcourtmatter== '':
        pendingexplanation = 'None'
    else:
        pendingexplanation = petitioner.explanationofpendingcourtmatter
    if petitioner.nameofapplicant == '':
        nameofapplicant = 'None'
    else:
        nameofapplicant = petitioner.nameofapplicant
    if petitioner.relationshipofapplicantwithpetitioner == '':
        relationshipofapplicantwithpetitioner = 'None'
    else:
        relationshipofapplicantwithpetitioner = petitioner.relationshipofapplicantwithpetitioner
    if petitioner.addressoftheapplicant == '':
        addressoftheapplicant = 'None'
    else:
        addressoftheapplicant = petitioner.addressoftheapplicant
    if petitioner.telephonenumberoftheapplicant == '':
        telephonenumberoftheapplicant = 'None'
    else:
        telephonenumberoftheapplicant = petitioner.telephonenumberoftheapplicant
    petitiondate = petitioner.created
    data = {
        'name': petitioner.name,
        'prisonno':petitioner.prisonno,
        'created_at': petitioner.created,
        'prison': petitioner.prison,
        'nationality': petitioner.nationality,
        'court': petitioner.court,
        'courtno': petitioner.courtcaseno,
        'ageatconviction': petitioner.ageatconviction,
        'dateofconviction': petitioner.dateofconviction,
        'currentage': today.year - petitioner.dateofconviction.year + petitioner.ageatconviction,
        'ageoffense': petitioner.agewhenoffensewascommited,
        'nextofkin':nextofkin,
        'nextofkinrelationship':relationshipwithnextofkin,
        'contactperson':contactperson,
        'telno':contactpersontelno,
        'county':petitioner.county,
        'subcounty':petitioner.subcounty,
        'location':petitioner.location,
        'nearestschool':petitioner.nearestschool,
        'nameofhomechief':nameofhomechief,
        'offensecommitted':petitioner.whereoffensewascommitted,
        'dateofcustody':petitioner.dateofcustody,
        'yearsserved':today.year - petitioner.dateofcustody.year,
        'yearsinremand':yearsinremand,
        'sentence':sentence,
        'reliefsought':petitioner.reliefsought,
        'offence':petitioner.offence,
        'natureofoffense':petitioner.natureandparticularsofoffense,
        'chargedalone':chargedalone,
        'coaccused':coaccused,
        'knowledgeofvictim':knowledgeofvictim,
        'nameofvictim':nameofvictim,
        'areaofresidence':areaofresidence,
        'previousconvictions':previousconvictions,
        'previouspetition':previouspetition,
        'dateofpreviouspetition':petitioner.dateofpreviouspetition,
        'reasonofdenial':reasonofdenial,
        'reasonsforpetitining':petitioner.reasonforcurrentpetition,
        'disciplinaryaction':disciplinaryaction,
        'explanationofdisciplinaryaction':explanationofdisciplinaryaction,
        'anyspecialcondition':anyspecialcondition,
        'explanationofspecialcondition':explanationofspecialcondition,
        'trustee':trustee,
        'trustedate':trustedate,
        'anyskills':anyskills,
        'skillsexplanation':skillsexplanation,
        'appealed':appealed,
        'appealoutcome':appealoutcome,
        'appealcaseno':appealcaseno,
        'pendingcourtmatter':pendingcourtmatter,
        'pendingexplanation':pendingexplanation,
        'nameofapplicant':nameofapplicant,
        'relationshipofapplicantwithpetitioner':relationshipofapplicantwithpetitioner,
        'addressoftheapplicant':addressoftheapplicant,
        'telephonenumberoftheapplicant':telephonenumberoftheapplicant,
        'month':petitiondate.strftime("%B"),
        'day':petitiondate.day,
        'year':petitiondate.year,
    }
    pdf = render_to_pdf('petitions/petition_form/petitionform_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


class AdmissibilityFormAdmissibleListView(ListView):
    template_name = 'petitions/admissibility_form/admissibilityformadmissible_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(AdmissibilityFormAdmissibleListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(AdmissibilityFormAdmissibleListView, self).get_queryset()
        queryset = queryset.filter(admissability=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_admissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AdmissibilityFormAdmissibleListView, self).dispatch(request, *args, **kwargs)

class AdmissibilityFormInAdmissibleListView(ListView):
    template_name = 'petitions/admissibility_form/admissibilityforminadmissible_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(AdmissibilityFormInAdmissibleListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(AdmissibilityFormInAdmissibleListView, self).get_queryset()
        queryset = queryset.filter(admissability=False)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_admissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AdmissibilityFormInAdmissibleListView, self).dispatch(request, *args, **kwargs)

class AdmissibilityFormCreateView(CreateView):
    template_name = 'petitions/admissibility_form/admissibilityform_form.html'
    model = AdmissibilityForm
    form_class = AdmissibilityCreateForm
    def form_valid(self, form):
         instance = form.save(commit=False)
         instance.added_by = CustomUser.objects.get(id=self.request.user.id)
         instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
         instance.save()
         sweetify.success(self.request, 'Admissibility on a petition submitted successfully', button=True, timer=15000)
         return  redirect ('admissibilityform_detail', instance.id)

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_admissibilityform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AdmissibilityFormCreateView, self).dispatch(request, *args, **kwargs)


class AdmissibilityFormDetailView(DetailView):
    template_name = 'petitions/admissibility_form/admissibilityform_detail.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(AdmissibilityFormDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_admissibilityformdetails'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AdmissibilityFormDetailView, self).dispatch(request, *args, **kwargs)


class AdmissibilityFormUpdateView(UpdateView):
    template_name = 'petitions/admissibility_form/admissibilityform_update.html'
    model = AdmissibilityForm
    form_class = AdmissibilityUpdateForm

    def form_valid(self, form):
        admimissibilitycreate = form.save(commit=False)
        admimissibilitycreate.updated_by = CustomUser.objects.get(id=self.request.user.id)
        admimissibilitycreate.save()
        sweetify.success(self.request, 'Admissibility on a petition updated successfully', button=True, timer=15000)
        return redirect('admissibilityform_detail', admimissibilitycreate.id)

    def dispatch(self, request, *args, **kwargs):
        admissibilitytoupdate = AdmissibilityForm.objects.get(pk=self.kwargs.get('pk'))
        admissibilitydate = admissibilitytoupdate.created.date()
        if not admissibilitydate == date.today():
            """ Permission check for this class """
            if not request.user.has_perm('petitions.change_admissibilityform'):
                raise PermissionDenied("You do not have permission to delete events")
        else:
            if not request.user.has_perm('petitions.change_admissibilityform'):
                if not admissibilitytoupdate.added_by == self.request.user:
                    raise PermissionDenied("You do not have permission to delete events")
        return super(AdmissibilityFormUpdateView, self).dispatch(request, *args, **kwargs)


@permission_required ('petitions.can_print_admissibilityform', raise_exception=True)
def GenerateAdmissibilityForm(request, pk):
    admissibility = AdmissibilityForm.objects.get(pk=pk)
    today = date.today()
    if admissibility.petitioner.nextofkin== '':
        nextofkin = None
        relationshipwithnextofkin = None
    else:
        nextofkin = admissibility.petitioner.nextofkin
        relationshipwithnextofkin = admissibility.petitioner.relationshipwithnextofkin
    if admissibility.petitioner.contactperson == '':
        contactperson = None
        contactpersontelno = None
    else:
        contactperson = admissibility.petitioner.contactperson
        contactpersontelno = admissibility.petitioner.telnoofcontactperson
    if admissibility.petitioner.homechief == '':
        nameofhomechief = None
    else:
        nameofhomechief = admissibility.petitioner.homechief
    if admissibility.petitioner.dateofconviction.year - admissibility.petitioner.dateofcustody.year == '':
        yearsinremand = 0
    else:
        yearsinremand = admissibility.petitioner.dateofconviction.year - admissibility.petitioner.dateofcustody.year
    if admissibility.petitioner.sentence==None:
        sentence = 'LIFE IMPRISONMENT'
    else:
        sentence = str(admissibility.petitioner.sentence)+' '+'YEARS IMPRISONMENT'
    if admissibility.petitioner.chargedalonefortheoffense==True:
        chargedalone = 'YES'
    else:
        chargedalone = 'NO'
    if admissibility.petitioner.namesofcoaccused=='':
        coaccused = 'None'
    else:
        coaccused = admissibility.petitioner.namesofcoaccused
    if admissibility.petitioner.knowledgeofthevictim== True:
        knowledgeofvictim = 'YES'
    else:
        knowledgeofvictim = 'NO'
    if admissibility.petitioner.nameofvictim== '':
        nameofvictim = 'None'
    else:
        nameofvictim = admissibility.petitioner.nameofvictim
    if admissibility.petitioner.areaofresidence== '':
        areaofresidence = 'None'
    else:
        areaofresidence = admissibility.petitioner.areaofresidence
    if admissibility.petitioner.previousconvictions== '':
        previousconvictions = 'None'
    else:
        previousconvictions = admissibility.petitioner.previousconvictions
    if admissibility.petitioner.previouspetition== True:
        previouspetition = 'YES'
    else:
        previouspetition = 'NO'
    if admissibility.petitioner.reasonofdenialofpreviouspetition== '':
        reasonofdenial = 'None'
    else:
        reasonofdenial = admissibility.petitioner.reasonofdenialofpreviouspetition
    if admissibility.petitioner.anydisplinaryactioninprison== True:
        disciplinaryaction = 'YES'
    else:
        disciplinaryaction = 'NO'
    if admissibility.petitioner.detailsofdisplinaryactioninprison== '':
        explanationofdisciplinaryaction = 'None'
    else:
        explanationofdisciplinaryaction = admissibility.petitioner.detailsofdisplinaryactioninprison
    if admissibility.petitioner.anyspecialcondition== True:
        anyspecialcondition = 'YES'
    else:
        anyspecialcondition = 'NO'
    if admissibility.petitioner.detailsofspecialcondition== '':
        explanationofspecialcondition = 'None'
    else:
        explanationofspecialcondition = admissibility.petitioner.detailsofspecialcondition
    if admissibility.petitioner.areyouatrustee== True:
        trustee = 'YES'
    else:
        trustee = 'NO'
    if admissibility.petitioner.dateofpromotiontotrustee== '':
        trustedate = 'None'
    else:
        trustedate = admissibility.petitioner.dateofpromotiontotrustee
    if admissibility.petitioner.anyspecialattributesorskills== True:
        anyskills = 'YES'
    else:
        anyskills = 'NO'
    if admissibility.petitioner.explanationofspecialattributesorskills== '':
        skillsexplanation = 'None'
    else:
        skillsexplanation = admissibility.petitioner.explanationofspecialattributesorskills
    if admissibility.petitioner.appealedagainsttheconviction== True:
        appealed = 'YES'
    else:
        appealed = 'NO'
    if admissibility.petitioner.appealoutcome== '':
        appealoutcome = 'None'
    else:
        appealoutcome = admissibility.petitioner.appealoutcome
    if admissibility.petitioner.appealcaseno== '':
        appealcaseno = 'None'
    else:
        appealcaseno = admissibility.petitioner.appealcaseno
    if admissibility.petitioner.anypendingcourtmatter== True:
        pendingcourtmatter = 'YES'
    else:
        pendingcourtmatter = 'NO'
    if admissibility.petitioner.explanationofpendingcourtmatter== '':
        pendingexplanation = 'None'
    else:
        pendingexplanation = admissibility.petitioner.explanationofpendingcourtmatter

    if admissibility.admissability == True:
        if admissibility.hearingdate ==None:
            information = 'Hear the petition taking into account the criteria provided in section 22 of the Power of Mercy Act, ' \
                         '2011 on unspecified date'
        else:
            information ='Hear the petition taking into account the criteria provided in section 22 of the Power of Mercy Act, ' \
                         '2011 on :'+' '+ str((admissibility.hearingdate).strftime('%d, %b %Y'))
    else:
        if admissibility.inadmissibilityreason =='':
            information = 'Render this petition INADMISSIBLE due to unspecified reasons'
        else:
            information = 'Render this petition INADMISSIBLE on the basis that'+' '+admissibility.inadmissibilityreason
    if admissibility.descriptionforcallofevidence =='':
        evidence = 'None'
    else:
        evidence = admissibility.descriptionforcallofevidence
    if admissibility.descriptionforrequstreport == '':
        reports = 'None'
    else:
        reports = admissibility.descriptionforrequstreport
    if admissibility.orderforinvestigationdescription =='':
        investigations = 'None'
    else:
        investigations = admissibility.orderforinvestigationdescription
    admissibilitydate = admissibility.created
    data = {
        'name': admissibility.petitioner.name,
        'prisonno':admissibility.petitioner.prisonno,
        'created_at': admissibility.petitioner.created,
        'prison': admissibility.petitioner.prison,
        'nationality': admissibility.petitioner.nationality,
        'court': admissibility.petitioner.court,
        'courtno': admissibility.petitioner.courtcaseno,
        'ageatconviction': admissibility.petitioner.ageatconviction,
        'dateofconviction': admissibility.petitioner.dateofconviction,
        'currentage': today.year - admissibility.petitioner.dateofconviction.year + admissibility.petitioner.ageatconviction,
        'ageoffense': admissibility.petitioner.agewhenoffensewascommited,
        'nextofkin':nextofkin,
        'nextofkinrelationship':relationshipwithnextofkin,
        'contactperson':contactperson,
        'telno':contactpersontelno,
        'county':admissibility.petitioner.county,
        'subcounty':admissibility.petitioner.subcounty,
        'location':admissibility.petitioner.location,
        'nearestschool':admissibility.petitioner.nearestschool,
        'nameofhomechief':nameofhomechief,
        'offensecommitted':admissibility.petitioner.whereoffensewascommitted,
        'dateofcustody':admissibility.petitioner.dateofcustody,
        'yearsserved':today.year - admissibility.petitioner.dateofcustody.year,
        'yearsinremand':yearsinremand,
        'sentence':sentence,
        'reliefsought':admissibility.petitioner.reliefsought,
        'offence':admissibility.petitioner.offence,
        'natureofoffense':admissibility.petitioner.natureandparticularsofoffense,
        'chargedalone':chargedalone,
        'coaccused':coaccused,
        'knowledgeofvictim':knowledgeofvictim,
        'nameofvictim':nameofvictim,
        'areaofresidence':areaofresidence,
        'previousconvictions':previousconvictions,
        'previouspetition':previouspetition,
        'dateofpreviouspetition':admissibility.petitioner.dateofpreviouspetition,
        'reasonofdenial':reasonofdenial,
        'reasonsforpetitining':admissibility.petitioner.reasonforcurrentpetition,
        'disciplinaryaction':disciplinaryaction,
        'explanationofdisciplinaryaction':explanationofdisciplinaryaction,
        'anyspecialcondition':anyspecialcondition,
        'explanationofspecialcondition':explanationofspecialcondition,
        'trustee':trustee,
        'trustedate':trustedate,
        'anyskills':anyskills,
        'skillsexplanation':skillsexplanation,
        'appealed':appealed,
        'appealoutcome':appealoutcome,
        'appealcaseno':appealcaseno,
        'pendingcourtmatter':pendingcourtmatter,
        'pendingexplanation':pendingexplanation,
        'month':admissibilitydate.strftime("%B"),
        'day':admissibilitydate.day,
        'year':admissibilitydate.year,
        'information':information,
        'evidence':evidence,
        'reports':reports,
        'investigations':investigations,
    }
    pdf = render_to_pdf('petitions/admissibility_form/admissibilityform_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


class PetitionSummaryListView(ListView):
    template_name = 'petitions/summaries/petitionsummary_list.html'
    model = PetitionSummary
    def get_queryset(self):
        queryset = PetitionSummary.objects.all()
        return queryset
    def get_context_data(self, **kwargs):
        context = super(PetitionSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        form = SummariesDateFilterForm
        context['today'] = today
        context['form'] = form
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_petitionsummary'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PetitionSummaryListView, self).dispatch(request, *args, **kwargs)

def SummariesByDate(request):
    if request.method == 'POST':
        form = SummariesDateFilterForm(request.POST)
        if form.is_valid():
            filterdate = request.POST['reservation']
            daterange = filterdate.split("-")
            start = daterange[0]
            startdate = start.split("/")
            startfilterdate = datetime(int(startdate[2]),int(startdate[0]),int(startdate[1]))
            end = daterange[1]
            enddate = end.split("/")
            endfilterdatepassed = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))
            endfilterdate = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))+timedelta(days=1)

            object_list = PetitionSummary.objects.filter(created__range=[startfilterdate.date(), endfilterdate.date()])

            context = {
                'startdate': startfilterdate.date(),
                'enddate': endfilterdatepassed.date(),
                'form':SummariesDateFilterForm,
                'today':date.today(),
                'object_list' : object_list
            }
            return render(request, 'petitions/summaries/filteredsummariesbydate_list.html',context)
        return  redirect('petitionsummary_list')
    else:
        return redirect('petitionsummary_list')


class MyPetitionSummaryListView(ListView):
    template_name = 'petitions/summaries/mypetitionsummary_list.html'
    model = PetitionSummary
    def get_queryset(self):
        queryset = PetitionSummary.objects.filter(added_by=self.request.user)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(MyPetitionSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_mypetitionsummary'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyPetitionSummaryListView, self).dispatch(request, *args, **kwargs)

class AwaitingPetitionSummaryListView(ListView):
    template_name = 'petitions/summaries/awaitingpetitionsummary_list.html'
    model = AdmissibilityForm
    def get_queryset(self):
        queryset = AdmissibilityForm.objects.filter(admissability=True).filter(petitionsummary__isnull=True).filter(petitioner__exit__isnull=True)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(AwaitingPetitionSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_petitionsummary'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AwaitingPetitionSummaryListView, self).dispatch(request, *args, **kwargs)

class MyAwaitingPetitionSummaryListView(ListView):
    template_name = 'petitions/summaries/myawaitingpetitionsummary_list.html'
    model = AdmissibilityForm
    def get_queryset(self):
        queryset = AdmissibilityForm.objects.filter(admissability=True).filter(petitionsummary__isnull=True).filter(
            petitioner__exit__isnull=True).filter(added_by=self.request.user)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(MyAwaitingPetitionSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_mypetitionsummary'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAwaitingPetitionSummaryListView, self).dispatch(request, *args, **kwargs)


class PetitionSummaryCreateView(CreateView):
    template_name = 'petitions/summaries/petitionsummary_form.html'
    model = PetitionSummary
    form_class = PetitionSummaryForm
    def form_valid(self, form):
         instance = form.save(commit=False)
         instance.added_by = CustomUser.objects.get(id=self.request.user.id)
         instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
         instance.save()
         sweetify.success(self.request, 'Petition summary submitted successfully', button=True, timer=15000)
         return  redirect ('petitionsummary_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_petitionsummary'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PetitionSummaryCreateView, self).dispatch(request, *args, **kwargs)


class PetitionSummaryDetailView(DetailView):
    template_name = 'petitions/summaries/petitionsummary_details.html'
    model = PetitionSummary
    def get_context_data(self, **kwargs):
        context = super(PetitionSummaryDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_petitionsummarydetails'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(PetitionSummaryDetailView, self).dispatch(request, *args, **kwargs)


class PetitionSummaryUpdateView(UpdateView):
    template_name = 'petitions/summaries/petitionsummary_update.html'
    model = PetitionSummary
    form_class = PetitionSummaryEditForm

    def form_valid(self, form):
        summary = form.save(commit=False)
        summary.updated_by = CustomUser.objects.get(id=self.request.user.id)
        summary.save()
        sweetify.success(self.request, 'Petition summary updated successfully', button=True, timer=15000)
        return redirect('petitionsummary_detail', summary.id)
    def dispatch(self, request, *args, **kwargs):
        summarytoupdate = PetitionSummary.objects.get(pk=self.kwargs.get('pk'))
        summarydate = summarytoupdate.created.date()
        if not summarydate == date.today():
            """ Permission check for this class """
            if not request.user.has_perm('petitions.change_petitionsummary'):
                raise PermissionDenied("You do not have permission to delete events")
        else:
            if not request.user.has_perm('petitions.change_petitionsummary'):
                if not summarytoupdate.added_by == self.request.user:
                    raise PermissionDenied("You do not have permission to delete events")
        return super(PetitionSummaryUpdateView, self).dispatch(request, *args, **kwargs)

@permission_required ('petitions.can_print_petitionsummary', raise_exception=True)
def GeneratePetitionSummary(request, pk):
    summary = PetitionSummary.objects.get(pk=pk)
    today = date.today()
    if summary.admissibility.petitioner.nextofkin== '':
        nextofkin = None
        relationshipwithnextofkin = None
    else:
        nextofkin = summary.admissibility.petitioner.nextofkin
        relationshipwithnextofkin = summary.admissibility.petitioner.relationshipwithnextofkin
    if summary.admissibility.petitioner.contactperson == '':
        contactperson = None
        contactpersontelno = None
    else:
        contactperson = summary.admissibility.petitioner.contactperson
        contactpersontelno = summary.admissibility.petitioner.telnoofcontactperson
    if summary.admissibility.petitioner.homechief == '':
        nameofhomechief = None
    else:
        nameofhomechief = summary.admissibility.petitioner.homechief
    if summary.admissibility.petitioner.dateofconviction.year - summary.admissibility.petitioner.dateofcustody.year == '':
        yearsinremand = 0
    else:
        yearsinremand = summary.admissibility.petitioner.dateofconviction.year - summary.admissibility.petitioner.dateofcustody.year
    if summary.admissibility.petitioner.sentence==None:
        sentence = 'LIFE IMPRISONMENT'
    else:
        sentence = str(summary.admissibility.petitioner.sentence)+' '+'YEARS IMPRISONMENT'
    if summary.admissibility.petitioner.chargedalonefortheoffense==True:
        chargedalone = 'YES'
    else:
        chargedalone = 'NO'
    if summary.admissibility.petitioner.namesofcoaccused=='':
        coaccused = 'None'
    else:
        coaccused = summary.admissibility.petitioner.namesofcoaccused
    if summary.admissibility.petitioner.knowledgeofthevictim== True:
        knowledgeofvictim = 'YES'
    else:
        knowledgeofvictim = 'NO'
    if summary.admissibility.petitioner.nameofvictim== '':
        nameofvictim = 'None'
    else:
        nameofvictim = summary.admissibility.petitioner.nameofvictim
    if summary.admissibility.petitioner.areaofresidence== '':
        areaofresidence = 'None'
    else:
        areaofresidence = summary.admissibility.petitioner.areaofresidence
    if summary.admissibility.petitioner.previousconvictions== '':
        previousconvictions = 'None'
    else:
        previousconvictions = summary.admissibility.petitioner.previousconvictions
    if summary.admissibility.petitioner.previouspetition== True:
        previouspetition = 'YES'
    else:
        previouspetition = 'NO'
    if summary.admissibility.petitioner.reasonofdenialofpreviouspetition== '':
        reasonofdenial = 'None'
    else:
        reasonofdenial = summary.admissibility.petitioner.reasonofdenialofpreviouspetition
    if summary.admissibility.petitioner.anydisplinaryactioninprison== True:
        disciplinaryaction = 'YES'
    else:
        disciplinaryaction = 'NO'
    if summary.admissibility.petitioner.detailsofdisplinaryactioninprison== '':
        explanationofdisciplinaryaction = 'None'
    else:
        explanationofdisciplinaryaction = summary.admissibility.petitioner.detailsofdisplinaryactioninprison
    if summary.admissibility.petitioner.anyspecialcondition== True:
        anyspecialcondition = 'YES'
    else:
        anyspecialcondition = 'NO'
    if summary.admissibility.petitioner.detailsofspecialcondition== '':
        explanationofspecialcondition = 'None'
    else:
        explanationofspecialcondition = summary.admissibility.petitioner.detailsofspecialcondition
    if summary.admissibility.petitioner.areyouatrustee== True:
        trustee = 'YES'
    else:
        trustee = 'NO'
    if summary.admissibility.petitioner.dateofpromotiontotrustee== '':
        trustedate = 'None'
    else:
        trustedate = summary.admissibility.petitioner.dateofpromotiontotrustee
    if summary.admissibility.petitioner.anyspecialattributesorskills== True:
        anyskills = 'YES'
    else:
        anyskills = 'NO'
    if summary.admissibility.petitioner.explanationofspecialattributesorskills== '':
        skillsexplanation = 'None'
    else:
        skillsexplanation = summary.admissibility.petitioner.explanationofspecialattributesorskills
    if summary.admissibility.petitioner.appealedagainsttheconviction== True:
        appealed = 'YES'
    else:
        appealed = 'NO'
    if summary.admissibility.petitioner.appealoutcome== '':
        appealoutcome = 'None'
    else:
        appealoutcome = summary.admissibility.petitioner.appealoutcome
    if summary.admissibility.petitioner.appealcaseno== '':
        appealcaseno = 'None'
    else:
        appealcaseno = summary.admissibility.petitioner.appealcaseno
    if summary.admissibility.petitioner.anypendingcourtmatter== True:
        pendingcourtmatter = 'YES'
    else:
        pendingcourtmatter = 'NO'
    if summary.admissibility.petitioner.explanationofpendingcourtmatter== '':
        pendingexplanation = 'None'
    else:
        pendingexplanation = summary.admissibility.petitioner.explanationofpendingcourtmatter
    summarydate = summary.created
    data = {
        'name': summary.admissibility.petitioner.name,
        'pmnumber': 'PM/'+str(summary.admissibility.petitioner.created.year)+'/'+str(summary.admissibility.petitioner.created.month)+'/'+str(summary.admissibility.petitioner.created.day)+'/'+str(summary.admissibility.petitioner.id),
        'prisonno':summary.admissibility.petitioner.prisonno,
        'created_at': summary.admissibility.petitioner.created,
        'prison': summary.admissibility.petitioner.prison,
        'nationality': summary.admissibility.petitioner.nationality,
        'court': summary.admissibility.petitioner.court,
        'courtno': summary.admissibility.petitioner.courtcaseno,
        'ageatconviction': summary.admissibility.petitioner.ageatconviction,
        'dateofconviction': summary.admissibility.petitioner.dateofconviction,
        'currentage': today.year - summary.admissibility.petitioner.dateofconviction.year + summary.admissibility.petitioner.ageatconviction,
        'ageoffense': summary.admissibility.petitioner.agewhenoffensewascommited,
        'nextofkin':nextofkin,
        'nextofkinrelationship':relationshipwithnextofkin,
        'contactperson':contactperson,
        'telno':contactpersontelno,
        'county':summary.admissibility.petitioner.county,
        'subcounty':summary.admissibility.petitioner.subcounty,
        'location':summary.admissibility.petitioner.location,
        'nearestschool':summary.admissibility.petitioner.nearestschool,
        'nameofhomechief':nameofhomechief,
        'offensecommitted':summary.admissibility.petitioner.whereoffensewascommitted,
        'dateofcustody':summary.admissibility.petitioner.dateofcustody,
        'yearsserved':today.year - summary.admissibility.petitioner.dateofcustody.year,
        'yearsinremand':yearsinremand,
        'sentence':sentence,
        'reliefsought':summary.admissibility.petitioner.reliefsought,
        'offence':summary.admissibility.petitioner.offence,
        'natureofoffense':summary.admissibility.petitioner.natureandparticularsofoffense,
        'chargedalone':chargedalone,
        'coaccused':coaccused,
        'knowledgeofvictim':knowledgeofvictim,
        'nameofvictim':nameofvictim,
        'areaofresidence':areaofresidence,
        'previousconvictions':previousconvictions,
        'previouspetition':previouspetition,
        'dateofpreviouspetition':summary.admissibility.petitioner.dateofpreviouspetition,
        'reasonofdenial':reasonofdenial,
        'reasonsforpetitining':summary.admissibility.petitioner.reasonforcurrentpetition,
        'disciplinaryaction':disciplinaryaction,
        'explanationofdisciplinaryaction':explanationofdisciplinaryaction,
        'anyspecialcondition':anyspecialcondition,
        'explanationofspecialcondition':explanationofspecialcondition,
        'trustee':trustee,
        'trustedate':trustedate,
        'anyskills':anyskills,
        'skillsexplanation':skillsexplanation,
        'appealed':appealed,
        'appealoutcome':appealoutcome,
        'appealcaseno':appealcaseno,
        'pendingcourtmatter':pendingcourtmatter,
        'pendingexplanation':pendingexplanation,
        'typeandcircumstances':summary.typeandcircumstancesofoffence,
        'petitionoverview':summary.petitionoverview,
        'month':summarydate.strftime("%B"),
        'day':summarydate.day,
        'year':summarydate.year,
    }
    pdf = render_to_pdf('petitions/summaries/petitionsummary_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@permission_required ('petitions.delete_petitionsummary', raise_exception=True)
def DeletePetitionSummary(request,pk):
    PetitionSummary.objects.get(pk=pk).delete()
    sweetify.success(request, 'Petition Summary Deleted Successfully', button=True, timer=15000)
    return redirect('petitionsummary_list')


class HearingSummaryListView(ListView):
    template_name = 'petitions/hearings/hearingsummary_list.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(HearingSummaryListView, self).get_context_data(**kwargs)
        context['today'] = date.today()
        context['form'] = HearingsDateFilterForm
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingsummaries'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(HearingSummaryListView, self).dispatch(request, *args, **kwargs)

def FilterHearingsByDate(request):
    if request.method == 'POST':
        form = HearingsDateFilterForm(request.POST)
        if form.is_valid():
            filterdate = request.POST['reservation']
            daterange = filterdate.split("-")
            start = daterange[0]
            startdate = start.split("/")
            startfilterdate = datetime(int(startdate[2]),int(startdate[0]),int(startdate[1]))
            end = daterange[1]
            enddate = end.split("/")
            endfilterdatepassed = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))
            endfilterdate = datetime(int(enddate[2]), int(enddate[0]), int(enddate[1]))+timedelta(days=1)

            object_list = HearingSummary.objects.filter(created__range=[startfilterdate.date(), endfilterdate.date()])

            context = {
                'startdate': startfilterdate.date(),
                'enddate': endfilterdatepassed.date(),
                'form':HearingsDateFilterForm,
                'today': date.today(),
                'object_list' : object_list
            }
            return render(request, 'petitions/hearings/filteredhearingsbydate_list.html',context)
        return  redirect('hearingsummary_list')
    else:
        return redirect('hearingsummary_list')


class MyHearingSummaryListView(ListView):
    template_name = 'petitions/hearings/myhearingsummary_list.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(MyHearingSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset=HearingSummary.objects.filter(added_by=self.request.user)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myhearings'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyHearingSummaryListView, self).dispatch(request, *args, **kwargs)


class AwaitingHearingSummaryListView(ListView):
    template_name = 'petitions/hearings/awaitinghearingsummary_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(AwaitingHearingSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset=AdmissibilityForm.objects.filter(admissability=True).filter(hearingdate__isnull=False).filter(hearing__isnull=True).filter(petitioner__exit__isnull=True)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingsummaries'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AwaitingHearingSummaryListView, self).dispatch(request, *args, **kwargs)

class AwaitingScheduleforHearingSummaryListView(ListView):
    template_name = 'petitions/hearings/awaitingschedulehearingsummary_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(AwaitingScheduleforHearingSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset=AdmissibilityForm.objects.filter(admissability=True).filter(hearingdate__isnull=True).filter(hearing__isnull=True).filter(petitioner__exit__isnull=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingsummaries'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AwaitingScheduleforHearingSummaryListView, self).dispatch(request, *args, **kwargs)

class MyAwaitingHearingSummaryListView(ListView):
    template_name = 'petitions/hearings/myawaitinghearingsummary_list.html'
    model = AdmissibilityForm
    def get_context_data(self, **kwargs):
        context = super(MyAwaitingHearingSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = AdmissibilityForm.objects.filter(admissability=True).filter(hearingdate__isnull=False).filter(hearing__isnull=True).filter(
            petitioner__exit__isnull=True).filter(added_by=self.request.user)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myhearings'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAwaitingHearingSummaryListView, self).dispatch(request, *args, **kwargs)



class HearingSummaryDeferredListView(ListView):
    template_name = 'petitions/hearings/hearingsummary_deferred.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(HearingSummaryDeferredListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(HearingSummaryDeferredListView, self).get_queryset()
        queryset = queryset.filter(action='Defer the petition to a later date')
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingsummaries'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(HearingSummaryDeferredListView, self).dispatch(request, *args, **kwargs)

class MyHearingSummaryDeferredListView(ListView):
    template_name = 'petitions/hearings/myhearingsummary_deferred.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(MyHearingSummaryDeferredListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(MyHearingSummaryDeferredListView, self).get_queryset().filter(added_by=self.request.user)
        queryset = queryset.filter(action='Defer the petition to a later date')
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myhearings'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyHearingSummaryDeferredListView, self).dispatch(request, *args, **kwargs)

class HearingSummaryDeclinedListView(ListView):
    template_name = 'petitions/hearings/hearingsummary_declined.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(HearingSummaryDeclinedListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(HearingSummaryDeclinedListView, self).get_queryset()
        queryset = queryset.filter(action='Decline the Petition')
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingsummaries'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(HearingSummaryDeclinedListView, self).dispatch(request, *args, **kwargs)

class MyHearingSummaryDeclinedListView(ListView):
    template_name = 'petitions/hearings/myhearingsummary_declined.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(MyHearingSummaryDeclinedListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(MyHearingSummaryDeclinedListView, self).get_queryset()
        queryset = queryset.filter(action='Decline the Petition').filter(added_by=self.request.user)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myhearings'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyHearingSummaryDeclinedListView, self).dispatch(request, *args, **kwargs)

class HearingSummaryScheduledforInterviewListView(ListView):
    template_name = 'petitions/hearings/hearingsummary_scheduledforinterview.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(HearingSummaryScheduledforInterviewListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(HearingSummaryScheduledforInterviewListView, self).get_queryset()
        queryset = queryset.filter(action='Interview the Petitioner').filter(interviewdate__isnull= False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingsummaries'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(HearingSummaryScheduledforInterviewListView, self).dispatch(request, *args, **kwargs)

class MyHearingSummaryScheduledforInterviewListView(ListView):
    template_name = 'petitions/hearings/myhearingsummary_scheduledforinterview.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(MyHearingSummaryScheduledforInterviewListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull= False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True).filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myhearings'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyHearingSummaryScheduledforInterviewListView, self).dispatch(request, *args, **kwargs)


class HearingSummaryAwaitingScheduleforInterviewListView(ListView):
    template_name = 'petitions/hearings/hearingsummary_awaitingscheduledforinterview.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(HearingSummaryAwaitingScheduleforInterviewListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(HearingSummaryAwaitingScheduleforInterviewListView, self).get_queryset()
        queryset = queryset.filter(action='Interview the Petitioner').filter(interviewdate__isnull= True).filter(interviewsummary__isnull=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingsummaries'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(HearingSummaryAwaitingScheduleforInterviewListView, self).dispatch(request, *args, **kwargs)


class MyHearingSummaryAwaitingScheduleforInterviewListView(ListView):
    template_name = 'petitions/hearings/myhearingsummary_awaitingscheduledforinterview.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(MyHearingSummaryAwaitingScheduleforInterviewListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(MyHearingSummaryAwaitingScheduleforInterviewListView, self).get_queryset()
        queryset = queryset.filter(action='Interview the Petitioner').filter(interviewdate__isnull= True).filter(interviewsummary__isnull=True).filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myhearings'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyHearingSummaryAwaitingScheduleforInterviewListView, self).dispatch(request, *args, **kwargs)


class HearingSummaryCreateView(CreateView):
    template_name = 'petitions/hearings/hearingsummary_form.html'
    model = HearingSummary
    form_class = HearingSummaryForm
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.added_by = CustomUser.objects.get(id=self.request.user.id)
        instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
        instance.save()
        sweetify.success(self.request, 'Petition Hearing Summary added successfully', button=True, timer=15000)
        return redirect('hearingsummary_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_hearingsummary'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(HearingSummaryCreateView, self).dispatch(request, *args, **kwargs)


class HearingSummaryDetailView(DetailView):
    template_name = 'petitions/hearings/hearingsummary_detail.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(HearingSummaryDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_hearingdetails'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(HearingSummaryDetailView, self).dispatch(request, *args, **kwargs)


class HearingSummaryUpdateView(UpdateView):
    template_name = 'petitions/hearings/hearingsummary_update.html'
    model = HearingSummary
    form_class = HearingSummaryUpdateForm

    def form_valid(self, form):
        hearing = form.save(commit=False)
        hearing.updated_by = CustomUser.objects.get(id=self.request.user.id)
        hearing.save()
        sweetify.success(self.request, 'Petition Hearing Summary updated successfully', button=True, timer=15000)
        return redirect('hearingsummary_detail', hearing.id)
    def dispatch(self, request, *args, **kwargs):
        hearingsummarytoupdate = HearingSummary.objects.get(pk=self.kwargs.get('pk'))
        hearingdate = hearingsummarytoupdate.created.date()
        if not hearingdate == date.today():
            """ Permission check for this class """
            if not request.user.has_perm('petitions.change_hearingsummary'):
                raise PermissionDenied("You do not have permission to delete events")
        else:
            if request.user.has_perm('petitions.change_petitionform'):
                return super(HearingSummaryUpdateView, self).dispatch(request, *args, **kwargs)
            else:
                if not hearingsummarytoupdate.added_by == self.request.user:
                    raise PermissionDenied("You do not have permission to delete events")
        return super(HearingSummaryUpdateView, self).dispatch(request, *args, **kwargs)


@permission_required ('petitions.can_print_hearing', raise_exception=True)
def GenerateHearingForm(request, pk):
    hearing = HearingSummary.objects.get(pk=pk)
    today = date.today()
    if hearing.admissibility.petitioner.nextofkin== '':
        nextofkin = None
        relationshipwithnextofkin = None
    else:
        nextofkin = hearing.admissibility.petitioner.nextofkin
        relationshipwithnextofkin = hearing.admissibility.petitioner.relationshipwithnextofkin
    if hearing.admissibility.petitioner.contactperson == '':
        contactperson = None
        contactpersontelno = None
    else:
        contactperson = hearing.admissibility.petitioner.contactperson
        contactpersontelno = hearing.admissibility.petitioner.telnoofcontactperson
    if hearing.admissibility.petitioner.homechief == '':
        nameofhomechief = None
    else:
        nameofhomechief = hearing.admissibility.petitioner.homechief
    if hearing.admissibility.petitioner.dateofconviction.year - hearing.admissibility.petitioner.dateofcustody.year == '':
        yearsinremand = 0
    else:
        yearsinremand = hearing.admissibility.petitioner.dateofconviction.year - hearing.admissibility.petitioner.dateofcustody.year
    if hearing.admissibility.petitioner.sentence==None:
        sentence = 'LIFE IMPRISONMENT'
    else:
        sentence = str(hearing.admissibility.petitioner.sentence)+' '+'YEARS IMPRISONMENT'
    if hearing.admissibility.petitioner.chargedalonefortheoffense==True:
        chargedalone = 'YES'
    else:
        chargedalone = 'NO'
    if hearing.admissibility.petitioner.namesofcoaccused=='':
        coaccused = 'None'
    else:
        coaccused = hearing.admissibility.petitioner.namesofcoaccused
    if hearing.admissibility.petitioner.knowledgeofthevictim== True:
        knowledgeofvictim = 'YES'
    else:
        knowledgeofvictim = 'NO'
    if hearing.admissibility.petitioner.nameofvictim== '':
        nameofvictim = 'None'
    else:
        nameofvictim = hearing.admissibility.petitioner.nameofvictim
    if hearing.admissibility.petitioner.areaofresidence== '':
        areaofresidence = 'None'
    else:
        areaofresidence = hearing.admissibility.petitioner.areaofresidence
    if hearing.admissibility.petitioner.previousconvictions== '':
        previousconvictions = 'None'
    else:
        previousconvictions = hearing.admissibility.petitioner.previousconvictions
    if hearing.admissibility.petitioner.previouspetition== True:
        previouspetition = 'YES'
    else:
        previouspetition = 'NO'
    if hearing.admissibility.petitioner.reasonofdenialofpreviouspetition== '':
        reasonofdenial = 'None'
    else:
        reasonofdenial = hearing.admissibility.petitioner.reasonofdenialofpreviouspetition
    if hearing.admissibility.petitioner.anydisplinaryactioninprison== True:
        disciplinaryaction = 'YES'
    else:
        disciplinaryaction = 'NO'
    if hearing.admissibility.petitioner.detailsofdisplinaryactioninprison== '':
        explanationofdisciplinaryaction = 'None'
    else:
        explanationofdisciplinaryaction = hearing.admissibility.petitioner.detailsofdisplinaryactioninprison
    if hearing.admissibility.petitioner.anyspecialcondition== True:
        anyspecialcondition = 'YES'
    else:
        anyspecialcondition = 'NO'
    if hearing.admissibility.petitioner.detailsofspecialcondition== '':
        explanationofspecialcondition = 'None'
    else:
        explanationofspecialcondition = hearing.admissibility.petitioner.detailsofspecialcondition
    if hearing.admissibility.petitioner.areyouatrustee== True:
        trustee = 'YES'
    else:
        trustee = 'NO'
    if hearing.admissibility.petitioner.dateofpromotiontotrustee== '':
        trustedate = 'None'
    else:
        trustedate = hearing.admissibility.petitioner.dateofpromotiontotrustee
    if hearing.admissibility.petitioner.anyspecialattributesorskills== True:
        anyskills = 'YES'
    else:
        anyskills = 'NO'
    if hearing.admissibility.petitioner.explanationofspecialattributesorskills== '':
        skillsexplanation = 'None'
    else:
        skillsexplanation = hearing.admissibility.petitioner.explanationofspecialattributesorskills
    if hearing.admissibility.petitioner.appealedagainsttheconviction== True:
        appealed = 'YES'
    else:
        appealed = 'NO'
    if hearing.admissibility.petitioner.appealoutcome== '':
        appealoutcome = 'None'
    else:
        appealoutcome = hearing.admissibility.petitioner.appealoutcome
    if hearing.admissibility.petitioner.appealcaseno== '':
        appealcaseno = 'None'
    else:
        appealcaseno = hearing.admissibility.petitioner.appealcaseno
    if hearing.admissibility.petitioner.anypendingcourtmatter== True:
        pendingcourtmatter = 'YES'
    else:
        pendingcourtmatter = 'NO'
    if hearing.admissibility.petitioner.explanationofpendingcourtmatter== '':
        pendingexplanation = 'None'
    else:
        pendingexplanation = hearing.admissibility.petitioner.explanationofpendingcourtmatter
    if hearing.healthstatus== '':
        healthstatus = 'None'
    else:
        healthstatus = hearing.healthstatus
    if hearing.familystatus== '':
        familystatus = 'None'
    else:
        familystatus = hearing.familystatus
    if hearing.natureandseriousnessoftheoffense== '':
        seriousnessofoffence = 'None'
    else:
        seriousnessofoffence = hearing.natureandseriousnessoftheoffense
    if hearing.personalcircumstances== '':
        personalcircumstances = 'None'
    else:
        personalcircumstances = hearing.personalcircumstances
    if hearing.interestofstateandcommunity== '':
        interestofstate = 'None'
    else:
        interestofstate = hearing.interestofstateandcommunity
    if hearing.postconvictionconduct== '':
        postconvictionconduct = 'None'
    else:
        postconvictionconduct = hearing.postconvictionconduct
    if hearing.officialrecommendationsandreports== '':
        officialrecommendations = 'None'
    else:
        officialrecommendations = hearing.officialrecommendationsandreports
    if hearing.wherethepetitionerhaspersued== '':
        otheravailableremedies = 'None'
    else:
        otheravailableremedies = hearing.wherethepetitionerhaspersued
    if hearing.representationofvictim== '':
        represenationofvictim = 'None'
    else:
        represenationofvictim = hearing.representationofvictim
    if hearing.reportoffellowinmates== '':
        reportoffellowinmates = 'None'
    else:
        reportoffellowinmates = hearing.reportoffellowinmates
    if hearing.reportsfromprobationservices== '':
        reportsfromprobationservices = 'None'
    else:
        reportsfromprobationservices = hearing.reportsfromprobationservices
    if hearing.observationswithmainreasons== '':
        observationswithmainreasons = 'None'
    else:
        observationswithmainreasons = hearing.observationswithmainreasons
    if hearing.member1== '':
        member1 = 'None'
    else:
        member1 = hearing.member1
    if hearing.member2== '':
        member2 = 'None'
    else:
        member2 = hearing.member2
    if hearing.member3== '':
        member3 = 'None'
    else:
        member3 = hearing.member3
    if hearing.member4== '':
        member4 = 'None'
    else:
        member4 = hearing.member4
    if hearing.member5== '':
        member5 = 'None'
    else:
        member5 = hearing.member5
    if hearing.member6== '':
        member6 = 'None'
    else:
        member6 = hearing.member6
    if hearing.member7== '':
        member7 = 'None'
    else:
        member7 = hearing.member7
    if hearing.member8== '':
        member8 = 'None'
    else:
        member8 = hearing.member8
    if hearing.member9== '':
        member9 = 'None'
    else:
        member9 = hearing.member9
    if hearing.member10== '':
        member10 = 'None'
    else:
        member10 = hearing.member10

    hearingdate = hearing.created
    data = {
        'name': hearing.admissibility.petitioner.name,
        'prisonno':hearing.admissibility.petitioner.prisonno,
        'created_at': hearing.admissibility.petitioner.created,
        'prison': hearing.admissibility.petitioner.prison,
        'nationality': hearing.admissibility.petitioner.nationality,
        'court': hearing.admissibility.petitioner.court,
        'courtno': hearing.admissibility.petitioner.courtcaseno,
        'ageatconviction': hearing.admissibility.petitioner.ageatconviction,
        'dateofconviction': hearing.admissibility.petitioner.dateofconviction,
        'currentage': today.year - hearing.admissibility.petitioner.dateofconviction.year + hearing.admissibility.petitioner.ageatconviction,
        'ageoffense': hearing.admissibility.petitioner.agewhenoffensewascommited,
        'nextofkin':nextofkin,
        'nextofkinrelationship':relationshipwithnextofkin,
        'contactperson':contactperson,
        'telno':contactpersontelno,
        'county':hearing.admissibility.petitioner.county,
        'subcounty':hearing.admissibility.petitioner.subcounty,
        'location':hearing.admissibility.petitioner.location,
        'nearestschool':hearing.admissibility.petitioner.nearestschool,
        'nameofhomechief':nameofhomechief,
        'offensecommitted':hearing.admissibility.petitioner.whereoffensewascommitted,
        'dateofcustody':hearing.admissibility.petitioner.dateofcustody,
        'yearsserved':today.year - hearing.admissibility.petitioner.dateofcustody.year,
        'yearsinremand':yearsinremand,
        'sentence':sentence,
        'reliefsought':hearing.admissibility.petitioner.reliefsought,
        'offence':hearing.admissibility.petitioner.offence,
        'natureofoffense':hearing.admissibility.petitioner.natureandparticularsofoffense,
        'chargedalone':chargedalone,
        'coaccused':coaccused,
        'knowledgeofvictim':knowledgeofvictim,
        'nameofvictim':nameofvictim,
        'areaofresidence':areaofresidence,
        'previousconvictions':previousconvictions,
        'previouspetition':previouspetition,
        'dateofpreviouspetition':hearing.admissibility.petitioner.dateofpreviouspetition,
        'reasonofdenial':reasonofdenial,
        'reasonsforpetitining':hearing.admissibility.petitioner.reasonforcurrentpetition,
        'disciplinaryaction':disciplinaryaction,
        'explanationofdisciplinaryaction':explanationofdisciplinaryaction,
        'anyspecialcondition':anyspecialcondition,
        'explanationofspecialcondition':explanationofspecialcondition,
        'trustee':trustee,
        'trustedate':trustedate,
        'anyskills':anyskills,
        'skillsexplanation':skillsexplanation,
        'appealed':appealed,
        'appealoutcome':appealoutcome,
        'appealcaseno':appealcaseno,
        'pendingcourtmatter':pendingcourtmatter,
        'pendingexplanation':pendingexplanation,
        'healthstatus':healthstatus,
        'familystatus':familystatus,
        'seriousnessofoffence':seriousnessofoffence,
        'personalcircumstances':personalcircumstances,
        'interestofstate':interestofstate,
        'postconvictionconduct':postconvictionconduct,
        'officialrecommendations':officialrecommendations,
        'otheravailableremedies':otheravailableremedies,
        'represenationofvictim':represenationofvictim,
        'reportoffellowinmates':reportoffellowinmates,
        'reportsfromprobationservices':reportsfromprobationservices,
        'observationswithmainreasons':observationswithmainreasons,
        'member1':member1,
        'member2':member2,
        'member3':member3,
        'member4':member4,
        'member5':member5,
        'member6':member6,
        'member7':member7,
        'member8':member8,
        'member9':member9,
        'member10':member10,
        'space':'',
        'month':hearingdate.strftime("%B"),
        'day':hearingdate.day,
        'year':hearingdate.year,
        'printedon':today
    }
    pdf = render_to_pdf('petitions/hearings/hearingsummary_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@permission_required ('petitions.delete_hearingsummary', raise_exception=True)
def DeleteHearing(request,pk):
    HearingSummary.objects.get(pk=pk).delete()
    sweetify.success(request, 'Hearing form  for the petitioner deleted successfully and all its consequent information ', button=True, timer=15000)
    return redirect('hearingsummary_list')


class InterviewSummaryListView(ListView):
    template_name = 'petitions/interviews/interviewsummary_list.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(InterviewSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_interviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(InterviewSummaryListView, self).dispatch(request, *args, **kwargs)

class MyInterviewSummaryListView(ListView):
    template_name = 'petitions/interviews/myinterviewsummary_list.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(MyInterviewSummaryListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = InterviewSummary.objects.filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myinterviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyInterviewSummaryListView, self).dispatch(request, *args, **kwargs)

class AwaitingInterviewFormListView(ListView):
    template_name = 'petitions/interviews/awaitinginterviewsummary_list.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(AwaitingInterviewFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = HearingSummary.objects.filter(action='Interview the Petitioner').filter(
            interviewdate__isnull=False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_interviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AwaitingInterviewFormListView, self).dispatch(request, *args, **kwargs)

class MyAwaitingInterviewFormListView(ListView):
    template_name = 'petitions/interviews/myawaitinginterviewsummary_list.html'
    model = HearingSummary
    def get_context_data(self, **kwargs):
        context = super(MyAwaitingInterviewFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = HearingSummary.objects.filter(action='Interview the Petitioner').filter(
            interviewdate__isnull=False).filter(interviewsummary__isnull=True).filter(
            admissibility__petitioner__exit__isnull=True).filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myinterviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAwaitingInterviewFormListView, self).dispatch(request, *args, **kwargs)

class InterviewSummaryRecommendedListView(ListView):
    template_name = 'petitions/interviews/interviewsummary_recommended.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(InterviewSummaryRecommendedListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(InterviewSummaryRecommendedListView, self).get_queryset()
        queryset = queryset.filter(finalresolution = 'Recommended to President')
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_interviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(InterviewSummaryRecommendedListView, self).dispatch(request, *args, **kwargs)

class MyInterviewSummaryRecommendedListView(ListView):
    template_name = 'petitions/interviews/myinterviewsummary_recommended.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(MyInterviewSummaryRecommendedListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(MyInterviewSummaryRecommendedListView, self).get_queryset()
        queryset = queryset.filter(finalresolution = 'Recommended to President').filter(added_by=self.request.user)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myinterviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyInterviewSummaryRecommendedListView, self).dispatch(request, *args, **kwargs)

class InterviewSummaryNotRecommendedListView(ListView):
    template_name = 'petitions/interviews/interviewsummary_notrecommended.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(InterviewSummaryNotRecommendedListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(InterviewSummaryNotRecommendedListView, self).get_queryset()
        queryset = queryset.filter(finalresolution = 'Not Recommended to President')
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_interviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(InterviewSummaryNotRecommendedListView, self).dispatch(request, *args, **kwargs)

class myInterviewSummaryNotRecommendedListView(ListView):
    template_name = 'petitions/interviews/myinterviewsummary_notrecommended.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(myInterviewSummaryNotRecommendedListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = super(myInterviewSummaryNotRecommendedListView, self).get_queryset()
        queryset = queryset.filter(finalresolution = 'Not Recommended to President').filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myinterviews'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(myInterviewSummaryNotRecommendedListView, self).dispatch(request, *args, **kwargs)



class InterviewSummaryCreateView(CreateView):
    template_name = 'petitions/interviews/interviewsummary_form.html'
    model = InterviewSummary
    form_class = InterviewSummaryForm
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.added_by = CustomUser.objects.get(id=self.request.user.id)
        instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
        instance.save()
        sweetify.success(self.request, 'Interview Summary for the petitioner added sucessfully', button=True, timer=15000)
        return redirect('interviewsummary_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_interviewsummary'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(InterviewSummaryCreateView, self).dispatch(request, *args, **kwargs)


class InterviewSummaryDetailView(DetailView):
    template_name = 'petitions/interviews/interviewsummary_detail.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(InterviewSummaryDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_interviewdetails'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(InterviewSummaryDetailView, self).dispatch(request, *args, **kwargs)


class InterviewSummaryUpdateView(UpdateView):
    template_name = 'petitions/interviews/interviewsummary_edit.html'
    model = InterviewSummary
    form_class = InterviewSummaryEditForm
    def form_valid(self, form):
        interview = form.save(commit=False)
        interview.updated_by = CustomUser.objects.get(id=self.request.user.id)
        interview.save()
        sweetify.success(self.request, 'Interview Summary for the petitioner updated sucessfully', button=True,
                         timer=15000)
        return redirect('interviewsummary_detail', interview.id)

    def dispatch(self, request, *args, **kwargs):
        interviewtoupdate = InterviewSummary.objects.get(pk=self.kwargs.get('pk'))
        interviewdate = interviewtoupdate.created.date()
        if not interviewdate == date.today():
            """ Permission check for this class """
            if not request.user.has_perm('petitions.change_interviewsummary'):
                raise PermissionDenied("You do not have permission to delete events")
        else:
            if  request.user.has_perm('petitions.change_interviewsummary'):
                return super(InterviewSummaryUpdateView, self).dispatch(request, *args, **kwargs)
            else:
                if not interviewtoupdate.added_by == self.request.user:
                    raise PermissionDenied("You do not have permission to delete events")
        return super(InterviewSummaryUpdateView, self).dispatch(request, *args, **kwargs)

@permission_required ('petitions.can_print_interviews', raise_exception=True)
def GenerateInterviewSummary(request, pk):
    interview = InterviewSummary.objects.get(pk=pk)
    today = date.today()
    if interview.hearing.admissibility.petitioner.nextofkin== '':
        nextofkin = None
        relationshipwithnextofkin = None
    else:
        nextofkin = interview.hearing.admissibility.petitioner.nextofkin
        relationshipwithnextofkin = interview.hearing.admissibility.petitioner.relationshipwithnextofkin
    if interview.hearing.admissibility.petitioner.contactperson == '':
        contactperson = None
        contactpersontelno = None
    else:
        contactperson = interview.hearing.admissibility.petitioner.contactperson
        contactpersontelno = interview.hearing.admissibility.petitioner.telnoofcontactperson
    if interview.hearing.admissibility.petitioner.homechief == '':
        nameofhomechief = None
    else:
        nameofhomechief = interview.hearing.admissibility.petitioner.homechief
    if interview.hearing.admissibility.petitioner.dateofconviction.year - interview.hearing.admissibility.petitioner.dateofcustody.year == '':
        yearsinremand = 0
    else:
        yearsinremand = interview.hearing.admissibility.petitioner.dateofconviction.year - interview.hearing.admissibility.petitioner.dateofcustody.year
    if interview.hearing.admissibility.petitioner.sentence==None:
        sentence = 'LIFE IMPRISONMENT'
    else:
        sentence = str(interview.hearing.admissibility.petitioner.sentence)+' '+'YEARS IMPRISONMENT'
    if interview.hearing.admissibility.petitioner.chargedalonefortheoffense==True:
        chargedalone = 'YES'
    else:
        chargedalone = 'NO'
    if interview.hearing.admissibility.petitioner.namesofcoaccused=='':
        coaccused = 'None'
    else:
        coaccused = interview.hearing.admissibility.petitioner.namesofcoaccused
    if interview.hearing.admissibility.petitioner.knowledgeofthevictim== True:
        knowledgeofvictim = 'YES'
    else:
        knowledgeofvictim = 'NO'
    if interview.hearing.admissibility.petitioner.nameofvictim== '':
        nameofvictim = 'None'
    else:
        nameofvictim = interview.hearing.admissibility.petitioner.nameofvictim
    if interview.hearing.admissibility.petitioner.areaofresidence== '':
        areaofresidence = 'None'
    else:
        areaofresidence = interview.hearing.admissibility.petitioner.areaofresidence
    if interview.hearing.admissibility.petitioner.previousconvictions== '':
        previousconvictions = 'None'
    else:
        previousconvictions = interview.hearing.admissibility.petitioner.previousconvictions
    if interview.hearing.admissibility.petitioner.previouspetition== True:
        previouspetition = 'YES'
    else:
        previouspetition = 'NO'
    if interview.hearing.admissibility.petitioner.reasonofdenialofpreviouspetition== '':
        reasonofdenial = 'None'
    else:
        reasonofdenial = interview.hearing.admissibility.petitioner.reasonofdenialofpreviouspetition
    if interview.hearing.admissibility.petitioner.anydisplinaryactioninprison== True:
        disciplinaryaction = 'YES'
    else:
        disciplinaryaction = 'NO'
    if interview.hearing.admissibility.petitioner.detailsofdisplinaryactioninprison== '':
        explanationofdisciplinaryaction = 'None'
    else:
        explanationofdisciplinaryaction = interview.hearing.admissibility.petitioner.detailsofdisplinaryactioninprison
    if interview.hearing.admissibility.petitioner.anyspecialcondition== True:
        anyspecialcondition = 'YES'
    else:
        anyspecialcondition = 'NO'
    if interview.hearing.admissibility.petitioner.detailsofspecialcondition== '':
        explanationofspecialcondition = 'None'
    else:
        explanationofspecialcondition = interview.hearing.admissibility.petitioner.detailsofspecialcondition
    if interview.hearing.admissibility.petitioner.areyouatrustee== True:
        trustee = 'YES'
    else:
        trustee = 'NO'
    if interview.hearing.admissibility.petitioner.dateofpromotiontotrustee== '':
        trustedate = 'None'
    else:
        trustedate = interview.hearing.admissibility.petitioner.dateofpromotiontotrustee
    if interview.hearing.admissibility.petitioner.anyspecialattributesorskills== True:
        anyskills = 'YES'
    else:
        anyskills = 'NO'
    if interview.hearing.admissibility.petitioner.explanationofspecialattributesorskills== '':
        skillsexplanation = 'None'
    else:
        skillsexplanation = interview.hearing.admissibility.petitioner.explanationofspecialattributesorskills
    if interview.hearing.admissibility.petitioner.appealedagainsttheconviction== True:
        appealed = 'YES'
    else:
        appealed = 'NO'
    if interview.hearing.admissibility.petitioner.appealoutcome== '':
        appealoutcome = 'None'
    else:
        appealoutcome = interview.hearing.admissibility.petitioner.appealoutcome
    if interview.hearing.admissibility.petitioner.appealcaseno== '':
        appealcaseno = 'None'
    else:
        appealcaseno = interview.hearing.admissibility.petitioner.appealcaseno
    if interview.hearing.admissibility.petitioner.anypendingcourtmatter== True:
        pendingcourtmatter = 'YES'
    else:
        pendingcourtmatter = 'NO'
    if interview.hearing.admissibility.petitioner.explanationofpendingcourtmatter== '':
        pendingexplanation = 'None'
    else:
        pendingexplanation = interview.hearing.admissibility.petitioner.explanationofpendingcourtmatter
    if interview.hearing.healthstatus== '':
        healthstatus = 'None'
    else:
        healthstatus = interview.hearing.healthstatus
    if interview.hearing.familystatus== '':
        familystatus = 'None'
    else:
        familystatus = interview.hearing.familystatus
    if interview.ownaccountofcircumstances== '':
        ownaccount = 'None'
    else:
        ownaccount = interview.ownaccountofcircumstances
    if interview.reconciliationefforts== '':
        reconciliationefforts = 'None'
    else:
        reconciliationefforts = interview.reconciliationefforts
    if interview.indicationofremosefulness== '':
        indicationofremorsefulness = 'None'
    else:
        indicationofremorsefulness = interview.indicationofremosefulness
    if interview.anyothercomments== '':
        anyothercomments = 'None'
    else:
        anyothercomments = interview.anyothercomments
    if interview.representationofthevictim== '':
        representationofvictim = 'None'
    else:
        representationofvictim = interview.representationofthevictim
    if interview.concludingobservations== '':
        concludingobservations = 'None'
    else:
        concludingobservations = interview.concludingobservations
    if interview.chairpersonvote== True:
        chairvote = 'Recommended'
    else:
        chairvote = 'Not Recommended'
    if interview.chairpersonvotereason== '':
        chairreason = 'None'
    else:
        chairreason = interview.chairpersonvotereason
    if interview.vicechairvote== True:
        vicechairvote = 'Recommended'
    else:
        vicechairvote = 'Not Recommended'
    if interview.vicechairvotereason== '':
        vicechairreason = 'None'
    else:
        vicechairreason = interview.vicechairvotereason
    if interview.m1vote== True:
        member1vote = 'Recommended'
    else:
        member1vote = 'Not Recommended'
    if interview.m1votereason== '':
        member1votereason = 'None'
    else:
        member1votereason = interview.m1votereason
    if interview.m2vote== True:
        member2vote = 'Recommended'
    else:
        member2vote = 'Not Recommended'
    if interview.m2votereason== '':
        member2votereason = 'None'
    else:
        member2votereason = interview.m2votereason
    if interview.m3vote== True:
        member3vote = 'Recommended'
    else:
        member3vote = 'Not Recommended'
    if interview.m3votereason== '':
        member3votereason = 'None'
    else:
        member3votereason = interview.m3votereason
    if interview.m4vote== True:
        member4vote = 'Recommended'
    else:
        member4vote = 'Not Recommended'
    if interview.m4votereason== '':
        member4votereason = 'None'
    else:
        member4votereason = interview.m4votereason
    if interview.m5vote== True:
        member5vote = 'Recommended'
    else:
        member5vote = 'Not Recommended'
    if interview.m5votereason== '':
        member5votereason = 'None'
    else:
        member5votereason = interview.m5votereason
    if interview.m6vote== True:
        member6vote = 'Recommended'
    else:
        member6vote = 'Not Recommended'
    if interview.m6votereason== '':
        member6votereason = 'None'
    else:
        member6votereason = interview.m6votereason

    interviewdate = interview.created
    data = {
        'name': interview.hearing.admissibility.petitioner.name,
        'prisonno':interview.hearing.admissibility.petitioner.prisonno,
        'created_at': interview.hearing.admissibility.petitioner.created,
        'prison': interview.hearing.admissibility.petitioner.prison,
        'nationality': interview.hearing.admissibility.petitioner.nationality,
        'court': interview.hearing.admissibility.petitioner.court,
        'courtno': interview.hearing.admissibility.petitioner.courtcaseno,
        'ageatconviction': interview.hearing.admissibility.petitioner.ageatconviction,
        'dateofconviction': interview.hearing.admissibility.petitioner.dateofconviction,
        'currentage': today.year - interview.hearing.admissibility.petitioner.dateofconviction.year + interview.hearing.admissibility.petitioner.ageatconviction,
        'ageoffense': interview.hearing.admissibility.petitioner.agewhenoffensewascommited,
        'nextofkin':nextofkin,
        'nextofkinrelationship':relationshipwithnextofkin,
        'contactperson':contactperson,
        'telno':contactpersontelno,
        'county':interview.hearing.admissibility.petitioner.county,
        'subcounty':interview.hearing.admissibility.petitioner.subcounty,
        'location':interview.hearing.admissibility.petitioner.location,
        'nearestschool':interview.hearing.admissibility.petitioner.nearestschool,
        'nameofhomechief':nameofhomechief,
        'offensecommitted':interview.hearing.admissibility.petitioner.whereoffensewascommitted,
        'dateofcustody':interview.hearing.admissibility.petitioner.dateofcustody,
        'yearsserved':today.year - interview.hearing.admissibility.petitioner.dateofcustody.year,
        'yearsinremand':yearsinremand,
        'sentence':sentence,
        'reliefsought':interview.hearing.admissibility.petitioner.reliefsought,
        'offence':interview.hearing.admissibility.petitioner.offence,
        'natureofoffense':interview.hearing.admissibility.petitioner.natureandparticularsofoffense,
        'chargedalone':chargedalone,
        'coaccused':coaccused,
        'knowledgeofvictim':knowledgeofvictim,
        'nameofvictim':nameofvictim,
        'areaofresidence':areaofresidence,
        'previousconvictions':previousconvictions,
        'previouspetition':previouspetition,
        'dateofpreviouspetition':interview.hearing.admissibility.petitioner.dateofpreviouspetition,
        'reasonofdenial':reasonofdenial,
        'reasonsforpetitining':interview.hearing.admissibility.petitioner.reasonforcurrentpetition,
        'disciplinaryaction':disciplinaryaction,
        'explanationofdisciplinaryaction':explanationofdisciplinaryaction,
        'anyspecialcondition':anyspecialcondition,
        'explanationofspecialcondition':explanationofspecialcondition,
        'trustee':trustee,
        'trustedate':trustedate,
        'anyskills':anyskills,
        'skillsexplanation':skillsexplanation,
        'appealed':appealed,
        'appealoutcome':appealoutcome,
        'appealcaseno':appealcaseno,
        'pendingcourtmatter':pendingcourtmatter,
        'pendingexplanation':pendingexplanation,
        'healthstatus':healthstatus,
        'familystatus':familystatus,
        'ownaccount':ownaccount,
        'reconciliationefforts':reconciliationefforts,
        'indicationofremorsefulness':indicationofremorsefulness,
        'anyothercomments':anyothercomments,
        'representationofvictim':representationofvictim,
        'concludingobservations':concludingobservations,
        'chairvote':chairvote,
        'chairreason':chairreason,
        'vicechairvote':vicechairvote,
        'vicechairreason':vicechairreason,
        'member1vote':member1vote,
        'member1votereason':member1votereason,
        'member2vote':member2vote,
        'member2votereason':member2votereason,
        'member3vote':member3vote,
        'member3votereason':member3votereason,
        'member4vote':member4vote,
        'member4votereason':member4votereason,
        'member5vote':member5vote,
        'member5votereason':member5votereason,
        'member6vote':member6vote,
        'member6votereason':member6votereason,
        'finalresolution':interview.finalresolution,
        'month':interviewdate.strftime("%B"),
        'day':interviewdate.day,
        'year':interviewdate.year,
    }
    pdf = render_to_pdf('petitions/interviews/interviewsummary_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@permission_required ('petitions.delete_interviewsummary', raise_exception=True)
def DeleteInterviewSummary(request,pk):
    InterviewSummary.objects.get(pk=pk).delete()
    sweetify.success(request, 'Interview summary  for the petitioner deleted successfully and all its consequent information ', button=True, timer=15000)
    return redirect('interviewsummary_list')


class RecommendationFormListView(ListView):
    template_name = 'petitions/recommendations/recommendationform_list.html'
    model = RecommendationForm
    def get_context_data(self, **kwargs):
        context = super(RecommendationFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_recommendations'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(RecommendationFormListView, self).dispatch(request, *args, **kwargs)

class MasterRecommendationFormListView(ListView):
    template_name = 'petitions/recommendations/master_recommendationform_list.html'
    model = RecommendationForm
    def get_context_data(self, **kwargs):
        context = super(MasterRecommendationFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_master_recommendations'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MasterRecommendationFormListView, self).dispatch(request, *args, **kwargs)

class MyRecommendationFormListView(ListView):
    template_name = 'petitions/recommendations/myrecommendationform_list.html'
    model = RecommendationForm
    def get_context_data(self, **kwargs):
        context = super(MyRecommendationFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = RecommendationForm.objects.filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myrecommendations'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyRecommendationFormListView, self).dispatch(request, *args, **kwargs)

class AwaitingRecommendationFormListView(ListView):
    template_name = 'petitions/recommendations/awaitingrecommendationform_list.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(AwaitingRecommendationFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = InterviewSummary.objects.filter(finalresolution='Recommended to President').filter(recommendationform__isnull=True).filter(hearing__admissibility__petitioner__exit__isnull=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_recommendations'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AwaitingRecommendationFormListView, self).dispatch(request, *args, **kwargs)

class MyAwaitingRecommendationFormListView(ListView):
    template_name = 'petitions/recommendations/myawaitingrecommendationform_list.html'
    model = InterviewSummary
    def get_context_data(self, **kwargs):
        context = super(MyAwaitingRecommendationFormListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = InterviewSummary.objects.filter(finalresolution='Recommended to President').filter(
            recommendationform__isnull=True).filter(hearing__admissibility__petitioner__exit__isnull=True).filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_myrecommendations'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAwaitingRecommendationFormListView, self).dispatch(request, *args, **kwargs)


class RecommendationFormCreateView(CreateView):
    template_name = 'petitions/recommendations/recommendationform_form.html'
    model = RecommendationForm
    form_class = RecommendationFormForm
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.added_by = CustomUser.objects.get(id=self.request.user.id)
        instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
        instance.save()
        sweetify.success(self.request, 'Recommendation for the petitioner submitted successfully', button=True,timer=15000)
        return redirect('recommendationform_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_recommendationform'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(RecommendationFormCreateView, self).dispatch(request, *args, **kwargs)

class RecommendationFormDetailView(DetailView):
    template_name = 'petitions/recommendations/recommendationform_detail.html'
    model = RecommendationForm
    def get_context_data(self, **kwargs):
        context = super(RecommendationFormDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_recommendationdetails'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(RecommendationFormDetailView, self).dispatch(request, *args, **kwargs)


class RecommendationFormUpdateView(UpdateView):
    template_name = 'petitions/recommendations/recommendationform_edit.html'
    model = RecommendationForm
    form_class = RecommendationUpdateForm
    def form_valid(self, form):
        recommendation = form.save(commit=False)
        recommendation.updated_by = CustomUser.objects.get(id=self.request.user.id)
        recommendation.save()
        sweetify.success(self.request, 'Recommendation for the petitioner updated successfully', button=True,
                         timer=15000)
        return redirect('recommendationform_detail', recommendation.id)
    def dispatch(self, request, *args, **kwargs):
        recommendationtoupdate = RecommendationForm.objects.get(pk=self.kwargs.get('pk'))
        recommendationdate = recommendationtoupdate.created.date()
        if not recommendationdate == date.today():
            """ Permission check for this class """
            if not request.user.has_perm('petitions.change_interviewsummary'):
                raise PermissionDenied("You do not have permission to delete events")
        else:
            if  request.user.has_perm('petitions.change_interviewsummary'):
                return super(RecommendationFormUpdateView, self).dispatch(request, *args, **kwargs)
            else:
                if not recommendationtoupdate.added_by == self.request.user:
                    raise PermissionDenied("You do not have permission to delete events")
        return super(RecommendationFormUpdateView, self).dispatch(request, *args, **kwargs)

def get_circumstance_from_summary(request):
    interview_id = request.GET.get('interview')
    interview = InterviewSummary.objects.get(pk=interview_id)
    admissibility = interview.hearing.admissibility
    try:
        summary = PetitionSummary.objects.get(admissibility=admissibility.id).typeandcircumstancesofoffence
    except PetitionSummary.DoesNotExist:
        summary = ''
    return render(request, 'petitions/recommendations/get-circumstance-from-summary.html', {'summary': summary})


@permission_required ('petitions.can_print_recommendations', raise_exception=True)
def GenerateRecommendationForm(request, pk):
        recommendation = RecommendationForm.objects.get(pk=pk)
        recommendationdate = recommendation.created
        petitiondate = recommendation.interview.hearing.admissibility.petitioner.created
        data = {
             'name': recommendation.interview.hearing.admissibility.petitioner.name,
             'prisonno': recommendation.interview.hearing.admissibility.petitioner.prisonno,
            'petitionmonth': petitiondate.strftime("%B"),
            'petitionday': petitiondate.day,
            'petitionyear': petitiondate.year,
             'prison': recommendation.interview.hearing.admissibility.petitioner.prison,
             'mercy': recommendation.mercy,
             'explanationforrecommendation': recommendation.explanationofrecommedation,
            'month': recommendationdate.strftime("%B"),
            'day': recommendationdate.day,
            'year': recommendationdate.year,
        }
        pdf = render_to_pdf('petitions/recommendations/recommendation_print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

@permission_required ('petitions.delete_recommendationform', raise_exception=True)
def DeleteRecommendationForm(request,pk):
    RecommendationForm.objects.get(pk=pk).delete()
    sweetify.success(request, 'Recommendation for the petitioner deleted successfully and all its consequent information', button=True, timer=15000)
    return redirect('recommendationform_list')

class GrantListView(ListView):
    template_name = 'petitions/grants/grant_list.html'
    model = Grant
    def get_context_data(self, **kwargs):
        context = super(GrantListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_grants'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(GrantListView, self).dispatch(request, *args, **kwargs)

class MyGrantListView(ListView):
    template_name = 'petitions/grants/mygrant_list.html'
    model = Grant
    def get_context_data(self, **kwargs):
        context = super(MyGrantListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = Grant.objects.all().filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_mygrants'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyGrantListView, self).dispatch(request, *args, **kwargs)


class AwaitingGrantListView(ListView):
    template_name = 'petitions/grants/awaitingrant_list.html'
    model = Grant
    def get_context_data(self, **kwargs):
        context = super(AwaitingGrantListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = RecommendationForm.objects.filter(grant__isnull=True).filter(interview__hearing__admissibility__petitioner__exit__isnull=True)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_grants'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(AwaitingGrantListView, self).dispatch(request, *args, **kwargs)

class MyAwaitingGrantListView(ListView):
    template_name = 'petitions/grants/myawaitingrant_list.html'
    model = Grant
    def get_context_data(self, **kwargs):
        context = super(MyAwaitingGrantListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = RecommendationForm.objects.filter(grant__isnull=True).filter(interview__hearing__admissibility__petitioner__exit__isnull=True).filter(added_by=self.request.user)
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_mygrants'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(MyAwaitingGrantListView, self).dispatch(request, *args, **kwargs)


class GrantCreateView(CreateView):
    template_name = 'petitions/grants/grant_form.html'
    model = Grant
    form_class = GrantForm
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.added_by = CustomUser.objects.get(id=self.request.user.id)
        instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
        instance.save()
        sweetify.success(self.request, 'Grand of petition generated successfully', button=True, timer=15000)
        return redirect('petitions_grant_detail', instance.id)
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_grant'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(GrantCreateView, self).dispatch(request, *args, **kwargs)


class GrantDetailView(DetailView):
    template_name = 'petitions/grants/grant_detail.html'
    model = Grant
    def get_context_data(self, **kwargs):
        context = super(GrantDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_grantdetails'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(GrantDetailView, self).dispatch(request, *args, **kwargs)

@permission_required ('petitions.delete_grant', raise_exception=True)
def DeleteGrant(request,pk):
    Grant.objects.get(pk=pk).delete()
    sweetify.success(request, 'Grand of petition generated successfully', button=True, timer=15000)
    return redirect('petitions_grant_list')

@permission_required ('petitions.can_print_grants', raise_exception=True)
def GenerateGrant(request, pk):
    grant = Grant.objects.get(pk=pk)
    today = date.today()
    if grant.recommendation.interview.hearing.admissibility.petitioner.nextofkin== '':
        nextofkin = None
        relationshipwithnextofkin = None
    else:
        nextofkin = grant.recommendation.interview.hearing.admissibility.petitioner.nextofkin
        relationshipwithnextofkin = grant.recommendation.interview.hearing.admissibility.petitioner.relationshipwithnextofkin
    if grant.recommendation.interview.hearing.admissibility.petitioner.contactperson == '':
        contactperson = None
        contactpersontelno = None
    else:
        contactperson = grant.recommendation.interview.hearing.admissibility.petitioner.contactperson
        contactpersontelno = grant.recommendation.interview.hearing.admissibility.petitioner.telnoofcontactperson
    if grant.recommendation.interview.hearing.admissibility.petitioner.homechief == '':
        nameofhomechief = None
    else:
        nameofhomechief = grant.recommendation.interview.hearing.admissibility.petitioner.homechief
    if grant.recommendation.interview.hearing.admissibility.petitioner.dateofconviction.year - grant.recommendation.interview.hearing.admissibility.petitioner.dateofcustody.year == '':
        yearsinremand = 0
    else:
        yearsinremand = grant.recommendation.interview.hearing.admissibility.petitioner.dateofconviction.year - grant.recommendation.interview.hearing.admissibility.petitioner.dateofcustody.year
    if grant.recommendation.interview.hearing.admissibility.petitioner.sentence==None:
        sentence = 'LIFE IMPRISONMENT'
    else:
        sentence = str(grant.recommendation.interview.hearing.admissibility.petitioner.sentence)+' '+'YEARS IMPRISONMENT'
    if grant.recommendation.interview.hearing.admissibility.petitioner.chargedalonefortheoffense==True:
        chargedalone = 'YES'
    else:
        chargedalone = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.namesofcoaccused=='':
        coaccused = 'None'
    else:
        coaccused = grant.recommendation.interview.hearing.admissibility.petitioner.namesofcoaccused
    if grant.recommendation.interview.hearing.admissibility.petitioner.knowledgeofthevictim== True:
        knowledgeofvictim = 'YES'
    else:
        knowledgeofvictim = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.nameofvictim== '':
        nameofvictim = 'None'
    else:
        nameofvictim = grant.recommendation.interview.hearing.admissibility.petitioner.nameofvictim
    if grant.recommendation.interview.hearing.admissibility.petitioner.areaofresidence== '':
        areaofresidence = 'None'
    else:
        areaofresidence = grant.recommendation.interview.hearing.admissibility.petitioner.areaofresidence
    if grant.recommendation.interview.hearing.admissibility.petitioner.previousconvictions== '':
        previousconvictions = 'None'
    else:
        previousconvictions = grant.recommendation.interview.hearing.admissibility.petitioner.previousconvictions
    if grant.recommendation.interview.hearing.admissibility.petitioner.previouspetition== True:
        previouspetition = 'YES'
    else:
        previouspetition = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.reasonofdenialofpreviouspetition== '':
        reasonofdenial = 'None'
    else:
        reasonofdenial = grant.recommendation.interview.hearing.admissibility.petitioner.reasonofdenialofpreviouspetition
    if grant.recommendation.interview.hearing.admissibility.petitioner.anydisplinaryactioninprison== True:
        disciplinaryaction = 'YES'
    else:
        disciplinaryaction = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.detailsofdisplinaryactioninprison== '':
        explanationofdisciplinaryaction = 'None'
    else:
        explanationofdisciplinaryaction = grant.recommendation.interview.hearing.admissibility.petitioner.detailsofdisplinaryactioninprison
    if grant.recommendation.interview.hearing.admissibility.petitioner.anyspecialcondition== True:
        anyspecialcondition = 'YES'
    else:
        anyspecialcondition = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.detailsofspecialcondition== '':
        explanationofspecialcondition = 'None'
    else:
        explanationofspecialcondition = grant.recommendation.interview.hearing.admissibility.petitioner.detailsofspecialcondition
    if grant.recommendation.interview.hearing.admissibility.petitioner.areyouatrustee== True:
        trustee = 'YES'
    else:
        trustee = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.dateofpromotiontotrustee== '':
        trustedate = 'None'
    else:
        trustedate = grant.recommendation.interview.hearing.admissibility.petitioner.dateofpromotiontotrustee
    if grant.recommendation.interview.hearing.admissibility.petitioner.anyspecialattributesorskills== True:
        anyskills = 'YES'
    else:
        anyskills = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.explanationofspecialattributesorskills== '':
        skillsexplanation = 'None'
    else:
        skillsexplanation = grant.recommendation.interview.hearing.admissibility.petitioner.explanationofspecialattributesorskills
    if grant.recommendation.interview.hearing.admissibility.petitioner.appealedagainsttheconviction== True:
        appealed = 'YES'
    else:
        appealed = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.appealoutcome== '':
        appealoutcome = 'None'
    else:
        appealoutcome = grant.recommendation.interview.hearing.admissibility.petitioner.appealoutcome
    if grant.recommendation.interview.hearing.admissibility.petitioner.appealcaseno== '':
        appealcaseno = 'None'
    else:
        appealcaseno = grant.recommendation.interview.hearing.admissibility.petitioner.appealcaseno
    if grant.recommendation.interview.hearing.admissibility.petitioner.anypendingcourtmatter== True:
        pendingcourtmatter = 'YES'
    else:
        pendingcourtmatter = 'NO'
    if grant.recommendation.interview.hearing.admissibility.petitioner.explanationofpendingcourtmatter== '':
        pendingexplanation = 'None'
    else:
        pendingexplanation = grant.recommendation.interview.hearing.admissibility.petitioner.explanationofpendingcourtmatter
    petitiondate = grant.recommendation.interview.hearing.admissibility.petitioner.created
    grantdate = grant.created
    data = {
        'name': grant.recommendation.interview.hearing.admissibility.petitioner.name,
        'prisonno':grant.recommendation.interview.hearing.admissibility.petitioner.prisonno,
        'created_at': grant.recommendation.interview.hearing.admissibility.petitioner.created,
        'prison': grant.recommendation.interview.hearing.admissibility.petitioner.prison,
        'nationality': grant.recommendation.interview.hearing.admissibility.petitioner.nationality,
        'court': grant.recommendation.interview.hearing.admissibility.petitioner.court,
        'courtno': grant.recommendation.interview.hearing.admissibility.petitioner.courtcaseno,
        'ageatconviction': grant.recommendation.interview.hearing.admissibility.petitioner.ageatconviction,
        'dateofconviction': grant.recommendation.interview.hearing.admissibility.petitioner.dateofconviction,
        'currentage': today.year - grant.recommendation.interview.hearing.admissibility.petitioner.dateofconviction.year + grant.recommendation.interview.hearing.admissibility.petitioner.ageatconviction,
        'ageoffense': grant.recommendation.interview.hearing.admissibility.petitioner.agewhenoffensewascommited,
        'nextofkin':nextofkin,
        'nextofkinrelationship':relationshipwithnextofkin,
        'contactperson':contactperson,
        'telno':contactpersontelno,
        'county':grant.recommendation.interview.hearing.admissibility.petitioner.county,
        'subcounty':grant.recommendation.interview.hearing.admissibility.petitioner.subcounty,
        'location':grant.recommendation.interview.hearing.admissibility.petitioner.location,
        'nearestschool':grant.recommendation.interview.hearing.admissibility.petitioner.nearestschool,
        'nameofhomechief':nameofhomechief,
        'offensecommitted':grant.recommendation.interview.hearing.admissibility.petitioner.whereoffensewascommitted,
        'dateofcustody':grant.recommendation.interview.hearing.admissibility.petitioner.dateofcustody,
        'yearsserved':today.year - grant.recommendation.interview.hearing.admissibility.petitioner.dateofcustody.year,
        'yearsinremand':yearsinremand,
        'sentence':sentence,
        'reliefsought':grant.recommendation.interview.hearing.admissibility.petitioner.reliefsought,
        'offence':grant.recommendation.interview.hearing.admissibility.petitioner.offence,
        'natureofoffense':grant.recommendation.interview.hearing.admissibility.petitioner.natureandparticularsofoffense,
        'chargedalone':chargedalone,
        'coaccused':coaccused,
        'knowledgeofvictim':knowledgeofvictim,
        'nameofvictim':nameofvictim,
        'areaofresidence':areaofresidence,
        'previousconvictions':previousconvictions,
        'previouspetition':previouspetition,
        'dateofpreviouspetition':grant.recommendation.interview.hearing.admissibility.petitioner.dateofpreviouspetition,
        'reasonofdenial':reasonofdenial,
        'reasonsforpetitining':grant.recommendation.interview.hearing.admissibility.petitioner.reasonforcurrentpetition,
        'disciplinaryaction':disciplinaryaction,
        'explanationofdisciplinaryaction':explanationofdisciplinaryaction,
        'anyspecialcondition':anyspecialcondition,
        'explanationofspecialcondition':explanationofspecialcondition,
        'trustee':trustee,
        'trustedate':trustedate,
        'anyskills':anyskills,
        'skillsexplanation':skillsexplanation,
        'appealed':appealed,
        'appealoutcome':appealoutcome,
        'appealcaseno':appealcaseno,
        'pendingcourtmatter':pendingcourtmatter,
        'pendingexplanation':pendingexplanation,
        'petitionmonth':petitiondate.strftime("%B"),
        'petitionday':petitiondate.day,
        'petitionyear':petitiondate.year,
        'grantmonth':grantdate.strftime("%B"),
        'grantday':grantdate.day,
        'grantyear':grantdate.year,
    }
    pdf = render_to_pdf('petitions/grants/grantpetition_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')



class ExitListView(ListView):
    template_name = 'petitions/exits/exits_list.html'
    model = Exit
    def get_context_data(self, **kwargs):
        context = super(ExitListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_exits'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitListView, self).dispatch(request, *args, **kwargs)

class ExitEscapeListView(ListView):
    template_name = 'petitions/exits/exitsescapes_list.html'
    model = Exit
    def get_context_data(self, **kwargs):
        context = super(ExitEscapeListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = Exit.objects.filter(exitreason='The Petitioner escaped the prison')
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_exits'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitEscapeListView, self).dispatch(request, *args, **kwargs)

class ExitDeathsListView(ListView):
    template_name = 'petitions/exits/exitsdeaths_list.html'
    model = Exit
    def get_context_data(self, **kwargs):
        context = super(ExitDeathsListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = Exit.objects.filter(exitreason='The petitioner died while in prison')
        return queryset

    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_exits'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitDeathsListView, self).dispatch(request, *args, **kwargs)

class ExitReleasedUnderPomacListView(ListView):
    template_name = 'petitions/exits/exitsreleasedunderpomac_list.html'
    model = Exit
    def get_context_data(self, **kwargs):
        context = super(ExitReleasedUnderPomacListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = Exit.objects.filter(exitreason='Released under POMAC')
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_exits'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitReleasedUnderPomacListView, self).dispatch(request, *args, **kwargs)

class ExitServedTermListView(ListView):
    template_name = 'petitions/exits/exitsservedterm_list.html'
    model = Exit
    def get_context_data(self, **kwargs):
        context = super(ExitServedTermListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = Exit.objects.filter(exitreason='Released after serving the term')
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_exits'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitServedTermListView, self).dispatch(request, *args, **kwargs)

class ExitAfterResentencingListView(ListView):
    template_name = 'petitions/exits/exitsreleasedafterresentencing_list.html'
    model = Exit
    def get_context_data(self, **kwargs):
        context = super(ExitAfterResentencingListView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def get_queryset(self):
        queryset = Exit.objects.filter(exitreason='The petitioner was released after resentencing')
        return queryset
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_exits'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitAfterResentencingListView, self).dispatch(request, *args, **kwargs)


class ExitCreateView(CreateView):
    template_name = 'petitions/exits/exits_form.html'
    model = Exit
    form_class = ExitForm
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.added_by = CustomUser.objects.get(id=self.request.user.id)
        instance.updated_by = CustomUser.objects.get(id=self.request.user.id)
        instance.save()
        sweetify.success(self.request, 'Exit Details for the petitioner submitted successfully', button=True, timer=15000)
        return redirect('petitions_exit_detail', instance.id)
    def get_context_data(self, **kwargs):
        context = super(ExitCreateView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.add_exit'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitCreateView, self).dispatch(request, *args, **kwargs)


class ExitDetailView(DetailView):
    template_name = 'petitions/exits/exits_detail.html'
    model = Exit
    def get_context_data(self, **kwargs):
        context = super(ExitDetailView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        """ Permission check for this class """
        if not request.user.has_perm('petitions.can_view_exitdetails'):
            raise PermissionDenied("You do not have permission to view status events")
        return super(ExitDetailView, self).dispatch(request, *args, **kwargs)


class ExitUpdateView(UpdateView):
    template_name = 'petitions/exits/updateexits_form.html'
    model = Exit
    form_class = ExitFormUpdate
    def form_valid(self, form):
        exitpetitioner = form.save(commit=False)
        exitpetitioner.updated_by = CustomUser.objects.get(id=self.request.user.id)
        exitpetitioner.save()
        sweetify.success(self.request, 'Exit Details for the petitioner updated successfully', button=True,
                         timer=15000)
        return redirect('petitions_exit_detail', exitpetitioner.id)
    def get_context_data(self, **kwargs):
        context = super(ExitUpdateView, self).get_context_data(**kwargs)
        today = date.today()
        context['today'] = today
        return context
    def dispatch(self, request, *args, **kwargs):
        exittoupdate = Exit.objects.get(pk=self.kwargs.get('pk'))
        exitdate = exittoupdate.created.date()
        if not exitdate == date.today():
            """ Permission check for this class """
            if not request.user.has_perm('petitions.change_exit'):
                raise PermissionDenied("You do not have permission to delete events")
        else:
            if  request.user.has_perm('petitions.change_exit'):
                return super(ExitUpdateView, self).dispatch(request, *args, **kwargs)
            else:
                if not exittoupdate.added_by == self.request.user:
                    raise PermissionDenied("You do not have permission to delete events")
        return super(ExitUpdateView, self).dispatch(request, *args, **kwargs)

@permission_required ('petitions.delete_exit', raise_exception=True)
def DeleteExit(request,pk):
    Exit.objects.get(pk=pk).delete()
    sweetify.success(request, 'Exit Deleted Successfully', button=True, timer=15000)
    return redirect('petitions_exit_list')


@permission_required ('petitions.can_view_main_dashboard', raise_exception=False, login_url='/my-dashboard')
def dashboard(request):
    user = CustomUser.objects.get(pk=request.user.id)
    if (user.first_name == '' and user.last_name == ''):
        sweetify.warning(request,
                         'Please update your profile using your official name. If you have already done that ignore this message',
                         button=True, timer=15000)
        return redirect('updateprofile', request.user.id)
    data = {
        'noofpetitions': PetitionForm.objects.count(),
        'eligiblepetitions': PetitionForm.objects.filter(anypendingcourtmatter=False).count(),
        'ineligiblepetitions': PetitionForm.objects.filter(anypendingcourtmatter=True).count(),
        'totaladmissibilities': AdmissibilityForm.objects.count(),
        'admissiblepetitions': AdmissibilityForm.objects.filter(admissability=True).count(),
        'inadmissiblepetitions': AdmissibilityForm.objects.filter(admissability=False).count(),
        'awaitingadmissibility': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(admissibilityform__isnull=True).filter(exit__isnull=True).count(),
        'summaries': PetitionSummary.objects.all().count(),
        'hearings': HearingSummary.objects.all().count(),
        'deferredhearings': HearingSummary.objects.filter(action='Defer the petition to a later date').count(),
        'declinedhearings': HearingSummary.objects.filter(action='Decline the Petition').count(),
        'scheduledforinterview': HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull= False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True).count(),
        'awaitingscheduleforinterview': HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull= True).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True).count(),
        'interviews': InterviewSummary.objects.all().count(),
        'interviewsrecommended': InterviewSummary.objects.filter(finalresolution = 'Recommended to President').count(),
        'notinterviewsrecommended': InterviewSummary.objects.filter(finalresolution = 'Not Recommended to President').count(),
        'recommendations': RecommendationForm.objects.all().count(),
        'awaitingsummaries': AdmissibilityForm.objects.filter(admissability=True).filter(petitionsummary__isnull=True).filter(petitioner__exit__isnull=True).count(),
        'awaitinghearing':AdmissibilityForm.objects.filter(admissability=True).filter(hearing__isnull=True).filter(hearingdate__isnull=False).filter(petitioner__exit__isnull=True).count(),
        'awaitingscheduleforhearing':AdmissibilityForm.objects.filter(admissability=True).filter(hearingdate__isnull=True).filter(hearing__isnull=True).filter(petitioner__exit__isnull=True).count(),
        'awaitingrecommendations':InterviewSummary.objects.filter(finalresolution='Recommended to President').filter(recommendationform__isnull=True).filter(hearing__admissibility__petitioner__exit__isnull=True).count(),
        'awaitinginterviews':HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull=False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True).count(),
        'awaitingregrant':RecommendationForm.objects.filter(grant__isnull=True).filter(interview__hearing__admissibility__petitioner__exit__isnull=True).count(),
        'grants':Grant.objects.all().count(),
        'trustees': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(areyouatrustee=True).count(),
        'foreigners': PetitionForm.objects.filter(anypendingcourtmatter=False).exclude(nationality='Kenyan').count(),
        'ppmental': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialcondition=True).filter(ageatconviction__gte=18).filter(prisonno__endswith='P').count(),
        'ppunderage': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialcondition=True).filter(ageatconviction__lt=18).filter(prisonno__endswith='P').count(),
        'specialcondition': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialcondition=True).count(),
        'appealed': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(appealedagainsttheconviction=True).count(),
        'withskillsattainedinprison': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(anyspecialattributesorskills=True).count(),
        'offences': Offence.objects.count(),
        'exitslist': Exit.objects.count(),
        'exitslistescaped': Exit.objects.filter(exitreason='The Petitioner escaped the prison').count(),
        'exitsdeath': Exit.objects.filter(exitreason='The petitioner died while in prison').count(),
        'exitsservedsentence': Exit.objects.filter(exitreason='Released after serving the term').count(),
        'exitsreleasedbypomac': Exit.objects.filter(exitreason='exitsreleasedbypomac').count(),
        'exitsresetencing': Exit.objects.filter(exitreason='The petitioner was released after resentencing').count(),
        'prisons': Prison.objects.count(),
        'courts': Court.objects.count(),

    }
    return render(request, 'petitions/dashboard/index.html',data)

def mydashboard(request):
    user = CustomUser.objects.get(pk=request.user.id)
    if (user.first_name == '' and user.last_name == ''):
        sweetify.warning(request,'Please update your profile. Provide your official names. If you have done that already ignore this message',button=True, timer=15000)
        return redirect('updateprofile', request.user.id)
    data = {
        'noofpetitions': PetitionForm.objects.filter(added_by=request.user).count(),
        'eligiblepetitions': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(added_by=request.user).count(),
        'ineligiblepetitions': PetitionForm.objects.filter(anypendingcourtmatter=True).filter(added_by=request.user).count(),
        'totaladmissibilities': AdmissibilityForm.objects.filter(added_by=request.user).count(),
        'admissiblepetitions': AdmissibilityForm.objects.filter(admissability=True).filter(added_by=request.user).count(),
        'inadmissiblepetitions': AdmissibilityForm.objects.filter(admissability=False).filter(added_by=request.user).count(),
        'awaitingadmissibility': PetitionForm.objects.filter(anypendingcourtmatter=False).filter(admissibilityform__isnull=True).filter(exit__isnull=True).filter(added_by=request.user).count(),
        'summaries': PetitionSummary.objects.all().filter(added_by=request.user).count(),
        'hearings': HearingSummary.objects.all().filter(added_by=request.user).count(),
        'deferredhearings': HearingSummary.objects.filter(action='Defer the petition to a later date').filter(added_by=request.user).count(),
        'declinedhearings': HearingSummary.objects.filter(action='Decline the Petition').filter(added_by=request.user).count(),
        'scheduledforinterview': HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull= False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True).filter(added_by=request.user).count(),
        'awaitingscheduleforinterview': HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull= True).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True).filter(added_by=request.user).count(),
        'interviews': InterviewSummary.objects.all().filter(added_by=request.user).count(),
        'interviewsrecommended': InterviewSummary.objects.filter(finalresolution = 'Recommended to President').filter(added_by=request.user).count(),
        'notinterviewsrecommended': InterviewSummary.objects.filter(finalresolution = 'Not Recommended to President').filter(added_by=request.user).count(),
        'recommendations': RecommendationForm.objects.all().filter(added_by=request.user).count(),
        'awaitingsummaries': AdmissibilityForm.objects.filter(admissability=True).filter(petitionsummary__isnull=True).filter(petitioner__exit__isnull=True).filter(added_by=request.user).count(),
        'awaitinghearing':AdmissibilityForm.objects.filter(admissability=True).filter(hearingdate__isnull= False).filter(hearing__isnull=True).filter(petitioner__exit__isnull=True).filter(added_by=request.user).count(),
        'awaitingrecommendations':InterviewSummary.objects.filter(finalresolution='Recommended to President').filter(recommendationform__isnull=True).filter(hearing__admissibility__petitioner__exit__isnull=True).filter(added_by=request.user).count(),
        'awaitinginterviews':HearingSummary.objects.filter(action='Interview the Petitioner').filter(interviewdate__isnull=False).filter(interviewsummary__isnull=True).filter(admissibility__petitioner__exit__isnull=True).filter(added_by=request.user).count(),
        'myawaitingregrant':RecommendationForm.objects.filter(grant__isnull=True).filter(interview__hearing__admissibility__petitioner__exit__isnull=True).filter(added_by=request.user).count(),
        'mygrants': Grant.objects.all().filter(added_by=request.user).count(),
    }
    return render(request, 'petitions/dashboard/mydashboard.html',data)

