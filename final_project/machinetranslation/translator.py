"""
Translation functions using IBM Watson Language Translator
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2021-03-11',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    """
    Translates English text to French.
    """
    if english_text is None:
        return None
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source='en',
        target='fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.
    """
    if french_text is None:
        return None
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source='fr',
        target='en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
