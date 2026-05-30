import pandas as pd

# Load dataset
df = pd.read_csv("drinks.csv")

print("=" * 60)
print("🍹 PERSO - AI PERSONALIZED DRINK RECOMMENDATION SYSTEM")
print("=" * 60)

# User Inputs
mood = input("Enter Mood (happy/tired/relaxed): ").lower()
taste = input("Enter Taste (sweet/bitter/fruity): ").lower()
energy = input("Enter Energy Level (low/medium/high): ").lower()

# Calculate similarity score
scores = []

for index, row in df.iterrows():
    score = 0

    if row["Mood"] == mood:
        score += 40

    if row["Taste"] == taste:
        score += 35

    if row["Energy"] == energy:
        score += 25

    scores.append(score)

df["Match Score"] = scores

# Sort recommendations
recommendations = df.sort_values(
    by="Match Score",
    ascending=False
)

print("\n✨ TOP RECOMMENDATIONS FOR YOU ✨\n")

for i, row in recommendations.head(3).iterrows():
    print(
        f"🍹 {row['Drink']} "
        f"(Match Score: {row['Match Score']}%)"
    )

print("\nThank you for using Perso!")