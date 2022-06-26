
import json
def process():
    print(1)
    with open("../datasets/big_train_data.json", 'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)

    with open("../datasets/2021_train.json", "r") as dump_f:
        load_example = json.load(dump_f)
        print(load_example)
process()