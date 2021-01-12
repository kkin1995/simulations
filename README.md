# Numerical Simulations

## Install the required dependencies:

```
pip3 install -r requirements.txt
```

## 1. Simple Pendulum

To execute:

Edit the file "parameters.yaml" to modify the parameters for the Pendulum.

For Python:
```
python3 simple-pendulum/all_in_one.py
```

The file "simple-pendulum.py" has the implementation of Runge-Kutta 4th Order Method solving the equation of motion.

For the Phase Space trajectory, use the file "phase_space.py"
For plotting the energy, use the file "energy.py"

If you are importing into a different file, copy the "simple-pendulum.py" into the same folder and add the following line to beginning of your file:

```
from simple-pendulum import SimplePendulum
```

For Julia:
```
julia simple-pendulum.jl [Initial Angle]
```

If you are importing into a different file, copy the "simple-pendulum.jl" into the same folder and add the following line to beginning of your file:

```
include("./simple-pendulum.jl")
using .SimplePendulumSimulation
import Plots.savefig
```

Specify the initial angle of the simple pendulum as a command line argument.

To build the TeX file in simple-pendulum/theory/

```
chmod +x make.sh
./make.sh
```
