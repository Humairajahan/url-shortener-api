import shortuuid


def short_uuid(longurl):
    """Generates a short UUID (Universally Unique Identifiers)
    version 5 against a long URL.

    Args:
        longurl (string): URL that needs to be shortened
    """
    return shortuuid.uuid(name=longurl)
