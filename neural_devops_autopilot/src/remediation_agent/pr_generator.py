def generate_fix(model, metrics):
    prompt = f"Deployment failure predicted! Metrics: CPU {metrics['cpu_usage']:.1f}%, Memory {metrics['memory_usage']:.1f}%, Error Rate {metrics['error_rate']:.1f}%. Generate a Python script that implements a mock fix for this infrastructure issue (e.g., adding a Redis cache, load balancer logic, or rate limiting). Return ONLY the raw Python code."
    response = model.generate_content(prompt)
    return response.text.replace("```python", "").replace("```", "").strip()