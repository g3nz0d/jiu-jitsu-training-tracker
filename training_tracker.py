import json

# Load training log
with open("training_log.json", "r") as f:
    training_data = json.load(f)

# Define move categories
move_categories = {
    "submissions": {"armbar", "kimura"},
    "chokes": {"triangle choke", "guillotine choke"},
    "escapes": {"hip escape", "bridge escape", "back escape"}
}

# Calculate attendance
total_days = len(training_data)
days_attended = sum(1 for v in training_data.values() if v["attended"])
days_missed = total_days - days_attended

# Attendance percentages
attended_pct = (days_attended / total_days) * 100
missed_pct = (days_missed / total_days) * 100

# Count moves
move_counts = {"submissions": 0, "chokes": 0, "escapes": 0}
total_moves = 0

for session in training_data.values():
    for move in session["moves"]:
        total_moves += 1
        for category, moves in move_categories.items():
            if move in moves:
                move_counts[category] += 1

# Move percentages
move_percentages = {
    k.title(): round((v / total_moves) * 100, 2) if total_moves else 0
    for k, v in move_counts.items()
}

# Summary
summary = {
    "Total Days Logged": total_days,
    "Days Attended": days_attended,
    "Days Missed": days_missed,
    "Attendance %": round(attended_pct, 2),
    "Missed %": round(missed_pct, 2),
    "Move Percentages": move_percentages
}

# Save summary
with open("training_summary.json", "w") as f:
    json.dump(summary, f, indent=4)

# Output to console
print(json.dumps(summary, indent=4))
