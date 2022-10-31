from simpful import *
import random

FS = FuzzySystem()


def sugeno(service: int, food: int):

    S_1 = FuzzySet(points=[[0., 1.], [5., 0.]], term="poor")
    S_2 = FuzzySet(points=[[0., 0.], [5., 1.], [10., 0.]], term="good")

    S_3 = FuzzySet(points=[[5., 0.], [10., 1.]], term="excellent")
    FS.add_linguistic_variable("Service", LinguisticVariable(
        [S_1, S_2, S_3], concept="Service quality"))

    F_1 = FuzzySet(points=[[0., 1.], [10., 0.]], term="rancid")
    F_2 = FuzzySet(points=[[0., 0.], [10., 1.]], term="delicious")
    FS.add_linguistic_variable("Food", LinguisticVariable(
        [F_1, F_2], concept="Food quality"))

    FS.set_crisp_output_value("small", 5)
    FS.set_crisp_output_value("average", 15)

    FS.set_output_function("generous", "Food+Service+5")

    R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"
    R2 = "IF (Service IS good) THEN (Tip IS average)"
    R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)"
    FS.add_rules([R1, R2, R3])

    FS.set_variable("Service", service)
    FS.set_variable("Food", food)

    return FS.Sugeno_inference(["Tip"])


def mamdani(service: int, food: int):
    S_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=5), term="poor")
    S_2 = FuzzySet(function=Triangular_MF(a=0, b=5, c=10), term="good")

    S_3 = FuzzySet(function=Triangular_MF(a=5, b=10, c=10), term="excellent")
    FS.add_linguistic_variable("Service", LinguisticVariable(
        [S_1, S_2, S_3], concept="Service quality", universe_of_discourse=[0, 10]))

    F_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="rancid")
    F_2 = FuzzySet(function=Triangular_MF(a=0, b=10, c=10), term="delicious")
    FS.add_linguistic_variable("Food", LinguisticVariable(
        [F_1, F_2], concept="Food quality", universe_of_discourse=[0, 10]))

    T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="small")
    T_2 = FuzzySet(function=Triangular_MF(a=0, b=10, c=20), term="average")
    T_3 = FuzzySet(function=Trapezoidal_MF(
        a=10, b=20, c=25, d=25), term="generous")
    FS.add_linguistic_variable("Tip", LinguisticVariable(
        [T_1, T_2, T_3], universe_of_discourse=[0, 25]))

    R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"
    R2 = "IF (Service IS good) THEN (Tip IS average)"
    R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)"
    FS.add_rules([R1, R2, R3])

    FS.set_variable("Service", service)
    FS.set_variable("Food", food)

    return FS.Mamdani_inference(["Tip"])


for i in range(0, 100):
    service_random = random.randrange(0, 10)
    food_random = random.randrange(0, 10)
    print("service: ", service_random, ", ")
    print("food: ", food_random)
    print("sugeno: ", sugeno(service_random, food_random))
    print("mamdani: ", mamdani(service_random, food_random))
