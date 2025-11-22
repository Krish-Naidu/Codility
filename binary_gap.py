def solution(N):
    """
    Find the longest binary gap in the binary representation of N.
    
    A binary gap is a maximal sequence of consecutive zeros
    surrounded by ones at both ends.
    
    Args:
        N: A positive integer
        
    Returns:
        The length of the longest binary gap, or 0 if no gap exists
    """
    # Convert N to binary and remove '0b' prefix
    binary_representation = bin(N)[2:]
    
    max_gap_length = 0
    current_gap_length = 0
    found_first_one = False
    
    for bit in binary_representation:
        if bit == '1':
            if found_first_one:
                # We found the end of a gap, update max if current is longer
                max_gap_length = max(max_gap_length, current_gap_length)
            # Mark that we've found the first '1' and reset gap counter
            found_first_one = True
            current_gap_length = 0
        elif bit == '0' and found_first_one:
            # We're in a gap (counting zeros after finding first '1')
            current_gap_length += 1
    
    return max_gap_length

