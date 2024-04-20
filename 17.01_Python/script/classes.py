from typing import List, Optional

class Categorie:
    def __init__(self, categories: List[str]):
        self.categories = categories

class ScoresLisibilite:
    def __init__(self, flesch_kincaid_grade_level: float, flesch_reading_ease: float, gunning_fog_index: float,
                 coleman_liau_index: float, dale_chall_readability_score: float, automated_readability_index: float,
                 linsear_write_formula: float, smog: float, spache_readability_score: float):
        self.flesch_kincaid_grade_level = flesch_kincaid_grade_level
        self.flesch_reading_ease = flesch_reading_ease
        self.gunning_fog_index = gunning_fog_index
        self.coleman_liau_index = coleman_liau_index
        self.dale_chall_readability_score = dale_chall_readability_score
        self.automated_readability_index = automated_readability_index
        self.linsear_write_formula = linsear_write_formula
        self.smog = smog
        self.spache_readability_score = spache_readability_score

class Article:
    def __init__(self, id: int, texte: str, categorie: Categorie, date: str, is_historical: bool,
                 source: str, upvotes: Optional[int], date_num: int, longueur_texte: int, nombre_mots: int,
                 longueur_phrase: float, scores_lisibilite: ScoresLisibilite):
        self.id = id
        self.texte = texte
        self.categorie = categorie
        self.date = date
        self.is_historical = is_historical
        self.source = source
        self.upvotes = upvotes  # Peut être None
        self.date_num = date_num
        self.longueur_texte = longueur_texte
        self.nombre_mots = nombre_mots
        self.longueur_phrase = longueur_phrase
        self.scores_lisibilite = scores_lisibilite

# Exemple d'utilisation

categories = Categorie(['Nature', 'Reality', 'Videos', 'Killahawke1'])
scores = ScoresLisibilite(14.85, 11.41, 72.46, 9.33, 6.74, 7.85, 5.65, 7.94, 10.16)
article = Article(4, "Texte de l'article ici", categories, "2015-10-07", False, "fandom", None, 1886, 5208, 915, 12.83, scores)

print(article.texte)
print(article.categorie.categories)
print(article.scores_lisibilite.flesch_reading_ease)
