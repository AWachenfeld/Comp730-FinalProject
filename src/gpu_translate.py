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

    def gpu_price(choice):
        pd.set_option('display.expand_frame_repr', False)
        df = pd.read_csv('../data/gpu_benchmarks.csv')
        df = pd.DataFrame.set_index(df, keys="gpuName")
        df = df.drop('TDP', axis=1)
        df = df.drop('powerPerformance', axis=1)
        df = df.drop('testDate', axis=1)
        df = df.drop('category', axis=1)
        sorted_df = df.sort_values(by=["price"], ascending=False)
        if (choice == "1"):
            print(sorted_df.head(5))
        elif (choice == "2"):
            print(sorted_df.head(10))
        elif (choice == "3"):
            print(sorted_df.head(25))
        elif (choice == "4"):
            print(sorted_df.head(50))

    def gpu_performance_price(choice):
        pd.set_option('display.expand_frame_repr', False)
        df = pd.read_csv('../data/gpu_benchmarks.csv')
        df = pd.DataFrame.set_index(df, keys="gpuName")
        df = df.drop('TDP', axis=1)
        df = df.drop('powerPerformance', axis=1)
        df = df.drop('testDate', axis=1)
        df = df.drop('category', axis=1)
        value_df = df.sort_values(by=["gpuValue"], ascending=False)
        if (choice == "1"):
            print(value_df.head(5))
        elif (choice == "2"):
            print(value_df.head(10))
        elif (choice == "3"):
            print(value_df.head(25))
        elif (choice == "4"):
            print(value_df.head(50))

class Specs():

    def gpu_years(choice):
        pd.set_option('display.expand_frame_repr', False)
        df = pd.read_csv('../data/gpu_specs.csv')
        df = pd.DataFrame.set_index(df, keys="productName")
        df = df.drop('memBusWidth', axis=1)
        df = df.drop('unifiedShader', axis=1)
        df = df.drop('tmu', axis=1)
        df = df.drop('rop', axis=1)
        df = df.drop('pixelShader', axis=1)
        df = df.drop('vertexShader', axis=1)
        value_df = df.sort_values(by=["releaseYear"], ascending=False)
        if (choice == "1"):
            print(value_df.head(5))
        elif (choice == "2"):
            print(value_df.head(10))
        elif (choice == "3"):
            print(value_df.head(25))
        elif (choice == "4"):
            print(value_df.head(50))

    def gpu_PCIE_type(choice):
        pd.set_option('display.expand_frame_repr', False)
        df = pd.read_csv('../data/gpu_specs.csv')
        df = pd.DataFrame.set_index(df, keys="productName")
        df = df.drop('memBusWidth', axis=1)
        df = df.drop('unifiedShader', axis=1)
        df = df.drop('tmu', axis=1)
        df = df.drop('rop', axis=1)
        df = df.drop('pixelShader', axis=1)
        df = df.drop('vertexShader', axis=1)
        if (choice == "1"):
            print(df['bus'].value_counts()["PCIe 4.0 x16"])
            print(" GPUs Have PCIe 4.0 x16 as their PCIE type")
        elif (choice == "2"):
            print(df['bus'].value_counts()["PCIe 4.0 x8"])
            print(" GPUs Have PCIe 4.0 x8 as their PCIE type")
        elif (choice == "3"):
            print(df['bus'].value_counts()["PCIe 4.0 x4"])
            print(" GPUs Have PCIe 4.0 x4 as their PCIE type")
        elif (choice == "4"):
            print(df['bus'].value_counts()["PCIe 5.0 x16"])
            print(" GPUs Have PCIe 5.0 x16 as their PCIE type")
        elif (choice == "5"):
            print(df['bus'].value_counts()["PCIe 3.0 x16"])
            print(" GPUs Have PCIe 3.0 x16 as their PCIE type")
        elif (choice == "6"):
            print(df['bus'].value_counts()["PCIe 3.0 x8"])
            print(" GPUs Have PCIe 3.0 x8 as their PCIE type")
        elif (choice == "7"):
            print(df['bus'].value_counts()["PCIe 3.0 x4"])
            print(" GPUs Have PCIe 3.0 x4 as their PCIE type")
        elif (choice == "8"):
            print(df['bus'].value_counts()["Ring Bus"])
            print(" GPUs Have Ring Bus as their PCIE type")
        elif (choice == "9"):
            print(df['bus'].value_counts()["IGP"])
            print(" GPUs Have IGP as their PCIE type")

    def gpu_memory_type(choice):
        pd.set_option('display.expand_frame_repr', False)
        df = pd.read_csv('../data/gpu_specs.csv')
        df = pd.DataFrame.set_index(df, keys="productName")
        df = df.drop('memBusWidth', axis=1)
        df = df.drop('unifiedShader', axis=1)
        df = df.drop('tmu', axis=1)
        df = df.drop('rop', axis=1)
        df = df.drop('pixelShader', axis=1)
        df = df.drop('vertexShader', axis=1)
        if (choice == "1"):
            print(df['memType'].value_counts()["GDDR6"])
            print(" GPUs Have GDDR6 as their PCIE type")
        elif (choice == "2"):
            print(df['memType'].value_counts()["GDDR6X"])
            print(" GPUs Have GDDR6X as their PCIE type")
        elif (choice == "3"):
            print(df['memType'].value_counts()["GDDR5"])
            print(" GPUs Have GDDR5 as their PCIE type")
        elif (choice == "4"):
            print(df['memType'].value_counts()["GDDR5X"])
            print(" GPUs Have GDDR5X as their PCIE type")
        elif (choice == "5"):
            print(df['memType'].value_counts()["DDR4"])
            print(" GPUs Have DDR4 as their PCIE type")
        elif (choice == "6"):
            print(df['memType'].value_counts()["DDR3"])
            print(" GPUs Have DDR3 as their PCIE type")
        elif (choice == "7"):
            print(df['memType'].value_counts()["DDR2"])
            print(" GPUs Have DDR2 as their PCIE type")
        elif (choice == "8"):
            print(df['memType'].value_counts()["System Shared"])
            print(" GPUs Have System Shared as their PCIE type")
        elif (choice == "9"):
            print(df['memType'].value_counts()["HBM2e"])
            print(" GPUs Have HBM2e as their PCIE type")
        elif (choice == "0"):
            print(df['memType'].value_counts()["HBM2"])
            print(" GPUs Have HBM2 as their PCIE type")