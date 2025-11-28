import numpy as np
import matplotlib.pyplot as plt

MySubs = np.array(["English", "Math", "Filipino"])
Mdict = {
    "English": 0,
    "Math": 1,
    "Filipino": 2
}

GradePeriod = np.array(["1stGrading", "2ndGrading", "3rdGrading"])
GDict = {
    "1stGrading": 0,
    "2ndGrading": 1,
    "3rdGrading": 2
}

# Grades
English_G = [89, 91, 84]
Math_G = [95, 88, 78]
Filipino_G = [87, 85, 91]

FinalGrades = np.array([English_G, Math_G, Filipino_G])

# Real Grades
English_RG = [78, 75, 76]
Math_RG = [75, 76, 77]
Filipino_RG = [76, 78, 76]

RealGrades = np.array([English_RG, Math_RG, Filipino_RG])