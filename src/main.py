#!/usr/bin/env python3
"""
Course Scheduler Main Application

This application helps students plan their course schedules by analyzing
completed courses and recommending optimal schedules for upcoming semesters.
"""

from typing import List, Dict, Any
from course_scheduler import callAPI


def get_user_input() -> Dict[str, Any]:
    """
    Collect user input for course planning.
    
    Returns:
        Dict containing student information including name and course history
    """
    print("Welcome to the Course Scheduler!")
    print("=" * 50)
    
    name = input("Enter your name: ").strip()
    
    print("\nEnter courses you have **already completed**, separated by commas")
    print("(e.g., CPSC 1010, ENGL 1030):")
    completed_input = input().strip()
    completed_courses = [
        course.strip() 
        for course in completed_input.split(',') 
        if course.strip()
    ] if completed_input else []
    
    print("\nEnter courses you are **currently enrolled in**, separated by commas")
    print("(or leave blank if none):")
    current_input = input().strip()
    current_courses = [
        course.strip() 
        for course in current_input.split(',') 
        if course.strip()
    ] if current_input else []
    
    return {
        "name": name,
        "completed_courses": completed_courses,
        "current_courses": current_courses,
    }


def main() -> None:
    """Main application entry point."""
    try:
        # Get student information
        student_info = get_user_input()
        
        # Generate schedule recommendation
        print("\nGenerating your personalized course schedule...")
        print("This may take a moment...\n")
        
        response = callAPI(student_info)
        
        if response:
            print("Recommended Course Schedule:")
            print("=" * 50)
            print(response)
        else:
            print("Unable to generate a schedule recommendation at this time.")
            
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again or contact support if the issue persists.")


if __name__ == "__main__":
    main()