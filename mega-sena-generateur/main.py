"""Analyse les 20 derniers tirages de la Mega-Sena et génère des grilles."""

from __future__ import annotations

import random
import time
from collections import Counter

import requests


URL_API = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"
NOMBRE_TIRAGES = 20
DELAI_ENTRE_REQUETES = 0.2
DELAI_REQUETE = 15


def recuperer_tirage(numero: int | None = None) -> dict:
    """Récupère un tirage précis, ou le plus récent si le numéro est absent."""
    url = URL_API if numero is None else f"{URL_API}/{numero}"
    reponse = requests.get(
        url,
        headers={"Accept": "application/json", "User-Agent": "mega-sena-generateur/1.0"},
        timeout=DELAI_REQUETE,
    )
    reponse.raise_for_status()
    return reponse.json()


def extraire_numeros(tirage: dict) -> list[int]:
    """Convertit les numéros reçus de l'API en entiers."""
    numeros = tirage.get("listaDezenas", [])
    if len(numeros) != 6:
        raise ValueError("Le tirage reçu ne contient pas six numéros.")
    return [int(numero) for numero in numeros]


def recuperer_derniers_tirages(nombre: int = NOMBRE_TIRAGES) -> list[list[int]]:
    """Télécharge les derniers tirages, du plus récent au plus ancien."""
    dernier = recuperer_tirage()
    dernier_numero = int(dernier["numero"])
    tirages = [extraire_numeros(dernier)]

    for numero in range(dernier_numero - 1, dernier_numero - nombre, -1):
        try:
            tirages.append(extraire_numeros(recuperer_tirage(numero)))
        except (requests.RequestException, ValueError, KeyError) as erreur:
            print(f"Avertissement : concours {numero} ignoré ({erreur}).")
        time.sleep(DELAI_ENTRE_REQUETES)

    return tirages


def calculer_frequences(tirages: list[list[int]]) -> Counter[int]:
    """Compte la fréquence de chaque numéro dans les tirages."""
    return Counter(numero for tirage in tirages for numero in tirage)


def generer_grille(frequences: Counter[int]) -> list[int]:
    """Génère six numéros distincts, pondérés par leur fréquence observée."""
    population = list(range(1, 61))
    poids = [frequences.get(numero, 0) + 1 for numero in population]
    grille: set[int] = set()

    while len(grille) < 6:
        grille.add(random.choices(population, weights=poids, k=1)[0])

    return sorted(grille)


def demander_nombre_grilles() -> int:
    """Demande un nombre positif de grilles à l'utilisateur."""
    while True:
        try:
            nombre = int(input("Combien de grilles voulez-vous générer ? "))
            if nombre > 0:
                return nombre
        except ValueError:
            pass
        print("Veuillez saisir un nombre entier supérieur à zéro.")


def main() -> None:
    print(f"Récupération des {NOMBRE_TIRAGES} derniers concours…")
    try:
        tirages = recuperer_derniers_tirages()
    except (requests.RequestException, ValueError, KeyError) as erreur:
        raise SystemExit(f"Impossible de récupérer les tirages : {erreur}") from erreur

    frequences = calculer_frequences(tirages)
    print(f"\n{len(tirages)} concours obtenus.")
    print("\nFréquence des numéros :")
    for numero in range(1, 61):
        print(f"{numero:02d} : {frequences.get(numero, 0):2d}")

    nombre_grilles = demander_nombre_grilles()
    print("\nGrilles générées :")
    for index in range(1, nombre_grilles + 1):
        numeros = " ".join(f"{numero:02d}" for numero in generer_grille(frequences))
        print(f"Grille {index:02d} : {numeros}")

    print("\nCes grilles sont générées à titre éducatif et ne prédisent pas les résultats.")


if __name__ == "__main__":
    main()

