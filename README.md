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
