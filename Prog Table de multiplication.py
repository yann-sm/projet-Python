"""
 Cahier des charges :
-recuperer ce que saisit l'utilisateur;
-tester si c'est un nombre.
-si oui, continuer, afficher la table de multiplication, et demander à l'utilisateur
 s'il souhaite quitter le programme ou non.
-si no, arreter la boucle et demander a l'utilisateurde saisir un nombre.
"""

quitter = ""

while quitter != "o" :

    oInput = input("Svp, entrez un nombre :")

    if oInput.isdigit() :
        oInput = int(oInput)
        for i in range (11) :
            print(str(i) + "*" + str(oInput) + "=" + str(i*oInput))
       #ou peu s'ecrire :
        #print("{0}*{1}={2}".format(i,Nombre1,i*Nombre1))
            

        quitter = input("voulez-vous quitter ? o/n ")
        if quitter == "o" :
            print("Au revoir")
        if quitter == "n" :
            print("continue")     #continue permet de recommencer la boucle
                
        

    elif not oInput.isdigit() :
        print("Erreur, vous n'avez pas entré un nombre !")
        

        
