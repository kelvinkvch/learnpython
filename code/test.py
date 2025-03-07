from chatbot import Chat,register_call
import wikipedia
import os
import warnings

@register_call("whoIs")
def who_is(session,query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try