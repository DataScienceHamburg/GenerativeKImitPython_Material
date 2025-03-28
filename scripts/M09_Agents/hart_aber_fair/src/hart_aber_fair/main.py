#!/usr/bin/env python
import sys
import warnings
import datetime
from hart_aber_fair.crew import HartAberFair

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Get the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")


def run():
    """
    Run the crew.
    """
    inputs = {
        'date': current_date
    }
    HartAberFair().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        HartAberFair().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        HartAberFair().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        HartAberFair().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
