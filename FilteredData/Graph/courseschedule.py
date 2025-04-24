import matplotlib.pyplot as plt

# --- 1. Hardcoded JSON SCHEDULE (defined directly in code) ---
schedule = {
    "Monday": [
        {"course": "DSA 210-A", "time": "12:40 pm - 2:30 pm", "location": "FASS G062"},
        {"course": "MATH 102-B", "time": "2:40 pm - 4:30 pm", "location": "FMAN G071"},
        {"course": "MATH 306R-H", "time": "4:40 pm - 5:30 pm", "location": "FENS L035"},
        {"course": "IE 303R-A", "time": "5:40 pm - 6:30 pm", "location": "FENS L061"}
    ],
    "Tuesday": [
        {"course": "MATH 102-B", "time": "11:40 am - 12:30 pm", "location": "FMAN G071"},
        {"course": "HUM 201-0", "time": "12:40 pm - 2:30 pm", "location": "FASS G062"},
        {"course": "CS 204-B", "time": "3:40 pm - 5:30 pm", "location": "FASS G062"}
    ],
    "Wednesday": [
        {"course": "CS 204-B", "time": "9:40 am - 10:30 am", "location": "UC G030"},
        {"course": "DSA 210-A", "time": "10:40 am - 11:30 am", "location": "FENS G077"},
        {"course": "MATH 306-B", "time": "2:40 pm - 3:30 pm", "location": "UC G030"}
    ],
    "Thursday": [
        {"course": "MATH 306-B", "time": "10:40 am - 12:30 pm", "location": "UC G030"},
        {"course": "HUM 201D-C2", "time": "2:40 pm - 3:30 pm", "location": "FASS 2023"}
    ],
    "Friday": [
        {"course": "MATH 102R-B7", "time": "10:40 am - 12:30 pm", "location": "FASS 1102"},
        {"course": "CS 204L-C1", "time": "3:40 pm - 5:30 pm", "location": "FASS G049"},
        {"course": "DSA 210R-H", "time": "5:40 pm - 7:30 pm", "location": "FENS L027"}
    ]
}

# --- 2. Count number of courses per day ---
course_counts = {day: len(schedule[day]) for day in schedule}

# --- 3. Order days in calendar sequence ---
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ordered_counts = {day: course_counts.get(day, 0) for day in ordered_days}

# --- 4. Draw the bar chart ---
plt.figure(figsize=(8, 5))
plt.bar(ordered_counts.keys(), ordered_counts.values(), color="steelblue")
plt.title("📚 Number of Courses per Day")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Courses")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("course_distribution_bar.png", dpi=300)
plt.show()
