   #Tech Productivity (TPI) calculation
def calculation_tpi(coding_values):
    total_coding = sum(coding_values)
    valid_day = len(coding_values)
    if valid_day > 0:
        tpi = total_coding / valid_day
    else:
        tpi = 0
    return tpi
    
#Academic Activity(AAI) calculation
def calculation_aai(study_values,class_values):
    total_academic = sum(study_values)+sum(class_values)
    # Both activity measures contribute to a valid academic day.
    valid_day = min(len(study_values), len(class_values))
    if valid_day > 0:
        aai = total_academic / valid_day
    else:
        aai = 0
    return aai

     #Physical Activity (PhAI) calculation
def calculation_phAI(fitness_values):
    total_fitness = sum(fitness_values)
    valid_day = len(fitness_values)
    if valid_day > 0:
        phAI = total_fitness / valid_day
    else:
        phAI = 0
    return phAI

         #Sleep & recovery(SRI) calculation
def calculation_sri(sleep_values):
    total_sleep = sum(sleep_values)
    valid_day = len(sleep_values)
    if valid_day > 0:
        sri = total_sleep / valid_day
    else:
        sri = 0
    return sri

    #Activity Balance (ABI) calculation
def calculation_ABI(unaccounted_values):
    total_unaccounted = sum(unaccounted_values)
    valid_day = len(unaccounted_values)
    if valid_day > 0:
        abi = total_unaccounted / valid_day
    else:
        abi = 0
    return abi

    #Time Utilization (TUI) calculation
def calculation_tui(trackedtime_values):
    total_trackedtime = sum(trackedtime_values)
    valid_day = len(trackedtime_values)
    if valid_day > 0:
        tui = total_trackedtime / valid_day
    else:
        tui = 0
    return tui

    #Experience Index (EI) calculation
def calculation_EI(feeling_values,satisfaction_value,energy_values):
    total_feeling = sum(feeling_values)
    total_satisfaction = sum(satisfaction_value)
    total_energy = sum(energy_values)
    valid_days = len(feeling_values)

    if valid_days > 0:
        ei = (total_feeling + total_satisfaction + total_energy) / (3 * valid_days)
    else:
        ei = 0
    return ei

    #Data Continuity (DCI) calculation    
def calculation_DCI(valid_days,expected_days):
    if expected_days >0:
        dci = (valid_days/expected_days)*100
    else:
        dci = 0
    return dci

    #Personal Activity Index (PAI) calculation
def calculation_PAI(tpi, aai, phAI, sri, tui, ei, dci):
    pai=(0.15*tpi
    +0.20*aai
    +0.15*phAI
    +0.20*sri
    +0.15*tui
    +0.10*ei   #0.15×TPI + 0.20×AAI + 0.15×PhAI + 0.20×SRI + 0.15×TUI + 0.10×EI + 0.05×DCI
    +0.05*dci)
    return pai    

    #=====================ALL FUNCTION ============================
