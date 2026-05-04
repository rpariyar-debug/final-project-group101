def process_unique_requests(requests, max_position):
    """
    Processes a list of requested positions and accepts only valid
    positions that havent been used
    
    woudl be used in a system where each position can only be selected 
    once
    
    Args: 
    requests (list): list of requested position
    max_position (int): highest allowed position number
Returns:
    dict: summary of accepted and rejected requests
"""
    if not isinstance(requests, list):
        raise ValueError("requests must be a list")
    if not isinstance(max_position, int) or max_position < 0:
        raise ValueError("max_position must be a nonnegative integer")

    used_positions = set()
    accepted = []
    rejected = []

    for request in requests:
    # check that the request is an integer
        if not isinstance(request, int):
            rejected.append((request, "not an integer"))
            continue
    
    # check that the request is within range
        if request < 0 or request > max_position:
            rejected.append((request, "out of range"))
            continue
    
    # check whether the request was already used
        if request in used_positions:
            rejected.append((request, "already used"))
            continue
    # accept the request if it passes all checks
        used_positions.add(request)
        accepted.append(request)
    return {
        "accepted": accepted,
        "rejected": rejected,
        "total_accepted": len(accepted),
        "total_rejected": len(rejected)
}
# example 
if __name__ == "__main__": 
    sample_requests = [3, 7, 3, 12, -1, "A", 5, 7, 9]
    result = process_unique_requests(sample_requests, 10)

    print("Accepted requests:", result["accepted"])
    print("Rejected requests:", result["rejected"])
    print("Total accepted:", result["total_accepted"])
    print("Total rejected:", result["total_rejected"])
    
