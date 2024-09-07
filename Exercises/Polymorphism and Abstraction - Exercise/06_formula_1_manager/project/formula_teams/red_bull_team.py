from abc import ABC
from typing import Dict

from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def team_data(self):
        expenses: int = 250000
        sponsors: Dict[str, Dict[int, int]] = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}

        return expenses, sponsors

