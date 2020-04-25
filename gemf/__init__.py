
""" Main package for GEMF the general ecosystem modelling framework """

import gemf.caller
import gemf.models
import gemf.plot

from gemf.models import model_class as model_class

from gemf.caller import forward_model as forward_model 
from gemf.caller import inverse_model as inverse_model
from gemf.caller import time_evolution as time_evolution

from gemf.plot import output_summary as output_summary
from gemf.plot import interaction_graph as interaction_graph


