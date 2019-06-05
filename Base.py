from Classes import *
from random import randrange

pygame.init()

#Variables
listeProjectiles = []
listeEnnemis = []
compteurEnnemis = 0

#Fenetre
largeur = 640
hauteur = 480
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.mouse.set_visible(False)

#Chargement des images
imagesProjectiles = [pygame.image.load("Ressources/Sprites/Projectiles/Boule de feu 1.png").convert_alpha(),
                      pygame.image.load("Ressources/Sprites/Projectiles/Boule de feu 2.png").convert_alpha(),
                      pygame.image.load("Ressources/Sprites/Projectiles/Boule de feu 3.png").convert_alpha(),
                      pygame.image.load("Ressources/Sprites/Projectiles/Boule de feu 4.png").convert_alpha()]

imagesJoueur = [pygame.image.load("Ressources/Sprites/Vaisseaux/Joueur neutre.png").convert_alpha(),
                 pygame.image.load("Ressources/Sprites/Vaisseaux/Joueur droite.png").convert_alpha(),
                 pygame.image.load("Ressources/Sprites/Vaisseaux/Joueur gauche.png").convert_alpha()]

imageEnnemi = [pygame.image.load("Ressources/Sprites/Vaisseaux/Ennemi neutre.png").convert_alpha(),
               pygame.image.load("Ressources/Sprites/Vaisseaux/Ennemi droite.png").convert_alpha(),
               pygame.image.load("Ressources/Sprites/Vaisseaux/Ennemi gauche.png").convert_alpha()]

imageFond = pygame.image.load("Ressources/Sprites/Utiles/Fond.png").convert_alpha()


#Creation des objets
fond = ElementGraphique(imageFond, fenetre)
joueur = Joueur(imagesJoueur, fenetre, 6, 100, 100)
creerEnnemis(7, 3, 6, 300, imageEnnemi, fenetre, listeEnnemis)
projectile = Projectile(imagesProjectiles, fenetre)

#Timer
horloge = pygame.time.Clock()
continuer = True

#Boucle du jeu
while continuer:
    horloge.tick(60)
    touche = pygame.key.get_pressed()

    #Deplacement des projectiles
    for projectile in listeProjectiles:
        projectile.deplacer()

    #Deplacement des ennemis
    compteurEnnemis += 1

    for ennemi in listeEnnemis:
        if compteurEnnemis > 0 and compteurEnnemis < 50:
            ennemi.deplacer("droite", largeur, hauteur)
        if compteurEnnemis > 50 and compteurEnnemis < 100:
            ennemi.deplacer("gauche", largeur, hauteur)
        if compteurEnnemis > 100:
            listeEnnemis[randrange(listeEnnemis.__len__())].tirer(imagesProjectiles, listeProjectiles, fenetre)
            compteurEnnemis = 0





    #Deplacement du joueur
    if 0 in touche:
        joueur.deplacer("neutre", largeur, hauteur)
    if touche[pygame.K_d]:
        joueur.deplacer("droite", largeur, hauteur)
    if touche[pygame.K_a]:
        joueur.deplacer("gauche", largeur, hauteur)
    if touche[pygame.K_w]:
        joueur.deplacer("haut", largeur, hauteur)
    if touche[pygame.K_s]:
        joueur.deplacer("bas", largeur, hauteur)

    #Action du joueur
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            projectile = Projectile(imagesProjectiles, fenetre, joueur.rect.x + joueur.dimension_x/2.5, joueur.rect.y)
            listeProjectiles.append(projectile)
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False


    #Affichage
    fond.afficher()

    for projectile in listeProjectiles:
        projectile.afficher()

    for ennemi in listeEnnemis:
        ennemi.afficher()

    joueur.afficher()
    pygame.display.flip()


pygame.quit()