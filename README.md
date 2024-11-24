# Curl-BreakingTech

![Capture d’écran 2024-08-19 à 09 19 09](https://github.com/user-attachments/assets/0a05faea-b578-43cc-a479-8f67668b586b)

Ce script Python permet d'analyser les redirections d'une URL donnée en utilisant curl. Il affiche le statut HTTP initial de l'URL ainsi que toutes les redirections rencontrées jusqu'à l'URL finale. Les codes de statut HTTP sont affichés avec des couleurs pour une meilleure lisibilité.

# Fonctionnalités :
Affiche le statut HTTP de l'URL initiale.
Suit les redirections et affiche chaque URL intermédiaire avec son code de statut.
Affiche l'URL finale et son code de statut.
Utilise des couleurs pour différencier les codes de statut :
Vert pour les codes 2xx (succès)
Jaune pour les codes 3xx (redirections)
Rouge pour les codes 4xx (erreurs client)
Magenta pour les codes 5xx (erreurs serveur)
Bleu pour les autres cas

# Utilisation :
- Copier les fichiers sources
```shell
git clone https://github.com/BreakingTechFr/Curl-BreakingTech.git
```
-Allez deans le repertoire curl : 
```shell
cd Curl-BreakingTech
```
- Lancez le fichier curl.py en utilisant la commande :
```shell
python curl.py
```
# Exemple : 
Entrez l'URL que vous souhaitez tester (http ou https) : https://exemple.com
Statut de l'URL de base (https://exemple.com) : 301
Liste des redirections :
Redirection 1 : URL = https://www.exemple.com, Statut HTTP = 302
Redirection 2 : URL finale : https://www.exemple.com, Statut HTTP = 200

## Suivez-nous

- [@breakingtechfr](https://twitter.com/BreakingTechFR) sur Twitter.
- [Facebook](https://www.facebook.com/BreakingTechFr/) likez notre page.
- [Instagram](https://www.instagram.com/breakingtechfr/) taguez nous sur vos publications !
- [Discord](https://discord.gg/VYNVBhk) pour parler avec nous !
