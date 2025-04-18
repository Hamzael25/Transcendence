PROJECT_NAME = pong_project

COMPOSE_FILE = docker-compose.yml

.PHONY: up
up:
	@echo "Démarrage des conteneurs..."
	@docker compose -f $(COMPOSE_FILE) up -d --build

.PHONY: stop
stop:
	@echo "Arrêt des conteneurs..."
	@docker compose -f $(COMPOSE_FILE) stop

.PHONY: down
down:
	@echo "Arrêt et suppression des conteneurs..."
	@docker compose -f $(COMPOSE_FILE) down

.PHONY: clean
clean:
	@echo "Nettoyage des conteneurs, volumes et orphelins..."
	@docker compose -f $(COMPOSE_FILE) down --volumes --remove-orphans

.PHONY: build
build:
	@echo "Reconstruction des images..."
	@docker compose -f $(COMPOSE_FILE) build

.PHONY: prune
prune:
	@echo "Suppression des données inutilisées..."
	@docker system prune --all --force
	@docker volume prune --force
	@docker network prune --force


.PHONY: db-shell
db-shell:
	@echo "Visualiser les tables avec : \dt;"
	@echo "Montrer la tables des utilisateurs avec : SELECT * FROM accounts_customuser"
	@docker compose -f $(COMPOSE_FILE) exec db psql -U postgres -d pong_db

.PHONY: reset
reset: clean build up
	@echo "Containers et volumes supprimés, images reconstruites, environnement prêt !"

.PHONY: re
re:
	@echo "Redémarrage complet des conteneurs..."
	@docker compose -f $(COMPOSE_FILE) down --volumes --remove-orphans
	@docker compose -f $(COMPOSE_FILE) up --build -d
