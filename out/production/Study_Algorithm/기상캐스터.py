h,w = map(int,input().split())

answer = [[-1] * w for _ in range(h)]
sky = list()
for _ in range(h):
    sky.append(list(input()))

# for s in range(len(sky)):
#     time = 0
#     while "c" in sky[s]:
#         for r in range(len(sky[s])):
#             if sky[s][r]== "c":
#                 if answer[s][r] == -1:
#                     answer[s][r] = time
             
#         sky[s].pop()
#         sky[s].insert(0,".")
#         time += 1

# for i in range(h):
#     for j in range(w):
#         print(answer[i][j],end=" ")
#     print()

for i in range(h):
    cloud = False
    for j in range(w):
        if cloud == False and sky[i][j] == ".":
            answer[i][j] = -1
        elif sky[i][j] == "c":
            cloud = True
            answer[i][j] = 0
            num = 1
        elif cloud == True and sky[i][j] == ".":
            answer[i][j] = num
            num += 1
for i in range(h):
    for j in range(w):
        print(answer[i][j],end=" ")
    print()
            


