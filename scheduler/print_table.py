def print_tables(table, mp_n):
    '''
    Method to separate the tables by microprocessors and be able to display them in the terminal.

    Args:
        table (list): A list containing rows with each process data.
        mp_n (int): The number of microprocessors.
    '''
    for i in range(mp_n):
        print("")
        print("---- Microprocessor", i+1, "----")
        for j in range(len(table)):
            if(table[j][0] == i):
                print(table[j])