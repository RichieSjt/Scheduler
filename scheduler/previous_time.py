def get_previous_time(processor_id, table):
    '''
    Method to obtain the final time of the previous process.

    Args:
        processor_id (int): The processor id.
        table (list): A list containing rows with each process data.
    
    Returns:
        previous_time (int): The previous process final time.
    '''
    for i in range(len(table)-1, -1, -1):
        #If the processor id matches the assigned processor, then we return the final end time
        if(processor_id == table[i][0]):
            return table[i][8]