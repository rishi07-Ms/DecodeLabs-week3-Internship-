🍹 Perso - AI Personalized Drink Recommendation System
Project Overview

Perso is an AI-based recommendation system that suggests drinks based on a user's mood, taste preference, and energy requirements. The system analyzes user inputs and provides personalized drink recommendations using similarity scoring and recommendation logic.

This project was developed as part of the DecodeLabs Artificial Intelligence Internship Program.

Objective

The main objective of this project is to create a recommendation system that:

Collects user preferences
Analyzes user choices
Matches preferences with available drink options
Generates personalized recommendations
Features
Interactive user input
Personalized recommendations
Similarity-based matching logic
Top 3 recommendations display
CSV dataset integration
User-friendly console interface
Technologies Used
Python
Pandas
CSV Dataset
Project Structure

Project-3-AI-Recommendation-System

├── recommendation_system.py

├── drinks.csv

├── README.md

└── screenshots

  └── output.png

Dataset

The dataset contains information about different drinks and their characteristics such as mood, taste, and energy level.

Example:

Mango Smoothie → Happy, Fruity, Medium
Cold Coffee → Tired, Sweet, High
Black Coffee → Tired, Bitter, High
Strawberry Shake → Happy, Sweet, Medium
Green Tea → Relaxed, Bitter, Low
Watermelon Juice → Relaxed, Fruity, Low
How It Works
The user enters:
Mood
Taste Preference
Energy Requirement
The system compares user inputs with drink attributes stored in the dataset.
A similarity score is calculated for each drink.
Drinks are ranked according to their match score.
The top recommendations are displayed to the user.
How to Run

Install Pandas:

pip install pandas

Run the program:

python recommendation_system.py

Sample Output

==================================================

🍹 PERSO - AI PERSONALIZED DRINK RECOMMENDATION SYSTEM

==================================================

Enter Mood (happy/tired/relaxed): happy

Enter Taste (sweet/bitter/fruity): sweet

Enter Energy Level (low/medium/high): medium

✨ TOP RECOMMENDATIONS FOR YOU ✨

🍹 Strawberry Shake (Match Score: 100%)

🍹 Mango Smoothie (Match Score: 65%)

🍹 Cold Coffee (Match Score: 35%)

Thank you for using Perso!

Key Concepts Used
Recommendation Systems
Similarity Matching
Data Handling
User Preference Analysis
Python Programming
Pandas Library
Internship Project

This project was completed as part of the Artificial Intelligence Internship Program at DecodeLabs. The project focuses on understanding the fundamentals of recommendation systems, user preference analysis, and personalization logic.

Author

Rishika Chunduru

B.Tech – CSE (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, and Software Development. 🚀
