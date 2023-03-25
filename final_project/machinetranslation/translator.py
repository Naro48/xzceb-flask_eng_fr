import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Initialize IBM Watson Language Translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


# English to French Translation Function
def english_to_french(english_text):
    """
    Translates text from English to French using IBM Watson Language Translator
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


# French to English Translation Function
def french_to_english(french_text):
    """
    Translates text from French to English using IBM Watson Language Translator
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
