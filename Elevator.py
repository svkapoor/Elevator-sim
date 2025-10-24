"""
Elevator Simulation
-----------------------------------
Simulates one elevator moving between floors with basic pickup and drop requests.

Run:
  python3 elevator_simple.py

Commands:
  p <floor>   — Add a pickup request
  s           — Show current state
  q           — Quit simulation

Assumptions:
  - Building has floors 0 to 10
  - One elevator only

Not Implemented:
  - Multiple elevators
  - Capacity or timing metrics
"""

import time

class Elevator:
    # Initalize
    def __init__(self, min_floor=0, max_floor=10):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = 0
        self.direction = "IDLE"
        self.doors_open = False
        self.door_timer = 0
        self.targets = []

    # Tells what to print when object is called for printing
    def __str__(self):
        return (f"Floor: {self.current_floor} | Direction: {self.direction} | "
                f"Doors: {'Open' if self.doors_open else 'Closed'} | Targets: {list(self.targets)}")
    
    # Adding to elevator list
    def add_request(self, floor):
        if self.min_floor <= floor <= self.max_floor and floor not in self.targets:
            self.targets.append(floor)
        


    def step(self):
        self.doors_open = False
        # If not target floors elevator is idle
        if self.targets and self.current_floor in self.targets:
            self.targets.remove(self.current_floor)
            self.open_doors()
        elif not self.targets:
            self.direction = "IDLE"
            return
        elif self.targets and min(self.targets) > self.current_floor:
            self.direction = "UP"
            self.current_floor += 1
        elif self.targets and max(self.targets) < self.current_floor:
            self.direction = "DOWN"
            self.current_floor -= 1
            
    # Open doors for timer length
    def open_doors(self):
        self.doors_open = True
        

def main():
    elevator = Elevator()
    tick = 0

    print("Commands: p <floor> | s | q")

    while True:
        elevator.step()
    
        if tick % 1 == 0:
            print(f"Tick {tick}: {elevator}")
            print("Please input command: ", end="")
        

        time.sleep(0.3)
        tick += 1

        try:
            if tick % 1 == 0:
                # Gets input
                cmd = input("").strip()

                # Quit program
                if cmd == 'q':
                    break
                elif cmd == 's':
                    pass
                # Show state
                elif cmd.startswith('p '):
                    parts = cmd.split()
                    if len(parts) == 2 and parts[1].isdigit():
                        floor = int(parts[1])
                        elevator.add_request(floor)
                else:
                    print("Enter a valid command")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
