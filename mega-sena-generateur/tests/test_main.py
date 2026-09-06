import unittest
from collections import Counter

from main import calculer_frequences, extraire_numeros, generer_grille


class TestMegaSena(unittest.TestCase):
    def test_extraire_numeros(self):
        self.assertEqual(
            extraire_numeros({"listaDezenas": ["01", "12", "23", "34", "45", "60"]}),
            [1, 12, 23, 34, 45, 60],
        )

    def test_calculer_frequences(self):
        self.assertEqual(calculer_frequences([[1, 2, 3], [2, 3, 4]]), Counter({2: 2, 3: 2, 1: 1, 4: 1}))

    def test_generer_grille(self):
        grille = generer_grille(Counter({10: 5, 20: 3}))
        self.assertEqual(len(grille), 6)
        self.assertEqual(len(set(grille)), 6)
        self.assertTrue(all(1 <= numero <= 60 for numero in grille))


if __name__ == "__main__":
    unittest.main()

