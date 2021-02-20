import math

def generate_row(microprocessors, processes, assigned_processor, priority_counter, process_key, execution_time, timer_stops, quantum_time, context_switch_time, stop_time, initial_time):
    '''
    Method to obtain each of the table's row using the given data.

    Args:
        microprocessors (list): A list containing all of the microprocessors objects.
        processes (dict): A dictionary containing all of the processes and their data.
        assigned_processor (int): The selected microprocessor id.
        priority_counter (int): The process priority.
        process_key (int): The key to access the process data in the processes dictionary.
        execution_time (int): The accumulated microprocessor execution time.
        timer_stops (dict): A dictionary containing the stop time a process will have depending on its execution time.
        quantum_time (int): The quantum expiration time.
        context_switch_time (int): The context switch time.
        stop_time (int): The time the processor waits before executing the next process.
        initial_time (int): The microprocessor time at which the process is set to start.
    
    Returns:
        data_row (list): A list containing the generated row's data.
    '''

    # If it is the first process in the microprocessor, then the context switch time is 
    # zero, otherwise it is the defined time
    row_context_switch_time = 0
    if (microprocessors[assigned_processor] != 0):
        row_context_switch_time = context_switch_time
    
    if initial_time <= processes[process_key].start_limit:
        row_context_switch_time = 0

    if initial_time < processes[process_key].start_limit:
            initial_time = processes[process_key].start_limit

    # Equation to obtain the quantum expiration time value
    quantum_expiration_time = (math.ceil(execution_time/quantum_time)-1)

    # Depending on the stablished ranges in the timer stops dictionary, the stop time 
    # for the process is set.
    for x in timer_stops:
        temp = timer_stops[x]
        if(execution_time >= temp[0] and execution_time <= temp[1]):
            row_stop_time = stop_time * temp[2]

    total_time = row_context_switch_time + execution_time + quantum_expiration_time + row_stop_time
    final_time = initial_time + total_time

    data_row = [assigned_processor, process_key, row_context_switch_time, execution_time, quantum_expiration_time, row_stop_time, total_time, initial_time, final_time]
    return data_row