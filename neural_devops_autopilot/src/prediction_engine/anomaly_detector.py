def predict_failure(metrics):
    risk_score = 0
    if metrics["cpu_usage"] > 85.0:
        risk_score += 40
    if metrics["memory_usage"] > 80.0:
        risk_score += 30
    if metrics["error_rate"] > 2.5:
        risk_score += 30
        
    will_fail = risk_score >= 70
    return will_fail, risk_score