import pygame
from config import *
from genetic_algorithm import GeneticAlgorithm
from game import Game
from utils import plot_fitness

def main():
    # Initialisation de la fenêtre Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake AI - Algorithme Génétique")
    clock = pygame.time.Clock()

    # Initialisation de l'algorithme génétique (taille par défaut 50)
    ga = GeneticAlgorithm()

    running = True
    while running:
        print(f"--- Génération {ga.generation} ---")
        
        # 1. ÉVALUATION : Chaque serpent de la population doit jouer son tour
        for i, snake in enumerate(ga.population):
            game = Game(snake) 

            # Boucle de vie du serpent individuel
            while snake.alive:
                # Gestion des événements Pygame (pour pouvoir fermer la fenêtre)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        snake.alive = False
                        break
                
                if not running:
                    break

                # Mise à jour de la logique du jeu
                game.update() 
                
                # Rendu graphique
                game.draw(screen) 
                
                # Affichage des infos de génération sur l'écran
                font = pygame.font.SysFont("Arial", 18)
                img = font.render(f"Gen: {ga.generation} | Serpent: {i+1}/{ga.size}", True, WHITE)
                screen.blit(img, (10, 10))
                
                pygame.display.flip()
                
                # Vitesse d'exécution (augmentez FPS dans config.py pour accélérer l'apprentissage)
                clock.tick(FPS)  

            if not running:
                break

        # 2. ÉVOLUTION : Une fois que toute la population a fini de jouer
        ga.evaluate()    # Calcule les scores de fitness 
        selected = ga.select()   # Sélectionne les meilleurs parents 
        ga.reproduce(selected)   # Crée la génération suivante 

        print(f"Meilleure Fitness: {ga.best_fitness:.2f}")

    # Une fois la boucle quittée, afficher le graphique de progression
    plot_fitness(ga.history)  
    pygame.quit()

if __name__ == "__main__":
    main()