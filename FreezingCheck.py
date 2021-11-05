from networkx.classes.function import is_frozen
from networkx.drawing.layout import spring_layout
from UniversalClasses import System, State, TransitionRule
import networkx as nx
import matplotlib.pyplot as plt


def main(system):
    system_graph = nx.DiGraph()  # Initialize graph
    # Grab transitions from current system
    v_transitions = system.returnVerticalTransitionList()
    h_transitions = system.returnHorizontalTransitionList()

    # For each vertical transition...
    for rule in v_transitions:
        # Record each label from the rule...
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        label1Final = rule.returnLabel1Final()
        label2Final = rule.returnLabel2Final()

        # And record an edge for a graph if a rule:
        # Has an actual change for either label 1, label 2, or both...
        # Note: Since Networkx keeps the graph as a dictionary, repeated edges are not an issue.
        if(label1 != label1Final):
            system_graph.add_edge(label1, label1Final)
        if(label2 != label2Final):
            system_graph.add_edge(label2, label2Final)

    # Do the same thing for each horizontal transition.
    for rule in h_transitions:
        # Record each label from the rule...
        label1 = rule.returnLabel1()
        label2 = rule.returnLabel2()
        label1Final = rule.returnLabel1Final()
        label2Final = rule.returnLabel2Final()

        # And record an edge for a graph if a rule:
        # Has an actual change for either label 1, label 2, or both...
        # Note: Since Networkx keeps the graph as a dictionary, repeated edges are not an issue.
        if(label1 != label1Final):
            system_graph.add_edge(label1, label1Final)
        if(label2 != label2Final):
            system_graph.add_edge(label2, label2Final)

    # Now, check if the graph is acyclic.
    # If the check fails, the system is non-freezing; if the check passes, then it's freezing.
    is_system_freezing = nx.is_directed_acyclic_graph(system_graph)
    # Testing for Freezing Check
    if(is_system_freezing):
        print("The current system is freezing.")
    else:
        print("The current system is non-freezing.")

    # Draw and save graph
    nx.draw_shell(system_graph, with_labels=True)
    plt.savefig("freezing_check.svg")
    return is_system_freezing
