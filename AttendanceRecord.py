import pandas as pd
# here 1 means present and 0 means absent
attendance = pd.Series([1,0,1,1,0], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(attendance)
print("total Present days:", attendance.sum())
print("total attendance days:", attendance.count())
print('average attendance:', attendance.mean()*100, '%')