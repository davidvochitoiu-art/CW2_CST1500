

class Process:

    """Holds process data and calculates metrics."""
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        
        # Results (calculated later)
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def get_user_processes():
    """Prompts the user for the number of processes, then for the custom PID, AT, and BT of each."""
    
    processes = []
    
    # 1. Get the number of processes
    while True:
        try:
            num_processes = int(input("Enter the number of processes you want to define: "))
            if num_processes > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # 2. Get the custom PID, Arrival Time (AT), and Burst Time (BT) for each process
    for i in range(num_processes):
        print(f"\n--- Entering details for Process #{i + 1} of {num_processes} ---")
        
        # Get CUSTOM Process ID (PID)
        while True:
            try:
                # FIX: Prompt for the custom PID (e.g., 101, 250, etc.)
                pid = int(input(f"Enter the Process ID (PID) for this process: "))
                if pid > 0:
                    break
                print("PID must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a whole number for the PID.")

        # Get Burst Time (BT)
        while True:
            try:
                bt = int(input(f"Enter Burst Time (BT) for P{pid}: "))
                if bt > 0:
                    break
                print("Burst Time must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a number for BT.")
        
        # Get Arrival Time (AT)
        while True:
            try:
                at = int(input(f"Enter Arrival Time (AT) for P{pid}: "))
                if at >= 0:
                    break
                print("Arrival Time cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a number for AT.")
        
        # Create the Process object
        processes.append(Process(pid=pid, arrival_time=at, burst_time=bt))
        
    return processes

def run_fcfs_simulation(processes):
    """Calculates all metrics based on the FCFS rule: sort by arrival time."""
    
    # FCFS Rule: Execute in the order they arrive (Arrival Time).
    # This is the core logic.
    processes.sort(key=lambda p: p.arrival_time)
    
    cpu_current_time = 0 

    for p in processes:
        
        # Start Time: CPU starts the process at the later of (current time OR arrival time).
        p_start_time = max(cpu_current_time, p.arrival_time)
        
        # Calculate all metrics
        p.completion_time = p_start_time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p_start_time - p.arrival_time
        
        # Update the CPU clock
        cpu_current_time = p.completion_time

    return processes

def print_results(processes):
    """Displays the final calculated results clearly."""
    
    if not processes:
        print("No processes were entered.")
        return
        
    print("\n" + "="*58)
    print("--- FCFS Scheduling Results ---")
    print("="*58)
    
    # Header
    # Note: The table now uses the custom PID entered by the user.
    print(f"{'P. ID':<8}{'A. Time':<10}{'B. Time':<10}{'C. Time':<10}{'TAT':<10}{'W. Time':<10}")
    print("-" * 58)
    
    total_wt = 0
    total_tat = 0

    # Print data and accumulate totals
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
        print(f"{p.pid:<8}{p.arrival_time:<10}{p.burst_time:<10}{p.completion_time:<10}{p.turnaround_time:<10}{p.waiting_time:<10}")

    # Calculate and display simple averages
    num_processes = len(processes)
    avg_wt = total_wt / num_processes
    avg_tat = total_tat / num_processes
    
    print("\n--- Summary ---")
    print(f"Average Waiting Time: {avg_wt:.2f} units")
    print(f"Average Turn Around Time: {avg_tat:.2f} units")
    print("-----------------\n")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    
    # 1. Get all process data from the user
    user_processes = get_user_processes()

    # 2. Run the simulation
    scheduled_processes = run_fcfs_simulation(user_processes)

    # 3. Print the results
    print_results(scheduled_processes)