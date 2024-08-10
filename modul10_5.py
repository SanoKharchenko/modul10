import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
#
# start_line = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# end_line = datetime.datetime.now()
# print(end_line - start_line)
#  0:00:03.225168

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:

        start_multi = datetime.datetime.now()
        pool.map(read_info, filenames)
    end_multi = datetime.datetime.now()
    print(end_multi - start_multi)
#  0:00:01.419741