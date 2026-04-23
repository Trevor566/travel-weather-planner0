# travel-weather-planner0
A Python app that determines if commuting is possible based on distance, weather conditions, and available transportation using conditional logic.

# 🌦️ Travel Weather Planner

A simple Python project that determines whether commuting is possible based on distance, weather conditions, and available transportation options.

## 🚀 Features
- Takes user input for:
  - Distance (miles)
  - Weather conditions (rain or not)
  - Available transport (bike, car, ride-share)
- Uses conditional logic to determine if travel is possible
- Beginner-friendly Python project

## 🧠 Logic Overview
- Distance ≤ 1 mile → Walk if not raining
- Distance ≤ 6 miles → Bike if available and not raining
- Distance > 6 miles → Use car or ride-share
- Falsy distance (0) → Not possible

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/travel-weather-planner0.git
