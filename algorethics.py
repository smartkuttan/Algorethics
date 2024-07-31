# Algorethics.py
# Steve@techgeek.co.in

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
