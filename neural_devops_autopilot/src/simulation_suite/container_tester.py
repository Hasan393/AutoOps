import time

def simulate_test(code):
    time.sleep(2)
    if "def " in code or "import " in code:
        return True
    return False