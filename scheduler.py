#Authors:
#RichieSjt https://github.com/RichieSjt
#EduardoHerreraJ https://github.com/EduardoHerreraJ

from micro import Microprocessor
from process import Process
from table_row import generate_row
from print_table import print_tables
from previous_time import get_previous_time
from check_zeroes_in_micro import check_zeroes

def generate_tables(mp_n, quantum_time, context_switch_time, stop_time, file_path):
    '''
    Method to generate the final table containing each process data.

    Args:
        mp_n (int): The number of microprocessors.
        quantum_time (int): The quantum expiration time.
        context_switch_time (int): The context switch time.
        stop_time (int): The time the processor waits before executing the next process.
        file_path (String): The file path to the processes data.

    Returns:
        table (list): A list containing rows with each process data.
    '''
    # Time ranges to assign each process a stop time.
    timer_stops = {1: [1, 400, 2], 2: [401, 600, 3],
                3: [601, 800, 4], 4: [801, 10000, 5]}

    # We initialize the lists and dictionaries that we will use throughout the program
    processes = dict()
    table = list()

    file = open(file_path, "r")

    for idx, line in enumerate(file):
        temp = line.rstrip('\n').split()
        # Creating the processes with their respective letter identifier, execution time and startup limit
        processes[temp[0]] = Process(temp[0], int(temp[1]), int(temp[2]))

    # The priority is defined
    priority = ["B", "D", "F", "H", "J", "L", "N", "O",
                "A", "C", "E", "G", "I", "K", "M", "P", "W"]

    # Initializing the processors with a time of 0 and a local counter for each process that enters
    microprocessors = [Microprocessor(i, 0, 0) for i in range(mp_n)]

    # We initialize the counter to 0 to start going through the list of processes
    # in the order established in the priority list
    priority_counter = 0

    # While there are still processes we assign them to a processor
    while processes:
        process_key = priority[priority_counter]

        # We go through the processors to see which one has the
        # smallest time and assign it a process
        min_time = 100000
        min_processor_time = -1

        for i in range(mp_n):
            # If it finds a processor that does not have processes yet
            # (its time is zero) it takes it
            if(microprocessors[i].time == 0):
                min_processor_time = i
                break
            else:
                if check_zeroes(microprocessors):
                    continue
                else:
                    if processes[process_key].start_limit > microprocessors[i].time:
                        microprocessors[i].time = processes[process_key].start_limit
                        min_processor_time = i
                        break

                    # If the processors have a time greater than 0,
                    # it looks for the processor with the lower final time
                    if microprocessors[i].time <= min_time:
                        min_time = microprocessors[i].time
                        min_processor_time = i

        # If it is the first process of the processor, then the initial time is equal to 0
        if microprocessors[min_processor_time].local_process_counter == 0:
            initial_time = 0
        else:
            # If it is not the first process of the processor,
            # the initial time is equal to the final time of the previous process
            initial_time = get_previous_time(min_processor_time, table)
            if initial_time < processes[process_key].start_limit:
                initial_time = processes[process_key].start_limit

        # We store the generated row
        table.append(generate_row(microprocessors, processes, min_processor_time, priority_counter,
                                process_key, processes[process_key].execution_time, timer_stops, quantum_time, 
                                context_switch_time, stop_time, initial_time))

        # We remove the process from our list
        del processes[process_key]

        # We increase the microprocessor's process counter
        microprocessors[min_processor_time].local_process_counter += 1
        #We add to the processor the total execution time of the process
        microprocessors[min_processor_time].time += table[len(table)-1][6]

        # When the process ends, we look for the next item in the priority list
        priority_counter += 1

    # The method is called to print the tables separately for each microprocessor
    print_tables(table, mp_n)
    return(table)
