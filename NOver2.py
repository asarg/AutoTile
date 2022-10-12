#
# NOver2.py --- Oct. 11, 2022
#

from UniversalClasses import System, Assembly, State, AffinityRule, TransitionRule
from assemblyEngine import Engine

# Default System
# - No aff.
# - No tr.
# - No states
# - No tiles
# - Empty assembly
system = System(1, [], [], [], [], [], [], [], [], [], seed_assembly = Assembly(), empty=True)

# Add states
# TODO remove A1-E1, we only need A-E
sts = [State("A", "00ff00"), State("B", "00ff00"), State("C", "00ff00"), State("D", "00ff00"), State("E", "00ff00"),
State("A1", "00ff00"), State("B1", "00ff00"), State("C1", "00ff00"), State("D1", "00ff00"), State("E1", "00ff00")]
for s in sts:
	system.addState(s)

# Set initial states
for s in sts:
	system.addInitialState(s)

# TODO do all combos here, repeating LOOP
# START LOOP:

# Set seed
system.addSeedState(sts[0])

# Add affinity
# system.addAffinity(AffinityRule("X", "Y", "h")) example
system.addAffinity(AffinityRule("A", "A1", "h"))
system.addAffinity(AffinityRule("A1", "B", "h"))
system.addAffinity(AffinityRule("B", "B1", "h"))
system.addAffinity(AffinityRule("B1", "C", "h"))
system.addAffinity(AffinityRule("C", "C1", "h"))
system.addAffinity(AffinityRule("C1", "D", "h"))
system.addAffinity(AffinityRule("D", "D1", "h"))
system.addAffinity(AffinityRule("D1", "E", "h"))
system.addAffinity(AffinityRule("E", "E1", "h"))

# Add transitions
# system.addTransitionRule(TransitionRule("X", "Y", "Q", "R", "h")) example

# Build engine
e = Engine(system)

# build assembly A while
# - A contains less than 10 tiles
# - A is not terminal
res = 0
while res == 0 and len(e.currentAssembly.tiles) <= 10:
	res = e.step()

# We found it!
if res == -1 and len(e.currentAssembly.tiles) == 10:
	print("\n*** STRUCK GOLD ***\n")

# :END LOOP

print("done.")
