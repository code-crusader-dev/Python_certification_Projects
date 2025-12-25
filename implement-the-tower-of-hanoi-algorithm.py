#"start of main.py"

def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),  # source rod
        [],                     # auxiliary rod
        []                      # destination rod
    ]

    output = []

    def record_state():
        output.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move(disks, source, auxiliary, destination):
        if disks == 1:
            rods[destination].append(rods[source].pop())
            record_state()
        else:
            move(disks - 1, source, destination, auxiliary)
            rods[destination].append(rods[source].pop())
            record_state()
            move(disks - 1, auxiliary, source, destination)

    # record initial state
    record_state()

    # solve the puzzle
    move(n, 0, 1, 2)

    return "\n".join(output)


#end of main.py

