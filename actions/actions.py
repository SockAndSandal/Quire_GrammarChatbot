from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
# from rasa_sdk.forms import FormAction

from actions import config

import requests
import random

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionMeaning(Action):
    def name(self) -> Text:
        return "action_meaning"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot("vocab_word"))
        url = "https://wordsapiv1.p.rapidapi.com/words/{}/definitions"
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': config.api_key
            }
        response = requests.request("GET", url.format(word), headers=headers)
        data = response.json()
        try:
            meaning = data["definitions"][0]["definition"]
            part_of_speech = data["definitions"][0]["partOfSpeech"]
        except:
            meaning = "Sorry, I don't know the meaning of this word"
        dispatcher.utter_message(text="{}({}): {}".format(word,part_of_speech, meaning))
        # dispatcher.utter_message(text="it's a word.")
        return []

class ActionNext(Action):
    def name(self) -> Text:
        return "action_next"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot("vocab_word"))
        url = "https://wordsapiv1.p.rapidapi.com/words/{}/definitions"
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': config.api_key
            }
        response = requests.request("GET", url.format(word), headers=headers)
        data = response.json()
        try:
            if(len(data['definitions'])<2):
                meaning = "Sorry, there's no other meanings to this word."
                dispatcher.utter_message(text={}.format(meaning))
            else:
                rl = random.choice(data["definitions"])
                meaning = rl["definition"]
                part_of_speech = rl["partOfSpeech"]
                dispatcher.utter_message(text="{}({}): {}".format(word,part_of_speech, meaning))
        except:
            meaning = "Sorry, I don't know the meaning of this word"
            dispatcher.utter_message(text={}.format(meaning))
        return []


class ActionRhyming(Action):
    def name(self) -> Text:
        return "action_rhyming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot("rhyme_word"))
        url = "https://wordsapiv1.p.rapidapi.com/words/{}/rhymes"

        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': config.api_key
        }
        response = requests.request("GET", url.format(word), headers=headers)
        data = response.json()
        rl= []
        for i in data['rhymes']['all']:
            if ' ' not in i:
                rl.append(i)
        try:
            if(len(rl)>2):
                dispatcher.utter_message(text="{} rhymes with {}, {}, and {}".format(word, random.choice(rl),random.choice(rl), random.choice(rl)))
            elif(len(rl)==2):
                dispatcher.utter_message(text="{} rhymes with {}".format(word, rl[1]))
            else:
                dispatcher.utter_message(text="Sorry, I don't know anything that rhymes with this word")
        except:
            dispatcher.utter_message(text="Sorry, I don't know anything that rhymes with this word")
        return []


class ActionSynonym(Action):
    def name(self) -> Text:
        return "action_synonym"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot("synonym_word"))
        url = "https://wordsapiv1.p.rapidapi.com/words/{}/synonyms"
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': config.api_key
        }
        response = requests.request("GET", url.format(word), headers=headers)
        data = response.json()
        rl = list(data["synonyms"])
        dispatcher.utter_message(text="{} - {}".format(word, rl))
        return []

class ActionAntonym(Action):
    def name(self) -> Text:
        return "action_antonym"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot("opposite_word"))
        url = "https://wordsapiv1.p.rapidapi.com/words/{}/antonyms"
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': config.api_key
        }
        response = requests.request("GET", url.format(word), headers=headers)
        data = response.json()
        dispatcher.utter_message(text="{} x {}".format(word, str(data["antonyms"][0])))

class ActionUseInSentence(Action):
    def name(self) -> Text:
        return "action_use_in_sentence"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot("example_word"))
        url = "https://wordsapiv1.p.rapidapi.com/words/{}/examples"
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': config.api_key
        }
        response = requests.request("GET", url.format(word), headers=headers)
        data = response.json()
        rl = data['examples']
        try:
            dispatcher.utter_message(text="{}".format(random.choice(rl)))
        except:
            dispatcher.utter_message(text="Sorry, I don't know how to use this in a sentence either.")
        return []