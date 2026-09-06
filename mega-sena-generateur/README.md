# Générateur de grilles Mega-Sena

Petit projet Python qui récupère les **20 derniers concours** de la Mega-Sena,
calcule la fréquence des numéros et génère des grilles pondérées à partir de ces
fréquences.

Ce projet a été créé pour pratiquer :

- la consommation d'une API REST avec `requests` ;
- la gestion des erreurs réseau et la validation des données ;
- la manipulation de listes, ensembles et dictionnaires ;
- l'organisation et la documentation d'un petit projet Python.

> **Remarque :** tous les numéros ont la même probabilité lors d'un nouveau
> tirage. Les fréquences passées ne permettent pas de prédire les résultats.

## Prérequis

- Python 3.10 ou version ultérieure
- une connexion Internet

## Installation

```bash
git clone https://github.com/michelspead-ai/uninter.ads.git
cd uninter.ads/mega-sena-generateur
python -m venv .venv
```

Sous Windows :

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Sous macOS ou Linux :

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

Le programme affiche la fréquence des numéros, demande combien de grilles
générer, puis présente les résultats dans le terminal.

## Tests

```bash
python -m unittest discover -s tests
```

## Structure

```text
mega-sena-generateur/
├── main.py
├── requirements.txt
├── tests/
│   └── test_main.py
├── .gitignore
└── README.md
```

## Licence

Projet éducatif. Vous pouvez l'étudier, le modifier et le partager.

## Source des données

Les résultats sont consultés sur le service public du portail des loteries de
la Caixa Econômica Federal. La disponibilité du programme dépend de ce service.

