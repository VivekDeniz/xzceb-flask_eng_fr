# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=unused-import
# pylint: disable=import-error
# pylint: disable=invalid-name

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('fauxWeNAHvKC1sfetg0TxeRE64PBZfdli37t46C7QXLL')

language_translator = LanguageTranslatorV3(
version ='2018-05-01',
authenticator = authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/68386e8f-2f1e-4871-b6b9-17290f0d88d7')

def english_to_french(englishText):
    translation = language_translator.translate(text=englishText, model_id="en-fr").get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText


def french_to_english(frenchText):
    translation = language_translator.translate(text=frenchText, model_id="fr-en").get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
