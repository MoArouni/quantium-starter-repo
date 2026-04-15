#!/bin/bash

# 1. Activate the virtual environment
# On Windows (Git Bash), the path uses 'Scripts'. On Mac/Linux, use 'bin'.
source venv/Scripts/activate

# 2. Execute the test suite
# We run pytest and capture its exit code
pytest test_app.py
pytest_exit_code=$?

# 3. Return the correct exit code
if [ $pytest_exit_code -eq 0 ]; then
    echo "Tests passed! Returning exit code 0."
    exit 0
else
    echo "Tests failed! Returning exit code 1."
    exit 1
fi