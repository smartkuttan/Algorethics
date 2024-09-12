from algorethics.core.ethical_policy import EthicalPolicy

import re

class ReliabilityPolicy(EthicalPolicy):
    def evaluate_policy(self, data, model):
        """
        Ensures that AI systems have high reliability.
        This policy verifies if the model demonstrates high operational reliability and consistent performance
        based on either direct model attributes or simulated input data.

        Parameters:
        - data (str): The processed data to be evaluated, possibly containing reliability metrics in natural language.
        - model (Any): The model or computational tool being used.

        Returns:
        - bool: Returns True if the model demonstrates high reliability, otherwise returns False.
        """
        try:
            # Extracting metrics from natural language data
            uptime = self.extract_metric(data, 'uptime')
            error_rate = self.extract_metric(data, 'error_rate')  # Adapting to handle 'error_rate' or 'error rate'

            # Use model's default attributes if metrics are not available in data
            uptime = uptime if uptime is not None else getattr(model, 'uptime', None)
            error_rate = error_rate if error_rate is not None else getattr(model, 'error_rate', None)

            # Validate that both metrics are available
            if uptime is None or error_rate is None:
                print("Missing reliability data.")
                return False

            # Check reliability standards with more lenient thresholds
            if uptime >= 99.0 and error_rate < 0.9:  # Adjusted thresholds for reliability
                print("Reliability compliance check passed.")
                return True
            else:
                print(f"Test failed: Model does not meet reliability standards with uptime {uptime}% and error rate {error_rate}.")
                return False
        except Exception as e:
            print(f"Failed to parse reliability data or model attributes. Error: {str(e)}")
            return False

    def extract_metric(self, text, keyword):
        """
        Extracts a numeric metric from a string based on a keyword.

        Parameters:
        - text (str): String containing the metric.
        - keyword (str): Keyword to search for the metric.

        Returns:
        - float or None: The extracted metric value or None if not found.
        """
        # Prepare the regex pattern, adapting for possible spaces or underscores
        pattern_keyword = keyword.replace('_', '\s*[_\s]*')
        pattern = rf"{pattern_keyword}\s*is\s*(\d+(\.\d+)?)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return float(match.group(1))
        return None




