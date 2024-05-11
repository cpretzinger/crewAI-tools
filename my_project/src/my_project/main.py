#!/usr/bin/env python
from my_project.crew import MyProjectCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    MyProjectCrew().crew().kickoff(inputs=inputs)