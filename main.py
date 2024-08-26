def readfile(path: str):
    d = {}
    for i in range(1, 3):
        name = f'{i}.txt'
        with open(name, 'r', encoding='utf-8') as f:
            d[name] = [x for x in f.read().splitlines() if x]3
    with open('the_source_file.txt', 'w', encoding='utf-8') as file:
        for k, v in sorted(d.items(), key=lambda x: -len([x[1]])):
            file.write(k + '\n')
            file.write(str(len(v)) + '\n')
            file.write('\n'.join(v))
            file.write('\n')