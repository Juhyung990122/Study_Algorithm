import sys
import re

string = sys.stdin.readline().rstrip()
st_list = dict()

alpha = "".join(re.findall("[a-z]+", string))
alpha = re.sub(r'(?s)(.)(?=\1)','',alpha)

for i in alpha:
    if i in st_list :
        continue
    else:
        st_list[i] = 0

now_alpha = ''
i = 0
while i < len(string):
        if i >= len(string):
                break

        if string[i].isalpha():
            now_alpha = string[i]
            i += 1
            continue
        else:
            if i+1 == len(string):
                st_list[string[i-1]] += int(string[i])
                break

            if string[i+1].isalpha():
                st_list[now_alpha] += int(string[i])
                i += 1
            
            else:
                idx = i
                while string[idx].isdigit() and idx < len(string):
                    idx += 1
                    if idx == len(string):
                        break
                move = idx - i
                idx -= 1
                d = 10 ** (idx - i)
                while idx != i:
                    idx -= 1
                    st_list[now_alpha] += d * int(string[idx])
                i += move

answer = ''
for i in st_list:
    answer+= i+str(st_list[i])

print(answer)
