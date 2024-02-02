# From PyPI:

# Import

import paralleldots
# Setting your API key

class API:
    def __init__(self):
        paralleldots.set_api_key('v0JMbqRgyhqd4S8iI1YdXhrSuXU8FxVEHYv2vlFX19o')

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

    def ner_Recognition(self, text):
        response = paralleldots.ner(text)
        return response

    def emotion_analysis(self, text):
        response = paralleldots.emotion(text)
        return response


