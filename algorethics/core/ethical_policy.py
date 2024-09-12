from abc import ABC, abstractmethod

class EthicalPolicy(ABC):
    """
    An abstract base class that defines a standard interface for all ethical policy classes.
    This class requires any subclass to implement the evaluate_policy method,
    which checks the compliance of data with a specified ethical policy based solely on the data and model.
    """

    @abstractmethod
    def evaluate_policy(self, data, model):
        """
        Evaluate the ethical compliance of data under a given model.

        Parameters:
        - data: The data to be evaluated, which could be of any type (text, images, etc.).
        - model: The machine learning model or any computational model being used.

        Returns:
        - bool: A boolean value indicating whether the policy is satisfied (True) or not (False).
        """
        pass
