import numpy as np

# Filtering = Refers to the process of selecting elements
#             from an array that match a given condition

ages = np.array([[17,73,23,43,26,16,25],
                 [18,26,27,19,52,17,21]])

teenager = ages[ages<18]
teenagers = np.where(ages<18    , ages,  0   )
#                    condition    array value

adult = ages[(ages>=18)&(ages<65)]
adults = np.where((ages>=18)&(ages<65), ages,0)

senior = ages[ages>=65]
senior = np.where(ages>=65, ages, 0)
evens = ages[ages %2 == 0]
odds = ages[ages %2 != 0]
print(teenagers)