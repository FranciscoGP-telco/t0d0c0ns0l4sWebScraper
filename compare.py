from csv_diff import load_csv, compare

diff = compare(
    load_csv(open("yesterday.csv"), key="Name"),
    load_csv(open("today.csv"), key="Name")
)
print(diff)
for difference in diff['added']:
    name = difference['Name']
    print(f'+ {name}')

for difference in diff['removed']:
    name = difference['Name']
    print(f'- {name}')

for changed in diff['changed']:
    name = changed['key']
    prices = changed['changes']['price']
    print(f'* {name} Previous Price {prices[0]}- New Price {prices[1]}')
