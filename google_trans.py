# Imports the Google Cloud client library
from google.cloud import translate


# Instantiates a client
translate_client = translate.Client()


def trans(text):

    # The target language
    target = 'ja'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    return translation['translatedText']


if __name__ == "__main__":
    print(trans("hello world"))
