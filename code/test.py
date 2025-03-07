from chatbot import Chat, register_call
import wikipedia
import os
import warnings


@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about " + query


first_quetion = "Hi, what would you like to know?"
chat = Chat(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "example.template")
)
chat.converse(first_quetion)

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