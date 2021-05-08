import pygame #Import du module pygame
import os     #Import du module os

pygame.init() #initialise les modules importé de pygame



Largeur_fenetre = 800                      #Variable largeur de la fenetre
hauteur_fenetre = int(Largeur_fenetre*0.8) #variable hauteur de la fenetre

fenetre = pygame.display.set_mode((Largeur_fenetre, hauteur_fenetre)) #Création de la fenêtre.
pygame.display.set_caption('Jeu')                                     #Titre de la fenêtre de jeu.


#fréquence d'image/temps
clock = pygame.time.Clock()     #timer
FPS = 60                        #images par secondes.


#création variables du jeu:
GRAVITE = 0.75                     #création de gravité pour permettre au joueur de tomber.

#variables de mouvements du joueur:
bouger_gauche = False
bouger_droite = False

#couleurs:
BG = (0)        #couleurs d'arrière plan.
RED= (255,0,0)  #couleur de la ligne

#fonction qui colore l'arrière plan:
def draw_bg():
    fenetre.fill(BG)
    pygame.draw.line(fenetre,RED,(0,300), (Largeur_fenetre,300)) #ligne rouge (substitue de sol pour le moment)


#Classe permettant de créer de spersonnages:
class Personnage(pygame.sprite.Sprite):
    def __init__(self,char_type,x,y,scale,speed):
        """
        méthode d'initialisation de la classe.
        Arguments: 
            self
            x: int de la position du joueur sur l'axe x
            y: int de la position du joueur sur l'axe y
            scale: int de la taille du joueur
        """
        pygame.sprite.Sprite.__init__(self)
        self.vivant = True                                                                                  #variable qui vérifie que le personnage est vivant.
        self.char_type = char_type                                                                          #type de personnage qui va permettre de faire des animations pendants les mouvements.
        self.speed = speed                                                                                  #vitesse de mouvement du joueur.
        self.direction = 1                                                                                  #direction du personnage.
        self.mvt_y = 0                                                                                      #variable de mouvement vertical.
        self.saut = False                                                                                   #variable qui vérifie que le joueur saute.
        self.in_air = True                                                                                  #variable qui vérifie quand le joueur est en l'air.
        self.flip= False                                                                                    #permet de changer la direction du personnage quand il avance à droite ou à gauche .
        self.animation_list = []                                                                            #création d'une liste qui accueilleras les animations du personnage
        self.frame_index = 0                                                                                #repère de frame d'animation.
        self.action = 0                                                                                     #variable qui permet d'accéder aux différente animation par exemple 1 pour courir.
        self.update_delay = pygame.time.get_ticks()                                                         #dalai à laquelle se rafraichi l'animation
        
        #importation des images du personnage:
        animation_types = ['Immobile', 'Courir', 'Sauter']
        for animation in animation_types:    
            #réinitialise la liste temporaire des images:
            temp_list=[]                                                                                        #liste temporaire dans laquel vont être stocké les animations pour éviter qu'elle s'accumulent l'une après les autres dans "animation_list".
            #compte le nombre d'image dans le dossier:
            nombre_images = len(os.listdir(f'images/{self.char_type}/{animation}'))                             #créer une liste de tout les élément du répertoire.
            for i in range (nombre_images):
                img = pygame.image.load(f'images/{self.char_type}/{animation}/{i}.png')                                     
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))    #on agrandit l'image du joueur.
                temp_list.append(img)                                                                           #on ajoute les animations à la fin de la liste animation_list.
            self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()                                                                   #création d'un réctangle autour du jouer pour permettre d'appliquer les collisions/mouvement etc.
        self.rect.center = (x,y)                                                                            #on positionne le réctangle sur les coordonée x et y.

    
    def bouger(self,bouger_gauche,bouger_droite):
        """
        méthode qui permet au joueur de pouvoir bouger
        Arguments:
            self
            bouger_gauche : variable permettant de bouger à gauche.
            bouger_droite :  variable permettant de bouger à droite.
        """ 
        #réinitialisé les variables de mouvement:
        dx=0            #variables de mouvement sur l'axe x.
        dy=0            #variables de mouvement sur l'axe y.

        #attribution des variables si on bouge à gauche ou à droite:
        if bouger_gauche:
            dx = -self.speed                    #mouvement à valeurs négatif car on bouge vers la gauche.
            self.flip = True
            self.direction = -1
        if bouger_droite:
            dx = self.speed                     #mouvement à valeurs positif car on bouge vers la droite.
            self.flip = False
            self.direction = 1

        #pour sauter:
        if self.saut == True and self.in_air == False:
            self.mvt_y = -11                    #chiffre négatif car l'axe y commence à 0 en haut de l'écran et augmente quand on descend, étant donné que l'on va vers le haut quand on saute, alors on créer une valeur négative.
            self.saut = False
            self.in_air = True

        #application de la gravité pour que le joueur retombe après avoir sauté:
        self.mvt_y += GRAVITE
        if self.mvt_y > 10:
            self.mvt_y
        dy += self.mvt_y

        #vérifie les collision avec le sol:
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        #update de la position du rectangle:
        self.rect.x += dx                       #mouvement du rectangles sur l'axe x.
        self.rect.y += dy                       #mouvement du rectangles sur l'axe y.


    def rafraichissement_animation(self):
        """
        Méthode qui met à jour l'animation du joueur.
        Arguments:
            self
        """ 
        DELAI_ANIMATION = 170                                                               #on défini la vitesse à laquelle l'animation se joue.
        self.image = self.animation_list[self.action][self.frame_index]                                  #rafraichi l'animation en fonction de la frame actuelle.
        #vérifie si il y a assez de temps qui est passé depuis le dernier rafraichissement:
        if pygame.time.get_ticks() - self.update_delay > DELAI_ANIMATION:  
            self.update_delay = pygame.time.get_ticks()
            self.frame_index += 1
        
        #si l'animation est finie elle reviens au début:
        if self.frame_index >= len(self.animation_list[self.action]):                             
            self.frame_index = 0

        

    def update_action(self, new_action):
        """
        méthode qui met à jour l'animation des actions
        Arguments:
            self
            new_action: nouvelle action qui permet de la comparer avec la précédente pour voir si elle est différente.
        """        
        #vérifie si la nouvelle action est différente à la précédente.
        if new_action != self.action:
            self.action = new_action
            #met à jour les paramétre d'animation
            self.frame_index = 0
            self.update_delay = pygame.time.get_ticks()


    def apparition(self):
        """
        méthode qui affiche le joueur dans la fenêtre.
        Arguments:
            self
        """
        fenetre.blit(pygame.transform.flip(self.image, self.flip, False), self.rect) 


#création du joueur:
joueur = Personnage('personnages',200,200,3/2,5)


run = True
while run: #Boucle contenant les différent événement de la fenêter pendant qu'elle est en route

    clock.tick(FPS)

    draw_bg()

    joueur.rafraichissement_animation()
    joueur.apparition()


    #met à jour les actions du joueur:
    if joueur.vivant:
        #pour sauter:
        if joueur.in_air:
            joueur.update_action(2)         #2=sauter.
        #pour bouger:
        elif bouger_gauche or bouger_droite:
            joueur.update_action(1)         #1=courir.
        else:
            joueur.update_action(0)         #0=immobile.
        joueur.bouger(bouger_gauche,bouger_droite)

    for event in pygame.event.get():  #Boucle qui parcourt les différent evénement de la fenêtre.
        #Commande permettant de quitter la fenêtre:
        if event.type == pygame.QUIT:
            run = False
        #touches du claviers appuyé:
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_q:   #quand la touche a est appuyé.
                bouger_gauche = True
            if event.key == pygame.K_d:   #quand la touche d est appuyé.
                bouger_droite = True
        #touches n'est plus appuyé:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:      #quand la touche a est appuyé.
                bouger_gauche = False
            if event.key == pygame.K_d:      #quand la touche d est appuyé.
                bouger_droite = False
            if event.key == pygame.K_SPACE and joueur.vivant:   #quand la touche w est appuyé et si le joueur est vivant.
                joueur.saut = True         
            if event.key == pygame.K_ESCAPE: #quand échape est appuyé.
                run = False


    pygame.display.update() #Afficher le joueur à l'écran.

pygame.quit() #Désactive l'initialisation des modules importé de pygame.
