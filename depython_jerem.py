# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:58:03 2020

@author: Jérémie Stym-Popper
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import requests

#------------- Analyse des données --------------

chemin_dep = r"C:\Users\Asus\Desktop\Jérémie\Fac_ENSAE\Informatique\Datapython_2AS1\Projet\nosdeputes.fr_deputes_en_mandat_2020-10-26.csv"
url_dep = "https://www.nosdeputes.fr/deputes/enmandat/csv"

df_dep = pd.read_csv(chemin_dep, sep=';')

parite = sns.catplot(x='groupe_sigle', hue="sexe", 
                     kind ='count', palette='ch:.25', data=df_dep)

parite.set(xlabel = 'Groupes parlementaires', ylabel = 'Effectif')

new_labels =['Homme', 'Femme']
for t, l in zip(parite._legend.texts, new_labels): t.set_text(l)


df_dep.groupby("groupe_sigle")['nom'].count().plot(kind="hist")


