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
    5: Return to home""")
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

    if (gpu_choice == "4"):
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
        print("Thank You for using GPU Information\n")