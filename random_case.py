import random
import comm_manip 

command = comm_manip.comm_join()

def get_list_alpha_char():
    alpha_indexes = []
    for char_ind in range(len(command)):
        current_char = command[char_ind]
        if current_char.isalpha():
            alpha_indexes.append(char_ind)
    return alpha_indexes

def assign_random_case():
    alpha_indexes = get_list_alpha_char()
    random_alpha_indexes = random.sample(alpha_indexes, random.randrange(1, len(alpha_indexes)))
    return random_alpha_indexes

def replace_char():
    random_alpha_indexes = assign_random_case()
    copy_comm = []
    for index in range(len(command)):
        if index in random_alpha_indexes:
            copy_comm.append(command[index].upper())
        else:
            copy_comm.append(command[index])
    return copy_comm

def rand_join():
    print("".join(replace_char()))
