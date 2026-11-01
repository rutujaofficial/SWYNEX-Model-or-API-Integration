
# SWYNEX - AI-Based Suspicious LinkedIn Profile Detection

## Project Overview
This project is a beginner-level Machine Learning prototype that analyses sample LinkedIn profile information and predicts whether a profile appears genuine-looking or potentially suspicious.

## Objective
To demonstrate how Machine Learning can analyse profile-related features and identify patterns in sample data.

## Technologies Used
- Python 3.14
- Pandas
- Scikit-learn
- Decision Tree Classifier
- CSV Dataset
- Visual Studio Code

## Features
- Reads profile information from a CSV dataset.
- Trains a Decision Tree classification model.
- Accepts profile details from the user.
- Predicts a profile category.
- Displays the prediction in the terminal.

## Input Features
1. Account age in months
2. Number of connections
3. Profile completeness percentage
4. Experience consistency

## Output
- 0: Genuine-looking
- 1: Potentially suspicious

## Installation

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

## Run the Project

```bash
python app.py
```

## Dataset
The project currently uses a small synthetic dataset created for educational demonstration.

## Limitations
This prototype is not connected to LinkedIn and does not verify real identities. Its small synthetic dataset is not sufficient for reliable real-world classification.

## Internship Task
SWYNEX Internship - Task 2: Model or API Integration.

