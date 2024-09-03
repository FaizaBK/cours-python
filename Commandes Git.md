# Git & Github

## <u>Les commandes les plus utilisé</u>

### Travail seul

- git pull
- git status
- git add <modifications_apportées>
- git commit -m "<message_de_commit>"
- git push

### Travail en équipe

- git branch
- git checkout
- git merge

Mention honorable pour le `.gitignore`

## <u>Les Commandes Basiques de Git</u>

Git est un système de contrôle de version largement utilisé pour le suivi des modifications de code source et la collaboration sur des projets de développement logiciel. Voici un cours sur les commandes basiques de Git pour vous aider à démarrer.

### 1. Configuration de Git

Avant d'utiliser Git, vous devez configurer votre nom d'utilisateur et votre adresse e-mail. Vous pouvez le faire avec les commandes suivantes :

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre@email.com"
```

### 2. Initialisation d'un Répertoire Git

Pour commencer à utiliser Git dans un projet, initialisez un répertoire Git en utilisant la commande suivante :

```bash
git init
```

### 3. Clonage d'un Dépôt Existants

Si vous souhaitez travailler sur un projet existant, vous pouvez le cloner avec la commande `git clone` :

```bash
git clone <URL_du_dépôt>
```

### 4. Cycle de Vie des Fichiers dans Git

- Untracked (Non Suivi) : Les fichiers non suivis par Git.
- Staged (Indexés) : Les fichiers prêts à être inclus dans le prochain commit.
- Committed (Committés) : Les fichiers qui ont été sauvegardés dans l'historique du projet.

### 5. Commandes de Base

- git status : Affiche l'état des fichiers dans votre répertoire de travail.
- git add : Ajoute des fichiers à la zone de staging.
- git commit : Crée un instantané (commit) des fichiers en staged.
- git log : Affiche l'historique des commits.
- git diff : Montre les modifications entre le répertoire de travail et le dernier commit.

### 6. Branches

- git branch : Affiche la liste des branches et indique la branche actuelle.
- git branch <nom_de_branche> : Crée une nouvelle branche.
- git checkout <nom_de_branche> : Passe à une autre branche.
- git checkout -b <nom_de_branche> : Crée une nouvelle branche et se déplace dessus.
- git merge <nom_de_branche> : Fusionne une branche dans la branche actuelle.

### 7. Récupération et Envoi (Pull & Push)

- git pull : Récupère les modifications depuis un dépôt distant et les fusionne dans votre branche locale.
- git push : Envoie vos commits vers un dépôt distant.

### 8. Collaboration avec des Dépôts Distants

- git remote -v : Affiche les dépôts distants associés à votre projet.
- git remote add <nom_dépôt> <URL_du_dépôt> : Ajoute un dépôt distant.
- git fetch <nom_dépôt> : Récupère des informations depuis un dépôt distant.
- git pull <nom_dépôt><nom_branche> : Récupère et fusionne les modifications depuis un dépôt distant.

### 9. Ignorer des Fichiers

Créez un fichier nommé `.gitignore` pour spécifier les fichiers que vous ne souhaitez pas suivre avec Git.

### 10. Résumé des Étapes Courantes

- Créez ou modifiez des fichiers.
- Utilisez `git add` pour les mettre en staging.
- Utilisez `git commit` pour les enregistrer dans un commit.
- Utilisez `git push` pour envoyer vos commits vers un dépôt distant.
