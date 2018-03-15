import requests
import json
from pprint import pprint


def APICall(word):

    app_id = '3280b8a3'
    app_key = '3b9f39addc6eae7a06787dc32be7a00a'

    language = 'en'
    word_id = word

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

    dictionary = r.json()
    results = dictionary.get("results")
    lexicalEntries = results[0]["lexicalEntries"]
    entries = lexicalEntries[0]["entries"]
    senses = entries[0]["senses"]
    defintions = senses[0]["definitions"]
    return defintions[0]
