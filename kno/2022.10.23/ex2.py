from simpful import *

FS = FuzzySystem()

speed_slow = FuzzySet(function=Triangular_MF(a=10, b=37, c=50), term="slow")
speed_medium = FuzzySet(function=Triangular_MF(
    a=35, b=52, c=73), term="medium")
speed_high = FuzzySet(function=Triangular_MF(a=45, b=78, c=94), term="high")
LV1 = LinguisticVariable(
    [speed_slow, speed_medium, speed_high], concept="Speed",
    universe_of_discourse=[10, 94])
FS.add_linguistic_variable("Speed", LV1)

distance_short = FuzzySet(function=Triangular_MF(
    a=2, b=7, c=10), term="short")
distance_medium = FuzzySet(function=Triangular_MF(
    a=5, b=15, c=27), term="medium")
distance_long = FuzzySet(function=Triangular_MF(
    a=20, b=35, c=45), term="long")
LV2 = LinguisticVariable(
    [distance_short, distance_medium, distance_long], concept="Distance",
    universe_of_discourse=[2, 45])
FS.add_linguistic_variable("Distance", LV2)

acceleration_big_minus = FuzzySet(function=Triangular_MF(
    a=-1., b=-.7, c=-0.5), term="big_minus")
acceleration_small_minus = FuzzySet(function=Triangular_MF(
    a=-.6, b=-.3, c=0.), term="small_minus")
acceleration_small_plus = FuzzySet(function=Triangular_MF(
    a=0, b=0.1, c=0.4), term="small_plus")
acceleration_big_plus = FuzzySet(function=Triangular_MF(
    a=0.3, b=.7, c=1), term="big_plus")
LV3 = LinguisticVariable(
    [acceleration_big_minus, acceleration_small_minus,
        acceleration_small_plus, acceleration_big_plus],
    concept="Acceleration", universe_of_discourse=[-1, 1])
FS.add_linguistic_variable("Acceleration", LV3)

FS.add_rules_from_file(path='list_of_rules.txt')

FS.set_variable("Speed", 80)
FS.set_variable("Distance", 10)

print(FS.Mamdani_inference(["Acceleration"]))
