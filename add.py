# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
trigger:
- main

pool:
  vmImage: ubuntu-latest
strategy:
  matrix:
    Python27:
      python.version: '2.7'
    Python35:
      python.version: '3.5'
    Python36:
      python.version: '3.6'
    Python37:
      python.version: '3.7'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(python.version)'
  displayName: 'Use Python $(python.version)'

- script: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
  displayName: 'Install dependencies'

- script: |
    pip install pytest pytest-azurepipelines
    pytest
  displayName: 'pytest'
  
