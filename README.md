# Task Tracker CLI

Task Tracker CLI est une application en ligne de commande développée en Python permettant de gérer une liste de tâches directement depuis le terminal.

L'application permet d'ajouter, modifier, supprimer et suivre l'état des tâches. Les données sont stockées localement dans un fichier JSON.

---

## 📌 Fonctionnalités

L'application permet de :

- ✅ Ajouter une tâche
- ✅ Modifier une tâche
- ✅ Supprimer une tâche
- ✅ Marquer une tâche comme `in-progress`
- ✅ Marquer une tâche comme `done`
- ✅ Afficher toutes les tâches
- ✅ Afficher uniquement les tâches `todo`
- ✅ Afficher uniquement les tâches `in-progress`
- ✅ Afficher uniquement les tâches `done`
- ✅ Générer automatiquement des identifiants uniques
- ✅ Enregistrer la date de création et de modification
- ✅ Stocker les données dans un fichier JSON
- ✅ Gérer plusieurs erreurs utilisateur

---

## 🛠️ Technologies utilisées

Le projet utilise uniquement les fonctionnalités natives de Python.

### Langage

- Python 3

### Modules utilisés

- `sys` — récupération des arguments de la ligne de commande
- `json` — lecture et écriture des données JSON
- `os` — gestion du fichier `tasks.json`
- `datetime` — gestion des dates et heures

Aucune bibliothèque externe ou framework n'est nécessaire.

---

## 📁 Structure du projet

```text
task-tracker/
│
├── task-cli.py
├── tasks.json
└── README.md
```

### `task-cli.py`

Contient toute la logique de l'application :

- gestion des commandes
- ajout des tâches
- modification des tâches
- suppression des tâches
- changement de statut
- affichage des tâches
- gestion des erreurs

### `tasks.json`

Fichier utilisé pour stocker les tâches.

Le fichier est créé automatiquement lorsqu'une opération nécessitant une sauvegarde est effectuée.

### `README.md`

Documentation du projet et guide d'utilisation.

---

# 🚀 Installation

## 1. Vérifier que Python est installé

Dans un terminal :

```bash
python --version
```

Exemple :

```text
Python 3.12.0
```

Si Python est correctement installé, aucune installation supplémentaire n'est nécessaire.

---

## 2. Accéder au projet

Ouvrir un terminal dans le dossier du projet :

```bash
cd task-tracker
```

---

# 💻 Utilisation

La syntaxe générale est :

```bash
python task-cli.py <commande> [arguments]
```

---

# ➕ Ajouter une tâche

Pour ajouter une nouvelle tâche :

```bash
python task-cli.py add "Buy groceries"
```

Résultat :

```text
Task added successfully (ID: 1)
```

Une tâche créée possède automatiquement :

- un identifiant unique
- une description
- le statut `todo`
- une date de création
- une date de modification

Exemple dans `tasks.json` :

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-10-06T18:30:00",
    "updatedAt": "2026-10-06T18:30:00"
  }
]
```

---

# 📋 Afficher toutes les tâches

Commande :

```bash
python task-cli.py list
```

Exemple :

```text
ID: 1 | Buy groceries | todo
ID: 2 | Learn Python | in-progress
ID: 3 | Finish project | done
```

---

# 📝 Afficher les tâches `todo`

Pour afficher uniquement les tâches qui ne sont pas encore commencées :

```bash
python task-cli.py list todo
```

Exemple :

```text
ID: 1 | Buy groceries | todo
ID: 4 | Learn Git | todo
```

---

# 🔄 Afficher les tâches `in-progress`

Pour afficher uniquement les tâches en cours :

```bash
python task-cli.py list in-progress
```

Exemple :

```text
ID: 2 | Learn Python | in-progress
```

---

# ✅ Afficher les tâches terminées

Pour afficher uniquement les tâches terminées :

```bash
python task-cli.py list done
```

Exemple :

```text
ID: 3 | Finish project | done
```

---

# ✏️ Modifier une tâche

Pour modifier la description d'une tâche :

```bash
python task-cli.py update 1 "Buy groceries and cook dinner"
```

Résultat :

```text
Task updated successfully (ID: 1)
```

La description est modifiée et `updatedAt` est mis à jour.

Le champ `createdAt` reste inchangé.

---

# 🗑️ Supprimer une tâche

Pour supprimer une tâche :

```bash
python task-cli.py delete 1
```

Résultat :

```text
Task deleted successfully (ID: 1)
```

La tâche est définitivement supprimée du fichier `tasks.json`.

---

# 🔄 Marquer une tâche comme `in-progress`

Pour indiquer qu'une tâche est actuellement en cours :

```bash
python task-cli.py mark-in-progress 1
```

Résultat :

```text
Task marked as in-progress (ID: 1)
```

Le statut devient :

```text
in-progress
```

---

# ✅ Marquer une tâche comme `done`

Pour terminer une tâche :

```bash
python task-cli.py mark-done 1
```

Résultat :

```text
Task marked as done (ID: 1)
```

Le statut devient :

```text
done
```

---

# 📊 Statuts disponibles

Chaque tâche possède un statut parmi les trois suivants :

```text
todo
in-progress
done
```

### `todo`

La tâche vient d'être créée et n'est pas encore en cours.

### `in-progress`

La tâche est actuellement en cours.

### `done`

La tâche est terminée.

---

# 🗂️ Format des données

Chaque tâche est représentée par un objet JSON.

Exemple :

```json
{
  "id": 1,
  "description": "Learn Python",
  "status": "in-progress",
  "createdAt": "2026-10-06T18:30:00",
  "updatedAt": "2026-10-06T18:45:00"
}
```

## Description des champs

| Champ         | Description                            |
| ------------- | -------------------------------------- |
| `id`          | Identifiant unique de la tâche         |
| `description` | Description de la tâche                |
| `status`      | État actuel de la tâche                |
| `createdAt`   | Date et heure de création              |
| `updatedAt`   | Date et heure de dernière modification |

---

# 🆔 Gestion des identifiants

Chaque nouvelle tâche reçoit automatiquement un identifiant unique.

Par exemple :

```text
Task 1
Task 2
Task 3
```

Si la tâche `2` est supprimée :

```text
Task 1
Task 3
```

La prochaine tâche recevra :

```text
Task 4
```

L'application utilise l'identifiant maximal existant pour générer le prochain ID.

---

# ⚠️ Gestion des erreurs

L'application vérifie plusieurs situations incorrectes.

## Commande inconnue

```bash
python task-cli.py hello
```

Résultat :

```text
Error: unknown command 'hello'.
```

---

## Description manquante

```bash
python task-cli.py add
```

Résultat :

```text
Error: task description is required.
```

---

## Description vide

```bash
python task-cli.py add ""
```

Résultat :

```text
Error: task description cannot be empty.
```

---

## ID invalide

```bash
python task-cli.py delete abc
```

Résultat :

```text
Error: ID must be an integer.
```

---

## Tâche inexistante

```bash
python task-cli.py delete 999
```

Résultat :

```text
Error: task with ID 999 not found.
```

---

## Statut invalide

```bash
python task-cli.py list waiting
```

Résultat :

```text
Error: invalid status.
```

Les seuls statuts acceptés sont :

```text
todo
in-progress
done
```

---

# 🧪 Exemple d'utilisation complet

Voici un scénario complet d'utilisation.

## 1. Créer plusieurs tâches

```bash
python task-cli.py add "Learn Python"
```

```bash
python task-cli.py add "Learn Git"
```

```bash
python task-cli.py add "Build a project"
```

---

## 2. Afficher les tâches

```bash
python task-cli.py list
```

Résultat :

```text
ID: 1 | Learn Python | todo
ID: 2 | Learn Git | todo
ID: 3 | Build a project | todo
```

---

## 3. Commencer une tâche

```bash
python task-cli.py mark-in-progress 1
```

---

## 4. Vérifier les tâches en cours

```bash
python task-cli.py list in-progress
```

Résultat :

```text
ID: 1 | Learn Python | in-progress
```

---

## 5. Terminer la tâche

```bash
python task-cli.py mark-done 1
```

---

## 6. Vérifier les tâches terminées

```bash
python task-cli.py list done
```

Résultat :

```text
ID: 1 | Learn Python | done
```

---

## 7. Modifier une autre tâche

```bash
python task-cli.py update 2 "Learn Git and GitHub"
```

---

## 8. Supprimer une tâche

```bash
python task-cli.py delete 3
```

---

## 9. Afficher l'état final

```bash
python task-cli.py list
```

Résultat possible :

```text
ID: 1 | Learn Python | done
ID: 2 | Learn Git and GitHub | todo
```

---

# 🔍 Architecture de l'application

Le fonctionnement général de l'application est :

```text
                Utilisateur
                     │
                     ▼
             Ligne de commande
                     │
                     ▼
                 sys.argv
                     │
                     ▼
                  main()
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
      add         update        delete
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
               tasks.json
```

Pour les changements de statut :

```text
                 main()
                   │
          ┌────────┴────────┐
          ▼                 ▼
mark-in-progress       mark-done
          │                 │
          └────────┬────────┘
                   ▼
              tasks.json
```

Pour l'affichage :

```text
                 main()
                   │
                   ▼
                  list
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        todo  in-progress  done
                   │
                   ▼
              tasks.json
```

---

# 🧩 Fonctions principales

Le programme est organisé autour de plusieurs fonctions.

### `load_tasks()`

Charge les tâches depuis `tasks.json`.

```python
tasks = load_tasks()
```

### `save_tasks(tasks)`

Sauvegarde les tâches dans `tasks.json`.

```python
save_tasks(tasks)
```

### `add_task(description)`

Ajoute une nouvelle tâche.

### `list_tasks(status=None)`

Affiche toutes les tâches ou uniquement celles correspondant à un statut.

### `update_task(task_id, new_description)`

Modifie la description d'une tâche.

### `delete_task(task_id)`

Supprime une tâche.

### `mark_in_progress(task_id)`

Change le statut d'une tâche en :

```text
in-progress
```

### `mark_done(task_id)`

Change le statut d'une tâche en :

```text
done
```

### `main()`

Analyse les arguments de la ligne de commande et appelle la fonction appropriée.

---

# 📚 Concepts Python pratiqués

Ce projet permet de pratiquer plusieurs concepts fondamentaux de Python.

## Arguments de ligne de commande

```python
import sys

print(sys.argv)
```

## Fonctions

```python
def add_task(description):
    ...
```

## Listes

```python
tasks = []
```

## Boucles

```python
for task in tasks:
    ...
```

## Conditions

```python
if task["id"] == task_id:
    ...
```

## Dictionnaires

```python
task = {
    "id": 1,
    "description": "Learn Python",
    "status": "todo"
}
```

## Manipulation de fichiers

```python
with open(FILE_NAME, "r", encoding="utf-8") as file:
    ...
```

## JSON

```python
json.load(file)
```

et :

```python
json.dump(tasks, file)
```

## Gestion des exceptions

```python
try:
    ...
except ValueError:
    ...
```

## Date et heure

```python
datetime.now()
```

---

# 🔐 Dépendances

Le projet ne nécessite aucune bibliothèque externe.

Il utilise uniquement la bibliothèque standard Python :

```text
sys
json
os
datetime
```

---

# 📦 Données locales

Les tâches sont stockées localement dans :

```text
tasks.json
```

Aucune base de données externe n'est nécessaire.

Aucun serveur n'est nécessaire.

Aucune connexion Internet n'est nécessaire pour utiliser l'application.

---

# 🎯 Objectif du projet

Ce projet a pour objectif de pratiquer :

- la programmation Python
- les fonctions
- les structures de données
- la manipulation de fichiers
- le format JSON
- les arguments de ligne de commande
- la gestion des erreurs
- l'organisation d'une petite application

Il constitue également une première expérience dans la création d'une application CLI complète.

---

# 👨‍💻 Auteur

**Aziz Boukhayatia**

Projet réalisé dans le cadre d'un exercice de développement d'une application CLI en Python.

---

# 📄 Licence

Ce projet est un projet éducatif et peut être utilisé librement à des fins d'apprentissage.
