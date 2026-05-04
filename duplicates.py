def find_dupe_trans(transaction_amounts, threshold=0.01):
    """
    This function implements a significant algorithm that could be used in a financial transaction processing system.
    
    Args:
        transaction_amounts (list): List of transaction amounts 
        threshold (float): Maximum difference to consider amounts as duplicates
    
    Returns:
        dict: Dictionary mapping duplicate values to lists of their indices
        
    Raises:
        ValueError: If transaction_amounts is not a list or threshold is negative
    """
    #validates inputs
    if not isinstance(transaction_amounts, list):
        raise ValueError("transaction_amounts must be a list")
    
    if threshold < 0:
        raise ValueError("threshold cannot be negative")
    
    #handles empty list
    if not transaction_amounts:
        return {}
    
    #finds duplicate amounts within tolerance
    seen = {}
    duplicates = {} 
    #iterates through each transaction with its index
    for idx, amount in enumerate(transaction_amounts):
        matched = False
        
        for seen_amount, indices in seen.items():
            if abs(amount - seen_amount) <= threshold:
                # Record the duplicate
                if seen_amount not in duplicates:
                    duplicates[seen_amount] = indices.copy()
                duplicates[seen_amount].append(idx)
                matched = True
                break        
        #ifs no match found, add to seen dictionary
        if not matched:
            if amount not in seen:
                seen[amount] = []
            seen[amount].append(idx)    
    return duplicates

#mocks function to simulate database retrieval
def mock_get_trans(user_id):
    mock_data = {
        1: [10.00, 20.50, 10.00, 30.25, 20.51],
        2: [5.99, 15.00, 15.01, 25.00],
        3: [100.00, 100.01, 99.99, 50.00]
    }
    return mock_data.get(user_id, [])


#examples usage demonstrating the algorithm works
if __name__ == "__main__":
    #using mock data to test the function
    test_data = mock_get_trans(1)
    
    print(f"Transaction amounts: {test_data}")
    print(f"Duplicates (within 0.01 tolerance): {find_dupe_trans(test_data, 0.01)}")
    
    #anothers test with different threshold
    print(f"Duplicates (within 0.50 tolerance): {find_dupe_trans(test_data, 0.50)}")