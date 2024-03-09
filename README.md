# Disk Scheduling
 A crappy visualization of disk scheduling algorithms in operation systems.

# Requirements
- Python 3.8 or later
- Pygame module (lmao)

# How to use
 In the main file, there are variables that you can change:
- `entries` : The position of the addresses you want to read, where `entries[0]` is the read-hand (`entries[0]` and `entries[1]` shouldn't be the same, if itdoes  then just remove until they don't please).
- `min_val` and `max_val`: boundaries of the disk (`min_val` should always be 0 though).

 When run the program using the `main.py`, press LeftArrow or RightArrow to navigate through algorithms. There are names and the number of track movements (ex: `FCFS 100` means it's the First Come First Serve and the no. track movements is 100).

# Extra notes
- Need extra testing lmao
- The FCFS algorithm is named `fifo` in the files because it's similar to each other.