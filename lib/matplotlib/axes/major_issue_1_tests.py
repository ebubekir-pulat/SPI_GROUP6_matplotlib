import matplotlib.pyplot as plt
import numpy as np


# Test Whether Path Simplification is Causing An Effect
def simplification_test():
    for _ in range(1000):
        data = [np.random.random(np.random.randint(2, 10)) for i in range(500)]
        fig, axes = plt.subplots(2)

        res1 = axes[0].eventplot(data, linelength=1)

        for i in range(500):
            if len(data[i]) != len(res1[i].get_positions()):
                print("***PATH SIMPLIFICATION FAIL***")
                raise Exception("***PATH SIMPLIFICATION FAIL***")

        res2 = axes[1].eventplot(data, linelength=2)

        for i in range(500):
            if len(data[i]) != len(res2[i].get_positions()):
                print("***PATH SIMPLIFICATION FAIL***")
                raise Exception("***PATH SIMPLIFICATION FAIL***")

        plt.close('all')


# Prove Simply Turning Path Snapping Off Restores All Data.
# Also, Test Can Be Used to Verify The Correctness of the Patch/Changes to eventplot
def snapping_test():
    # Note: If You Want To Visually Confirm The Data Points Match, Comment Out The 'plt.close('all')' line.

    for _ in range(1000):
        data = [np.random.random(np.random.randint(2, 10)) for i in range(500)]
        fig, axes = plt.subplots(2)

        for line in data:
            line = sorted(line)

        res1 = axes[0].eventplot(data, linelength=1)

        for i in range(500):
            for j in range(data[i]):
                if data[i][j] != res1[i].get_positions()[j]:
                    print("***DATA DOESN'T MATCH***")
                    raise Exception("***DATA DOESN'T MATCH***")

        res2 = axes[1].eventplot(data, linelength=2)

        for i in range(500):
            for j in range(data[i]):
                if data[i][j] != res2[i].get_positions()[j]:
                    print("***DATA DOESN'T MATCH***")
                    raise Exception("***DATA DOESN'T MATCH***")

        plt.close('all')
