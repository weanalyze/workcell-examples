# TSP, Travelling salesman problem
import math
import random
from typing import Dict
import gurobipy as gp
import plotly.express as px
from itertools import combinations
from pydantic import BaseModel
from workcell.integrations.types import PlotlyPlot


# Callback - use lazy constraints to eliminate sub-tours
def subtourelim(model, where):
    if where == gp.GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        # find the shortest cycle in the selected edge list
        tour = subtour(model, vals)
        n = model._num_cities
        if len(tour) < n:
            # add subtour elimination constr. for every pair of cities in tour
            model._subtours += 1
            model.cbLazy(gp.quicksum(model._vars[i, j]
                                     for i, j in combinations(tour, 2))
                         <= len(tour)-1)


# Given a tuplelist of edges, find the shortest subtour
def subtour(model, vals):
    # make a list of edges selected in the solution
    edges = gp.tuplelist((i, j) for i, j in vals.keys()
                         if vals[i, j] > 0.5)
    # num of cities
    n = model._num_cities
    unvisited = list(range(n))
    cycle = range(n+1)  # initial length has 1 more city
    while unvisited:  # true if list is non-empty
        thiscycle = []
        neighbors = unvisited
        while neighbors:
            current = neighbors[0]
            thiscycle.append(current)
            unvisited.remove(current)
            neighbors = [j for i, j in edges.select(current, '*')
                         if j in unvisited]
        if len(cycle) > len(thiscycle):
            cycle = thiscycle
    return cycle

# Grobi Optimization 
def optimize_model(points, dist):
    # Init gurobi model
    m = gp.Model()
    m._subtours = 0
    n = len(points)
    m._num_cities = n
    # Create variables
    vars = m.addVars(dist.keys(), obj=dist, vtype=gp.GRB.BINARY, name='e')
    for i, j in vars.keys():
        vars[j, i] = vars[i, j]  # edge in opposite direction
    # Add degree-2 constraint
    m.addConstrs(vars.sum(i, '*') == 2 for i in range(n))    
    # Optimize model
    m._vars = vars
    m.Params.LazyConstraints = 1
    m.optimize(subtourelim)
    # Validation
    vals = m.getAttr('X', vars)
    tour = subtour(m, vals)
    assert len(tour) == n    
    print(tour, n)
    # Return value
    plan_tour = {
        'opt_runtime': m.Runtime,
        'opt_cost': m.ObjVal,
        'subtour_constraint': m._subtours
    }
    points_tour = [points[i] for i in tour+[tour[0]]]
    return points_tour, plan_tour

# Plot by plotly
def plot_tour(points_tour):
    n = len(points_tour) - 1
    fig = px.line(x=[x[0] for x in points_tour], 
                  y=[x[1] for x in points_tour], 
                  title="Travelling salesman problem: n={}".format(n),
                  width=600, height=600)
    fig.add_scatter(x=[x[0] for x in points_tour], 
                    y=[x[1] for x in points_tour], 
                    mode='markers')
    fig.update_layout(legend=dict(
        orientation="h",
        entrywidth=70,
        yanchor="bottom",
        y=0.9,
        xanchor="right",
        x=1
    ))
    return fig


# Main TSP workcell
class Input(BaseModel):
    n: int # number of cities

class Output(BaseModel):
    plan: Dict # plan cost
    plot: PlotlyPlot # plotly plot

def gurobi_tsp(input: Input) -> Output:
    """gurobi_tsp, a showcase using gurobi to optimize travelling salesman problem."""
    # Create n random points
    n = input.n
    points = [(random.randint(0,100),random.randint(0,100)) for i in range(n)]
    # Dictionary of Euclidean distance between each pair of points
    dist = {(i,j) :
        math.sqrt(sum((points[i][k]-points[j][k])**2 for k in range(2)))
        for i in range(n) for j in range(i)}
    # Optimization
    points_tour, plan_tour = optimize_model(points, dist)
    # Plot
    fig = plot_tour(points_tour)
    # Output
    output = Output(
        plan=plan_tour,
        plot=PlotlyPlot(data=fig)
    )
    return output


