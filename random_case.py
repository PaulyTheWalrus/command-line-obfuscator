import random
import comm_manip 

def list_alpha_char():
    alpha_indexes = []
    command = comm_manip.script
    for char_ind in range(len(command)):
        current_char = command[char_ind]
        if current_char.isalpha():
            alpha_indexes.append(char_ind)
    return alpha_indexes

def random_case():
    alpha_indexes = list_alpha_char()
    random_alpha_indexes = random.sample(alpha_indexes, random.randrange(1, len(alpha_indexes)))
    return random_alpha_indexes

def replace_char():
    random_alpha_indexes = random_case()
    copy_comm = []
    for index in range(len(comm_manip.script)):
        if index in random_alpha_indexes:
            copy_comm.append(comm_manip.script[index].upper())
        else:
            copy_comm.append(comm_manip.script[index])
    return copy_comm

def rand_join():
    print("".join(replace_char()))

rand_join()