def get_description():
    """return random weather,just like the pros"""
    from random import choice

    possibilities = ["rain", "snow", "sleet", "fog", "sun", "who knows"]
    return choice(possibilities)
