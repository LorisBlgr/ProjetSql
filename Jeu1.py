import pygame #Import de la bibiliothèque pygame



pygame.init() #initialise les modules importé de pygame


Largeur_fenetre = 800                      #Variable largeur de la fenetre
hauteur_fenetre = int(Largeur_fenetre*0.8) #variable hauteur de la fenetre

fenetre = pygame.display.set_mode((Largeur_fenetre, hauteur_fenetre)) #Création de la fenêtre.
pygame.display.set_caption('Jeu')                                     #Titre de la fenêtre de jeu.


#Classe permettant de créer de spersonnages:
class Personnage(pygame.sprite.Sprite):
    def __init__(self,x,y,scale):
        """
        Fonction d'initialisation de la classe.
        Arguments: 
            self
            x: int de la position du joueur sur l'axe x
            y: int de la position du joueur sur l'axe y
            scale: int de la taille du joueur
        """
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/personnages/personnage.png')                                                #importation du personnage.
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale))) #on agrandit l'image du joueur.
        self.rect = self.image.get_rect()                                                                   #création d'un réctangle autour du jouer pour permettre d'appliquer les collisions/mouvement etc.
        self.rect.center = (x,y)                                                                            #on positionne le réctangle sur les coordonée x et y.

    def apparition(self):
        """
        fonction qui affiche le joueur dans la fenêtre.
        Arguments:
            self
        """
        fenetre.blit(self.image,self.rect) 


#création du joueur:
joueur = Personnage(200,200,1)

run = True
while run: #Boucle contenant les différent événement de la fenêter pendant qu'elle est en route

    joueur.apparition()

    for event in pygame.event.get():  #Boucle qui parcourt les différent evénement de la fenêtre.
        if event.type == pygame.QUIT: #Commande permettant de quitter la fenêtre.
            run = False


    pygame.display.update() #Afficher le joueur à l'écran.

pygame.quit() #Désactive l'initialisation des modules importé de pygame.