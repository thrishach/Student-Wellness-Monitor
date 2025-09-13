# Simple Student Wellness Monitor
# Hackathon Demo Project

def wellness_monitor(name, sleep, study, stress, exercise):
    score = 0

    # Sleep (ideal 7-9 hrs)
    score += 25 if 7 <= sleep <= 9 else (15 if 5 <= sleep < 7 else 5)

    # Study (ideal 2-6 hrs)
    score += 25 if 2 <= study <= 6 else (10 if study < 2 else 15)

    # Stress (ideal low)
    score += 25 if stress <= 4 else (15 if stress <= 7 else 5)

    # Exercise (ideal 30+ mins)
    score += 25 if exercise >= 30 else (15 if exercise >= 10 else 5)

    # Output
    print(f"\n📊 Wellness Report for {name}")
    print(f"🛌 Sleep: {sleep} hrs | 📖 Study: {study} hrs | 😥 Stress: {stress}/10 | 🏃 Exercise: {exercise} mins")
    print(f"⭐ Total Wellness Score: {score}/100")

    if score >= 80:
        print("✅ Excellent wellness! Keep it up 🎉")
    elif score >= 60:
        print("🙂 Good wellness, but try to improve!")
    elif score >= 40:
        print("⚠️ Wellness is moderate. Balance your routine.")
    else:
        print("❌ Low wellness! Please take care 💡")


# Demo Runs
wellness_monitor("Trisha", sleep=6, study=5, stress=4, exercise=20)
wellness_monitor("sowjanya", sleep=4, study=7, stress=8, exercise=5)
wellness_monitor("chinni", sleep=8, study=3, stress=3, exercise=40)
