import os
import sys
from gpu_translate import Benchmarks
from gpu_translate import Specs

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

def gpu_main():
    print(f"""\nChoose what GPU Information you would like to see:
    1: Top GPU scores in G3Dmark
    2: Highest priced GPUs
    3: Best price to performance GPUs
    4: Newest to Oldest GPU
    5: PCIE type occurances
    6: GPU memory type
    7: Return to home""")
    gpu_choice = input("Enter num choice: ")

    if (gpu_choice == "1"):
        print(f"""How many would you like to see:
        1: 5 GPUs
        2: 10 GPUs
        3: 20 GPUs""")
        benchmark_choice = input("Enter choice: ")
        if (benchmark_choice == "1"):
            Benchmarks.gpu_benchmark(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "2"):
            Benchmarks.gpu_benchmark(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "3"):
            Benchmarks.gpu_benchmark(benchmark_choice)
            gpu_main()
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            gpu_main()
    
    elif (gpu_choice == "2"):
        print(f"""How many would you like to see:
        1: 5 GPUs
        2: 10 GPUs
        3: 20 GPUs
        4: 50 GPUs""")
        benchmark_choice = input("Enter choice: ")
        if (benchmark_choice == "1"):
            Benchmarks.gpu_price(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "2"):
            Benchmarks.gpu_price(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "3"):
            Benchmarks.gpu_price(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "4"):
            Benchmarks.gpu_price(benchmark_choice)
            gpu_main()
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            gpu_main()

    elif (gpu_choice == "3"):
        print(f"""How many would you like to see:
        1: 5 GPUs
        2: 10 GPUs
        3: 20 GPUs
        4: 50 GPUs""")
        benchmark_choice = input("Enter choice: ")
        if (benchmark_choice == "1"):
            Benchmarks.gpu_performance_price(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "2"):
            Benchmarks.gpu_performance_price(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "3"):
            Benchmarks.gpu_performance_price(benchmark_choice)
            gpu_main()
        elif (benchmark_choice == "4"):
            Benchmarks.gpu_performance_price(benchmark_choice)
            gpu_main()
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            gpu_main()

    elif (gpu_choice == "4"):
        print(f"""How many would you like to see:
        1: 5 GPUs
        2: 10 GPUs
        3: 20 GPUs
        4: 50 GPUs""")
        specs_choice = input("Enter choice: ")
        if (specs_choice == "1"):
            Specs.gpu_years(specs_choice)
            gpu_main()
        elif (specs_choice == "2"):
            Specs.gpu_years(specs_choice)
            gpu_main()
        elif (specs_choice == "3"):
            Specs.gpu_years(specs_choice)
            gpu_main()
        elif (specs_choice == "4"):
            Specs.gpu_years(specs_choice)
            gpu_main()
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            gpu_main()

    elif (gpu_choice == "5"):
        print(f"""What PCIE Tye would you like to see the number of:
        1: PCIe 4.0 x16
        2: PCIe 4.0 x8
        3: PCIe 4.0 x4
        4: PCIe 5.0 x16
        5: PCIe 3.0 x16
        6: PCIe 3.0 x8
        7: PCIe 3.0 x4
        8: Ring Bus
        9: IGP""")
        specs_choice = input("Enter choice: ")
        if (specs_choice == "1"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "2"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "3"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "4"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "5"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "6"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "7"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "8"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        elif (specs_choice == "9"):
            Specs.gpu_PCIE_type(specs_choice)
            gpu_main()
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            gpu_main()

    elif (gpu_choice == "6"):
        print(f"""What Memory Tye would you like to see the number of:
        1: GDDR6
        2: GDDR6X
        3: GDDR5
        4: GDDR5X
        5: DDR4
        6: DDR3
        7: DDR2
        8: System Shared
        9: HBM2e
        0: HBM2""")
        specs_choice = input("Enter choice: ")
        if (specs_choice == "1"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "2"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "3"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "4"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "5"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "6"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "7"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "8"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "9"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        elif (specs_choice == "0"):
            Specs.gpu_memory_type(specs_choice)
            gpu_main()
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            gpu_main()

    elif (gpu_choice == "7"):
        print("Thank You for using GPU Information\n")