def moveForward(position, distance,velocity):
    x, y = position # current position
    vx, vy = velocity # current velocity

    # Calculate the new position based on the current position, velocity, and distance
    return (x + vx * distance, y + vy * distance)

position = (3, 2) # initial position
velocity = (2, -1) # initial velocity
dt = 0.1 # time step

for steps in range(20): # loop for 10 steps
    position = moveForward(position, dt, velocity) # update position
    print(f"Step {steps + 1}: Position = {position}") # current position