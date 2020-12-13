def FCFS():
    n = int(input("enter number of processes in integer value:"))
    brust_dict = {}
    arival_dict = {}
    process_name = []
    cpu = 0

    print('Enter Brust times and process names')
    for i in range(n):
        keys = input("enter name of process ")  # here i have taken keys as strings
        values = int(input("enter brust time of the process "))  # here i have taken values as integers
        brust_dict[keys] = values
        process_name.append(keys)
    print("Brust times", brust_dict)

    print('Enter Arrival times')
    for i in process_name:
        values = int(input("enter arival time of the process "))  # here i have taken values as integers
        arival_dict[i] = values
    print("Average times", arival_dict)

    ready_que = []
    temp = []
    cpu_lst = []

    for i in range(n):
        key_min = min(arival_dict.keys(), key=(lambda k: arival_dict[k]))

        while cpu != arival_dict[key_min]:
            cpu = cpu + 1
        temp.append(cpu)

        if cpu == arival_dict[key_min]:
            for key, value in arival_dict.items():
                if value == arival_dict[key_min]:
                    break
            ready_que.append(key)
            arival_dict.pop(key)
    cpu_lst.append(temp[0])

    for i in ready_que:
        val = brust_dict.get(i)
        cpu_lst.append(cpu_lst[-1] + val)

    TAT_lst = []
    for i in cpu_lst:
        TAT_lst.append(i)

    TAT_lst.pop(0)
    cpu_lst.pop()
    print('ready que', ready_que)
    print(cpu_lst)
    print(TAT_lst)
    avg_waiting_time = sum(cpu_lst) / len(cpu_lst)
    print("Average Waiting time : " , avg_waiting_time , ' units')
    turn_around_time = sum(TAT_lst) / len(TAT_lst)
    print("Turn around time is " ,turn_around_time, " units")


FCFS()