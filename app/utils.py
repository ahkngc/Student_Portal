def normalize_email(email: str) -> str:
    return (email or "").strip().lower()

def safe_str(s: str) -> str:
    return (s or "").strip()
