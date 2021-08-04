#REPONCES

#-------Declaration: 
s = int(input("Nombres des stagiares :"))
NomStagaires = []
Notes = []
Modules = ["JAVA","PYTHON","LARAVEL","VUEJS"]

#-------Affichage et remplisage des noms des stagiaires:

for NomStagiaire in range(s):
    NomStagaires.append(input("Nom de Stagiaire "  + str(NomStagiaire+1) + ": "))

#-------Affichage et remplisage des notes des stagiaires + vérification quand la note < 10 il sort à l'autre stgiaire:

for i in range(s):
    NotesStagiaires = []
    print(" ---> Les notes de Stagaire "+str(i+1)+" : ")

    for j in range(len(Modules)):
        NotesStagiaires.append(float(input("Note de module  " +Modules[j] +" : ")))
        if NotesStagiaires[j] < 10:
            break

    Notes.append(NotesStagiaires)

#-------Affichage du nom et notes des stagiaires:

print("--------------------------------------------------------------------------------")
print("|    NOM STAGIAIRE    |||    JAVA   | PYTHON |  LARAVEL   |    VUEJS   |")
print("--------------------------------------------------------------------------------")

for n in Notes:
    print(f"|    {NomStagaires[Notes.index(n)]}    |||    {Notes[Notes.index(n)][0]}    |      {Notes[Notes.index(n)][1]}     |    {Notes[Notes.index(n)][2]}    |    {Notes[Notes.index(n)][3]}    |")
    print("----------------------------------------------------------------------------")

print("Notes :", Notes)

#-------Calcule de moyenne de chaque stagiaire + affichage le premier moyenne + leur position :

max = sum(Notes[0])/len(Modules)
position = 0

for nt in Notes:
    print(" ---> Moyenne de Stagiaire :",sum(nt)/len(Modules))
    if max < sum(nt)/len(Modules):
        max = sum(nt)/len(Modules)
        position = Notes.index(nt)
print("Premier Moyenne :", max, "Position de Stagaire ", position+1)

