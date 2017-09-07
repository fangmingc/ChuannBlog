

def operate(filename):
    # with open(filename, encoding='utf-8') as rf, \
    #         open(filename+'_swap', 'w', encoding='utf-8') as wf:
    with open(filename, 'rb') as rf, \
            open(filename + '_swap', 'wb') as wf:
        for line in rf:
            # print(line, end='')
            # print(line)
            # temp_line = line.replace('|', '\\|')
            # temp_line = temp_line.replace("```", "\\r\\n```")
            # wf.write(temp_line)
            temp_line = line.replace(b'|', b'\|')
            temp_line = temp_line.replace(b"```", b"\r\n```")
            wf.write(temp_line)


if __name__ == '__main__':
    operate('MySQL.md')


