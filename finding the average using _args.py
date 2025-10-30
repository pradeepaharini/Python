#Code Author: Pradeepa Harini B 
def average(*args: int) -> float | None:
    if not args:
        return None
    return sum(args) / len(args)

