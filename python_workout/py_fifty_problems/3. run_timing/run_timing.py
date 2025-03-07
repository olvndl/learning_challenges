def run_timing():
    total_time = 0
    total_runs = 0

    while True:
        run_today = input("Input total time for today's run: ")
        if not run_today:
            break
        total_time += float(run_today)
        total_runs += 1

    average_run_time = total_time / total_runs
    print(
        f"\nAverage running time: {average_run_time}\nTotal runs: {total_runs}")


run_timing()
