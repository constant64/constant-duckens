#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Programme (models.Model):
    Domaine = models.CharField(max_length=5)
    Mention =models.CharField(max_length=5)
    Specialite = models.CharField(max_length=10)
    TypeCours = models.CharField(max_length=5)
    Langue = models.CharField(max_length=5)


class Cours (models.Model):
    program = models.ForeignKey('Programme')
    Etablissement = models.CharField(max_length=50)
    Grade = models.CharField(max_length=5)
    Semestre = models.CharField(max_length=5)
    NomCours = models.CharField(max_length=50)



class Professeurs (models.Model):
    NomProfesseur = models.CharField(max_length=20)
    PrenomProfesseur = models.CharField(max_length=20)
    Tel = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    Adresse = models.CharField(max_length=50)
    CINP = models.CharField(max_length=25)
    def __unicode__(self):
        return u'%s %s' % (self.NomProfesseur,self.PrenomProfesseur)

class DescriptionCours (models.Model):
     cours = models.ForeignKey('Cours')
     professeurs = models.ManyToManyField('Professeurs')
     CodeCours = models.CharField(max_length=50)
     NomCours = models.CharField(max_length=50)
     CrediEcts = models.IntegerField(max_length=10)
     Etablissement = models.CharField(max_length=20)
     PublicCible = models.CharField(max_length=20)
     PreRequis = models.CharField(max_length=100)
     Objectif = models.CharField(max_length=100)
     Description = models.CharField(max_length=50)
     PlanCours = models.CharField(max_length=200)
     Format = models.CharField(max_length=50)
     Ressource = models.CharField(max_length=50)
     Evalution = models.CharField(max_length=50)
     def __unicode__(self):
        return u'%s' % (self.cours)


class Ninstitut (models.Model):
    Ninstitut = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.Ninstitut)


class NnonCours(models.Model):
    NnonCours =  models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' % (self.NnonCours)

class  Ngrade(models.Model):
    Ngrade = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s' % (self.Ngrade)


class CV(models.Model):
    professeurs = models.ForeignKey('Professeurs')
    DateN = models.DateField()
    LieuN = models.CharField (max_length=100)
    Tel2 = models.CharField(max_length=15)
    EtatC = models.CharField(max_length=20)
    ExpP = models.CharField(max_length=400)
    DateE = models.DateField()
    FormationA = models.CharField(max_length=400)
    DateF = models.DateField()
    Specialite = models.CharField(max_length=500)
    Reference = models.CharField(max_length=400)
    Langue = models.CharField(max_length=20)

class admin (models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    

    def __unicode__(self):
        return u'%s %s' % (self.username,self.firstname)







