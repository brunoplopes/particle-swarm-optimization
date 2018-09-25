import sys
# Change directory to access the pyswarms module
sys.path.append('../')
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.formatters import Mesher
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation, rc

# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k': 2, 'p': 2}

#LOCAL
# Call instance of PSO
optimizer = ps.single.LocalBestPSO(n_particles=100, dimensions=2, options=options)

# Perform optimization
cost, pos = optimizer.optimize(fx.sphere_func, print_step=100, iters=100, verbose=3)

#GLOBAL
# optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=2, options=options)
# optimizer.optimize(fx.sphere_func, iters=100, verbose=3)

from pyswarms.utils.plotters.formatters import Designer
d = Designer(limits=[(-1,1), (-1,1), (-0.1,1)], label=['x-axis', 'y-axis', 'z-axis'])
m = Mesher(func=fx.sphere_func)



pos_history_3d = m.compute_history_3d(optimizer.pos_history)

animation3d = plot_surface(pos_history=pos_history_3d, # Use the cost_history we computed
                           mesher=m, designer=d,       # Customizations
                           mark=(0,0,0))               # Mark minima

# Enables us to view it in a Jupyter notebook
animation3d.save('plot_surface_local.gif', writer='imagemagick', dpi=96)
print("animation")