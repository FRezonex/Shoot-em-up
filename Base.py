from Classes import *

pygame.init()

#Variables
listeProjectiles = []
listeEnnemis = []

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
ennemi = Vaisseau(imageEnnemi, fenetre, 2, 100, 100)
listeEnnemis.append(ennemi)
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

    ennemi.deplacer("droite", largeur, hauteur)



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

    joueur.afficher()
    ennemi.afficher()
    pygame.display.flip()


pygame.quit()