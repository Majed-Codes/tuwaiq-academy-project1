# Tuwaiq Academy – Project 1
# Health Cluster Project

A simple hospital system built with Python OOP. It has four services: Diseases, Nutrition, Sports and Clinic.

## Classes

- `HealthCluster` - base class (name, age, height, weight, gender) with `calc_bmi()`
- `Diseases` - asks about symptoms and gives a quick assessment
- `nutrition` - calculates BMR and daily calories, and suggests meals
- `SportService` - checks run readiness, calories burned and a recovery plan
- `Clinic` - inherits from `Diseases`; picks the department, sets the priority and books an appointment

## OOP concepts used

- Inheritance and multi-level inheritance (`HealthCluster` -> `Diseases` -> `Clinic`)
- Abstraction (`HealthyFood` abstract class)
- Class attributes and instance attributes
- `super()` to reuse the parent constructor

## Files

| File | Description |
|---|---|
| `Health_Cluster_Project.py` | Full project in one file (terminal version) |
| `app.py` | Streamlit web app |
| `health_cluster.py` | Base class |
| `diseases.py` | Diseases class |
| `nutrition.py` | Nutrition class |
| `sports.py` | Sports class |
| `Clinic.py` | Clinic class |
| `.streamlit/config.toml` | App theme |

## How to run

Terminal version:

    python Health_Cluster_Project.py

Streamlit app:

    pip install -r requirements.txt
    streamlit run app.py

## Input notes (terminal version)

- Gender: `male` or `female`
- Yes/no questions: `y` or `n`
- Activity: `sedentary`, `light`, `moderate` or `high`
- Day and time: as shown in the list, for example `Sunday` and `9:00`
