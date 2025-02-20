from csv_diff import load_csv, compare

diff = compare(
    load_csv(open("manga_2023-03-29.csv"), key="Name"),
    load_csv(open("manga_2025-01-27.csv"), key="Name")
)
print(diff)
for difference in diff['added']:
    print(difference['Name'])
    
list(diff.keys())