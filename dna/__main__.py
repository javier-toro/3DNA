from .RotTable import RotTable
from .Traj3D import Traj3D
# from .genetic_algorithm import *
from .opti_genetic_algo import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename of DNA sequence")
parser.parse_args()
args = parser.parse_args()

def main():

    rot_table = RotTable()
    traj = Traj3D()

    # Read file
    lineList = [line.rstrip('\n') for line in open(args.filename)]
    # Formatting
    seq = ''.join(lineList[1:])
    traj.compute(seq, rot_table)

    # print(traj.getTraj())
    # a = GeneticAlgorithm(11,rot_table,0.3)
    # a.selection(seq,traj)
    # print(a.population_size)
    # traj.draw()
    # traj.write(args.filename+".png")
    algo = GeneticAlgorithm(40, rot_table, 0.3, seq, traj)
    algo.run()
    table, score=algo.get_results()
    print(f"Best score: {score}")
    print(f"Best table: {table.getTable()}")
    algo.write_results("./dna/results.json")

    traj=Traj3D()
    table=RotTable("./dna/results.json")
    traj.compute(seq,table)
    traj.draw()

if __name__ == "__main__" :
    main()
