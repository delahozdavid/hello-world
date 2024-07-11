from google.cloud import dialogflow_v2 as dialogflow
from google.cloud import storage
import os
import re

PROJECT_ID="gcp-dig-polaris-cwp-prd-01"
SERVICE_ACCOUNT_EMAIL="cwc-prod-bot-confusion-matrix@gcp-dig-polaris-shared-prd-01.iam.gserviceaccount.com"


def fetch_intents_training_phrases(service_account_file, project):
    dialogflow_entity_client = dialogflow.EntityTypesClient.from_service_account_file(service_account_file)
    parent = dialogflow_entity_client.common_project_path(project)
    list_entity_types_request = dialogflow.ListEntityTypesRequest(parent=parent)
    
    entities = list(dialogflow_entity_client.list_entity_types(list_entity_types_request))
    
    dialogflow_intents_client = dialogflow.IntentsClient.from_service_account_file(service_account_file)
    parent = dialogflow_intents_client.common_project_path(project)
    intents = list(dialogflow_intents_client.list_intents(
        parent=parent,
        intent_view=dialogflow.IntentView.INTENT_VIEW_FULL
    ))
    
    entities_name_to_value = {
    'date-time': 'tomorrow afternoon',
    'date': 'tomorrow',
    'date-period': 'April',
    'time': '4:30 pm',
    'time-period': 'afternoon',
    'number': 'one',
    'cardinal': 'ten',
    'ordinal': 'tenth',
    'number-integer': '1',
    'number-sequence': '1 2 3',
    'flight-number' : 'LH4234',
    'unit-area': 'ten square feet',
    'unit-currency': '5 dollars',
    'unit-length': 'ten meters',
    'unit-speed': '5 km/h',
    'unit-volume': '2 liters',
    'unit-weight': '5 kilos',
    'unit-information': '5 megabytes',
    'percentage': '10 percent',
    'temperature': '25 degrees',
    'duration': '5 days',
    'age': '1 year old',
    'currency-name': 'euros',
    'unit-area-name': 'suqare meters',
    'unit-length-name': 'meters',
    'unit-speed-name': 'kilometer per hour',
    'unit-volume-name': 'cubic meters',
    'unit-weight-name': 'kilograms',
    'unit-information-name': 'megabytes',
    'address': '1600 Amphitheatre Pkwy, Mountain View, CA 94043',
    'zip-code': '94122',
    'geo-capital': 'Rome',
    'geo-country': 'Denmark',
    'geo-country-code': 'US',
    'geo-city': 'Tokyo',
    'geo-state': 'Scotland',
    'place-attraction': 'Golden Gate Bridge',
    'airport': 'SFO',
    'location': '1600 Amphitheatre Pkwy, Mountain View, CA 94043',
    'email': 'test@example.com',
    'phone-number': '+11234567890',
    'given-name': 'Joe',
    'last-name': 'Smith',
    'music-artist': 'Beatles',
    'music-genre': 'Jazz',
    'color': 'Blue',
    'language': 'Japanese',
    'any': 'flower',
    'url': 'google.com'
  }
    
    for intent in intents:
        entities_used = {entity.display_name
            for entity in intent.parameters}
        
        for entity in entities:
            if entity.display_name in entities_used \
                and entity.display_name not in entities_name_to_value:
                    
                entities_name_to_value[entity.display_name] = np.random.choice(
                    np.random.choice(entity.entities).synonyms, replace=False
            )
                
    
    intent_training_phrases = defaultdict(list)
    for intent in intents:
        for training_phrase in intent.training_phrases:
            
            parts = [
                entities_name_to_value[part.alias]
                if part.alias in entities_name_to_value else part.text
                for part in training_phrase.parts
            ]
            
            if(not intent.input_context_names):
                
                intent_training_phrases[intent.display_name].append(
                    "".join(parts)
                )
                
            if not intent_training_phrases[intent.display_name]:
                del intent_training_phrases[intent.display_name]
        return intent_training_phrases
    
    
intent_training_phrases = fetch_intents_training_phrases("sa-key1.json", PROJECT_ID)