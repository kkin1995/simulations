using Plots

#Getting the initial parameters
println("Enter the angle in degrees: ")
theta = readline()
theta = parse(Float64,theta)
#theta = 45
theta = π*(theta/180)
println("Give me an initial velocity: ")
u = readline()
u = parse(Float64,u)
println("Give me the value of gravitational acceleration: ")
#u = 12
g = readline()
g = parse(Float64,g)
#g = 10

#Formulas
distance = (u^2)*sin(2*theta)/g
time_of_flight = 2*u*(sin(theta)/g)
Δt = time_of_flight/100

#Creating time steps
time_array = Float64[0.0]
for i=1:100
    push!(time_array,time_array[end]+Δt)
end

#printing values to verify
println(time_array)
println(length(time_array))
println(time_of_flight)
println(distance)

x = Float64[]
y = Float64[]
for j = 1:101
    push!(x, u*time_array[j]*cos(theta))
    push!(y,u*sin(theta)*time_array[j] - (0.5*g*time_array[j]^2))
end

#Building the animation
max_x = findmax(x)
max_y = findmax(y)

anim = Plots.Animation()
for i = 1:1:length(x)
    scatter(x[1:i],y[1:i],xlim = (0,max_x[1]+1), ylim = (0,max_y[1]+1),label = "position at a given time step",title = "Projectile_motion Trajectory_animation")
    xlabel!("length(in meters)-->")
    ylabel!("height(in meters)-->")
    Plots.frame(anim)
end 

gif(anim, "trajectory.gif",fps = 30)
