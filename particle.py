import matplotlib.pyplot as plt

class Particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.history_x = [x]
        self.history_y = [y]

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.history_x.append(self.x)
        self.history_y.append(self.y)


# Create the particles.
particles = [
    Particle(x=3.0, y=2.0, vx=2.0, vy=-1.0),
    Particle(x=0.0, y=0.0, vx=1.0, vy=0.5),
    Particle(x=1.0, y=1.0, vx=-0.5, vy=0.0),
]

# Configure the simulation.
duration = 2.0
dt = 0.1
num_steps = round(duration / dt)

# Run the simulation and record each position.
for step in range(num_steps):
    for particle in particles:
        particle.update(dt)

# Display the final results.
for index, particle in enumerate(particles, start=1):
    print(
        f"Particle {index}: "
        f"Position = ({particle.x:.2f}, {particle.y:.2f}), "
        f"{len(particle.history_x)} recorded positions"
    )

# Plot the recorded trajectories.
fig, ax = plt.subplots()

for index, particle in enumerate(particles, start=1):
    line, = ax.plot(
        particle.history_x,
        particle.history_y,
        marker=".",
        label=f"Particle {index}",
    )

    color = line.get_color()

    # Mark the starting position with a circle.
    ax.scatter(
        particle.history_x[0],
        particle.history_y[0],
        color=color,
        marker="o",
        s=80,
    )

    # Mark the final position with a cross.
    ax.scatter(
        particle.history_x[-1],
        particle.history_y[-1],
        color=color,
        marker="x",
        s=80,
    )

ax.set_title("Particle trajectories")
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend()

fig.tight_layout()
plt.show()