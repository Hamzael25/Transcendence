# TRANSCENDENCE – Pong Project

Bienvenue dans **TRANSCENDENCE**, un remake du classique *Pong* conçu pour le cursus 42. Ce dépôt contient tout le nécessaire pour lancer l’application localement à l’aide de **Docker Compose** et d’un simple `Makefile`. Suivez le guide ci‑dessous pour cloner, démarrer et tester le projet en quelques commandes !

---

## 🚀 Aperçu

> *« Un Pong… mais en mieux ! Tournois locaux, parties en ligne, profil personnalisable et interface multilingue. Jouez, défiez vos amis et amusez‑vous. »*

---

## 📦 Prérequis

| Outil | Version recommandée |
|-------|---------------------|
| Docker | ≥ 24.x |
| Docker Compose | ≥ 2.x (inclus dans Docker Desktop) |
| GNU Make | ≥ 4.x |

*Assurez‑vous que les commandes `docker`, `docker compose` et `make` sont disponibles dans votre terminal.*

---

## ⚡ Installation & démarrage rapide

### 1) Cloner le dépôt et se placer dans le dossier du projet
```bash
git clone https://github.com/Hamzael25/Transcendence.git
cd Transcendence/pong_project
```

### 2) Préparer le fichier d’environnement (Obligatoire)
Copier le modèle puis l’éditer :
```bash
cp .env.example .env
```

Générer une **SECRET_KEY** aléatoire :
```bash
openssl rand -hex 32
```
> *Astuce Windows :* sans `openssl`, exécutez :
> ```powershell
> powershell -Command "-join ((48..57)+(97..102) | Get-Random -Count 64 | % {[char]$_})"
> ```

Ouvrez le fichier `.env` puis :
- Collez la chaîne obtenue après `SECRET_KEY=`.
- **Définissez également un mot de passe pour `POSTGRES_PASSWORD=` (valeur obligatoire ; le conteneur Postgres refusera de démarrer si elle est vide).**


### 3) Construire et lancer les conteneurs
```bash
make up
```

### 4) Ouvrir l’application
Tapez dans votre naviguateur :
```
https://localhost:8443
```
> Le certificat TLS est auto‑signé ; acceptez l’avertissement de sécurité si besoin.

---

## 🛠️ Commandes Makefile essentielles

Toutes les commandes ci‑dessous sont à exécuter depuis le dossier **pong_project/** ; elles sont **copiables‑collables** telles quelles.

| Action | Commande | Description |
|--------|----------|-------------|
| Démarrer / mettre à jour | ```make up``` | Construit (si besoin) et démarre les conteneurs en arrière‑plan. |
| Stopper | ```make stop``` | Met en pause les conteneurs sans les supprimer. |
| Arrêter & supprimer | ```make down``` | Stop + suppression des conteneurs et du réseau. |
| Nettoyer (volumes + orphelins) | ```make clean``` | Libère **tous** les volumes liés et les conteneurs orphelins. |
| Rebuild images | ```make build``` | Force la reconstruction des images Docker. |
| Prune | ```make prune``` | Supprime images/volumes/réseaux inutilisés (⚠ opération globale). |
| Shell PostgreSQL | ```make db-shell``` | Ouvre `psql` dans le conteneur DB (`\dt;` pour lister les tables). |
| Reset complet | ```make reset``` | `clean` → `build` → `up` en une seule commande. |
| Redémarrage rapide | ```make re``` | Down (avec volumes) puis Up + build. |

---

## 🕹️ Premiers pas dans le jeu

1. **Créer un compte** 🗝️  
   • Mot de passe : minimum 8 caractères et doit contenir au moins une lettre et un chiffre.
   • Optionnel : une fois votre compte créé, activez la double authentification (2FA) depuis votre profil (Google Authenticator, Authy, etc.) pour renforcer la sécurité.
2. **Partie locale** 🎮 / **Tournoi local** 🏆
   • Joueur gauche : **W / S**.  
   • Joueur droit : **Flèche ↑ / Flèche ↓**.
3. **Partie en ligne** 🌍  
   • Ajoutez d’abord votre ami depuis le menu en haut à droite.  
   • Chaque joueur se connecte sur son propre appareil / compte.  
   • Contrôles par défaut : **Flèches**.
4. **Obstacles & Bonus** 🚧✨  
   • Pensez à les activer dans le menu de jeu pour pimenter vos parties.
5. **Personnalisation** 🎨  
   • Depuis votre **Profil**, changez la langue, l’avatar, le nom d’utilisateur..
6. Enfin… **Amusez‑vous !**

---

| 🌐 Technologie |
|-------------|
| Django|
| Django Channels|
| Uvicorn|
| Redis|
| PostgreSQL|
| Nginx|
| Docker Compose|
| PyOTP (TOTP 2FA) |

---

🙏 Remerciements

Projet réalisé dans le cadre du cursus 42. Un immense merci à nos camarades, mentors et testeurs dont les retours ont permis d’affiner chaque détail du jeu. 🎉







