from algorethics.core.ethical_policy import EthicalPolicy

class InclusionPolicy(EthicalPolicy):
    def evaluate_policy(self, data, model):
        """
        Promotes inclusivity and prevents discrimination.
        This policy checks whether the data content supports inclusivity and avoids discriminating language or patterns.

        Parameters:
        - data (str): The processed data to be evaluated, assumed to be text.
        - model (Any): The model or computational tool being used.

        Returns:
        - bool: Returns True if no discrimination is detected, otherwise returns False.
        """
        # Enhanced keyword check logic
        if isinstance(data, str):
            # Keywords that reflect inclusivity
            inclusive_keywords = ['everyone', 'all', 'anyone', 'inclusive', 'universal', 'diverse',
                'equality', 'equity', 'accessible', 'non-discriminatory']
            # Keywords that might indicate discriminatory practices
            discriminatory_keywords =   ['only', 'excluding', 'exception', 'restricted', 'prohibited',
                'limited', 'exclusive', 'apart', 'separate', 'privileged']

            # Check for presence of inclusive and absence of discriminatory language
            has_inclusive_language = any(keyword in data.lower() for keyword in inclusive_keywords)
            has_discriminatory_language = any(keyword in data.lower() for keyword in discriminatory_keywords)

            if has_inclusive_language and not has_discriminatory_language:
                print("Inclusion compliance check passed.")
                return True
            else:
                print("Test failed: Inclusive or discriminatory language issues detected.")
                return False
        else:
            print("Data type not supported for inclusivity checks.")
            return False
