import pandas as pd
import numpy as np

# Define the time slots
mwf_slots = [
    "8:00 AM - 8:50 AM", "9:05 AM - 9:55 AM", "10:10 AM - 11:00 AM",
    "11:15 AM - 12:05 PM", "12:20 PM - 1:10 PM", "1:25 PM - 2:15 PM",
    "2:30 PM - 3:20 PM", "3:35 PM - 4:25 PM", "4:40 PM - 5:30 PM"
]

tth_slots = [
    "8:00 AM - 9:15 AM", "10:30 AM - 11:45 AM",
    "12:00 PM - 1:15 PM", "1:30 PM - 2:45 PM"
]

# Define the classes and their structure
classes_structure = {
    "general_education_classes": {
        "class_options": {
            "arts_and_humanities_non_lit": [
                {"course": "MUSC 2100 - Music in the Western World", "credits": 3},
                {"course": "THEA 2100 - Theatre Appreciation", "credits": 3},
                {"course": "ARTS 2100 - Art Appreciation", "credits": 3}
            ],
            "arts_and_humanities_lit": [
                {"course": "ENGL 2120 - World Literature", "credits": 3},
                {"course": "ENGL 2130 - British Literature", "credits": 3},
                {"course": "ENGL 2140 - American Literature", "credits": 3}
            ],
            "oral_communication_requirement": [
                {"course": "COMM 1500 - Introduction to Human Communication", "credits": 3},
                {"course": "COMM 2500 - Public Speaking", "credits": 3},
                {"course": "ENGL 1030 - Composition and Rhetoric", "credits": 3}
            ],
            "natural_science_with_lab": [
                {
                    "path_name": "BIOL 1030/1050",
                    "courses": [
                        {"course": "BIOL 1030 - General Biology I", "credits": 3},
                        {"course": "BIOL 1050 - General Biology Lab", "credits": 1}
                    ]
                },
                {
                    "path_name": "CH 1010/1020",
                    "courses": [
                        {"course": "CH 1010 - General Chemistry", "credits": 4},
                        {"course": "CH 1011 - General Chemistry Lab", "credits": 0}
                    ]
                },
                {
                    "path_name": "PHYS 1220/1240",
                    "courses": [
                        {"course": "PHYS 1220 - Physics with Calculus I", "credits": 3},
                        {"course": "PHYS 1240 - Physics Laboratory I", "credits": 1}
                    ]
                }
            ],
            "social_sciences": [
                {"course": "ANTH 2010 - Introduction to Anthropology", "credits": 3},
                {"course": "GEOG 1010 - Introduction to Geography", "credits": 3},
                {"course": "POSC 1010 - American National Government", "credits": 3}
            ],
            "global_challenges": [
                {"course": "ENGL 2120 - World Literature", "credits": 3},
                {"course": "ENGL 2130 - British Literature", "credits": 3},
                {"course": "ENGL 2140 - American Literature", "credits": 3}
            ],
            "cross_cultural_awareness": [
                {"course": "MUSC 3140 - World Music", "credits": 3}
            ],
            "science_and_technology_in_society": [
                {"course": "ENGR 2210 - Technology, Culture and Design", "credits": 3}
            ],
            "mathematics": [
                {"course": "MATH 1060 - Calculus of One Variable I", "credits": 4},
                {"course": "MATH 1080 - Calculus of One Variable II", "credits": 4}
            ]
        }
    },
    # More categories like "major_related_classes" can be added here...
}

# Function to generate schedules
def generate_schedule(classes_structure, mwf_slots, tth_slots):
    data = []
    for category, details in classes_structure.items():
        if "class_options" in details:
            for subcategory, courses in details["class_options"].items():
                for course in courses:
                    if "courses" in course:  # For nested courses (e.g., natural_science_with_lab)
                        for sub_course in course["courses"]:
                            add_schedule(sub_course, data, mwf_slots, tth_slots)
                    else:
                        add_schedule(course, data, mwf_slots, tth_slots)
    return data

# Helper function to add schedules
def add_schedule(course, data, mwf_slots, tth_slots):
    course_name = course["course"]
    # Assign random MWF slots (up to 2 sections)
    for _ in range(np.random.randint(1, 3)):  # Max 2 sections
        for day in ["Monday", "Wednesday", "Friday"]:
            slot = np.random.choice(mwf_slots)
            data.append({
                "Course": course_name,
                "Day": day,
                "Time Slot": slot
            })
    # Assign random TTh slots (up to 2 sections)
    for _ in range(np.random.randint(1, 3)):  # Max 2 sections
        for day in ["Tuesday", "Thursday"]:
            slot = np.random.choice(tth_slots)
            data.append({
                "Course": course_name,
                "Day": day,
                "Time Slot": slot
            })

# Generate the schedule
data = generate_schedule(classes_structure, mwf_slots, tth_slots)

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("class_schedule.csv", index=False)

# Display the dataset
print(df.head(20))
