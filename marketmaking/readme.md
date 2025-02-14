# Super Simulateur de Market Making

Un jeu interactif pour s'entraîner au métier de **Market Maker** (teneur de marché). Ce projet simule un marché financier où vous pouvez jouer le rôle d'un market maker ou d'un participant au marché. L'objectif est de comprendre les mécanismes de la liquidité, des spreads, et de la gestion des risques.

## Fonctionnalités
- **Market Maker** : Fixez le prix médian et le spread pour générer des offres et des demandes.
- **Participant au Marché** : Achetez ou vendez des actifs en fonction des prix proposés.
- **Simulation en temps réel** : Visualisez les résultats de vos décisions avec un graphique de P/L (Profit et Perte).
- **Dés cachés** : Un mécanisme de dés simule l'incertitude du marché.

## Technologies Utilisées
- **Python** : Backend pour la logique du marché.
- **Flask** : Framework web pour l'interface utilisateur.
- **Chart.js** : Visualisation des données en temps réel.
- **HTML/CSS** : Interface utilisateur responsive.








Ce simulateur vous permet de jouer à un jeu de simulation de Market Making, où vous pouvez interagir en tant que **Market Maker** ou **Participant au Marché**. Le but du jeu est de gérer des offres et des demandes de prix, tout en calculant les profits et les pertes associés à vos actions de trading.

## Prérequis

1. Un navigateur web récent (Chrome, Firefox, Safari, etc.).
2. Une connexion Internet (pour charger les codes et bibliothèques externes).
   
## Lancement du jeu

1. Ouvrez le fichier HTML dans votre navigateur.
2. Vous verrez deux rôles disponibles :
   - **Market Maker**
   - **Participant au Marché**

Choisissez un rôle en cliquant sur l'un des boutons correspondants.

### Rôle de Market Maker

1. Lorsque vous sélectionnez **Market Maker**, vous devez définir un **prix médian** et un **spread**. 
   - **Prix médian** : le prix moyen auquel vous êtes prêt à acheter et vendre.
   - **Spread** : l'écart entre le prix d'achat (bid) et le prix de vente (offer).
2. Cliquez sur le bouton "Soumettre le Marché" pour définir votre marché.
3. Le jeu génère automatiquement les prix **bid** (achat) et **offer** (vente) en fonction de vos paramètres.
4. Vous pouvez visualiser l'évolution du profit et de la perte cumulés (P/L) à travers le graphique.
5. Le résultat du marché sera calculé et affiché, y compris :
   - **Spread collecté** (revenu tiré du spread)
   - **P/L réalisé** (profit ou perte basé sur les transactions effectuées)

### Rôle de Participant au Marché

1. Lorsque vous sélectionnez **Participant au Marché**, vous pouvez choisir de **acheter** ou de **vendre** à l'un des prix affichés (bid ou offer).
2. Entrez la **quantité** que vous souhaitez acheter ou vendre, puis cliquez sur le bouton correspondant (acheter ou vendre).
3. Le jeu affiche alors une transaction confirmée, et le résultat (P/L) est calculé en fonction du prix auquel vous avez effectué l'achat ou la vente.
4. Vous pouvez visualiser l'évolution de vos profits ou pertes sur le graphique.

### Progression du jeu

1. Les **dés** (représentés par trois dés) sont lancés à chaque cycle de marché pour générer une "réalisation", un score qui influencera les résultats des transactions.
2. Une **barre de progression** vous indique le temps restant avant la fin du cycle et le calcul des résultats.
3. Une fois le cycle terminé, vous pouvez prendre de nouvelles décisions et observer l'évolution de votre solde.

### Graphique de P/L

Le graphique en haut de la page affiche les **profits et pertes cumulés** pour chaque trade effectué. À chaque transaction, le jeu ajoute une nouvelle donnée au graphique pour suivre vos performances sur le long terme.

### Informations supplémentaires

- Vous pouvez réinitialiser le jeu en actualisant la page de votre navigateur.
- Le jeu utilise des calculs de "spread" et "réalisation" pour déterminer les profits et pertes en fonction des décisions prises par chaque joueur.

## Aide supplémentaire

- Si vous avez des questions ou souhaitez proposer des améliorations, n'hésitez pas à ouvrir un "issue" sur ce dépôt GitHub.

## Licences

Le code est sous licence MIT. Vous pouvez l'utiliser librement à des fins personnelles et éducatives.
