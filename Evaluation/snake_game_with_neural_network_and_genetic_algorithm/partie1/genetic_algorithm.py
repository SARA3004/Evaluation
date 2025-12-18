import random
import numpy as np
from snake import Snake
from neural_network import NeuralNetwork

class GeneticAlgorithm:
    def __init__(self, size=50):
        self.size = size
        self.population = [Snake() for _ in range(size)]
        self.generation = 1
        self.best_fitness = 0
        self.history = []

    # 1. ÉVALUATION 
    def evaluate(self):
        """Calcule la fitness de chaque serpent et enregistre le meilleur score."""
        for s in self.population:
            s.calculate_fitness()
        
        # Tri pour identifier le meilleur individu
        self.population.sort(key=lambda s: s.fitness, reverse=True)
        self.best_fitness = self.population[0].fitness
        self.history.append(self.best_fitness)

    # 2. SÉLECTION 
    def select(self):
        """Choisit les parents. Utilise l'élitisme et la sélection proportionnelle."""
        # On garde directement le top 10% (Élitisme)
        elite_count = max(1, self.size // 10)
        selected = self.population[:elite_count]
        
        # Sélection par roulette pour le reste du pool (25% de la population totale)
        total_fitness = sum(s.fitness for s in self.population)
        if total_fitness == 0:
            return random.sample(self.population, self.size // 4)

        while len(selected) < self.size // 4:
            pick = random.uniform(0, total_fitness)
            current = 0
            for snake in self.population:
                current += snake.fitness
                if current > pick:
                    selected.append(snake)
                    break
        return selected

    # 3. REPRODUCTION 
    def reproduce(self, selected):
        """Crée la génération suivante avec croisement (crossover) et mutation."""
        new_pop = []
        
        # On conserve les élites (5 meilleurs) sans modification
        for i in range(min(5, len(selected))):
            new_pop.append(Snake(selected[i].network))

        # On complète la population
        while len(new_pop) < self.size:
            p1, p2 = random.sample(selected, 2)
            # Combinaison des cerveaux des parents
            child_net = NeuralNetwork.crossover(p1.network, p2.network)
            # Introduction de variations aléatoires
            child_net.mutate(rate=0.1)
            new_pop.append(Snake(child_net))

        self.population = new_pop
        self.generation += 1