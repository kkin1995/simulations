# Numerical Simulations

## 1. Simple Pendulum

To execute:

For Python:
```
python3 simple-pendulum.py [Initial Angle]
```

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