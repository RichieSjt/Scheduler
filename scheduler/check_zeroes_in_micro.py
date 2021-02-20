def check_zeroes(microprocessors):
    '''
    Method to check if a microprocessor has its time set to zero.

    Args:
        microprocessors (list): A list containing all of the microprocessors objects.
    
    Returns:
        has_zeroes (bool): Wether or not a microprocessor has its time set to zero.
    '''
    has_zeroes = False
    for micro in microprocessors:
        if micro.time == 0:
            has_zeroes = True
            break
    
    return has_zeroes
