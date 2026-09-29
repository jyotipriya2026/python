"""Calculate activity indices from the populated 12604337.xlsx Daily Log."""

from pathlib import Path

import openpyxl

from functions import (
    calculation_ABI,
    calculation_DCI,
    calculation_EI,
    calculation_PAI,
    calculation_aai,
    calculation_phAI,
    calculation_sri,
    calculation_tpi,
    calculation_tui,
)


workbook = openpyxl.load_workbook(
    Path(__file__).with_name("12604337.xlsx"), data_only=True
)
sheet = workbook["Daily Log"]
rows = [row for row in sheet.iter_rows(min_row=6, values_only=True) if row[0]]
workbook.close()

number = lambda value: isinstance(value, (int, float)) and not isinstance(value, bool)

# Daily Log columns: B sleep, C fitness, D study, E coding, F class, H other.
coding = [r[4] for r in rows if number(r[4])]
academic = [(r[3], r[5]) for r in rows if number(r[3]) and number(r[5])]
fitness = [r[2] for r in rows if number(r[2])]
sleep = [r[1] for r in rows if number(r[1])]
tracked = [sum(r[i] for i in (1, 2, 3, 4, 5, 7) if number(r[i])) for r in rows]
unaccounted = [1440 - total for total in tracked]

feeling_scale = {"Stressed": 1, "Low": 2, "Neutral": 3, "Good": 4, "Excellent": 5}
satisfaction_scale = {
    "Very Unsatisfied": 1, "Unsatisfied": 2, "Neutral": 3,
    "Satisfied": 4, "Very Satisfied": 5,
}
energy_scale = {"Low": 1, "Medium": 2, "High": 3}
experience = [
    (feeling_scale.get(r[10]), satisfaction_scale.get(r[11]), energy_scale.get(r[12]))
    for r in rows
]
experience = [scores for scores in experience if all(score is not None for score in scores)]

tpi = calculation_tpi(coding)
aai = calculation_aai([day[0] for day in academic], [day[1] for day in academic])
phai = calculation_phAI(fitness)
sri = calculation_sri(sleep)
abi = calculation_ABI(unaccounted)
tui = calculation_tui(tracked)
ei = calculation_EI(
    [day[0] for day in experience],
    [day[1] for day in experience],
    [day[2] for day in experience],
)
dci = calculation_DCI(len(experience), 40)
pai = calculation_PAI(tpi, aai, phai, sri, tui, ei, dci)

for name, value in (
    ("TPI", tpi), ("AAI", aai), ("PhAI", phai), ("SRI", sri),
    ("ABI", abi), ("TUI", tui), ("EI", ei), ("DCI", dci), ("PAI", pai),
):
    suffix = "%" if name == "DCI" else ""
    print(f"{name}: {value:.2f}{suffix}")
