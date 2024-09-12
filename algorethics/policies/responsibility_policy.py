from algorethics.core.ethical_policy import EthicalPolicy

class ResponsibilityPolicy(EthicalPolicy):
    def evaluate_policy(self, data, model):
        """
        Ensures accountability in AI decisions and actions.
        This policy checks if the explanations or logs provided by the AI contain keywords that demonstrate accountability.

        Parameters:
        - data (str): The textual data to be evaluated, typically AI-generated explanations or decision logs.
        - model (Any): The model or computational tool being used, not directly used in this simple check.

        Returns:
        - bool: Returns True if accountability is sufficiently demonstrated, otherwise returns False.
        """
        # Keywords that suggest accountability in explanations or decision-making processes
        accountability_keywords = [ 'justified',       # Decisions are reasoned or based on evidence
            'responsible',     # Implies ownership and responsibility for actions
            'explained',       # Decisions are clearly articulated
            'documented',      # Processes or decisions are recorded
            'transparent',     # Operations are open and clear
            'ethical',         # Actions adhere to ethical standards
            'traceable',       # Decisions can be traced back to their origins
            'verifiable',      # Assertions or data can be confirmed
            'auditable',       # Actions and decisions are subject to review or audit
            'compliant'    ]

        # Check for presence of accountability keywords
        is_accountable = any(keyword in data.lower() for keyword in accountability_keywords)

        if is_accountable:
            print("Accountability compliance check passed.")
            return True
        else:
            print("Test failed: Lack of accountability in AI actions or decisions.")
            return False

