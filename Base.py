from Classes import *

pygame.init()

#Variables
listeProjectiles = []

#Fenetre
largeur = 640
hauteur = 480
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.mouse.set_visible(False)


#Creation objets
fond = ElementGraphique(pygame.image.load("Fond.png").convert_alpha(), fenetre)
joueur = Vaisseau(pygame.image.load("Vaisseau.png").convert_alpha(), fenetre, 100, 100)

imagesProjectiles = [pygame.image.load("Boule de feu 1.png").convert_alpha(), pygame.image.load("Boule de feu 2.png").convert_alpha(),
                     pygame.image.load("Boule de feu 3.png").convert_alpha(), pygame.image.load("Boule de feu 4.png").convert_alpha()]
projectile = Projectile(imagesProjectiles, fenetre)

#Timer
horloge = pygame.time.Clock()
continuer = True

#Boucle du jeu
while continuer:
    horloge.tick(60)

    #Script
    for projectile in listeProjectiles:
        projectile.deplacer()


    #Evenement
    touche = pygame.key.get_pressed()

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


    #Quitter le jeu
    if touche[pygame.K_ESCAPE]:
        pygame.quit()


    #Affichage
    fond.afficher()
    joueur.afficher()

    for projectile in listeProjectiles:
        projectile.afficher()

    #Quitter le jeu
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

pygame.quit()