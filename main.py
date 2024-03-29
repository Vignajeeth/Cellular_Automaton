from model import Cellular_Automaton_Model


if __name__ == "__main__":
    """
    Click to Toggle Cells.
    Spacebar for start/stop.
    q for Quitting.
    """
    models = {
        "Replicator": ("1357", "1357"),
        "Photon/XOR": ("25", "4"),
        "Life without Death": ("3", "012345678"),
        "34 Life": ("34", "34"),
        "2x2": ("36", "125"),
        "Morley": ("368", "245"),
        "Anneal": ("4678", "35678"),
        "Game of Life": ("3", "23"),
        "Seed": ("2", ""),
        "High Life": ("36", "23"),
        "Day and Night": ("3678", "34678"),
        "Diamoeba": ("35678", "5678"),
        "Persian Rug": ("234", ""),
        "Long Life": ("345", "5"),
    }

    m = Cellular_Automaton_Model(models["Game of Life"], time=10)

    m.driver()
