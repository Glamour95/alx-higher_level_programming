def class_to_json(obj):
    """Converts an instance of a Class to a dictionary representation for JSON serialization"""
    if hasattr(obj, "__dict__"):
        # Get the attributes of the object
        attributes = obj.__dict__.copy()
        # Remove any private attributes starting with '__'
        attributes = {key: value for key, value in attributes.items() if not key.startswith('__')}
        return attributes
    else:
        return obj
