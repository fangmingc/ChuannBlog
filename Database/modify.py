import re


def operate(filename):
    # with open(filename, encoding='utf-8') as rf, \
    #         open(filename+'_swap', 'w', encoding='utf-8') as wf:
    with open(filename, 'r', encoding='utf8') as rf, \
            open('123.md', 'w', encoding='utf-8') as wf:
        # for line in rf:
            # print(line, end='')
            # print(line)
            # temp_line = line.replace('|', '\\|')
            # temp_line = temp_line.replace("```", "\\r\\n```")
            # wf.write(temp_line)
            # temp_line = line.replace(b'|', b'\|')
            # temp_line = temp_line.replace(b"```", b"\r\n```")
            # wf.write(temp_line)
        text = rf.read()
        # print(text)
        all_text_old = re.findall('[`]{3}(.*?)[`]{3}', text, re.S)
        all_text_new = []
        for item in all_text_old:
            # print(item)
            all_text_new.append(item.replace(r'\|', r'|'))
        for i in range(len(all_text_old)):
            text = text.replace(all_text_old[i], all_text_new[i], 1)
        wf.write(text)
        # print(text)


if __name__ == '__main__':
    operate('MySQL.md')
