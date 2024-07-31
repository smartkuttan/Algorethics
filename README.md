# Algorethics AI Library Documentation
<div align="center">
  <img src="https://github.com/smartkuttan/Algorethics/blob/main/Algorethics.png" align="center" width="550">
</div>

## Introduction

The **Algorethics AI Library** is a Python library designed to help AI developers ensure their projects adhere to ethical principles. Inspired by the Universal Catholic Church's Rome Call for AI Ethics, this library promotes respect for human dignity, inclusion, transparency, responsibility, impartiality, and reliability in AI systems.

### Key Principles

- **Respecting Human Dignity**: "So God created mankind in his own image, in the image of God he created them; male and female he created them." (Genesis 1:27)
- **Promoting Inclusion**: "The body is a unit, though it is made up of many parts; and though all its parts are many, they form one body. So it is with Christ." (1 Corinthians 12:12)
- **Ensuring Transparency**: "For nothing is hidden that will not become evident, nor anything secret that will not be known and come to light." (Luke 8:17)
- **Upholding Responsibility**: "Everyone to whom much was given, of him much will be required; and from him to whom they entrusted much, they will demand the more." (Luke 12:48)

## Key Features

- **Privacy Policies**: Ensure the protection of sensitive information.
- **Transparency Policies**: Guarantee that AI models are explainable and understandable.
- **Inclusion Policies**: Promote inclusivity and prevent discrimination.
- **Responsibility Policies**: Establish accountability for AI actions and decisions.
- **Impartiality Policies**: Prevent bias in AI systems to safeguard fairness.
- **Reliability Policies**: Ensure high reliability and uptime for AI systems.

## Installation

To install the Algorethics AI Library, use pip:

```bash
pip install algorethics
```

## Usage

Here's an example of how to use the Algorethics AI Library in your project.

### Step 1: Define Ethical Policies

Define functions that represent your ethical policies. These functions should return a boolean indicating whether the policy is satisfied.

#### Privacy Policy Example

```python
def privacy_policy_example(data):
    """Ensure that sensitive information is not included in the data."""
    # Example: Filter out any entries with keys like "private", "confidential", "secret"
    return not any(key in data for key in ["private", "confidential", "secret"])

# Real-world sample usage
data_sample = {"name": "John Doe", "private": "Sensitive Data"}
print(privacy_policy_example(data_sample))  # Output: False
```

#### Transparency Policy Example

```python
def transparency_policy_example(model):
    """Ensure that the AI model is explainable."""
    # Example: Check if the model has an attribute for explainability
    return hasattr(model, 'explainability')

# Real-world sample usage
class AIModel:
    explainability = True

model_sample = AIModel()
print(transparency_policy_example(model_sample))  # Output: True
```

#### Inclusion Policy Example

```python
def inclusion_policy_example(data):
    """Ensure that no individual is excluded based on discriminatory attributes."""
    # Example: Ensure no one has the "excluded" status
    return all(item.get("status") != "excluded" for item in data)

# Real-world sample usage
data_sample = [{"status": "included"}, {"status": "excluded"}]
print(inclusion_policy_example(data_sample))  # Output: False
```

#### Responsibility Policy Example

```python
def responsibility_policy_example(action):
    """Ensure that there is accountability for actions taken by the AI."""
    # Example: Check if there is a responsible party for the action
    return action.get("responsible_party") is not None

# Real-world sample usage
action_sample = {"action": "delete_user", "responsible_party": "admin"}
print(responsibility_policy_example(action_sample))  # Output: True
```

#### Impartiality Policy Example

```python
def impartiality_policy_example(data):
    """Ensure that the AI system does not create or follow biases."""
    # Example: Check if there is any bias value in the data
    return all(item.get("bias") == 0 for item in data)

# Real-world sample usage
data_sample = [{"bias": 0}, {"bias": 1}]
print(impartiality_policy_example(data_sample))  # Output: False
```

#### Reliability Policy Example

```python
def reliability_policy_example(system):
    """Ensure that the AI system maintains high reliability."""
    # Example: Check if the system uptime is greater than 99.9%
    return system.get("uptime", 0) > 99.9

# Real-world sample usage
system_sample = {"uptime": 99.95}
print(reliability_policy_example(system_sample))  # Output: True
```

### Step 2: Initialize Algorethics and Add Policies

Create an instance of the Algorethics class and add the defined policies.

```python
from algorethics import Algorethics

# Initialize the Algorethics class
ai_lib = Algorethics()

# Add policies to the library
ai_lib.add_privacy_policy(privacy_policy_example)
ai_lib.add_transparency_policy(transparency_policy_example)
ai_lib.add_inclusion_policy(inclusion_policy_example)
ai_lib.add_responsibility_policy(responsibility_policy_example)
ai_lib.add_impartiality_policy(impartiality_policy_example)
ai_lib.add_reliability_policy(reliability_policy_example)
```

### Step 3: Validate AI Project

Use the `validate` method to check if your AI project adheres to the defined ethical policies.

```python
# Example data, model, action, and system for validation
data = [{"status": "included", "bias": 0}]
model = {"explainability": True}
action = {"responsible_party": "team_lead"}
system = {"uptime": 99.95}

# Validate the AI project
if ai_lib.validate(data, model, action, system):
    print("AI project is ethically compliant")
else:
    print("AI project is not ethically compliant")
```

## Full Example

Combining all steps into a complete example:

```python
from algorethics import Algorethics

# Define ethical policies
def privacy_policy_example(data):
    """Ensure that sensitive information is not included in the data."""
    return not any(key in data for key in ["private", "confidential", "secret"])

def transparency_policy_example(model):
    """Ensure that the AI model is explainable."""
    return hasattr(model, 'explainability')

def inclusion_policy_example(data):
    """Ensure that no individual is excluded based on discriminatory attributes."""
    return all(item.get("status") != "excluded" for item in data)

def responsibility_policy_example(action):
    """Ensure that there is accountability for actions taken by the AI."""
    return action.get("responsible_party") is not None

def impartiality_policy_example(data):
    """Ensure that the AI system does not create or follow biases."""
    return all(item.get("bias") == 0 for item in data)

def reliability_policy_example(system):
    """Ensure that the AI system maintains high reliability."""
    return system.get("uptime", 0) > 99.9

# Initialize Algorethics
ai_lib = Algorethics()

# Add policies
ai_lib.add_privacy_policy(privacy_policy_example)
ai_lib.add_transparency_policy(transparency_policy_example)
ai_lib.add_inclusion_policy(inclusion_policy_example)
ai_lib.add_responsibility_policy(responsibility_policy_example)
ai_lib.add_impartiality_policy(impartiality_policy_example)
ai_lib.add_reliability_policy(reliability_policy_example)

# Example data, model, action, and system
data = [{"status": "included", "bias": 0}]
model = {"explainability": True}
action = {"responsible_party": "team_lead"}
system = {"uptime": 99.95}

# Validate AI project
if ai_lib.validate(data, model, action, system):
    print("AI project is ethically compliant")
else:
    print("AI project is not ethically compliant")
```

## Detailed Policy implementation Example 

Here is a detailed implementation of all six policies, including privacy, transparency, inclusion, responsibility, impartiality, and reliability, along with real-world examples.

### Privacy Policy Implementation

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def privacy_policy_example(data):
    """
    Ensure that sensitive information is not included in the data.
    
    Parameters:
    data (dict): The data to be checked for sensitive information.
    
    Returns:
    bool: True if no sensitive information is found, False otherwise.
    """
    sensitive_keywords = ["private", "confidential", "secret", "ssn", "password", "credit_card"]
    
    for key in sensitive_keywords:
        if key in data:
            logger.warning(f"Sensitive information detected: {key}")
            return False
    
    for key, value in data.items():
        if isinstance(value, dict):
            if not privacy_policy_example(value):
                logger.warning(f"Sensitive information detected in nested data: {key}")
                return False
    
    for key, value in data.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    if not privacy_policy_example(item):
                        logger.warning(f"Sensitive information detected in list data: {key}")
                        return False
    
    logger.info("No sensitive information detected.")
    return True

# Real-world sample usage
data_sample = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "private": "Sensitive Data",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "confidential": "Hidden Info"
    },
    "transactions": [
        {"amount": 100, "credit_card": "1234-5678-9012-3456"},
        {"amount": 200, "ssn": "123-45-6789"}
    ]
}

print(privacy_policy_example(data_sample))  # Output: False (due to multiple violations)
```

### Transparency Policy Implementation

```python
def transparency_policy_example(model):
    """
    Ensure that the AI model is explainable.
    
    Parameters:
    model (object): The AI model to be checked for explainability.
    
    Returns:
    bool: True if the model is explainable, False otherwise.
    """
    if hasattr(model, 'explainability'):
        logger.info("Model is explainable.")
        return True
    else:
        logger.warning("Model is not explainable.")
        return False

# Real-world sample usage
class AIModel:
    explainability = True

model_sample = AIModel()
print(transparency_policy_example(model_sample))  # Output: True
```

### Inclusion Policy Implementation

```python
def inclusion_policy_example(data):
    """
    Ensure that no individual is excluded based on discriminatory attributes.
    
    Parameters:
    data (list): The data to be checked for inclusivity.
    
    Returns:
    bool: True if no individual is excluded, False otherwise.
    """
    for item in data:
        if item.get("status") == "excluded":
            logger.warning(f"Discriminatory exclusion detected: {item}")
            return False
    
    logger.info("No discriminatory exclusions detected.")
    return True

# Real-world sample usage
data_sample = [{"status": "included"}, {"status": "excluded"}]
print(inclusion_policy_example(data_sample))  # Output: False
```

### Responsibility Policy Implementation

```python
def responsibility_policy_example(action):
    """
    Ensure that there is accountability for actions taken by the AI.
    
    Parameters:
    action (dict): The action to be checked for accountability.
    
    Returns:
    bool: True if there is accountability, False otherwise.
    """
    if action.get("responsible_party") is not None:
        logger.info("Action is accountable.")
        return True
    else:
        logger.warning("Action is not accountable.")
        return False

# Real-world sample usage
action_sample = {"action": "delete_user", "responsible_party": "admin"}
print(responsibility_policy_example(action_sample))  # Output: True
```

### Impartiality Policy Implementation

```python
def impartiality_policy_example(data):
    """
    Ensure that the AI system does not create or follow biases.
    
    Parameters:
    data (list): The data to be checked for biases.
    
    Returns:
    bool: True if no biases are found, False otherwise.
    """
    for item in data:
        if item.get("bias") != 0:
            logger.warning(f"Bias detected: {item}")
            return False
    
    logger.info("No biases detected.")
    return True

# Real-world sample usage
data_sample = [{"bias": 0}, {"bias": 1}]
print(impartiality_policy_example(data_sample))  # Output: False
```

### Reliability Policy Implementation

```python
def reliability_policy_example(system):
    """
    Ensure that the AI system maintains high reliability.
    
    Parameters:
    system (dict): The system to be checked for reliability.
    
    Returns:
    bool: True if the system is reliable, False otherwise.
    """
    if system.get("uptime", 0) > 99.9:
        logger.info("System is reliable.")
        return True
    else:
        logger.warning("System is not reliable.")
        return False

# Real-world sample usage
system_sample = {"uptime": 99.95}
print(reliability_policy_example(system_sample))  # Output: True
```

### Full Example

Combining all steps into a complete example:

```python
from algorethics import Algorethics

# Define ethical policies
def privacy_policy_example(data):
    sensitive_keywords = ["private", "confidential", "secret", "ssn", "password", "credit_card"]
    
    for key in sensitive_keywords:
        if key in data:
            logger.warning(f"Sensitive information detected: {key}")
            return False
    
    for key, value in data.items():
        if isinstance(value, dict):
            if not privacy_policy_example(value):
                logger.warning(f"Sensitive information detected in nested data: {key}")
                return False
    
    for key, value in data.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    if not privacy_policy_example(item):
                        logger.warning(f"Sensitive information detected in list data: {key}")
                        return False
    
    logger.info("No sensitive information detected.")
    return True

def transparency_policy_example(model):
    if hasattr(model, 'explainability'):
        logger.info("Model is explainable.")
        return True
    else:
        logger.warning("Model is not explainable.")
        return False

def inclusion_policy_example(data):
    for item in data:
        if item.get("status") == "excluded":
            logger.warning(f"Discriminatory exclusion detected: {item}")
            return False
    
    logger.info("No discriminatory exclusions detected.")
    return True

def responsibility_policy_example(action):
    if action.get("responsible_party") is not None:
        logger.info("Action is accountable.")
        return True
    else:
        logger.warning("Action is not accountable.")
        return False

def impartiality_policy_example(data):
    for item in data:
        if item.get("bias") != 0:
            logger.warning(f"Bias detected: {item}")
            return False
    
    logger.info("No biases detected.")
    return True

def reliability_policy_example(system):
    if system.get("uptime", 0) > 99.9:
        logger.info("System is reliable.")
        return True
    else:
        logger.warning("System is not reliable.")
        return False

# Initialize Algorethics
ai_lib = Algorethics()

# Add policies
ai_lib.add_privacy_policy(privacy_policy_example)
ai_lib.add_transparency_policy(transparency_policy_example)
ai_lib.add_inclusion_policy(inclusion_policy_example)
ai_lib.add_responsibility_policy(responsibility_policy_example)
ai_lib.add_impartiality_policy(impartiality_policy_example)
ai_lib.add_reliability_policy(reliability_policy_example)

# Example data, model, action, and system
data = [{"status": "included", "bias": 0}]
model = {"explainability": True}
action = {"responsible_party": "team_lead"}
system = {"uptime": 99.95}

# Validate AI project
if ai_lib.validate(data, model, action, system):
    print("AI project is ethically compliant")
else:
    print("AI project is not ethically compliant")
```

This implementation ensures thorough checking for each ethical principle and provides clear logging to identify any violations.


### `Algorethics.py`

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Algorethics:
    def __init__(self):
        self.privacy_policies = []
        self.transparency_policies = []
        self.inclusion_policies = []
        self.responsibility_policies = []
        self.impartiality_policies = []
        self.reliability_policies = []

    def add_privacy_policy(self, policy_func):
        self.privacy_policies.append(policy_func)

    def add_transparency_policy(self, policy_func):
        self.transparency_policies.append(policy_func)

    def add_inclusion_policy(self, policy_func):
        self.inclusion_policies.append(policy_func)

    def add_responsibility_policy(self, policy_func):
        self.responsibility_policies.append(policy_func)

    def add_impartiality_policy(self, policy_func):
        self.impartiality_policies.append(policy_func)

    def add_reliability_policy(self, policy_func):
        self.reliability_policies.append(policy_func)

    def validate(self, data, model, action, system):
        all_policies = {
            'Privacy': self.privacy_policies,
            'Transparency': self.transparency_policies,
            'Inclusion': self.inclusion_policies,
            'Responsibility': self.responsibility_policies,
            'Impartiality': self.impartiality_policies,
            'Reliability': self.reliability_policies
        }

        for policy_type, policies in all_policies.items():
            for policy in policies:
                if not policy(data, model, action, system):
                    logger.warning(f"{policy_type} policy validation failed.")
                    return False

        logger.info("All policies validated successfully.")
        return True

def privacy_policy_example(data, model, action, system):
    sensitive_keywords = ["private", "confidential", "secret", "ssn", "password", "credit_card"]

    def check_sensitive_info(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key.lower() in sensitive_keywords:
                    logger.warning(f"Sensitive information detected: {key}")
                    return False
                if isinstance(value, (dict, list)):
                    if not check_sensitive_info(value):
                        return False
        elif isinstance(data, list):
            for item in data:
                if not check_sensitive_info(item):
                    return False
        return True

    return check_sensitive_info(data)

def transparency_policy_example(data, model, action, system):
    if hasattr(model, 'explainability'):
        logger.info("Model is explainable.")
        return True
    else:
        logger.warning("Model is not explainable.")
        return False

def inclusion_policy_example(data, model, action, system):
    for item in data:
        if item.get("status") == "excluded":
            logger.warning(f"Discriminatory exclusion detected: {item}")
            return False
    logger.info("No discriminatory exclusions detected.")
    return True

def responsibility_policy_example(data, model, action, system):
    if action.get("responsible_party") is not None:
        logger.info("Action is accountable.")
        return True
    else:
        logger.warning("Action is not accountable.")
        return False

def impartiality_policy_example(data, model, action, system):
    for item in data:
        if item.get("bias") != 0:
            logger.warning(f"Bias detected: {item}")
            return False
    logger.info("No biases detected.")
    return True

def reliability_policy_example(data, model, action, system):
    if system.get("uptime", 0) > 99.9:
        logger.info("System is reliable.")
        return True
    else:
        logger.warning("System is not reliable.")
        return False

# Sample usage
if __name__ == "__main__":
    ai_lib = Algorethics()

    ai_lib.add_privacy_policy(privacy_policy_example)
    ai_lib.add_transparency_policy(transparency_policy_example)
    ai_lib.add_inclusion_policy(inclusion_policy_example)
    ai_lib.add_responsibility_policy(responsibility_policy_example)
    ai_lib.add_impartiality_policy(impartiality_policy_example)
    ai_lib.add_reliability_policy(reliability_policy_example)

    data = [{"status": "included", "bias": 0, "private": "Sensitive Data"}]
    model = {"explainability": True}
    action = {"responsible_party": "team_lead"}
    system = {"uptime": 99.95}

    if ai_lib.validate(data, model, action, system):
        print("AI project is ethically compliant")
    else:
        print("AI project is not ethically compliant")
```

### Sample Template Framework for Developers

Below is a comprehensive sample template framework for developers to use the `Algorethics` library in their AI projects.

```python
# Import necessary libraries
from algorethics import Algorethics

# Define custom policy functions if needed
def custom_privacy_policy(data, model, action, system):
    sensitive_keywords = ["private", "confidential", "secret", "ssn", "password", "credit_card"]
    
    def check_sensitive_info(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key.lower() in sensitive_keywords:
                    return False
                if isinstance(value, (dict, list)):
                    if not check_sensitive_info(value):
                        return False
        elif isinstance(data, list):
            for item in data:
                if not check_sensitive_info(item):
                    return False
        return True

    return check_sensitive_info(data)

def custom_transparency_policy(data, model, action, system):
    if hasattr(model, 'explainability'):
        return True
    else:
        return False

def custom_inclusion_policy(data, model, action, system):
    for item in data:
        if item.get("status") == "excluded":
            return False
    return True

def custom_responsibility_policy(data, model, action, system):
    if action.get("responsible_party") is not None:
        return True
    else:
        return False

def custom_impartiality_policy(data, model, action, system):
    for item in data:
        if item.get("bias") != 0:
            return False
    return True

def custom_reliability_policy(data, model, action, system):
    if system.get("uptime", 0) > 99.9:
        return True
    else:
        return False

# Initialize Algorethics
ai_lib = Algorethics()

# Add predefined or custom policies
ai_lib.add_privacy_policy(custom_privacy_policy)
ai_lib.add_transparency_policy(custom_transparency_policy)
ai_lib.add_inclusion_policy(custom_inclusion_policy)
ai_lib.add_responsibility_policy(custom_responsibility_policy)
ai_lib.add_impartiality_policy(custom_impartiality_policy)
ai_lib.add_reliability_policy(custom_reliability_policy)

# Define example data, model, action, and system
data = [{"status": "included", "bias": 0, "private": "Sensitive Data"}]
model = {"explainability": True}
action = {"responsible_party": "admin"}
system = {"uptime": 99.8}

# Validate AI project
if ai_lib.validate(data, model, action, system):
    print("AI project is ethically compliant")
else:
    print("AI project is not ethically compliant")

# Implement further project logic
# ...
```

### Detailed Explanation

1. **Privacy Policy**:
   - Checks for sensitive keywords in the data to ensure no private information is included.
   - Handles nested data structures (dictionaries within dictionaries or lists).

2. **Transparency Policy**:
   - Verifies if the model has an 'explainability' attribute to ensure it can be explained.

3. **Inclusion Policy**:
   - Ensures that no individual is excluded based on discriminatory attributes.

4. **Responsibility Policy**:
   - Checks if there is a responsible party for the AI's actions, ensuring accountability.

5. **Impartiality Policy**:
   - Verifies that the AI system does not create or follow biases.

6. **Reliability Policy**:
   - Ensures the system's uptime is above 99.9%, indicating high reliability.

### Sample Template Framework

- **Custom Policy Functions**:
  - Developers can define custom policy functions tailored to their specific needs.

- **Initialization and Adding Policies**:
  - Initialize the `Algorethics` class and add predefined or custom policies.

- **Example Data, Model, Action, and System**:
  - Define example inputs to validate the AI project against the policies.

- **Validation**:
  - Use the `validate` method to check if the AI project adheres to the defined policies.

This enhanced implementation ensures a comprehensive framework for developers to integrate and validate ethical policies in their AI projects, promoting responsible and fair AI systems.
## Contributing

We welcome contributions from the community to enhance the functionality and reach of Algorethics. Please feel free to fork this repository, submit pull requests, and raise issues.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## This Project is inspired by Rome Call
<!-- Footer -->
<div align="center">
  <img src="https://github.com/smartkuttan/Algorethics/blob/main/Romecall.jpg" alt="Romecall" width="600">
</div>

### About the Rome Call for AI Ethics

The Rome Call for AI Ethics is a significant initiative led by the Vatican and various organizations, calling for the development of AI systems that adhere to ethical standards. The initiative emphasizes principles such as human dignity, inclusion, transparency, and accountability in AI technologies.

For more information about the Rome Call, visit [Rome Call for AI Ethics](https://www.romecall.org).

### Resources

- **Twitter**: Follow the Rome Call on Twitter
- **YouTube**: Watch related videos on YouTube
- **Download Rome Call Document**: [Download the Rome Call Paper](https://www.romecall.org/document.pdf)

By adhering to the ethical guidelines set forth in the Rome Call for AI Ethics, the Algorethics AI Library aims to foster a future where AI serves humanity responsibly and respectfully. Join us in this mission to build a more ethical AI landscape.
