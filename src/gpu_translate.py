import pandas as pd
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

class Benchmarks():

    def gpu_benchmark(choice):
        pd.set_option('display.expand_frame_repr', False)
        df = pd.read_csv('../data/gpu_benchmarks.csv')
        df = pd.DataFrame.set_index(df, keys="gpuName")
        df = df.drop('TDP', axis=1)
        df = df.drop('powerPerformance', axis=1)
        df = df.drop('testDate', axis=1)
        df = df.drop('category', axis=1)
        if (choice == "1"):
            print(df.head(5))
        elif (choice == "2"):
            print(df.head(10))
        elif (choice == "3"):
            print(df.head(25))