# Generated by Django 2.0.1 on 2018-01-28 19:30

from django.db import migrations


def add_initial_data(apps, schema_editor):
    County = apps.get_model('petitions', 'County')
    SubCounty = apps.get_model('petitions', 'SubCounty')

    baringo = County.objects.create(name='BARINGO')
    SubCounty.objects.create(name='BARINGO EAST', county=baringo)
    SubCounty.objects.create(name='BARINGO WEST', county=baringo)
    SubCounty.objects.create(name='BARINGO CENTRAL', county=baringo)
    SubCounty.objects.create(name='MOCHONGOI', county=baringo)
    SubCounty.objects.create(name='MOGOTIO', county=baringo)
    SubCounty.objects.create(name='ELDAMA RAVINE', county=baringo)

    bomet = County.objects.create(name='BOMET')
    SubCounty.objects.create(name='SOTIK', county=bomet)
    SubCounty.objects.create(name='CHEPALUNGU', county=bomet)
    SubCounty.objects.create(name='BOMET EAST', county=bomet)
    SubCounty.objects.create(name='BOMET CENTRAL', county=bomet)
    SubCounty.objects.create(name='KONOIN', county=bomet)

    bungoma = County.objects.create(name='BUNGOMA')
    SubCounty.objects.create(name='MT ELGON', county=bungoma)
    SubCounty.objects.create(name='SIRISIA', county=bungoma)
    SubCounty.objects.create(name='KABUCHIA', county=bungoma)
    SubCounty.objects.create(name='BUMULA', county=bungoma)
    SubCounty.objects.create(name='KANDUNYI', county=bungoma)
    SubCounty.objects.create(name='WEBUYE', county=bungoma)
    SubCounty.objects.create(name='BOKOLI', county=bungoma)
    SubCounty.objects.create(name='KIMILILI', county=bungoma)
    SubCounty.objects.create(name='TONGAREN', county=bungoma)

    busia = County.objects.create(name='BUSIA')
    SubCounty.objects.create(name='TESO NORTH', county=busia)
    SubCounty.objects.create(name='TESO SOUTH', county=busia)
    SubCounty.objects.create(name='NAMBALE', county=busia)
    SubCounty.objects.create(name='MATAYOS', county=busia)
    SubCounty.objects.create(name='BUTULA', county=busia)
    SubCounty.objects.create(name='FUNYULA', county=busia)
    SubCounty.objects.create(name='BUDALANGI', county=busia)

    elgeiyomarakwet = County.objects.create(name='ELGEYO MARAKWET')
    SubCounty.objects.create(name='MARAKWET EAST', county=elgeiyomarakwet)
    SubCounty.objects.create(name='MARAKWET WEST', county=elgeiyomarakwet)
    SubCounty.objects.create(name='KEIYO EAST', county=elgeiyomarakwet)
    SubCounty.objects.create(name='KEIYO SOUTH', county=elgeiyomarakwet)

    embu = County.objects.create(name='EMBU')
    SubCounty.objects.create(name='MANYATTA', county=embu)
    SubCounty.objects.create(name='RUNYENJES', county=embu)
    SubCounty.objects.create(name='GACHOKA', county=embu)
    SubCounty.objects.create(name='SIAKAGO', county=embu)

    garissa = County.objects.create(name='GARISSA')
    SubCounty.objects.create(name='TAVEDUJIS', county=garissa)
    SubCounty.objects.create(name='BALAMBALA', county=garissa)
    SubCounty.objects.create(name='LAGDERA', county=garissa)
    SubCounty.objects.create(name='DADAAB', county=garissa)
    SubCounty.objects.create(name='FAFI', county=garissa)
    SubCounty.objects.create(name='IJARA', county=garissa)

    homabay = County.objects.create(name='HOMA BAY')
    SubCounty.objects.create(name='KASIPUL', county=homabay)
    SubCounty.objects.create(name='KABONDO', county=homabay)
    SubCounty.objects.create(name='KARACHUONYO', county=homabay)
    SubCounty.objects.create(name='RANGWE', county=homabay)
    SubCounty.objects.create(name='HOMABAY TOWN', county=homabay)
    SubCounty.objects.create(name='NDHIWA', county=homabay)
    SubCounty.objects.create(name='MBITA', county=homabay)
    SubCounty.objects.create(name='GWASSI', county=homabay)

    isiolo = County.objects.create(name='ISIOLO')
    SubCounty.objects.create(name='ISIOLO NORTH', county=isiolo)
    SubCounty.objects.create(name='ISIOLO SOUTH', county=isiolo)

    kajiado = County.objects.create(name='KAJIADO')
    SubCounty.objects.create(name='KAJIADO CENTRAL', county=kajiado)
    SubCounty.objects.create(name='KAJIADO NORTH', county=kajiado)
    SubCounty.objects.create(name='KAJIADO SOUTH', county=kajiado)

    kakamega = County.objects.create(name='KAKAMEGA')
    SubCounty.objects.create(name='LUGARI', county=kakamega)
    SubCounty.objects.create(name='LIKUYANI', county=kakamega)
    SubCounty.objects.create(name='MALAVA', county=kakamega)
    SubCounty.objects.create(name='LURAMBI', county=kakamega)
    SubCounty.objects.create(name='MAKHOLO', county=kakamega)
    SubCounty.objects.create(name='MUMIAS', county=kakamega)
    SubCounty.objects.create(name='MUMIAS EAST', county=kakamega)
    SubCounty.objects.create(name='MATUNGU', county=kakamega)
    SubCounty.objects.create(name='BUTERE', county=kakamega)
    SubCounty.objects.create(name='KHWISERO', county=kakamega)
    SubCounty.objects.create(name='SHINYALU', county=kakamega)
    SubCounty.objects.create(name='IKOLOMANI', county=kakamega)

    kericho = County.objects.create(name='KERICHO')
    SubCounty.objects.create(name='AINAMOI', county=kericho)
    SubCounty.objects.create(name='BELGUT', county=kericho)
    SubCounty.objects.create(name='KIPKELION', county=kericho)

    kiambu = County.objects.create(name='KIAMBU')
    SubCounty.objects.create(name='GATUNDU SOUTH', county=kiambu)
    SubCounty.objects.create(name='GATUNDU NORTH', county=kiambu)
    SubCounty.objects.create(name='JUJA', county=kiambu)
    SubCounty.objects.create(name='THIKA TOWN', county=kiambu)
    SubCounty.objects.create(name='RUIRU GITHUNGURI', county=kiambu)
    SubCounty.objects.create(name='KIAMBU', county=kiambu)
    SubCounty.objects.create(name='KIAMBAA', county=kiambu)
    SubCounty.objects.create(name='KABETE', county=kiambu)
    SubCounty.objects.create(name='KIKUYU', county=kiambu)
    SubCounty.objects.create(name='LIMURU', county=kiambu)
    SubCounty.objects.create(name='LARI', county=kiambu)

    kilifi = County.objects.create(name='KILIFI')
    SubCounty.objects.create(name='KILIFI NORTH', county=kilifi)
    SubCounty.objects.create(name='KILIFI SOUTH', county=kilifi)
    SubCounty.objects.create(name='KALOLENI', county=kilifi)
    SubCounty.objects.create(name='RABAI', county=kilifi)
    SubCounty.objects.create(name='GANZE', county=kilifi)
    SubCounty.objects.create(name='MALINDI', county=kilifi)
    SubCounty.objects.create(name='MAGARINI', county=kilifi)

    kirinyaga = County.objects.create(name='KIRINYAGA')
    SubCounty.objects.create(name='MWEA', county=kirinyaga)
    SubCounty.objects.create(name='GICHUGU', county=kirinyaga)
    SubCounty.objects.create(name='NDIA', county=kirinyaga)
    SubCounty.objects.create(name='KIRINYAGA CENTRAL', county=kirinyaga)

    kisii = County.objects.create(name='KISII')
    SubCounty.objects.create(name='BONCHARI', county=kisii)
    SubCounty.objects.create(name='SOUTH MUGIRANGO', county=kisii)
    SubCounty.objects.create(name='BOMACHOGE', county=kisii)
    SubCounty.objects.create(name='BOBASI', county=kisii)
    SubCounty.objects.create(name='GUCHA', county=kisii)
    SubCounty.objects.create(name='NYARIBARI MASABA', county=kisii)
    SubCounty.objects.create(name='NYARIBARI CHACHE', county=kisii)
    SubCounty.objects.create(name='MATRANI', county=kisii)
    SubCounty.objects.create(name='MOSOCHO', county=kisii)

    kisumu = County.objects.create(name='KISUMU')
    SubCounty.objects.create(name='KISUMU EAST', county=kisumu)
    SubCounty.objects.create(name='KISUMU WEST', county=kisumu)
    SubCounty.objects.create(name='KISUMU CENTRAL', county=kisumu)
    SubCounty.objects.create(name='SEME', county=kisumu)
    SubCounty.objects.create(name='NYANDO', county=kisumu)
    SubCounty.objects.create(name='MUHORONI', county=kisumu)
    SubCounty.objects.create(name='NYAKACH', county=kisumu)

    kitui = County.objects.create(name='KITUI')
    SubCounty.objects.create(name='MWINGI NORTH', county=kitui)
    SubCounty.objects.create(name='MWINGI CENTRAL', county=kitui)
    SubCounty.objects.create(name='MWINGI SOUTH', county=kitui)
    SubCounty.objects.create(name='KITUI WEST', county=kitui)
    SubCounty.objects.create(name='KITUI RURAL', county=kitui)
    SubCounty.objects.create(name='KITUI TOWN', county=kitui)
    SubCounty.objects.create(name='MUTITU', county=kitui)
    SubCounty.objects.create(name='KITUI SOUTH', county=kitui)

    kwale = County.objects.create(name='KWALE')
    SubCounty.objects.create(name='MSAMBWENI', county=kwale)
    SubCounty.objects.create(name='LUNGA LUNGA', county=kwale)
    SubCounty.objects.create(name='MATUGA', county=kwale)
    SubCounty.objects.create(name='KINANGO', county=kwale)

    laikipia = County.objects.create(name='LAIKIPIA')
    SubCounty.objects.create(name='LAIKIPIA WEST', county=laikipia)
    SubCounty.objects.create(name='LAIKIPIA EAST', county=laikipia)
    SubCounty.objects.create(name='LAIKIPIA NORTH', county=laikipia)

    lamu = County.objects.create(name='LAMU')
    SubCounty.objects.create(name='LAMU EAST', county=lamu)
    SubCounty.objects.create(name='LAMU WEST', county=lamu)

    machakos = County.objects.create(name='MACHAKOS')
    SubCounty.objects.create(name='MASINGA', county=machakos)
    SubCounty.objects.create(name='YATTA', county=machakos)
    SubCounty.objects.create(name='KANGUNDO', county=machakos)
    SubCounty.objects.create(name='MATUNGULU', county=machakos)
    SubCounty.objects.create(name='KATHIANI', county=machakos)
    SubCounty.objects.create(name='MAVOKO', county=machakos)
    SubCounty.objects.create(name='MACHAKOS TOWN', county=machakos)
    SubCounty.objects.create(name='MWALA', county=machakos)

    makueni = County.objects.create(name='MAKUENI')
    SubCounty.objects.create(name='MBOONI', county=makueni)
    SubCounty.objects.create(name='KILOME', county=makueni)
    SubCounty.objects.create(name='KAITI', county=makueni)
    SubCounty.objects.create(name='MAKUENI', county=makueni)
    SubCounty.objects.create(name='KIBWEZI WEST', county=makueni)
    SubCounty.objects.create(name='KIBWEZI EAST', county=makueni)

    mandera = County.objects.create(name='MANDERA')
    SubCounty.objects.create(name='MANDERA WEST', county=mandera)
    SubCounty.objects.create(name='BANISA', county=mandera)
    SubCounty.objects.create(name='MANDERA NORTH', county=mandera)
    SubCounty.objects.create(name='MANDERA EAST', county=mandera)
    SubCounty.objects.create(name='LAFEY', county=mandera)

    marsabit = County.objects.create(name='MARSABIT')
    SubCounty.objects.create(name='MOYALE', county=marsabit)
    SubCounty.objects.create(name='NORTH HORR', county=marsabit)
    SubCounty.objects.create(name='SAKU', county=marsabit)
    SubCounty.objects.create(name='LAISAMIS', county=marsabit)

    meru = County.objects.create(name='MERU')
    SubCounty.objects.create(name='IGEMBE SOUTH', county=meru)
    SubCounty.objects.create(name='IGEMBE CENTRAL', county=meru)
    SubCounty.objects.create(name='IGEMBE NORTH', county=meru)
    SubCounty.objects.create(name='TIGANIA WEST', county=meru)
    SubCounty.objects.create(name='TIGANIA EAST', county=meru)
    SubCounty.objects.create(name='NORTH IMENTI', county=meru)
    SubCounty.objects.create(name='BUURI', county=meru)
    SubCounty.objects.create(name='CENTRAL IMENTI', county=meru)
    SubCounty.objects.create(name='SOUTH IMENTI', county=meru)


    migori = County.objects.create(name='MIGORI')
    SubCounty.objects.create(name='RONGO', county=migori)
    SubCounty.objects.create(name='AWENDO', county=migori)
    SubCounty.objects.create(name='MIGORI EAST', county=migori)
    SubCounty.objects.create(name='MIGORI WEST', county=migori)
    SubCounty.objects.create(name='URIRI', county=migori)
    SubCounty.objects.create(name='NYATIKE', county=migori)
    SubCounty.objects.create(name='KURIA EAST', county=migori)
    SubCounty.objects.create(name='KURIA WEST', county=migori)

    mombasa = County.objects.create(name='MOMBASA')
    SubCounty.objects.create(name='CHANGAMWE', county=mombasa)
    SubCounty.objects.create(name='JOMVU', county=mombasa)
    SubCounty.objects.create(name='KISAUNI', county=mombasa)
    SubCounty.objects.create(name='NYALI', county=mombasa)
    SubCounty.objects.create(name='LIKONI', county=mombasa)
    SubCounty.objects.create(name='MVITA', county=mombasa)

    muranga = County.objects.create(name='MURANGA')
    SubCounty.objects.create(name='KANGEMA', county=muranga)
    SubCounty.objects.create(name='MATHIOYA', county=muranga)
    SubCounty.objects.create(name='KIHARU', county=muranga)
    SubCounty.objects.create(name='KIGUMO', county=muranga)
    SubCounty.objects.create(name='MARAGWA', county=muranga)
    SubCounty.objects.create(name='KANDARA', county=muranga)
    SubCounty.objects.create(name='GATANGA', county=muranga)

    nairobi = County.objects.create(name='NAIROBI')
    SubCounty.objects.create(name='WESTLANDS', county=nairobi)
    SubCounty.objects.create(name='PARKLANDS', county=nairobi)
    SubCounty.objects.create(name='DAGORETTI', county=nairobi)
    SubCounty.objects.create(name='KAREN / LANGATA', county=nairobi)
    SubCounty.objects.create(name='KIBIRA', county=nairobi)
    SubCounty.objects.create(name='ROYSAMBU', county=nairobi)
    SubCounty.objects.create(name='KASARANI', county=nairobi)
    SubCounty.objects.create(name='RUARAKA', county=nairobi)
    SubCounty.objects.create(name='KARIOBANGI', county=nairobi)
    SubCounty.objects.create(name='KAYOLE', county=nairobi)
    SubCounty.objects.create(name='EMBAKASI', county=nairobi)
    SubCounty.objects.create(name='MIHANG’O', county=nairobi)
    SubCounty.objects.create(name='NAIROBI WEST', county=nairobi)
    SubCounty.objects.create(name='MAKADARA', county=nairobi)
    SubCounty.objects.create(name='KAMUKUNJI', county=nairobi)
    SubCounty.objects.create(name='STAREHE', county=nairobi)
    SubCounty.objects.create(name='MATHARE', county=nairobi)

    nakuru = County.objects.create(name='NAKURU')
    SubCounty.objects.create(name='MOLO', county=nakuru)
    SubCounty.objects.create(name='NJORO', county=nakuru)
    SubCounty.objects.create(name='NAIVASHA', county=nakuru)
    SubCounty.objects.create(name='GILGIL', county=nakuru)
    SubCounty.objects.create(name='KURESOI SOUTH', county=nakuru)
    SubCounty.objects.create(name='KURESOI NORTH', county=nakuru)
    SubCounty.objects.create(name='SUBUKIA', county=nakuru)
    SubCounty.objects.create(name='RONGAI', county=nakuru)
    SubCounty.objects.create(name='BAHATI', county=nakuru)
    SubCounty.objects.create(name='NAKURU TOWN WEST', county=nakuru)
    SubCounty.objects.create(name='NAKURU TOWN EAST', county=nakuru)

    nandi = County.objects.create(name='NANDI')
    SubCounty.objects.create(name='TINDERET', county=nandi)
    SubCounty.objects.create(name='ALDAI', county=nandi)
    SubCounty.objects.create(name='NANDI HILLS', county=nandi)
    SubCounty.objects.create(name='EMGWEN NORTH', county=nandi)
    SubCounty.objects.create(name='EMGWEN SOUTH', county=nandi)
    SubCounty.objects.create(name='MOSOP', county=nandi)

    narok = County.objects.create(name='NAROK')
    SubCounty.objects.create(name='KILGORIS', county=narok)
    SubCounty.objects.create(name='EMURUA DIKIRR', county=narok)
    SubCounty.objects.create(name='NAROK NORTH', county=narok)
    SubCounty.objects.create(name='KAJIADO EAST', county=narok)
    SubCounty.objects.create(name='KAJIADO WEST', county=narok)

    nyamira = County.objects.create(name='NYAMIRA')
    SubCounty.objects.create(name='KITUTU MASABA', county=nyamira)
    SubCounty.objects.create(name='NORTH MUGIRANGO', county=nyamira)
    SubCounty.objects.create(name='WEST MUGIRANGO', county=nyamira)

    nyandarua = County.objects.create(name='NYANDARUA')
    SubCounty.objects.create(name='KINANGOP', county=nyandarua)
    SubCounty.objects.create(name='KIPIPIRI', county=nyandarua)
    SubCounty.objects.create(name='OL-KALOU', county=nyandarua)
    SubCounty.objects.create(name='OL-JOROK', county=nyandarua)
    SubCounty.objects.create(name='NDARAGWA', county=nyandarua)

    nyeri = County.objects.create(name='NYERI')
    SubCounty.objects.create(name='TETU', county=nyeri)
    SubCounty.objects.create(name='KIENI', county=nyeri)
    SubCounty.objects.create(name='MATHIRA', county=nyeri)
    SubCounty.objects.create(name='OTHAYA', county=nyeri)
    SubCounty.objects.create(name='MUKUWE-INI', county=nyeri)
    SubCounty.objects.create(name='NYERI TOWN', county=nyeri)

    samburu = County.objects.create(name='SAMBURU')
    SubCounty.objects.create(name='SAMBURU WEST', county=samburu)
    SubCounty.objects.create(name='SAMBURU NORTH', county=samburu)
    SubCounty.objects.create(name='SAMBURU EAST', county=samburu)

    siaya = County.objects.create(name='SIAYA')
    SubCounty.objects.create(name='UGENYA', county=siaya)
    SubCounty.objects.create(name='UGUNJA', county=siaya)
    SubCounty.objects.create(name='ALEGO USONGA', county=siaya)
    SubCounty.objects.create(name='GEM', county=siaya)
    SubCounty.objects.create(name='BONDO', county=siaya)
    SubCounty.objects.create(name='RARIEDA', county=siaya)

    taitataveta = County.objects.create(name='TAITA TAVETA')
    SubCounty.objects.create(name='TAVETA', county=taitataveta)
    SubCounty.objects.create(name='WUNDANYI', county=taitataveta)
    SubCounty.objects.create(name='MWATATE', county=taitataveta)
    SubCounty.objects.create(name='VOI', county=taitataveta)

    tanariver = County.objects.create(name='TANA RIVER')
    SubCounty.objects.create(name='GARSEN', county=tanariver)
    SubCounty.objects.create(name='GALOLE', county=tanariver)
    SubCounty.objects.create(name='BURA', county=tanariver)

    tharakanithi = County.objects.create(name='THARAKA NITHI')
    SubCounty.objects.create(name='NITHI', county=tharakanithi)
    SubCounty.objects.create(name='MAARA', county=tharakanithi)
    SubCounty.objects.create(name='THARAKA', county=tharakanithi)

    transnzoia = County.objects.create(name='TRANS NZOIA')
    SubCounty.objects.create(name='KWANZA', county=transnzoia)
    SubCounty.objects.create(name='ENDEBESS', county=transnzoia)
    SubCounty.objects.create(name='SABOTI', county=transnzoia)
    SubCounty.objects.create(name='KIMININI', county=transnzoia)
    SubCounty.objects.create(name='CHERENGANYI', county=transnzoia)

    turkana = County.objects.create(name='TURKANA')
    SubCounty.objects.create(name='TURKANA NORTH', county=turkana)
    SubCounty.objects.create(name='TURKANA WEST', county=turkana)
    SubCounty.objects.create(name='TURKANA CENTRAL', county=turkana)
    SubCounty.objects.create(name='LOIMA', county=turkana)
    SubCounty.objects.create(name='TURKANA SOUTH', county=turkana)
    SubCounty.objects.create(name='TURKANA EAST', county=turkana)

    uasingishu = County.objects.create(name='UASIN GISHU')
    SubCounty.objects.create(name='ELDORET EAST', county=uasingishu)
    SubCounty.objects.create(name='ELDORET NORT', county=uasingishu)
    SubCounty.objects.create(name='ELDORET SOUTH', county=uasingishu)

    vihiga = County.objects.create(name='VIHIGA')
    SubCounty.objects.create(name='VIHIGA', county=vihiga)
    SubCounty.objects.create(name='SABATIA', county=vihiga)
    SubCounty.objects.create(name='HAMISI', county=vihiga)
    SubCounty.objects.create(name='EMUHAYA', county=vihiga)
    SubCounty.objects.create(name='LUANDA', county=vihiga)


    wajir = County.objects.create(name='WAJIR')
    SubCounty.objects.create(name='WAJIR NORTH', county=wajir)
    SubCounty.objects.create(name='WAJIR EAST', county=wajir)
    SubCounty.objects.create(name='TARBAJ', county=wajir)
    SubCounty.objects.create(name='WAJIR WEST', county=wajir)
    SubCounty.objects.create(name='ELDAS', county=wajir)
    SubCounty.objects.create(name='WAJIR SOUTH', county=wajir)

    westpokot = County.objects.create(name='WEST POKOT')
    SubCounty.objects.create(name='KAPENGURIA ', county=westpokot)
    SubCounty.objects.create(name='SIGOR ', county=westpokot)
    SubCounty.objects.create(name='KACHELIBA', county=westpokot)
    SubCounty.objects.create(name='POKOT SOUTH ', county=westpokot)












class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
