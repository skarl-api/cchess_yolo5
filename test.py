import os

label_original_path = "./source/label/"
# total_txt = os.listdir(label_original_path)
# num_txt = len(total_txt)
# list_all_txt = range(num_txt)
# print(total_txt)
# print(num_txt)
# print(list_all_txt)
# 14 0.496637 0.498457 0.834081 0.852881
for label_index in range(2, 100):
    with open("./source/label/%s.txt" % label_index, 'r') as f:
        lines = f.readlines()
        for index, board in enumerate(lines):
            if '14 ' in board:
                lines[index] = "14 0.496637 0.498457 0.834081 0.852881\n"
        with open("./source/label/%s.txt" % label_index, "w") as w:
            for index, board in enumerate(lines):
                w.write(board)

