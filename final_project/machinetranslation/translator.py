"""
    Translate French to English And English To French using IBM Watson

"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Trasnlates English to French Using IBM Watson

    Returns:
        string: Text in French
    """
    
    if type(english_text) != str:
        return ''
    
    if english_text == '':
        return ''
    
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
        ).get_result()
    french_text = translation["translations"][0]["translation"]
    
    return french_text


def french_to_english(french_text):
    """Translates French To English using IBM Watson
    Returns:
        string: Text in English
    """
    if type(french_text) != str:
        return ''
    
    if french_text == '':
        return ''
    
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
        ).get_result()
    english_text = translation["translations"][0]["translation"]
    
    return english_text
