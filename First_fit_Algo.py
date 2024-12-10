# Define memory blocks and process sizes
memory_Block = [50, 200, 70, 115, 15]  # Available memory block sizes
process = [100, 10, 35, 15, 50]  # Process sizes to allocate

def first_fit_algo(memory_Block, process):
    allocation = [-1] * len(process)  # Track which block each process is assigned to
    for i in range(len(process)):  # Loop through each process
        for j in range(len(memory_Block)):  # Loop through memory blocks
            if memory_Block[j] >= process[i]:  # If block fits the process
                allocation[i] = j  # Assign block index to process
                memory_Block[j] -= process[i]  # Reduce block size
                break
    return allocation


allocation = first_fit_algo(memory_Block, process)

# Display outputs
print("Status of process: ", process)
print("Memory allocation: ", allocation)
print("Remaining memory blocks: ", memory_Block)
