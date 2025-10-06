
import spacy
from rake_nltk import Rake
import nltk
from nltk.corpus import wordnet as wn
from rapidfuzz import fuzz


nlp = spacy.load("en_core_web_sm")
rake = Rake()

def preprocess_text(text: str) -> str:
    return text.strip()

def extract_verbs(text: str):
    doc = nlp(text)
    verbs = []
    for token in doc:
        if token.pos_ == "VERB" and token.is_alpha:
            v = token.lemma_.lower()
            if v not in verbs:
                verbs.append(v)
    return verbs

def extract_keywords(text: str, max_phrases: int = 6):
    rake.extract_keywords_from_text(text)
    phrases = rake.get_ranked_phrases()[:max_phrases]
    return phrases

def expand_verb_synonyms(verbs):
    syns = set()
    for v in verbs:
        syns.add(v)
        for syn in wn.synsets(v, pos=wn.VERB):
            for lemma in syn.lemmas():
                syns.add(lemma.name().replace("_", " ").lower())
    return syns

def analyze_text(text: str):
    t = preprocess_text(text)
    doc = nlp(t)
    verbs = extract_verbs(t)
    verbs_expanded = list(expand_verb_synonyms(verbs))
    keywords = extract_keywords(t)
    entities = [ent.text for ent in doc.ents]
    return {
        "text": t,
        "verbs": verbs,
        "verbs_expanded": verbs_expanded,
        "keywords": keywords,
        "entities": entities
    }

# Intent seeds
INTENT_SEED = {
    "DOWNLOAD_FILE": ["download", "save", "fetch"],
    "PLAY_MUSIC": ["play", "listen"],
    "STOP_PLAYBACK": ["stop", "pause", "halt"],
    "OPEN_FILE": ["open", "launch"],
    "SEARCH": ["search", "find", "look"],
    "EXIT_APP": ["exit", "quit", "close"]
}

INTENT_TRIGGERS = {}
for intent, seeds in INTENT_SEED.items():
    triggers = set()
    for s in seeds:
        triggers.add(s)
        for syn in wn.synsets(s, pos=wn.VERB):
            for lemma in syn.lemmas():
                triggers.add(lemma.name().replace("_", " ").lower())
    INTENT_TRIGGERS[intent] = triggers

def detect_intent(analysis, fuzzy_threshold=88):
    verbs = set(analysis.get("verbs", []))
    keywords = analysis.get("keywords", [])
    keyword_tokens = set()
    for phrase in keywords:
        for w in phrase.lower().split():
            keyword_tokens.add(w)
    all_tokens = verbs.union(keyword_tokens)

    
    for intent, triggers in INTENT_TRIGGERS.items():
        if verbs.intersection(triggers):
            return intent
        if all_tokens.intersection(triggers):
            return intent


    for token in all_tokens:
        for intent, triggers in INTENT_TRIGGERS.items():
            for trig in triggers:
                if fuzz.partial_ratio(token, trig) >= fuzzy_threshold:
                    return intent
    return "UNKNOWN"

def handle_intent(intent, analysis):
    if intent == "DOWNLOAD_FILE":
        print("ACTION → trigger download routine")
    elif intent == "PLAY_MUSIC":
        print("ACTION → trigger play / media routine")
    elif intent == "STOP_PLAYBACK":
        print("ACTION → trigger stop / pause routine")
    elif intent == "OPEN_FILE":
        print("ACTION → trigger open file routine")
    elif intent == "SEARCH":
        print("ACTION → trigger search routine (web/local)")
    elif intent == "EXIT_APP":
        print("ACTION → graceful shutdown / exit")
    else:
        print("ACTION → no matched intent (user might have said something else)")
