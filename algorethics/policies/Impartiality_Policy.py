import re
from algorethics.core.ethical_policy import EthicalPolicy

class ImpartialityPolicy(EthicalPolicy):
    def evaluate_policy(self, data, model):
        """
        Evaluate data for compliance with impartiality standards based on a fairness index or related metric extracted from text input.
        This implementation checks if the AI system is biased.

        Parameters:
        - data (str): Text input possibly containing a numerical fairness index.
        - model (Any): The model being evaluated.

        Returns:
        - bool: Returns True if the system is impartial, otherwise returns False.
        """

        # Improved regex to capture a number potentially preceded by 'fairness is' and possibly followed by non-numeric characters
        match = re.search(r'fairness is\s*(\d+\.?\d*)|\b(\d+\.?\d*)\b', data, re.IGNORECASE)
        if match:
            # Attempt to capture either group (with or without 'fairness is')
            fairness_index = float(match.group(1) if match.group(1) else match.group(2))
            # Adjusted condition: Fairness index from 0-100 scale; 80 or above passes
            if fairness_index >= 80:
                print("Impartiality compliance check passed.")
                return True
            else:
                print(f"Test failed: Bias detected in AI system. Fairness index: {fairness_index}")
                return False
        else:
            print("No valid fairness index found in the input.")
            return False
