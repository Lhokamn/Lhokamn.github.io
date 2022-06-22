## Donjon textuel

#lien de référence "https://nsi.xyz/projets/un-donjon-textuel-en-python-sur-la-numworks/"

##combat
from random import *

class Joueur:

    def __init__(self,pv,att,skills,name):
        self.maxpv=pv
        self.pv=self.maxpv
        self.attaque=att
        self.skills=skills
        self.name=name

    def tour(self, oponent):
        if len(self.skills)==3:
            print("quelles capacités voulez-vous utiliser ?  \n 1)", self.skills[0][0], " \n 2)", self.skills[1][0], " \n 3)", self.skills[2][0])
        elif len(self.skills)==2:
            print("quelles capacités voulez-vous utiliser?  \n 1)", self.skills[0][0], " \n 2)", self.skills[1][0])
        elif len(self.skills)==1:
            print("quelles capacités voulez-vous utiliser?  \n 1)", self.skills[0][0])
        else:
            tmor()
        capacite=input()
        if int(capacite)-1>=len(self.skills):
            tmor()  
        use_attaque(self.skills[int(capacite)-1][1],self.skills[int(capacite)-1][0],self,oponent)
        
    def heal(self):
        self.pv=self.maxpv
        
    def give_classe(self, classe):
        if classe==1:
            self.classe='m'
            self.skills.append(['boule életrique',5])
        elif classe==2:
            self.classe='a'
            self.skills.append(['dague furtive',5])
        elif classe==3:
            self.classe='g'
            self.skills.append(['coup d épée',5])
        else :
            tmor()

class Monstre:

    def __init__(self,pv,att,skills,name):
        self.pv=pv
        self.attaque=att
        self.skills=skills
        self.name=name

    def tour(self, oponent):
        percent=0                                                                             #variable qui compte la proba que l'attaque sorte
        atta=0                                                                                #place dans la liste de l'attaque 
        turn=1                                                                                #variable pour le while
        proba=random()                                                                        #probabilité choisi pour l'attaque
        while turn:
            percent+=self.skills[atta][2]                                              #incrémente la probabilité en fonction de l'attaque vérifier
            if proba<=percent:                                                                 #vérifie si c'est la bonne attaque
                use_attaque(self.skills[atta][1],self.skills[atta][0],self,oponent)      #utilise l'attaque
                turn=0                                                                        #stop le while
            else:
                atta+=1                                                                       #passe à l'attaque suivante
        


def use_attaque(dmg,name,user, oponent):
    oponent.pv-=dmg*user.attaque
    if name=='coup en traitre':
        print("vous êtes un lache /n Bienvenue au club")
    if is_dead(oponent):
        oponent.pv=0
    print(user.name,"à utiliser", name, "sur", oponent.name,"et à infliger", dmg*user.attaque, "dégât", "il reste à", oponent.name, oponent.pv,"pv")

def is_dead(entite):
    if entite.pv<=0:
        return 1
    return 0

def combat(joueur,monstre):
    fight=1
    debut=randint(1,6)
    if debut <=3:
        turn="m"
    else:
        turn="j"

    while fight:
        if turn=="m":
            monstre.tour(joueur)
            turn="j"
            
        elif turn=="j":
            joueur.tour(monstre)
            turn="m"


        else :
            print("BUG!")
        if is_dead(joueur):
            tmor()
            return 0
        if is_dead(monstre):
            print("vous avez gagné ! \n Félicitations.")
            print("")
            input("**appuyez sur entrée pour continuer**")
            for i in range (7):
                print()
            
            return 1


## mort

import sys

def tmor():
    print("*vous êtes mort*")
    time.sleep(5)
    sys.exit()

## histoire

import time 

#tableau1

for i in range (100):
    print("")

nom=str(input("Quel est ton nom ? \n"))

for i in range (7):
    print("")

joueur=Joueur(300,13,[['coup de poing ordinaire',3],],nom)

print("""
    *Fin de journée*
    
Lukas 
    Hey mec 
Lukas 
    Hey mec
Lukas 
    Mec
Lukas 
    Réveille-toi ! il y a M.Mcheyk qui te regarde\n""",
nom,"""
    Quoi ?... Laisse-moi dormiiiiir….
M.Mcheyk 
    Jeune homme, que faites-vous ?\n""",
nom,"""
    J’écoutais votre cours sur la mécanique des fluides monsieur !
M.Mcheyk : 
    Ça fait 12 jours qu’on a fini ce chapitre. Tu es sûr que tout va bien ?

    *La classe rigole*

M.Mcheyk
    Je vais devoir faire un rapport, ce n'est pas la première fois.

    *La sonnerie vous casse les oreilles*
        
Lukas: 
    Meeeec t’exagères\n""",
nom,"""
    Laisse-moi, je rêvais d’un monde où j’étais le héro venu d’ailleurs pour sauver la veuve et l’orphelin de la reine démone
Lukas 
    Tu as regardé beaucoup trop d’isekai mec, redescends sur terre ! D’ailleurs, on regarde Shield hero ce soir ?\n""",
nom,"""
    Non désolé, j’ai des choses à faire ce soir
Lukas 
    Jouer aux jeux vidéos ?\n""",
nom,"""
    Pas forcément… 
Lukas 
    Mon bus est arrivé, tu viens ?

 """)

a=int(input('Je fais quoi ? \n 1. CDI\n 2. je rentre à pied \n 3. je rentre en transport \n '))

for i in range (7):
    print("")

if a==1:
    print(nom,"""
    Je dois rester, mes parents veulent que je lise les livres pour la littérature…
Lukas
    cheh ! 
    
    *Se retourne, dépité*\n""",
nom,"""        
    Putain ! J’ai oublié de lui demander le nom du livre, je vais en chercher un autre
    
    *Cherche dans tout le CDI pendant 1h mais ne trouve rien*\n""",
nom,"""
    Je perd mon temps ici, je vais rentrer à pied pour que mes parents croient que j’ai beaucoup lu
    
    *Vous sortez du lycée*\n""",
nom,"""
    J’aurais dû rentrer avec Lukas tout à l’heure, maintenant il fait nuit et je n’ai plus de bus
    
    *Un mec approche*\n""",
nom,"""
    bonjour
Inconnu 
    Je viens te tuer pour faire avancer le scénario, ne pose pas de questions.\n""",
nom,"""
    Quoi ?
Inconnu
    J’ai dit pas de question !
    
    *L’inconnu vous donne un coup de couteau dans le ventre et vous mourrez *
""")
    joueur.pv+=50
elif a==2:
    print(nom,"""
    Non, il y a trop de monde dans le bus sérieux, comment tu fais ?
Lukas
    Pour de vrai ça passe…
    
    *Vous vous retournez sans rien ajouter.

     Vous traversez le passage piéton quand soudain un camion arrive à toutes vitesse vous faisant paniquer. Vous êtes tétanisé jusqu’à ce que le camion vous touche, vous faisant mourir pour que l’intrigue avance.
    
     N’oubliez pas les enfants, regardez des deux cotés avant de traverser l’autoroute ! *
""")
    joueur.attaque+=2
elif a==3:
    print(nom,"""
    Ouais, j’ai la flemme de marcher.
Lukas
    Ça me fera passer le temps plutôt que d’écouter des musiques commerciales de merde.
    
    *Vous êtes rentré en bus avec votre ami, mais il habite plus loin.
     Vous demarrez votre ordinateur et commencez à jouer à des jeux flash.
     Que faites vous de votre vie ?*\n""",
nom,"""
    J’ai la dalle...
 """)
    b=int(input("Je me fais à manger ? \n 1. oui \n 2. non, je commande \n"))
    if b==1:
        print("""
    *Vous fouillez dans votre frigo et trouvez une boite de pasta box que vous faites chauffer au micro-onde.
     Malheureusement vous êtes incroyablement stupide et vous avez oublié votre fourchette dedans...
     Votre nom sera inscrit au Darwin Award, bravo !*
""")
        joueur.pv+=50
    elif b==2:
        print("""
    *Vous choisissez de commander des huitres
     Malheureusement elles étaient avarié car vous avez commandé via internet explorer.
     En même temps pourquoi utilisiez-vous internet explorer ? 
     Vous êtes mort.*
        """)
        joueur.attaque+=2
    else:
        tmor()
else:
    tmor()

input("**appuyez sur entrée pour continuer**")

for i in range (7):
    print("")

#tableau2

print("""
Dieu
    T’es mort, comment t’as fait ? T’étais censé mourir à 120 ans en devenant l’homme le plus riche du monde ! Bon bah du coup je t’envoie dans un monde de fantasy car scénario etc. Tue la reine démone stp.
    
    *Vous êtes transporté par magie dans un autre monde et arrivez dans la ville de Arkaley*
\n""",
nom,"""
    Mais qu’est-ce qui vient de se passer ? Et comment je connais le nom de cette ville alors que je ne suis jamais venu ici ? Et c'est quoi ces vieux bâtiments ? On dirait le Moyen-âge... Bon je fais quoi ?
    
    *Vous voyez de l’agitation au loin : une personne au milieu d'une foule crie*
    
Side-kick 
    Je cherche le réincarné pour l’amener à la suite de l’histoire.\n""",
nom,"""
    On m’appelle ?
Side-kick 
    Bonjour, je suis Side-kick, un type inutile qui va te suivre partout et ne vas jamais être utile à l’intrigue. J’ai un nom mais les Créateurs m’appellent Side-kick tout le long du jeu donc pas besoin de le dire.\n""",
nom,"""
    Ouai, évidemment [ils sont tous fou ou quoi ?],et donc, tu me cherches pour quoi ?
Side-kick
    Ah oui, je dois t’amener combattre la reine démone.\n""",
nom,"""
    Attend, quoi ? je ne sais pas me battre.
Side-kicK
    Oui ! Je dois d’abord t’emmener faire le tuto puis te faire choisir ta classe.\n""",
nom,"""
    Et pourquoi pas prendre la classe avant le tuto ?
Side-kick
    On ne questionne pas le scénario !
""")

input("**appuyez sur entrée pour continuer**")

for i in range (7):
    print("")
    
#tableau3
print("""
    *Vous êtes arrivé au tuto. C'est Side-kick qui l'a dit, vous devez tuer les dragons devant vous*
""")
e=int(input("Je fuis ? \n 1. oui \n 2. non \n"))
if e==1:
    print("""
    *Vous prenez vos jambes à votre cou et fuyez le plus vite possible mais vous n'aviez pas vu la falaise devant vous.
     Vous tombez et vous vous écrasez comme une crêpes au Nutella*
""") 
    tmor()
elif e==2:
    m1=Monstre(100,2,[['trempette',0,1]],'miraé')
    
    combat(joueur,m1)
else:
    tmor()
    
print("""
Side-kick
    Félicitations, tu as tué un monstre de difficultée nul, tu es vraiment trop foooooooooooooooooooort.\n""",
nom,"""
    Merci, je ne pensais pas devoir me battre dès maintenant, sachant que je n'ai ni ma classe ni d'arme.

    *Vous recevez un coup de pied derrière le dos et vous vous écroulez par terre*\n""",
nom,"""
    Pourquoi tu m'as tapé Side-kick?
Side-kick
    Pose pas de question, c'est le scénario. 
Side-kick
    Maintenant on va aller à la Guilde.\n""",
nom,"""
    C'est quoi comme guilde? Les exterminateurs de démons? La guilde des chercheurs de dragons suprêmes ? La Féri Téil?
Side-kick
    C'est une guilde encore mieux que tout ça réuni !\n""",
nom,"""
    C'est quoi ?
Side-kick
    La Guide des réincarnés #nomprovisoire.\n""",
nom,"""
    Heuuuuuuuuuuuu...
    
    *Vous arrivez à la guilde*
    
Side-kick
    Je te laisse choisir ta classe. il n'y a pas d'originalité, mais on devait tout faire en 3 semaines.
""")


d=int(input("Quelle classe de personnage je prend ? \n 1. mage \n 2. assassin \n 3. guerrier \n"))

joueur.give_classe(d)

for i in range (7):
    print("")
    
#tableau4
print(""" 
    *Vous vous baladez en ville avec Side-kick*\n""",
nom,"""
    On fait quoi aussi ici?
Side-kick
    On fait du shopping, tu vas pas tuer la reine démone comme ça, tu fais crade et on peux pas laisser passer ça. J'ai eu de l'argent pour tout acheter car le farm c'est long et chiant.
    
    *Vous vous sentez humilié* (mais c'est vrai)

Side-kick
    Bon, tu aimerais quel type de vêtement ? aventurier ? homme d'affaires ?\n""",
nom,"""
    Je veux garder mon style.
Side-kick 
    Je dois dépenser l'argent, prends quelque chose et vite, la pauvre reine démone doit beaucoup trop s'ennuyer.
    
    *Vous passez devant un magasin de piscine*
""")


f=int(input("Vous voyez un maillot de bain, le voulez vous ? \n 1. oui \n 2. non \n"))

if f==1:
    print(
nom,"""
    Je veux ce maillot et c'est bon l'affaire est réglée.""")
    print("{Vous avez un maillot de bain !}")

else:
    print(nom,"""
    Je veux vraiment rien... donne cet argent aux dirigeants blindés de fric de cette petite ville.
Side-kick
    Comme tu veux.
""")

input("**appuyez sur entrée pour continuer**")

print(""" 
    *En continuant de vous balader, vous croisez une grand-mère qui a besoin d'aide*

""")

h=int(input("Voulez-vous l'aider ? \n 1. oui \n 2. non \n"))
if h==1:
    print("""
    *Vous l'aidez à descendre son petit chien tout mignon d'un arbre (vous avez beaucoup de coeur)*
    
vieille dame
    Merci beaucoup, je ne pensais pas que quelqu'un allait venir m'aider à descendre Médehor de l'unique arbre de ce village.\n""",
nom,"""
    C'est naturel d'aider les gens.
Side-kick
    Bon c'est pas tout, mais il faut tuer la reine démone, les auteurs commencent à trouver ça très long de tout écrire.
""") 
else:
    print("""
Grand-mère
        C'est vraiment ça le héro censé sauver notre monde ? je ne le confie pas à un héro pareil ! Side-kick ! abandonne ta mission avec ce héro car il ne vaut rien !
Side-kick
    Oui grand maître de la Guilde, je vous suis. 
    
    *Side-kick se retourne vers toi*
    
Side-kick
    Toi, ne nous suis pas, héro indigne !

    *Laissé à vous même dans un monde incunnu, vous mourrez de froid, faute de trouver un logement à la nuit tombée*

""")
    tmor()

input("**appuyez sur entrée pour continuer**")

for i in range (7):
    print("")

#tableau5
print("""
        *Après toutes ces aventures, vous sortez enfin du village. Le narrateur est impréssionné que vous soyez toujours vivant*
Side-kick
    N'empêche, je suis heureuse de te connaitre. Tu sais tu me fais beaucoup d'effet et je me disais que...\n""",
nom,"""
    Que quoi? {avec un air géné}
Side kick 
    Tu veux bien le faire?\n""",
nom,"""
    Tout ce que tu veux.
    
    *Tu sens qu'un sac est arrivé sur ton dos*

Side_kick
    Merci de me débarasser de mon sac, il commençais à être trop lourd pour moi. Tu pensais à quoi ?\n""",
nom,"""
    Rien du tout...
    
    *Un monstre apparaît*
    
""")

msortie=Monstre(150,3,[['saut',1,0.5],['coup de langue',3,0.5]],'Yuki')

combat(joueur,msortie)
print("""
    * vous continuez de marcher dans les herbes vertes de la plaine. *\n""",
nom,"""
    Il ne se passe rien ici, c'est terrible !
Side-kick
    Je t'ai dis quoi ? arrêtes de poser des questions sur cet univers, on essaye de le garder cohérent.\n""",
nom,"""
    Mais je disais juste que...
Side-kick
    Ne dis rien, c'est mieux comme ça.
    
    *Vous marchez 10 minutes avant d'avoir mal aux pieds*
\n""",
nom,"""
    J'en peux plus.
Side-kick 
    Gros flemmard, c'est pour ça que tu es mort.
    
    *Vous vous reposez 5 minutes avant de voir des braises autour de vous. Vous vous retournez*

Ifrit
    Ça fait cinq minutes que j'attend derrière vous comme ça ! Vous me voyer enfin. Je commençais à m'impatienter !
""" ) 

i=int(input("Comment je l'attaque ? \n 1. au corps à corps avec mon corps de lâche \n 2. attaque à distance comme un lâche \n 3. attaque par derrière comme un lâche \n 4. ne pas bougez \n"))
if i==1 and joueur.classe=='g':
    print(""" 
    *Vous arrivez à porter un coup fatal grâce à votre classe, il n'a rien pu faire*
""")
elif i==2 and joueur.classe=='m':
    print(""" 
    *Vous arrivez à porter un coup fatal grâce à votre classe, il n'a rien pu faire*
""")
elif i==3 and joueur.classe=='a':
    print(""" 
    *Vous arrivez à porter un coup fatal grâce à votre classe, il n'a rien pu faire*
""")
else:
    mdemon1=Monstre(200,5,[['flamme',3,0.45],['poing de feu',5,0.45],['explosion',50,0.1]],'Ifrit')
    combat(joueur,mdemon1)


print("""
    *Vous trouvez une moitié de carte indiquant l'emmplacement de la reine démone*
\n""",
nom,"""
    Ça veut dire qu'on va devoir affronter un autre seigneur démon ? La poisse.
Side-kick
    Tu t'en es plutôt bien sorti sur celui là pourtant.\n""",
nom,"""
    Pas sûr que l'autre soit aussi simple...
""") 

input("**appuyez sur entrée pour continuer**")

for i in range (7):
    print("")

#tableau6
print("""
    *Après une journée de marche, vous vous sentez sale. avec Side-kick, vous décidez de vous laver dans le lac tout proche*
Side-kick
    J'ai trop mal au pied, je vais me laver.\n""",
nom,"""
    Je te suis.
""")

if f==1:
    j=int(input("Voulez-vous mettre votre maillot de bain ? \n 1. oui \n 2. non \n"))
    if j==1:
        print("""
    *Vous enfilez votre maillot de bain et prenez une douche dans la rivière avec Side-kick*
""") 
    elif j==2:
        print(""" 
Side-kick
    Mais tu vas pas bien ?! Jamais je ne vais prendre ma douche avec toi si tu es nu. Tu es un porc et tu devrais revoir toutes tes habitudes ! J'ai une très très fortes envie de te tuer... Mais je vais pas le faire car tu dois réaliser ton objectif... Je ne t'aiderais plus jamais lors des combats.
    
    *Vous recevez un coup de poing qui vous éjecte de l'autre coté du lac alors que vous êtes encore habillé*
""") 

else:
    print(""" 
Side-kick
    Mais tu vas pas bien ?! Jamais je ne vais prendre ma douche avec toi si tu es nu. Tu es un porc et tu devrais revoir toutes tes habitudes ! J'ai une très très fortes envie de te tuer... Mais je vais pas le faire car tu dois réaliser ton objectif... Je ne t'aiderais plus jamais lors des combats.
    
    *Vous recevez un coup de poing qui vous éjecte de l'autre coté du lac alors que vous êtes encore habillé*
""") 
    j=2

input("**appuyez sur entrée pour continuer**")
for i in range (7):
    print("")

print("""
    *Après avoir fait plein de bruit, vous voyez un remous dans l'eau. de ce remous sors une créature magnifique, un trap !*

Trap 
    Je suis la seigneur démone de l'eau. qui ose déranger ma démonique sieste ?\n""",
nom,"""
    Vous savez qu'avec les reflets de l'eau, ça se voit que vous êtes un mec ?
Trap
    Je suis une reine démone! et personne d'autre que moi ne peut dicter mon genre.\n""",
nom,"""
    D'accord, mais je suis pour l'égalité des sexes. Et toi, en tant que seigneur démone, je vais te frapper aussi fort que si tu était un mec !
""") 

mdemon2=Monstre(200,6,[['aqua',0,0.05],['lame d eau',5.5,0.35],['tourbillon',15,0.5],['déluge',70,0.1]],'Trap')

combat(joueur,mdemon2)


print(nom,"""
    Je vois un truc briller sur l'eau.
Side-kick 
    Ah! ça doit la suite du scénario ! heuuu... je veux dire la carte qui mêne vers la reine démone. mais avant ça, tu ne penses pas qu'on devrait retourner en ville se reposer ?
""") 

k=int(input("Retourner en ville ? \n 1. oui \n 2. non \n"))

for i in range (7):
    print("")

if k== 1:
    print(nom,"""
    Ouai, pas con. Ça permetrra de recupérer des PV et d'améliorer cet équipement pourri.
Side-Kick 
    Ça tombe bien ! Je connais un forgeron qui propose de super armure, c'est le forgeron de la fameuse forge du dragon blanc aux yeux bleu. \n""",
nom,"""
    Je reconnais c'est un réference à ...
Side-kick 
    Chuuut, on a pas les droits !

    *Vous arrivez à la forge et vous voyez trois belles armures*
""")
    g=int(input("Quelle armure voulez-vous ? \n 1. armure de guerrier \n 2. robe de mage \n 3. armure légère d'assassin\n"))
    if g==1:
        joueur.maxpv+=300
        joueur.attaque+=2
        if joueur.classe=="g":
            joueur.skills.append(['contre-attaque',11])
    elif g==2:
        joueur.maxpv+=200
        joueur.attaque+=3
        if joueur.classe=="m":
            joueur.skills.append(['thunderstorm',11])
    elif g==3:
        joueur.maxpv+=250
        joueur.attaque+=2.5
        if joueur.classe=="a":
            joueur.skills.append(['coup en traître',11])
    else:
        joueur.maxpx-=50
    joueur.heal()
elif k==2:
    print(nom,"""
    Nan ! on a pas le temps ! je veux en finir au plus vite.
""")
else:
    print("*Vous passez trop de temps à réfléchir. vous êtes épuisé")
    tmor()
    
input("**appuyez sur entrée pour continuer**")

for i in range (7):
    print("")

#tableau7

print("""
    *Vous arrivez devant le château de la reine démone. Vous vous êtes sûrement imaginé un château immense avec des piques et des tours dans tout les sens, mais non! C'est un château normal, comme n'importe lequel au Moyen-âge : il ne faut pas que ce soit beau, ce doit être pratique* \n""",
nom,"""
    C'est vraiment ça le château de la reine démone ? Déçu.
Side-kick 
    Ouai bah, c'est l'être dans ce château qui menace le monde entier, alors on juge pas !\n""",
nom,"""
    Allez c'est l'heure de défoncer des gueules !
    
    *Vous vous apprêtez à défoncer la porte du château quand Side-kick vous arrête*

Side-Kick 
    La reine démone est très à cheval sur l'étiquette, tu devrais faire gaffe... Par exemple, toquer avant d'entrer.\n""",
nom,"""
    Je ne sais pas, je ne suis pas sur, j'ai peur de ce qui peut se passer.
Side-kick
        C'est ton choix.
""")

l=int(input("Voulez-vous toquer? \n 1. oui \n 2. non \n"))

for i in range (7):
    print("")
    
if l==2:
    print(" *Le pont-levis sur lequel vous vous trouvez se lève sur vous et vous vous retrouvez écrasé contre la porte en acier renforcé. Quelle idée d'essayer d'enfoncer ce genre de porte ?*")
    tmor()
elif l==1:
    print("""
    *La reine démone vous ouvre*
Milim
    Bonjour! je suis Milim, la reine démone, vous allez bien ? 
 
""")
    if j==1:
        print("""
reine démone
    D'ailleurs, j'ai vu votre combat contre Trap. Vous êtes très mignon en maillot de bain !
""")
    m=int(input("Dire bonjour? \n 1. oui \n 2. non \n"))
    
    for i in range (7):
        print("")
    
    if m==1:
        print(nom, """
    Bonjour.
Milim
    Enfin quelqu'un de poli dans ce monde !\n""",
nom,"""
    C'est bien normal face à une loli aussi belle que ça !
Milim
    Moi une loli ?\n""",
nom,"""
    De là où je viens, c'est un compliment ! Et j'adore les femmes plus petites que moi .
Milim 
    Me voilà bien ravie ! Asseyez-vous, je vous apporte le thé.
""")
        n=int(input("Accepter le thé? \n 1. oui \n 2. non \n"))
        
        for i in range (7):
            print("")
        
        if n==1:
            print(nom,"""
    Je prendrais avec plaisir du thé et un bon moment avec vous !
Milim
    Je vois que tu es un homme de culture ! Aimes tu te travestir ? J'ai un petit faible pour les gens comme ça.
""")            
            o=int(input("Aimez-vous vous travestir? \n 1. oui \n 2. non\n"))
            if o==1:
                print(nom,"""
    Je suis prêt à tout faire, même si je dois en perdre mon honneur ! J'ai toujours aimé me déguiser quand j'étais plus jeune.
Milim
    OH ! Tu sais que tu me plais de plus en plus. \n""",
nom,"""
    Mo... Moi?
Milim
    Et toi seul! Veux-tu que je te partage mon pouvoir pour que tu puisses diriger ce monde ?\n""",
nom,"""
    Je suis prêt à tout faire pour être à vos cotés !
Side-kick
    Comment oses-tu me faire ça ?\n""",
nom,"""
    Bah écoute, j'ai été déçu de toi au lac, au moins, avec elle, je peux avoir beaucoup de pouvoir.
Side-kick
    Tu ne me laisse pas le choix, je dois appeler papa.

    *Une puissante lumière vous éblouit*

Dieu
    Mec tu fais quoi ? Tu dois la tuer ! Pour que tu me rejoigne au paradis !\n""",
nom,"""
    Grosse flemme.
""")
                
                if j==1:
                    print("""
Milim
    Il a décidé de me faire confiance, dégage de chez moi ! Ça fait X années que je t'ai quitté, tu dois me laisser tranquille !
    Je vais me marier avec lui !\n""",
nom,"""
    J'accepte !
Dieu
    Je n'ai pas le choix...
    Je vous déclare mari et femme !
    
    Vous pouvez aller dans la chambre
""")
                if j==2:
                    print("""
Milim
    Si tu étais plus mignon je t'aurais bien épousé, c'est dommage.\n""",
nom,"""
    Si vous m'aviez vu en maillot de bain vous auriez su à quel point je suis mignon. Sur ce je vous laisse et je rentre à ma maison.
   *Vous partez du château trouvez un nouveau chez vous*
    
""")
                sys.exit()
            if o==2:
                print(nom,"""
    Me travestir? Et puis quoi encore ! Plutôt mourir !
""")
            
        if n==2: 
            print(nom,"""
    Nan ! C'est pas raisonable, on est là pour se battre au départ.
Milim
    Ah oui c'est vrai! Tiens-toi prêt car je ne compte pas perdre !
""")
            
    if m==2:
        print("""
reine démone
    T'as pas dit bonjour! Je vais allez voir ta maman !
""")
    if m==2 or m==1 and n==2 or m==1 and n==1 and o==2 :
        mReineDemon=Monstre(750,8,[['liane des ténèbres',10,0.2],['abysse infinie',12,0.312],['chaînes des enfers',16,0.438],['bisou',100000000000,0.05]],'Milim')
        combat(joueur,mReineDemon)
        if nom=='Constentin':
            print("""
    *Dieu descend te féliciter puis te donne sa place de Dieu car tu es Constentin, faisant de toi un être supérieur à lui*
""")
        else: 
            print("""
    *Félicitations, tu as fini notre jeu ! Tu peux allez au paradis désormais ! Voilà une autruche car on aime les autruches !(non il n'y a pas d'image, car on pas de tournevis)*
""")
else:
    tmor()
