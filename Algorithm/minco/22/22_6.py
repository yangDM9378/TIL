words = [input() for _ in range(4)]
result_max=0
result_min=0
def abc(level):
    global result_max
    global result_min
    if level==4:
        return
    if len(words[level-1])<len(words[level]):
        result_max=level
        result_min=level-1

    abc(level+1)

abc(0)
print(f'긴문장:{result_max}')
print(f'짧은문장:{result_min}')