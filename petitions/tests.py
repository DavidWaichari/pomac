import unittest
from django.urls import reverse
from django.test import Client
from .models import PetitionForm, Court, Prison, County, SubCounty
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_petitionform(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["prisonno"] = "prisonno"
    defaults["nationality"] = "nationality"
    defaults["courtcaseno"] = "courtcaseno"
    defaults["ageatconviction"] = "ageatconviction"
    defaults["currentage"] = "currentage"
    defaults["agewhenoffensewascommited"] = "agewhenoffensewascommited"
    defaults["nextofkin"] = "nextofkin"
    defaults["relationshipwithnextofkin"] = "relationshipwithnextofkin"
    defaults["contactperson"] = "contactperson"
    defaults["telnoofcontactperson"] = "telnoofcontactperson"
    defaults["location"] = "location"
    defaults["nearestschool"] = "nearestschool"
    defaults["homechief"] = "homechief"
    defaults["whereoffensewascommitted"] = "whereoffensewascommitted"
    defaults["dateofconviction"] = "dateofconviction"
    defaults["dateofcustody"] = "dateofcustody"
    defaults["reliefsought"] = "reliefsought"
    defaults["natureandparticularsofoffense"] = "natureandparticularsofoffense"
    defaults["chargedalonefortheoffense"] = "chargedalonefortheoffense"
    defaults["namesofcoaccused"] = "namesofcoaccused"
    defaults["knowledgeofthevictim"] = "knowledgeofthevictim"
    defaults["nameofvictim"] = "nameofvictim"
    defaults["areaofresidence"] = "areaofresidence"
    defaults["previousconvictions"] = "previousconvictions"
    defaults["previouspetition"] = "previouspetition"
    defaults["dateofpreviouspetition"] = "dateofpreviouspetition"
    defaults["reasonofdenialofpreviouspetition"] = "reasonofdenialofpreviouspetition"
    defaults["reasonforcurrentpetition"] = "reasonforcurrentpetition"
    defaults["anydisplinaryactioninprison"] = "anydisplinaryactioninprison"
    defaults["detailsofdisplinaryactioninprison"] = "detailsofdisplinaryactioninprison"
    defaults["anyspecialcondition"] = "anyspecialcondition"
    defaults["detailsofspecialcondition"] = "detailsofspecialcondition"
    defaults["areyouatrustee"] = "areyouatrustee"
    defaults["dateofpromotiontotrustee"] = "dateofpromotiontotrustee"
    defaults["anyspecialattributesorskills"] = "anyspecialattributesorskills"
    defaults["explanationofspecialattributesorskills"] = "explanationofspecialattributesorskills"
    defaults["appealedagainsttheconviction"] = "appealedagainsttheconviction"
    defaults["appealcaseno"] = "appealcaseno"
    defaults["appealoutcome"] = "appealoutcome"
    defaults["anypendingcourtmatter"] = "anypendingcourtmatter"
    defaults["explanationofpendingcourtmatter"] = "explanationofpendingcourtmatter"
    defaults.update(**kwargs)
    if "court" not in defaults:
        defaults["court"] = create_court()
    if "prison" not in defaults:
        defaults["prison"] = create_prison()
    if "county" not in defaults:
        defaults["county"] = create_county()
    if "subcounty" not in defaults:
        defaults["subcounty"] = create_subcounty()
    return PetitionForm.objects.create(**defaults)


def create_court(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Court.objects.create(**defaults)


def create_prison(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Prison.objects.create(**defaults)


def create_county(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return County.objects.create(**defaults)


def create_subcounty(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return SubCounty.objects.create(**defaults)


class PetitionFormViewTest(unittest.TestCase):
    '''
    Tests for PetitionForm
    '''
    def setUp(self):
        self.client = Client()

    def test_list_petitionform(self):
        url = reverse('petitions_petitionform_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_petitionform(self):
        url = reverse('petitions_petitionform_create')
        data = {
            "name": "name",
            "prisonno": "prisonno",
            "nationality": "nationality",
            "courtcaseno": "courtcaseno",
            "ageatconviction": "ageatconviction",
            "currentage": "currentage",
            "agewhenoffensewascommited": "agewhenoffensewascommited",
            "nextofkin": "nextofkin",
            "relationshipwithnextofkin": "relationshipwithnextofkin",
            "contactperson": "contactperson",
            "telnoofcontactperson": "telnoofcontactperson",
            "location": "location",
            "nearestschool": "nearestschool",
            "homechief": "homechief",
            "whereoffensewascommitted": "whereoffensewascommitted",
            "dateofconviction": "dateofconviction",
            "dateofcustody": "dateofcustody",
            "reliefsought": "reliefsought",
            "natureandparticularsofoffense": "natureandparticularsofoffense",
            "chargedalonefortheoffense": "chargedalonefortheoffense",
            "namesofcoaccused": "namesofcoaccused",
            "knowledgeofthevictim": "knowledgeofthevictim",
            "nameofvictim": "nameofvictim",
            "areaofresidence": "areaofresidence",
            "previousconvictions": "previousconvictions",
            "previouspetition": "previouspetition",
            "dateofpreviouspetition": "dateofpreviouspetition",
            "reasonofdenialofpreviouspetition": "reasonofdenialofpreviouspetition",
            "reasonforcurrentpetition": "reasonforcurrentpetition",
            "anydisplinaryactioninprison": "anydisplinaryactioninprison",
            "detailsofdisplinaryactioninprison": "detailsofdisplinaryactioninprison",
            "anyspecialcondition": "anyspecialcondition",
            "detailsofspecialcondition": "detailsofspecialcondition",
            "areyouatrustee": "areyouatrustee",
            "dateofpromotiontotrustee": "dateofpromotiontotrustee",
            "anyspecialattributesorskills": "anyspecialattributesorskills",
            "explanationofspecialattributesorskills": "explanationofspecialattributesorskills",
            "appealedagainsttheconviction": "appealedagainsttheconviction",
            "appealcaseno": "appealcaseno",
            "appealoutcome": "appealoutcome",
            "anypendingcourtmatter": "anypendingcourtmatter",
            "explanationofpendingcourtmatter": "explanationofpendingcourtmatter",
            "court": create_court().pk,
            "prison": create_prison().pk,
            "county": create_county().pk,
            "subcounty": create_subcounty().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_petitionform(self):
        petitionform = create_petitionform()
        url = reverse('petitions_petitionform_detail', args=[petitionform.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_petitionform(self):
        petitionform = create_petitionform()
        data = {
            "name": "name",
            "prisonno": "prisonno",
            "nationality": "nationality",
            "courtcaseno": "courtcaseno",
            "ageatconviction": "ageatconviction",
            "currentage": "currentage",
            "agewhenoffensewascommited": "agewhenoffensewascommited",
            "nextofkin": "nextofkin",
            "relationshipwithnextofkin": "relationshipwithnextofkin",
            "contactperson": "contactperson",
            "telnoofcontactperson": "telnoofcontactperson",
            "location": "location",
            "nearestschool": "nearestschool",
            "homechief": "homechief",
            "whereoffensewascommitted": "whereoffensewascommitted",
            "dateofconviction": "dateofconviction",
            "dateofcustody": "dateofcustody",
            "reliefsought": "reliefsought",
            "natureandparticularsofoffense": "natureandparticularsofoffense",
            "chargedalonefortheoffense": "chargedalonefortheoffense",
            "namesofcoaccused": "namesofcoaccused",
            "knowledgeofthevictim": "knowledgeofthevictim",
            "nameofvictim": "nameofvictim",
            "areaofresidence": "areaofresidence",
            "previousconvictions": "previousconvictions",
            "previouspetition": "previouspetition",
            "dateofpreviouspetition": "dateofpreviouspetition",
            "reasonofdenialofpreviouspetition": "reasonofdenialofpreviouspetition",
            "reasonforcurrentpetition": "reasonforcurrentpetition",
            "anydisplinaryactioninprison": "anydisplinaryactioninprison",
            "detailsofdisplinaryactioninprison": "detailsofdisplinaryactioninprison",
            "anyspecialcondition": "anyspecialcondition",
            "detailsofspecialcondition": "detailsofspecialcondition",
            "areyouatrustee": "areyouatrustee",
            "dateofpromotiontotrustee": "dateofpromotiontotrustee",
            "anyspecialattributesorskills": "anyspecialattributesorskills",
            "explanationofspecialattributesorskills": "explanationofspecialattributesorskills",
            "appealedagainsttheconviction": "appealedagainsttheconviction",
            "appealcaseno": "appealcaseno",
            "appealoutcome": "appealoutcome",
            "anypendingcourtmatter": "anypendingcourtmatter",
            "explanationofpendingcourtmatter": "explanationofpendingcourtmatter",
            "court": create_court().pk,
            "prison": create_prison().pk,
            "county": create_county().pk,
            "subcounty": create_subcounty().pk,
        }
        url = reverse('petitions_petitionform_update', args=[petitionform.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CourtViewTest(unittest.TestCase):
    '''
    Tests for Court
    '''
    def setUp(self):
        self.client = Client()

    def test_list_court(self):
        url = reverse('petitions_court_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_court(self):
        url = reverse('petitions_court_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_court(self):
        court = create_court()
        url = reverse('petitions_court_detail', args=[court.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_court(self):
        court = create_court()
        data = {
            "name": "name",
        }
        url = reverse('petitions_court_update', args=[court.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PrisonViewTest(unittest.TestCase):
    '''
    Tests for Prison
    '''
    def setUp(self):
        self.client = Client()

    def test_list_prison(self):
        url = reverse('petitions_prison_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_prison(self):
        url = reverse('petitions_prison_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_prison(self):
        prison = create_prison()
        url = reverse('petitions_prison_detail', args=[prison.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_prison(self):
        prison = create_prison()
        data = {
            "name": "name",
        }
        url = reverse('petitions_prison_update', args=[prison.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CountyViewTest(unittest.TestCase):
    '''
    Tests for County
    '''
    def setUp(self):
        self.client = Client()

    def test_list_county(self):
        url = reverse('petitions_county_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_county(self):
        url = reverse('petitions_county_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_county(self):
        county = create_county()
        url = reverse('petitions_county_detail', args=[county.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_county(self):
        county = create_county()
        data = {
            "name": "name",
        }
        url = reverse('petitions_county_update', args=[county.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SubCountyViewTest(unittest.TestCase):
    '''
    Tests for SubCounty
    '''
    def setUp(self):
        self.client = Client()

    def test_list_subcounty(self):
        url = reverse('petitions_subcounty_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_subcounty(self):
        url = reverse('petitions_subcounty_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_subcounty(self):
        subcounty = create_subcounty()
        url = reverse('petitions_subcounty_detail', args=[subcounty.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_subcounty(self):
        subcounty = create_subcounty()
        data = {
            "name": "name",
        }
        url = reverse('petitions_subcounty_update', args=[subcounty.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


