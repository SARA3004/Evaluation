**Fait part:**
  TARARIST Sara  
  MENDY Khadidiatou

**3.2 Questions d’architecture**
   **1. Choix de l’architecture** 

            Je choisirais l'Agent Apprenant basé sur le Deep Q-Network (DQN).

          **Pourquoi ?**

            Complexité : Le DQN, en utilisant un réseau neuronal (Deep Learning) pour approximer la fonction Q, peut gérer ces grands espaces d'états là où le Q-Learning classique (basé sur une table) échouerait.

            Performance : Le DQN est un algorithme robuste d'apprentissage par renforcement qui vise explicitement à maximiser la fonction de récompense à long terme, ce qui est le but ultime d'un agent rationnel.

            Intégration Génétique : L'architecture neuronale (les poids et biais du réseau) offre un ensemble clair de paramètres à optimiser et à modifier via un Algorithme Génétique.

            __-> Décrivez les composants de votre architecture choisie:__

            1. Le Module de Perception (Capteurs) :Reçoit l'observation de l'environnement.
            2. Le Module de Raisonnement/Action (Le Réseau Q) : -Un réseau neuronal (le LLM de l'agent) -Logique de décision -Actionneurs
            3. Le Module d'Apprentissage
            4. La Fonction de Performance


   **2. Problématique d’apprentissage**

      -> Une problématique spécifique que votre agent doit résoudre:
        
        Exploration vs. Exploitation dans un Environnement Déterministe

        Formulation de la Problématique:
            Développer un agent DQN pour un jeu de grille (style Labyrinthe ou Pac-Man simplifié) où la récompense maximale est située à la fin, mais où le chemin vers cette récompense est très long et semé de petites récompenses (pièces) et de petites pénalités (danger mineur). L'environnement est déterministe (chaque action mène au même état suivant) mais le coût de l'exploration est élevé (temps/énergie).

            Le Défi : L'agent doit éviter de tomber dans des optima locaux, c'est-à-dire une boucle où il exploite des récompenses mineures et faciles d'accès (ex: faire le tour de la zone de départ pour ramasser les 5 premières pièces sans jamais chercher la sortie).

            L'objectif est d'apprendre la politique optimale qui mène au but final, malgré le coût immédiat de l'exploration des chemins inconnus.

        Cette problématique est intéressante/challengante:

          (Exploration vs. Exploitation) : Ce problème est au cœur de l'apprentissage par renforcement.
           Un agent qui exploite trop vite ne découvre pas le chemin optimal global. Un agent qui explore trop ne converge jamais vers une politique stable. 
           La difficulté réside dans le réglage de la politique £-gloutonne (diminution du taux £) pour garantir que l'exploration est suffisante en début d'apprentissage, mais qu'elle diminue pour laisser place à l'exploitation une fois que le chemin optimal est découvert.

           Challenge (Dépendance aux Hyperparamètres) : Le DQN est très sensible aux hyperparamètres:
           Taux d'apprentissage.
           Taux d'exploration initial et final .
           Facteur d'actualisation.
           Taille de la Mémoire de Rejeu.
           L'échec de l'agent à trouver l'optimum global est souvent dû à un mauvais choix de ces hyperparamètres, ce qui fait de ce problème un candidat idéal pour l'optimisation génétique.

   **3.Intégration avec l'Algorithme Génétique** 

            -> L'Algorithme Génétique sera utilisé ici comme un Optimiseur d'Hyperparamètres et un Fine-Tuner de la politique DQN pour résoudre le problème des optima locaux.

            -> Schéma d'Interaction entre les deux Approches
                Le système fonctionnera en deux boucles imbriquées :

                    -Boucle Intérieure (DQN) : L'apprentissage par renforcement classique.

                   - Boucle Extérieure (Algorithme Génétique) : L'optimisation des paramètres du DQN.
            
           -> Aspects de l'Agent Optimisés Génétiquement
            L'Algorithme Génétique est excellent pour explorer un grand espace de paramètres non-linéaires.
              Il sera appliquer pour optimiser deux aspects :
                 -Hyperparamètres du DQN: ces valeurs ont un impact dramatique sur la capacité de l'agent à explorer et à converger.
                  L'Algorithme Génétique trouve rapidement des combinaisons performantes sans balayage manuel.
                 -Poids et Biais du Réseau Q: C'est une forme de Neuroévolution. Au lieu d'initialiser les poids aléatoirement (ce qui peut mener à des optima locaux), l'Algorithme Génétique fournit une population de réseaux "pré-adaptés" avant le début de l'apprentissage par renforcement, aidant l'agent à démarrer dans une région prometteuse.

            -> Composants de l'Algorithme Génétique: 
                    -Individu (Chromosome) : Un individu est une structure de données contenant tous les gènes à optimiser
                    -Fonction de Fitness (Performance) : La fonction de fitness est la performance moyenne de l'agent DQN après un nombre fixe d'époques d'entraînement

            ->Processus Génétique :
            -Initialisation -Évaluation- Sélection- Croisement -Mutation -Répétition jusqu'à convergence.

            -> Gestion du Compromis Temps d’Apprentissage / Performance:
                -Entraînement Partiel pour la Fitness:  L'agent DQN n'est entraîné que pour un petit nombre fixe d'étapes par évaluation génétique.
                   Gain de temps : Réduit considérablement le temps d'évaluation de la fitness, permettant à l'Algorithme Génétique de tester plus de combinaisons génétiques
                -"Warm Start" avec Neuroévolution:
                   Gain de performance: Même si le temps d'entraînement dans la Boucle Intérieure reste le même, l'agent commence déjà avec une politique semi-optimale, réduisant les étapes nécessaires pour atteindre l'optimum.
                -Arrêt Précoce (Early Stopping): Si la performance d'un agent généré par l'Algorithme Génétique plafonne rapidement pendant l'entraînement, l'évaluation de sa Fitness est interrompue prématurément.
                  Gain de temps : Évite de gaspiller des ressources sur des combinaisons d'hyperparamètres clairement inefficaces.