# Course Scheduler

> AI-Powered Academic Planning Tool for University Students

An intelligent course scheduling system that helps students plan their academic schedules by analyzing completed coursework and recommending optimal course selections for upcoming semesters. Built with AWS Bedrock AI services.

## Features

- **Smart Prerequisites Analysis**: Automatically determines course eligibility based on completed coursework
- **AI-Powered Recommendations**: Uses advanced AI to suggest optimal course combinations
- **Schedule Optimization**: Ensures no time conflicts and balanced credit loads (12-18 credits)
- **Academic Progress Tracking**: Aligns recommendations with degree requirements and academic standing
- **Interactive Command-Line Interface**: Easy-to-use terminal-based application

## Architecture

```
cuhackit/
├── src/                    # Source code
│   ├── main.py            # Main application entry point
│   └── course_scheduler.py # Core scheduling logic with AWS Bedrock integration
├── data/                  # Data files and course information
│   ├── course_structure.json    # Course structure definitions
│   ├── class_schedule.json      # Available class schedules
│   ├── cpscBs_degreepath.txt   # Degree requirement documentation
│   └── catalog_text.txt         # Extracted catalog information
├── scripts/               # Utility scripts
│   ├── preprocess.py      # PDF catalog preprocessing
│   └── classTimings.py    # Class timing generation
└── docs/                  # Documentation
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/cuhackit.git
   cd cuhackit
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure AWS credentials**:
   ```bash
   aws configure
   ```
   Or set environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=your-access-key
   export AWS_SECRET_ACCESS_KEY=your-secret-key
   export AWS_DEFAULT_REGION=us-west-2
   ```

### Usage

1. **Run the application**:

   ```bash
   python src/main.py
   ```

2. **Follow the interactive prompts**:
   - Enter your name
   - List completed courses (e.g., "CPSC 1010, ENGL 1030")
   - List current enrolled courses
   - The system will generate your personalized schedule

### Example Session

```
Welcome to the Course Scheduler!
==================================================

Enter your name: John Doe

Enter courses you have **already completed**, separated by commas
(e.g., CPSC 1010, ENGL 1030):
CPSC 1010, MATH 1060, ENGL 1030

Enter courses you are **currently enrolled in**, separated by commas
(or leave blank if none):
CPSC 1020, MATH 1080

Generating your personalized course schedule...
This may take a moment...

Recommended Course Schedule:
==================================================
CPSC 2070 - Computer Science II
  Time: MWF 10:10 AM - 11:00 AM
  Credits: 4

STAT 3090 - Applied Statistics
  Time: TTH 1:30 PM - 2:45 PM
  Credits: 3

BIOL 1030 - General Biology I
  Time: MWF 1:25 PM - 2:15 PM
  Credits: 3

Total Credits: 16
```

## Configuration

### AWS Bedrock Setup

The application uses two AWS Bedrock models:

- **Claude 3 Sonnet**: For course recommendation logic
- **Llama 3.2**: For response formatting

Update model IDs in `src/course_scheduler.py` if needed:

```python
self.model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
self.llama_model_id = "arn:aws:bedrock:us-west-2:363793501045:inference-profile/us.meta.llama3-2-1b-instruct-v1:0"
```

### Knowledge Base Configuration

The default Knowledge Base ID is set to `"IIPMMYP0DR"`. Update this in the CourseScheduler initialization if you're using a different knowledge base.

## Data Files

- **`course_structure.json`**: Contains degree requirements and course prerequisites
- **`class_schedule.json`**: Available class times and sections
- **`cpscBs_degreepath.txt`**: Computer Science BS degree pathway documentation
- **`catalog_text.txt`**: Raw university catalog text extracted from PDF

## Development

### Project Structure

- **`src/main.py`**: User interface and application entry point
- **`src/course_scheduler.py`**: Core business logic and AWS integration
- **`scripts/preprocess.py`**: Utilities for processing university catalog PDFs
- **`scripts/classTimings.py`**: Generates realistic class schedules with time slots

### Adding New Features

1. Course recommendation algorithms can be enhanced in `CourseScheduler._create_scheduling_prompt()`
2. New data sources can be integrated through the preprocessing scripts
3. UI improvements can be made in the `main.py` user interaction functions

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## Acknowledgments

- Built for CUHackit 2025
- Powered by AWS Bedrock AI services
- University catalog data processing with pdfplumber

## Support

If you encounter any issues or have questions:

1. Check the existing issues on GitHub
2. Create a new issue with detailed information about your problem
3. Include your Python version, AWS region, and error messages

---

**Happy Course Planning! 🎯**
