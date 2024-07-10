data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)
for row in data:
    row.append(abs(row[1] - row[2]))
print(data)
max_date=''
dt=0
for row in data:
    if row[3]>dt:
        max_date=row[0]
        dt=row[3]

print(max_date,dt)



# max_spread = data[0][-1]
# max_date = data[0][0]

# max_date, max_spread
# for dt, num_1, num_2, spread in data[1:]:
#     if spread > max_spread:
#         # found a new high
#         max_spread = spread
#         max_date = dt
        
# print(max_date, max_spread)