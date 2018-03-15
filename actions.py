from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import requests
import json
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from api_call import APICall


class ActionSearch(Action):

    def name(self):
        return 'utter_meaning'

    def run(self, dispatcher, tracker, domain):
        word = str(tracker.get_slot('word'))
        response = APICall(word)
        dispatcher.utter_message(response)
        return [SlotSet('word', word)]
