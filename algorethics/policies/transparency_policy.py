from algorethics.core.ethical_policy import EthicalPolicy

class TransparencyPolicy(EthicalPolicy):
    def evaluate_policy(self, data, model):
        """
        Ensures that AI models are explainable and understandable.
        This policy checks if the length of the data provided is sufficient for understandability.

        Parameters:
        - data (str): The processed data to be evaluated, typically AI-generated outputs or predictions.
        - model (Any): The model or computational tool being used. Expected to support explainability.

        Returns:
        - bool: Returns True if the data is of sufficient length, otherwise returns False.
        """
        # Check if the length of the data is greater than 50
        if len(data) > 50:
            print("Explanation is sufficiently long.")
            return True
        else:
            print("Explanation is too short.")
            return False
