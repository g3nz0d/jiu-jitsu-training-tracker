# Jiu-Jitsu Training Tracker

This Python tracker helps monitor your Jiu-Jitsu training, providing insights into attendance and move categorization.

## 🚀 Features

- Tracks training days attended vs. missed
- Categorizes practiced moves into:
  - Submissions
  - Chokes
  - Escapes/Reversals
- Outputs percentage breakdown of attendance and move types
- Stores data in JSON files for easy version control and updates

## 📁 Files

- `training_log.json`: Raw training data (editable to reflect your sessions)
- `training_summary.json`: Automatically generated summary from the script
- `training_tracker.py`: Python script to run the analysis

## 🛠 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/g3nz0d/jiu-jitsu-training-tracker.git
   cd jiu-jitsu-training-tracker


# Make sure you have Python installed: python --version
# Run the script: python training_tracker.py


# Editing Your Training Log

To add or update training data, open `training_log.json` and follow this format:

```json
{
  "2025-06-01": {
    "attended": true,
    "moves": ["armbar", "triangle choke", "hip escape"]
  }
}

