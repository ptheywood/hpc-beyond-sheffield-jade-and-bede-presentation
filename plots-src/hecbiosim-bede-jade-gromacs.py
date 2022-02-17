#! /usr/bin/env python3

"""Plot HECBioSim benchmark data comparing Bede and JADE 2 

Data accessed 2022-02-17 from:

+  https://www.hecbiosim.ac.uk/access-hpc/our-benchmark-results/bede-benchmarks
+  https://www.hecbiosim.ac.uk/access-hpc/our-benchmark-results/jade2-benchmarks
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas
import pathlib

gromacs_path = pathlib.Path("data/hecbiosim/gromacs-2020.3-single-node-single-gpu.csv")
gromacs_figure_path = pathlib.Path("../assets/img/figures/hecbiosim-gromacs.png")

def main():
    gromacs_df = pandas.read_csv(gromacs_path)
    sns.set(rc={'figure.figsize':(8,6)})
    sns.set_style("whitegrid")
    sns.set_palette(sns.color_palette("Dark2"))

    ax = sns.barplot(data=gromacs_df, x="atoms", y="ns/day", hue="HPC")
    ax.set_title("Gromacs 2020.3 Single Node Single GPU (HECBioSim Data)")
    ax.set_ylim(0, 450)
    plt.savefig(gromacs_figure_path, bbox_inches='tight') 


if __name__ == "__main__":
    main()