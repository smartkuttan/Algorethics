import argparse
import requests
from algorethics.core.validator import validate_policy
from algorethics.utils.logger import setup_logger
from algorethics.policies.privacy_policy import PrivacyPolicy
from algorethics.policies.transparency_policy import TransparencyPolicy
from algorethics.policies.inclusion_policy import InclusionPolicy
from algorethics.policies.responsibility_policy import ResponsibilityPolicy
from algorethics.policies.Impartiality_Policy import ImpartialityPolicy
from algorethics.policies.Reliability_Policy import ReliabilityPolicy

# Assuming setup_logger is correctly defined in the utils.logger module
logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description='Algorethics AI Policy Validator CLI')
    args = parser.parse_args()

    policies = {
        1: ('Privacy', PrivacyPolicy),
        2: ('Transparency', TransparencyPolicy),
        3: ('Inclusion', InclusionPolicy),
        4: ('Responsibility', ResponsibilityPolicy),
        5: ('Impartiality', ImpartialityPolicy),
        6: ('Reliability', ReliabilityPolicy)
    }

    policy_results = {}
    while len(policy_results) < 6:
        print("\nSelect a policy to validate:")
        for num, (name, _) in policies.items():
            if num not in policy_results:
                print(f"{num}: {name}")

        try:
            choice = int(input("Enter the number of the policy you want to validate: "))
            if choice in policies and choice not in policy_results:
                policy_name, policy_cls = policies[choice]
                print(f"You have selected the {policy_name} policy.")
                data_type = input("Enter the type of data to evaluate (text/image): ")
                data = input("Enter the data to evaluate: ")
                model = input("Enter the model type: ")
                policy_instance = policy_cls()
                is_compliant = validate_policy(data, data_type, model, policy_instance)
                policy_results[choice] = is_compliant
                print(f"{policy_name} compliance check {'passed' if is_compliant else 'failed'}.")
            else:
                print("Invalid selection or policy already validated.")
        except ValueError:
            print("Please enter a valid number.")

    if all(policy_results.values()):
        display_logo = input("\nAll policies are compliant. Would you like to display the Algorethics compliance logo on your project? (yes/no): ")
        if display_logo.lower() == 'yes':
            project_name = input("Enter your project name: ")
            project_url = input("Enter your project URL: ")
            developer_email = input("Enter your developer contact email: ")
            
            url = 'https://algorethics.info/algorethics_cert_gen.php'
            payload = {
                'project_name': project_name,
                'project_url': project_url,
                'developer_email': developer_email
            }
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                html_code = response.json().get('html_code')
                print("Registration successful. Here is your HTML embed code:")
                print("-" * 40)
                print(html_code)
                print("-" * 40)
                print("Copy and paste the above HTML code into your project to display the Algorethics compliance logo.")
            else:
                print("Failed to register with the Algorethics service. Please try again.")
        else:
            print("Logo display declined.")
    else:
        print("\nNot all policies are compliant. Cannot proceed with logo display.")

if __name__ == '__main__':
    main()
