# Script for preprocessing PDF catalog data
# For now I will focus on catalog year: 2024/2025
import pdfplumber

pdf_path = "/Users/angiediaz/Downloads/catalog2425.pdf"

text = ""
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text() + "\n"

# Save the extracted text for analysis
with open("catalog_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text extraction complete!")


# now we extract based on the infor in the text file
import json

data = {
    "general_education": {
        "arts_and_humanities": [
            {"course": "Arts and Humanities (Non-Literature)", "credits": 3, "semester": "First Semester - Second Year"},
            {"course": "Arts and Humanities (Literature)", "credits": 3, "semester": "First Semester - Sophomore Year"}
        ],
        "natural_science": [
            {"course": "Natural Science Requirement", "credits": 4, "semester": "First Semester - Freshman Year"},
            {"course": "Natural Science Requirement", "credits": 4, "semester": "Second Semester - Freshman Year"}
        ],
        "oral_communication": [
            {"course": "Oral Communication Requirement", "credits": 3, "semester": "First Semester - Sophomore Year"}
        ],
        "social_science": [
            {"course": "Social Science Requirement", "credits": 3, "semester": "First Semester - Junior Year"},
            {"course": "Social Science Requirement", "credits": 3, "semester": "Second Semester - Junior Year"}
        ],
        "global_challenges": [
            {"course": "Global Challenges Requirement", "credits": 3, "semester": "First Semester - Junior Year"},
            {"course": "Global Challenges Requirement", "credits": 3, "semester": "Second Semester - Senior Year"}
        ],
        "writing": [
            {"course": "Writing Requirement", "credits": 3, "semester": "First Semester - Senior Year"}
        ]
    },

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
                        {"course": "BIOL 1050 - General Biology Lab ", "credits": 1}
                    ],
                    "path_name": "CH 1010/1020",
                        "courses": [
                            {"course": "CH 1010 - General Chemistry", "credits": 4},
                            {"course": "CH 1011 - General Chemistry", "credits": 0}
                     ],
                     "path_name": "PHYS 1220/1240",
                        "courses": [
                            {"course": "PHYS 1220 Physics with Calculus I", "credits": 3},
                            {"course": "PHYS 1240 Physics Laboratory I", "credits": 1}
                     ]          
                }
            ],
            "social_sciences": [
                {"course": "ANTH 2010 - Introduction to Anthropology", "credits": 3},
                {"course": "GEOG 1010 - Introduction to Geography", "credits": 3},
                {"course": "POSC 1010 - Americal National Government", "credits": 3}
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
                {"course": "MATH 1080 - Calculus of One Variable II", "credits": 4},
            ],
        }
    },

    "major_related_classes": {
        "major_related_classes": {
            "first_year": [
                {"course": "ENGL 1030 - Composition and Rhetoric", "credits": 3,
                 "semester": "First Semester - Freshman Year"},
                {"course": "MATH 1060 - Calculus of One Variable I", "credits": 4,
                 "semester": "First Semester - Freshman Year"},
                {"course": "MATH 1080 - Calculus of One Variable II", "credits": 4,
                 "semester": "Second Semester - Freshman Year"},
                {
                    "course": "Introduction to Computing Requirement",
                    "credits": 4,
                    "semester": "First Semester - Freshman Year",
                    "paths": [
                        {
                            "path_name": "CPSC 1010/1020",
                            "courses": [
                                {"course": "CPSC 1010 - Introduction to Computing I", "credits": 4},
                                {"course": "CPSC 1020 - Introduction to Computing II", "credits": 4}
                            ]
                        },
                        {
                            "path_name": "CPSC 1060/1070",
                            "courses": [
                                {"course": "CPSC 1060 - Introduction to Programming", "credits": 4},
                                {"course": "CPSC 1070 - Programming Methodology", "credits": 4}
                            ]
                        }
                    ]
                },
                {
                    "course": "Introduction to Computing Requirement",
                    "credits": 4,
                    "semester": "Second Semester - Freshman Year",
                    "paths": [
                        {
                            "path_name": "CPSC 1010/1020",
                            "courses": [
                                {"course": "CPSC 1010 - Introduction to Computing I", "credits": 4},
                                {"course": "CPSC 1020 - Introduction to Computing II", "credits": 4}
                            ]
                        },
                        {
                            "path_name": "CPSC 1060/1070",
                            "courses": [
                                {"course": "CPSC 1060 - Introduction to Programming", "credits": 4},
                                {"course": "CPSC 1070 - Programming Methodology", "credits": 4}
                            ]
                        }
                    ]
                }
            ]
        },
        "sophomore_year": [
            {"course": "CPSC 2070 - Discrete Structures for Computing", "credits": 3, "semester": "First Semester - Sophomore Year", "prereq": ["MATH 1060"]},
            {"course": "CPSC 2120 - Algorithms and Data Structures", "credits": 4, "semester": "First Semester - Sophomore Year", "prereq": ["CPSC 2070"]},
            {"course": "CPSC 2150 - Software Development Foundations", "credits": 3, "semester": "Second Semester - Sophomore Year", "prereq": ["CPSC 2120"]},
            {"course": "CPSC 2310 - Introduction to Computer Organization", "credits": 4, "semester": "Second Semester - Sophomore Year", "prereq": ["CPSC 2120"]},
            {"course": "Natural Science Requirement ", "credits": 3,
                 "semester": "First Semester - Freshman Year"},
        ],
        "junior_year": [
            {"course": "CPSC 3720 - Introduction to Software Engineering", "credits": 3, "semester": "First Semester - Junior Year", "prereq": ["CPSC 2120"]},
            {"course": "CPSC 3220 - Advanced Systems", "credits": 3, "semester": "First Semester - Junior Year", "prereq": ["CPSC 2120"]},
            {"course": "CPSC 4030 - Data Science and Artificial Intelligence", "credits": 3, "semester": "Second Semester - Junior Year", "prereq": ["CPSC 2120"]}
        ],
        "senior_year": [
            {"course": "CPSC 4910 - Senior Computing Practicum", "credits": 3, "semester": "Second Semester - Senior Year", "prereq": ["CPSC 3720"]},
            {"course": "CPSC 3520 - Programming Systems", "credits": 3, "semester": "First Semester - Senior Year", "prereq": ["CPSC 3720"]}
        ]
    },

    #Grouping optional path classes together for simplicity
    "major_related_paths": {
        "major_related_paths": {
            "course": "Computer Science Path Requirement",
            "credits": 6,
            "semester": "Second Semester - Junior and Senior Year",
            "paths": [
                {
                "path_name": "Advanced Systems",
                "courses ": [
                    {"course": "CPSC 3220 - Introduction to Operating Systems", "credits": 3},
                    {"course": "CPSC 3600 - Network Programming", "credits": 3}
                    ]
                },
                {
                "courses alternate": [
                    {"course": "CPSC 4440 - Cloud Computing Architecture", "credits": 3},
                    {"course": "CPSC 4720 - Software Devel Methodolgy", "credits": 3}
                    ]
                },
                {
                "path_name": "Intelligent Computing",
                "courses ": [
                    {"course": "CPSC 4030 - Introduction to Operating Systems", "credits": 3},
                    {"course": "CPSC 4300 - Network Programming", "credits": 3}
                    ]
                },
                {
                "courses alternate": [
                    {"course": "CPSC 4420 - Cloud Computing Architecture", "credits": 3},
                    {"course": "CPSC 4430 - Software Devel Methodolgy", "credits": 3}
                    ]
                },
                {
                "path_name": "Interactive Systems",
                "courses ": [
                    {"course": "CPSC 3750 - Introduction to Operating Systems", "credits": 3},
                    {"course": "CPSC 4110 - Network Programming", "credits": 3}
                    ]
                },
                {
                "courses alternate": [
                    {"course": "CPSC 4140 - Cloud Computing Architecture", "credits": 3},
                    {"course": "CPSC 4150 - Software Devel Methodolgy", "credits": 3}
                    ]
                },     
            ]
        },
    

    "credits": {
        "total_credits": 122,
        "semester_credits": {
            "freshman_year": {
                "first_semester": 15,
                "second_semester": 15
            },
            "sophomore_year": {
                "first_semester": 16,
                "second_semester": 16
            },
            "junior_year": {
                "first_semester": 15,
                "second_semester": 15
            },
            "senior_year": {
                "first_semester": 15,
                "second_semester": 15
            }
        }
    }
}
}

# Saving the data to a JSON file
with open('course_structure2.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file 'course_structure.json' has been created!")


