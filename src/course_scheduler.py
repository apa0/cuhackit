"""
Course Scheduler Module

This module provides functionality to generate personalized course schedules
using AWS Bedrock AI services. It analyzes student course history and 
recommends optimal schedules for upcoming semesters.
"""

import boto3
import json
from typing import Dict, Any, Optional
from botocore.exceptions import ClientError


def callAPI(student: Dict[str, Any]) -> Optional[str]:
    """
    Generate a course schedule for a student using AWS Bedrock.
    
    Args:
        student: Dictionary containing student information including
                name, completed_courses, and current_courses
                
    Returns:
        Generated course schedule as a string, or None if generation fails
    """
    kb_id = "IIPMMYP0DR"

    # Extract courses from the student object
    completed_courses = "\n".join([f"- {course}" for course in student.get("completed_courses", [])])
    current_courses = "\n".join([f"- {course}" for course in student.get("current_courses", [])])

    input_text = (
        f"\n\nHuman: You are an AI assistant responsible for generating optimal course schedules for students. "
        f"You must strictly enforce course prerequisites and ensure schedules are balanced, appropriate for the student's level, "
        f"and avoid time conflicts.\n\n"
        f"I am currently planning my class schedule for the next semester. Here is a list of courses I have "
        f"already completed or am currently enrolled in. Use this to determine which courses I am eligible to take:\n\n"
        f"**Completed Courses:**\n{completed_courses if completed_courses else 'None'}\n\n"
        f"**Currently Enrolled Courses:**\n{current_courses if current_courses else 'None'}\n\n"
        f"**Class Offerings for the Next Semester:** [Provide the list of available courses in JSON format]\n\n"
        f"**Task:** Based on the courses I have already completed and the available class offerings for the next semester, "
        f"create a class schedule for me. Please make sure to:\n"
        f"1. Recommend only those courses for which I meet the prerequisites.\n"
        f"2. Ensure no recommended courses have overlapping class times.\n"
        f"3. Align your recommendations with my current academic progress and graduation year.\n"
        f"4. Ensure the schedule is appropriate for my academic standing and does not include courses I'm not eligible to take.\n"
        f"5. Ensure that my recommended schedule is at least 12 credits. Use the credit information for each class and aim for 16-18 credits while staying within the requirements.\n"
        f"6. If a course has prerequisites, only recommend it if I have already completed or am currently enrolled in all of those prerequisites.\n"
        f"7. Prioritize lower-level courses (1000- and 2000-level) before recommending upper-level courses (3000+). Only suggest upper-level courses if I have completed the necessary foundational courses.\n"
        f"8. If no courses meet my prerequisites, return 'No available courses based on prerequisites.' Do not guess or assume I can take missing prerequisites.\n\n"
        f"9. Ensure that every course in the recommended schedule includes its class time. If no valid schedule is possible due to time conflicts, explicitly state which courses conflict and suggest alternatives."
        f"Assistant:"
    )

    response = retrieveAndGenerate(input_text, kb_id)
    print(response)
    answer = createList(response)

    if answer:
        return answer
    else:
        print("No response received from AWS Bedrock.")
        return None


def retrieveAndGenerate(input_text: str, kb_id: str) -> Optional[str]:
    """
    Retrieve information and generate response using AWS Bedrock Knowledge Base.
    
    Args:
        input_text: The prompt text for the AI
        kb_id: Knowledge Base ID
        
    Returns:
        Generated text response or None if failed
    """
    session_id = None
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    region_id = "us-west-2"

    # Initialize AWS Bedrock Agent Runtime client
    bedrock_agent_client = boto3.client("bedrock-agent-runtime", region_name=region_id)

    request_payload = {
        "input": {"text": input_text},
        "retrieveAndGenerateConfiguration": {
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": kb_id,
                "modelArn": "arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
            }
        },
    }

    if session_id:
        request_payload["sessionId"] = session_id

    try:
        response = bedrock_agent_client.retrieve_and_generate(**request_payload)
        generated_text = response["output"]["text"]
        return generated_text

    except Exception as e:
        print(f"Error retrieving and generating response: {e}")
        return None


def createList(response: str) -> Optional[str]:
    """
    Create a formatted list from the AI response using Llama model.
    
    Args:
        response: The raw response from the first AI call
        
    Returns:
        Formatted list of courses or None if failed
    """
    client = boto3.client("bedrock-runtime", region_name="us-west-2")
    model_id = "arn:aws:bedrock:us-west-2:363793501045:inference-profile/us.meta.llama3-2-1b-instruct-v1:0"
    prompt = f"Create a list from this data providing the class numbers and class times with each class's data on a separate line: {response}"
    formatted_prompt = f"""
    <|begin_of_text|><|start_header_id|>user<|end_header_id|>
    {prompt}
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """

    native_request = {
        "prompt": formatted_prompt,
        "max_gen_len": 512,
        "temperature": 1,
        "top_p": 0.1,
    }

    request = json.dumps(native_request).encode('utf-8')

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=request,
            contentType="application/json",
            accept="application/json"
        )

        model_response = json.loads(response["body"].read())
        response_text = model_response["generation"]
        return response_text

    except ClientError as e:
        print(f"AWS ClientError: {e}")
        return None
    except Exception as e:
        print(f"General error: {e}")
        raise