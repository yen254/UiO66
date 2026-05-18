import os
from ase.build import molecule
from ase import Atoms
from ase.visualize.plot import plot_atoms
import matplotlib.pyplot as plt

output_dir = "/Users/admin/.gemini/antigravity/brain/5f6c4bda-c20e-4069-9294-aefb571989bf"

def save_fig(atoms, filename, rotation='', figsize=(4,4)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis('off') # Hide axes for cleaner look
    if rotation:
        plot_atoms(atoms, ax, rotation=rotation)
    else:
        plot_atoms(atoms, ax)
    
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)
    plt.close(fig)
    print(f"Saved: {output_path}")

def main():
    # 1. CO2
    co2 = molecule("CO2")
    save_fig(co2, "co2.png", rotation='90x,0y,0z')

    # 2. Methanol
    methanol = molecule("CH3OH")
    save_fig(methanol, "methanol.png", rotation='15x,15y,0z')

    # 3. Dimethyl carbonate (DMC)
    dmc = Atoms('C3H6O3',
                positions=[
                    (0.000, 0.000, 0.000),    # C (carbonyl)
                    (0.000, 1.200, 0.000),    # O (carbonyl)
                    (-1.150, -0.650, 0.000),  # O (ester 1)
                    (1.150, -0.650, 0.000),   # O (ester 2)
                    (-2.450, -0.150, 0.000),  # C (methyl 1)
                    (2.450, -0.150, 0.000),   # C (methyl 2)
                    (-2.550, 0.930, 0.000),   # H
                    (-2.950, -0.550, 0.880),  # H
                    (-2.950, -0.550, -0.880), # H
                    (2.550, 0.930, 0.000),    # H
                    (2.950, -0.550, 0.880),   # H
                    (2.950, -0.550, -0.880)   # H
                ])
    save_fig(dmc, "dmc.png", rotation='-15x,0y,0z')

    # 4. Zr cluster
    cluster = Atoms('ZrO2',
        positions=[
            (0,0,0),    # Zr
            (1.9,0,0),  # O
            (-1.9,0,0)  # O
        ]
    )
    save_fig(cluster, "zr_cluster.png")

    # 5. CO2 adsorption on Zr
    system = Atoms('ZrO2CO2',
        positions=[
            (0,0,0),       # Zr
            (1.9,0,0),     # O
            (-1.9,0,0),    # O
            (0,2.3,0),     # C (bent CO2)
            (-1.0, 3.0, 0),# O
            (1.0, 3.0, 0)  # O
        ]
    )
    save_fig(system, "co2_adsorption.png")

if __name__ == "__main__":
    main()
