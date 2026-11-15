skills = [
    'Python',
    'SQL',
    'Data Visualization',
    'Excel',
    'Data Analysis',
    'Problem Solving'
]

for index, skill in enumerate(skills, start=1):
    if index == 1:
        print(f'{index}. {skill} <- top pick!')
    else:
        print(f'{index}. {skill}')