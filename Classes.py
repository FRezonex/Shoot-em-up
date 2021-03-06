import pygame
from pygame.locals import *

class ElementGraphique:
    def __init__(self, image, fenetre, x=0, y=0):

        self.fenetre = fenetre
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def afficher(self):
        self.fenetre.blit(self.image, self.rect)

    def collision(self, objet):
        if self.rect.colliderect(objet.rect):
            return True
        return False

    def deplacer(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Objet(ElementGraphique):
    def __init__(self, image, fenetre, x=0, y=0):
        super().__init__(image, fenetre, x, y)

        self.mort = False

    def afficher(self):
        if not self.mort:
            ElementGraphique.afficher(self)


class Vaisseau(Objet):
    def __init__(self, images, fenetre, vitesse, x=0, y=0):
        super().__init__(images[0], fenetre, x, y)

        self.images = images
        self.vitesse = vitesse
        self.dimension_x = 48
        self.dimension_y = 54

    def deplacer(self, direction, largeur, hauteur):
        if direction == "droite" and self.rect.x <= largeur - self.dimension_x:
            self.rect.x += self.vitesse
            self.image = self.images[1]
        elif direction == "gauche" and self.rect.x >= 0:
            self.rect.x -= self.vitesse
            self.image = self.images[2]
        elif direction == "haut" and self.rect.y >= 0:
            self.rect.y -= self.vitesse
        elif direction == "bas" and self.rect.y <= hauteur - self.dimension_y:
            self.rect.y += self.vitesse
        elif direction == "neutre":
            self.image = self.images[0]

    def tirer(self, imagesProjectiles, listeProjectiles, fenetre):
        projectile = Projectile(imagesProjectiles, fenetre, self.rect.x + self.dimension_x/2.5, self.rect.y)
        listeProjectiles.append(projectile)
        print("Feu !")


class Joueur(Vaisseau):
    def __init__(self, images, fenetre, vitesse, x=0, y=0):
        super().__init__(images, fenetre, vitesse, x, y)


class Projectile(Objet):
    def __init__(self, images, fenetre, x=0, y=0):
        super().__init__(images[0], fenetre, x, y)

        self.images = images
        self.compteur = 0
        self.numImage = 0

    def afficher(self):
        self.compteur += 1

        if self.compteur%10 == 0:
            self.numImage += 1
            self.image = self.images[self.numImage]
            if self.numImage == 3:
                self.numImage = -1


        Objet.afficher(self)

    def deplacer(self):
        self.rect.y -= 5

        if self.rect.y == 0:
            self.mort = True


#Fonctions
def creerEnnemis(nombreColonne, nombreLigne, vitesse, positionFin, images, fenetre, listeEnnemis):
    for i in range(nombreLigne):
        y = i*60
        for i in range(nombreColonne):
            ennemi = Vaisseau(images, fenetre, vitesse, positionFin-i*50, y)
            listeEnnemis.append(ennemi)







