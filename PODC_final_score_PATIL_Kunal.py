"""
AUTHOR: PATIL Kunal
"""
import subprocess
import pandas as pd

file_to_execute = ['0_example.txt', '1_binary_landscapes.txt', '10_computable_moments.txt',
                   '11_randomizing_paintings.txt', '110_oily_portraits.txt']


Score = []
for file in file_to_execute:
    proc = subprocess.Popen(['python', 'PODC_PATIL_Kunal.py', file], stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    print(proc.communicate()[0])

    score_calculation = subprocess.Popen(['python', 'score_checker.py', file, "submit_"+file], stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    Score.append(int(score_calculation.communicate()[0].decode("utf-8").strip('\r\n').split('= ')[1]))


file_to_execute.append('Total Score')
Score.append(sum(Score))
d = {'Input Files': file_to_execute, 'Global Score': Score}
df = pd.DataFrame(data=d)
print(df)

