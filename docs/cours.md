CI / TBD :

Objectif :
Intégrer en continue dans le trunk (branch commune = main) avec le plus de sécurité possible. Rendre
la branche main déployable

Risques : 
failles de sécurité (code + dépendances)
code qui se compile pas
code avec mauvais formatage
bugs sur les fonctionnalités
qualité = convention du projet / de dev (archi / maintenabilité / code mort…)
infra qui se build pas (image docker)
ralentissement

Jobs pour détecter les risques :
tests automatisés (unitaires, intégration, e2e, secu, charge etc etc)
build
lint
sonarqube / check IA générative


Etapes : 

push main
jobs se lancent :
— CI OK : branch main clean donc déployable
— CI PAS OK : branch main pas clean donc non déployable 

Outils : 
Circle CI
GitHub Action
Jenkins
Fait maison
Husky (pour des check locaux)


CD : Déploiement continue (Delivery continue) 

Objectif :
Déployer en continue le trunk sur la prod (env de test, staging etc) = le avec le plus de sécurité possible.

Risques : 
failles de sécurité (code + dépendances)
code qui se compile pas
code avec mauvais formatage
bugs sur les fonctionnalités
qualité = convention du projet / de dev (archi / maintenabilité / code mort…)
infra qui se build pas (image docker)
ralentissement

Jobs pour détecter les risques :
tests automatisés (unitaires, intégration, e2e, secu, charge etc etc)
test idéalement à faire avec les données de prod, infra iso prod
build
déploiement des images docker

Etapes : 

Met un tag (versionnage sémantique : vx.x.x) et déploie un tag.

(Correctifs  : incremente le v0.0.X
Version mineur : incrémente le v0.X.0
Version majeure : incrémente le vX.0.0 )

sur les serveurs de prod / test : .env du serveur (VERSION=v1.2.3)
push le tag
run les jobs, et si OK :
déploiement de la version fait automatiquement

Outils : 
Circle CI
GitHub Action
Jenkins