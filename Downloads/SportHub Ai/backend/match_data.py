import random

# Mock match data
matches = [
    {"match_id": 1, "teams": ["Team A", "Team B"], "score": "1-1"},
    {"match_id": 2, "teams": ["Team C", "Team D"], "score": "2-0"},
]

def get_live_match_data():
    # Simulating live updates
    match = random.choice(matches)
    match["score"] = f"{random.randint(0, 3)}-{random.randint(0, 3)}"
    return match
