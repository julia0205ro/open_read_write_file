def lines_count():
    with (open('1.txt', encoding='utf-8') as f1,
          open('2.txt', encoding='utf-8') as f2,
          open('3.txt', encoding='utf-8') as f3):
        read_files = {f1: '1.txt', f2: '2.txt', f3: '3.txt'}
        all_dicts = []
        for read_file in read_files:
            help_dict = ({'Имя файла': read_files[read_file],
                          'Количество строк': len(read_file.readlines())})
            all_dicts.append(help_dict)
        sorted_all_dicts = sorted(all_dicts, key=lambda x: x['Количество строк'])
        return sorted_all_dicts

lines_count()


def content():
    with (open('1.txt', encoding='utf-8') as f1,
          open('2.txt', encoding='utf-8') as f2,
          open('3.txt', encoding='utf-8') as f3):
        read_files = {f1: '1.txt', f2: '2.txt', f3: '3.txt'}
        all_dicts = []
        for read_file in read_files:
            help_dict = ({'Имя файла': read_files[read_file],
                          'Содержание': read_file.read()})
            all_dicts.append(help_dict)
        return all_dicts

content()


def union(first_dict,second_dict):
    with (open('unioned.txt', 'w', encoding='utf-8') as f4):
        for i in first_dict:
            for j in second_dict:
                if i['Имя файла'] == j['Имя файла']:
                    merged_dictionary = {**i, **j}
                    f4.write(f'{merged_dictionary["Имя файла"]} \n')
                    f4.write(f'{merged_dictionary["Количество строк"]} \n')
                    f4.write(f'{merged_dictionary["Содержание"]} \n')
    return f'Done!'

print(union(lines_count(), content()))