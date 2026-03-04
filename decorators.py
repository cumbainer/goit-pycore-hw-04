from functools import wraps


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError) as e:
            if "not enough values to unpack" in str(e):
                return "Error: please provide all required arguments."
            return f"Error: {e}"
        except KeyError as e:
            return f"Error: contact {e} not found."
        except RuntimeError as e:
            return f"Error: {e}"

    return wrapper
