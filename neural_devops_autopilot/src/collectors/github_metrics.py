import random
import time

def fetch_live_metrics():
    return {
        "timestamp": time.time(),
        "cpu_usage": random.uniform(20.0, 98.0),
        "memory_usage": random.uniform(30.0, 90.0),
        "error_rate": random.uniform(0.0, 6.0),
        "recent_commits": random.randint(0, 15)
    }