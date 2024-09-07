from abc import ABC
from typing import Dict

from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def team_data(self):
        expenses: int = 200000
        sponsors: Dict[str, Dict[int, int]] = {"Petronas": {1: 1000000, 3: 500000}, "TeamViewer": {5: 100000, 7: 50000}}

        return expenses, sponsors


