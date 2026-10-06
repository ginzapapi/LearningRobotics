class Particle:
    def __init__(self, x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

particles = [
    Particle(x=3, y=2, vx=2, vy=-1), 
    Particle(x=0, y=0, vx=1, vy=0.5),
    Particle(x=1.0, y=1.0, vx=-0.5, vy=0.0)
]


period = 2.0 # total time of simulation
dt = 0.1 # time step
step_count = round(period / dt) # number of steps

for step in range(step_count):
    print(f"Step {step+1}:")
    for index, particle in enumerate(particles):
        particle.update(dt)
        print(
            f"Particle {index+1}: Position=({particle.x:.2f}, {particle.y:.2f}), Velocity=({particle.vx:.2f}, {particle.vy:.2f})"
        )