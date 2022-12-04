import os
import sys
from gpu_translate import Benchmarks

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

def gpu_main():
    print(f"""\nChoose what Telecom user data you would like to see:
    1: Top GPU scores in G3Dmark
    2: Highest priced GPUs
    3: Return to home""")
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

    elif (telecom_choice == "3"):
        print("Thank You for using GPU Information\n")