def get_valid_input(prompt, data_type=int, min_val=0, error_message="Invalid input."):
    """Helper function for robust numerical input."""
    while True:
        try:
            value = data_type(input(prompt))
            if value >= min_val:
                return value
            print(f"Error: Value must be at least {min_val}.")
        except ValueError:
            print(error_message)

def get_user_processes_data():
    """Prompts the user for all process details and returns a list of (PID, AT, BT)."""
    processes_data = []
    
    print("--- FCFS Process Input ---")
    num_processes = get_valid_input(
        prompt="Enter the number of processes: ", 
        min_val=1, 
        error_message="Invalid input. Please enter a positive whole number."
    )

    for i in range(num_processes):
        # PID is automatically generated (1, 2, 3, ...)
        pid = i + 1
        print(f"\n--- Details for Process {pid} of {num_processes} (P{pid}) ---")
        
        # Get Arrival Time (AT)
        arrival_time = get_valid_input(
            prompt=f"Enter Arrival Time (AT) for P{pid}: ", 
            min_val=0, 
            error_message="Invalid AT. Arrival Time cannot be negative."
        )
        
        # Get Burst Time (BT)
        burst_time = get_valid_input(
            prompt=f"Enter Burst Time (BT) for P{pid}: ", 
            min_val=1, 
            error_message="Invalid BT. Burst Time must be a positive integer."
        )
        
        processes_data.append((pid, arrival_time, burst_time))
        
    return processes_data

def run_fcfs_simulation(processes_data):
    """
    Calculates FCFS metrics for processes with non-zero Arrival Times (AT).
    Input: List of tuples (PID, AT, BT)
    """
    
    # 1. Sort by Arrival Time (AT) – Index 1 in the tuple
    processes_data.sort(key=lambda x: x[1]) 
    
    n = len(processes_data)
    
    # Lists to store results
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    start_time = [0] * n
    
    cpu_current_time = 0 

    for i in range(n):
        pid, at, bt = processes_data[i]
        
        # Start Time: The later of (CPU free time OR Process arrival time)
        start_time[i] = max(cpu_current_time, at)
        
        # Completion Time (CT) = Start Time + BT
        completion_time[i] = start_time[i] + bt
        
        # Turnaround Time (TAT) = CT - AT
        turnaround_time[i] = completion_time[i] - at
        
        # Waiting Time (WT) = Start Time - AT
        waiting_time[i] = start_time[i] - at
        
        # Update CPU clock
        cpu_current_time = completion_time[i]

    # Display Results
    print("\n" + "="*50)
    print("--- FCFS Scheduling Results ---")
    print("="*50)
    
    print(f"{'P. ID':<8}{'A. Time':<8}{'B. Time':<8}{'Start':<8}{'C. Time':<8}{'TAT':<8}{'W. Time':<8}")
    print("-" * 50)
    
    total_wt = 0
    total_tat = 0
    
    for i in range(n):
        pid, at, bt = processes_data[i]
        total_wt += waiting_time[i]
        total_tat += turnaround_time[i]
        print(f"{pid:<8}{at:<8}{bt:<8}{start_time[i]:<8}{completion_time[i]:<8}{turnaround_time[i]:<8}{waiting_time[i]:<8}")

    # Print Averages
    print("\n--- Summary ---")
    print(f"Average Waiting Time: {total_wt / n:.2f} units")
    print(f"Average Turn Around Time: {total_tat / n:.2f} units")
    print("-----------------\n")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    
    # 1. Get user input
    user_processes = get_user_processes_data()

    if user_processes:
        # 2. Run the simulation and print results
        run_fcfs_simulation(user_processes)
    else:
        print("No processes entered. Exiting.")