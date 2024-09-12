from typing import Any, List, Union
import logging
from algorethics.core.ethical_policy import EthicalPolicy
from algorethics.data.text import process_text_data
from algorethics.data.image import process_image_data

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def validate_policy(data: Any, data_type: str, model: Any, policies: Union[EthicalPolicy, List[EthicalPolicy]]) -> bool:
    """
    Validate one or multiple ethical policies to determine if the data is compliant with each policy within the ethical framework.

    Parameters:
    - data (Any): The data being evaluated, which can be of any type (text, image, etc.).
    - data_type (str): The type of data ('text' or 'image').
    - model (Any): The model or computational tool being used.
    - policies (Union[EthicalPolicy, List[EthicalPolicy]]): A policy instance or list of policy instances to be evaluated against the data.

    Returns:
    - bool: Returns True if all policies are satisfied, otherwise returns False.
    """
    # Log the data type received
    logger.info("Data type received: " + data_type)

    # Process data based on its type
    if data_type == 'image':
        data = process_image_data(data)
    elif data_type == 'text':
        data = process_text_data(data)
    else:
        logger.error("Invalid data type specified.")
        return False

    # Ensure policies is a list for uniform handling
    if not isinstance(policies, list):
        policies = [policies]

    # Evaluate each policy
    all_compliant = True
    for policy in policies:
        result = policy.evaluate_policy(data, model)
        if result:
            logger.info(f"Policy {policy.__class__.__name__} is compliant.")
        else:
            logger.error(f"Policy {policy.__class__.__name__} failed.")
            all_compliant = False

    return all_compliant
