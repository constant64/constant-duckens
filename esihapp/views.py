#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from esihapp.models import Cours, Programme, Professeurs, DescriptionCours, Ninstitut, NnonCours, Ngrade, CV, admin
# Create your views here.

def home(request):
    """fonction permettant d'appeler la page d'acceuille"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    return render(request, 'esihapp/index1.html')


def Code_cour(request):
    """fonction permettant de creer un code programme"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Prog_lister = Programme.objects.all() #lister tous les programmes
        program=Programme.objects.get(id=request.POST['program'])  #recupere un programme par son ID
        cours = Cours(program=program,Etablissement=request.POST['Etablissement'],Grade=request.POST['Grade']
            , Semestre=request.POST['Semestre'], NomCours=request.POST['NomCours'])
        cours.save()
        ninstitut_lister = Ninstitut.objects.all()
        nnonCours_lister = NnonCours.objects.all()
        ngrade_lister = Ngrade.objects.all()

        #Grad = ["L1", "L2", "L3", "MI", "M2", "Prop"]
        #Ncour = ["Analyse1", "SSI", "SIG", "Python", "Linux"]    A enlever..............................................
        Sem = {'SI': 'Semestre 1', 'SII': 'Semestre 2', 'Y': 'Deux Semestres'}
        #peut etre enleve pr ajouter autre chose
        return redirect("/../codage/")

    except KeyError:
        ninstitut_lister = Ninstitut.objects.all()
        nnonCours_lister = NnonCours.objects.all()
        ngrade_lister = Ngrade.objects.all()
        #Etab = ["Esih", "FDSE"]  A enlever.............................................................
        #Grad = ["L1", "L2", "L3", "MI", "M2", "Prop"]
        #Ncour = ["Analyse1", "SSI", "SIG", "Python", "Linux"]
        Sem = {'SI': 'Semestre 1', 'SII': 'Semestre 2', 'Y': 'Deux Semestres'}
        return render(request, 'esihapp/enregistrement.html', locals())



def Prog(request):
    """fonction permettant de creer un code programme"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        program = Programme(Domaine=request.POST['Domaine'], Mention=request.POST['Mention'],
                            Specialite=request.POST['Specialite'], TypeCours=request.POST['Typecours'],
                            Langue=request.POST['Langue'])
        program.save()
        Dom = {'ST': 'Sciences et technologies', 'E&G': 'Economie ET Gestion'}
        Ment = {'SI': 'Sciences informatiques', 'E&G': 'Economie ET Gestion'}
        Spec = {'Tel': 'Telecommunication', 'Bdd': 'Bases de donnees', 'ONe': 'Mone',
                'Sde': "Sciences de l'entreprise", 'SC': 'Sciences Comptables', 'NOSP': 'Aucune'}
        Tcour = {'O': 'Optionnel', 'OB': 'Obligatoire'}
        Lang = {'A': 'Anglais', 'F': 'Francais'}
        return redirect("/../Programme/")
    except KeyError:
        Dom = {'ST': 'Sciences et technologies', 'E&G': 'Economie ET Gestion'}
        Ment = {'SI': 'Sciences informatiques', 'E&G': 'Economie ET Gestion'}
        Spec = {'Tel': 'Telecommunication', 'Bdd': 'Bases de donnees', 'ONe': 'Mone',
                'Sde': "Sciences de l'entreprise", 'SC': 'Sciences Comptables', 'NOSP': 'Aucune'}
        Tcour = {'O': 'Optionnel', 'OB': 'Obligatoire'}
        Lang = {'A': 'Anglais', 'F': 'Francais'}
        return render(request, 'esihapp/Programme.html', locals())


def prof(request):
    """fonction permettant d'inscrire un prof"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        professeur = Professeurs(NomProfesseur=request.POST['NomProfesseur'],
                                 PrenomProfesseur=request.POST['PrenomProfesseur'],
                                 Tel=request.POST['Tel'],Email=request.POST['Email'],
                                 Adresse=request.POST['Adresse'],CINP=request.POST['CINP'])
        professeur.save()
        return redirect("/../prof/")
    except KeyError:
        return render(request, 'esihapp/prof.html', locals())


def listerc(request):
    """fonction permettant de lister un cours"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Code_cour_lister = Cours.objects.all()
        return render(request, 'esihapp/list.html', locals())

    except KeyError:
        return render(request, 'esihapp/list.html', locals())


def listerp(request):
    """fonction permettant de lister un programme"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Programme.objects.order_by("id")
        Prog_lister = Programme.objects.all()
        return render(request, 'esihapp/listp.html', locals())
    except KeyError:
        return render(request, 'esihapp/listp.html', locals())


def ProgM(request, id):
    """fonction permettant de modifier le programme"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Dom = {'ST': 'Sciences et technologies', 'E&G': 'Economie ET Gestion'}
        Ment = {'SI': 'Sciences informatiques', 'E&G': 'Economie ET Gestion'}
        Spec = {'Tel': 'Telecommunication', 'Bdd': 'Bases de donnees', 'ONe': 'Mone',
                'Sde': "Sciences de l'entreprise", 'SC': 'Sciences Comptables', 'NOSP': 'Aucune'}
        Tcour = {'O': 'Optionnel', 'OB': 'Obligatoire'}
        Lang = {'A': 'Anglais', 'F': 'Francais'}
        Prog_listerM = Programme.objects.get(id=id)#modifiacation du programme
        program = Prog_listerM
        program.Domaine = request.POST['Domaine']
        program.Mention = request.POST['Mention']
        program.Specialite = request.POST['Specialite']
        program.TypeCours = request.POST['TypeCours']
        program.Langue = request.POST['Langue']
        program.save()
        return redirect("/../listp/")
    except KeyError:
        return render(request, 'esihapp/modp.html', locals())


def CourM(request, id):
    """fonction permettant de modifier le programme"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Prog_lister = Programme.objects.all()#Pour modifier un cours on peut aussi vouloir modifier le programme auquel il est releie
        ninstitut_lister = Ninstitut.objects.all()

        #Etab = ["Esih", "FDSE"]   A enlever.............................................................
        #Grad = ["L1", "L2", "L3", "MI", "M2", "Prop"]
        ngrade_lister = Ngrade.objects.all()
        nnonCours_lister = NnonCours.objects.all()
        #Ncour = ["Analyse1", "SSI", "SIG", "Python", "Linux"]    A enlever.............................................................
        Sem = {'SI': 'Semestre 1', 'SII': 'Semestre 2', 'Y': 'Deux Semestres'}
        Code_cour_listerM = Cours.objects.get(id=id)#modifiacation du programme
        cours = Cours.objects.get(id=id)
        cours.Etablissement = request.POST['Etablissement']
        cours.Grade = request.POST['Grade']
        cours.Semestre = request.POST['Semestre']
        cours.NomCours = request.POST['NomCours']
        cours.program = Programme.objects.get(id=request.POST['program'])
        cours.save()
        return redirect("/../list/")
    except KeyError:
        return render(request, 'esihapp/modc.html', locals())


def CoursS(request, id):
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Cours.objects.filter(id=id).delete()
        return redirect("/../list/")
    except KeyError:
        return render(request, 'esihapp/list.html', locals())


def ProgS(request, id):
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Programme.objects.filter(id=id).delete()
        return redirect("/../listp/")
    except KeyError:
        return render(request, 'esihapp/listp.html', locals())

def Desc(request):
    if 'member_id' not in request.session:
        return redirect("/login/")

    try:
        Code_cour_lister = Cours.objects.all()
        Cred = ["0", "1", "2", "3", "4", "5"]
        Pub = ["Etudiant", "Professionnel", "Autres"]
        cours=Cours.objects.get(id=request.POST['CodeCours'])
        professeur = Professeurs.objects.get(id=request.POST['NomProfesseur'])
        d=DescriptionCours(CodeCours=request.POST['CodeCours'],NomCours=request.POST['NomCours'],CrediEcts=request.POST['CrediEcts'],
                           Etablissement=request.POST['Etablissement'], PublicCible=request.POST['PublicCible'],PreRequis=request.POST['PreRequis'],
                           Objectif=request.POST['Objectif'],Description =request.POST['Description'],PlanCours=request.POST['PlanCours'],
                           Format=request.POST['Format'],Ressource=request.POST['Ressource'],Evalution=request.POST['Evalution'],
                           cours=cours)
        #return HttpResponse(professeur)
        d.save()
        d.professeurs.add(professeur)

        return render(request, 'esihapp/desc.html', locals())
    except KeyError:
        Code_cour_lister = Cours.objects.all()
        Cred = ["0", "1", "2", "3", "4", "5"]
        Pub = ["Etudiant", "Professionnel", "Autres"]
        allprofesseurs = Professeurs.objects.all()
        return render(request, 'esihapp/desc.html', locals())


def nouvi(request):
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        ninstitut = Ninstitut(Ninstitut=request.POST['NEtablissement'])
        ninstitut.save()
        return redirect("/../codage/")
    except KeyError:
        return render(request,'esihapp/nouvi.html',locals())

def nouvc(request):
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        nnonCours =  NnonCours( NnonCours=request.POST['NNomCours'])
        nnonCours.save()

        return redirect("/../codage/")
    except KeyError:
        return render(request,'esihapp/nouvc.html',locals())

def nouvg(request):
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        ngrade =  Ngrade( Ngrade=request.POST['Ngrade'])
        ngrade.save()

        return redirect("/../codage/")
    except KeyError:
        return render(request,'esihapp/nouvg.html',locals())


def CVP (request, id):
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        professeurs = Professeurs.objects.get(id=id)
        cvp = CV ( DateN=request.POST['DateN'],professeurs=professeurs,
                   LieuN=request.POST['LieuN'],Tel2=request.POST['Tel2'],
                    EtatC=request.POST['EtatC'],ExpP=request.POST['ExpP'],
                    DateE=request.POST['DateE'],FormationA=request.POST['FormationA'],DateF=request.POST['DateF'],
                   Specialite=request.POST['Specialite'],Reference=request.POST['Reference'],Langue=request.POST['Langue'])
        cvp.save()
        etat=["Marie","Celibataire","Fiance","Divorce","veuf"]
        return redirect("/../listprof/")

    except KeyError:
        etat=["Marie","Celibataire","Fiance","Divorce","veuf"]
        return render(request,'esihapp/cv.html',locals())

# def CVP (request, id):
#     if 'member_id' not in request.session:
#         return redirect("/login/")
#     try:
#         professeurs = Professeurs.objects.get(id=id)
#         cvp = CV ( DateN=request.POST['DateN'],professeurs=professeurs,
#                    LieuN=request.POST['LieuN'],Tel2=request.POST['Tel2'],
#                     EtatC=request.POST['EtatC'],ExpP=request.POST['ExpP'],
#                     DateE=request.POST['DateE'],FormationA=request.POST['FormationA'],DateF=request.POST['DateF'],
#                    Specialite=request.POST['Specialite'],Reference=request.POST['Reference'],Langue=request.POST['Langue'])
#         cvp.save()
#         etat=["Marie","Celibataire","Fiance","Divorce","veuf"]
#         return redirect("/../listprof/")
#
#     except KeyError:
#         etat=["Marie","Celibataire","Fiance","Divorce","veuf"]
#         return render(request,'esihapp/cv.html',locals())

def listerprof(request):
    """fonction permettant de lister un cours"""
    if 'member_id' not in request.session:
        return redirect("/login/")

    try:
        allprofesseurs = Professeurs.objects.all()
        return render(request, 'esihapp/listprof.html', locals())

    except KeyError:
        return render(request, 'esihapp/listprof.html', locals())

def ProfM(request, id):
    """fonction permettant de modifier le programme"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:

        allprofesseursM = Professeurs.objects.get(id=id)#modifiacation du prof
        professeurs= allprofesseursM
        professeurs.NomProfesseur = request.POST['NomProfesseur']
        professeurs.PrenomProfesseur = request.POST['PrenomProfesseur']
        professeurs.Tel = request.POST['Tel']
        professeurs.Email = request.POST['Email']
        professeurs.Adresse = request.POST['Adresse']
        professeurs.CINP = request.POST['CINP']
        professeurs.save()
        return redirect("/../listprof/")
    except KeyError:
        return render(request, 'esihapp/modprof.html', locals())

def create(request):
    if 'member_id' not in request.session:
        return redirect("/login/")
    user=admin(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
    user.save()

def login(request):
    try:
        try:
            log_in = admin.objects.get(username=request.POST['username'])
            if log_in.password == request.POST['password']:
                request.session['member_id'] = log_in.id
                return redirect('/../')
            else:
                return render(request,'esihapp/formerno.html',locals())
        except:
             return render(request,'esihapp/form.html',locals())

    except KeyError:
        return render(request,'esihapp/form.html',locals())

def logout(request):
    try:
        del request.session['member_id']
        return render(request,"esihapp/form2.html",locals())
    except KeyError:
        return render(request,"esihapp/form2.html",locals())


def listerdesc(request):
    """fonction permettant de lister un programme"""
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:

        desc_lister =DescriptionCours.objects.all()
        return render(request, 'esihapp/listerdesc.html', locals())
    except KeyError:
        return render(request, 'esihapp/listd.html', locals())



def ProfS(request, id):
    if 'member_id' not in request.session:
        return redirect("/login/")
    try:
        Professeurs.objects.filter(id=id).delete()
        return redirect("/../listprof/")
    except KeyError:
        return render(request, 'esihapp/listprof.html', locals())







    
