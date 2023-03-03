# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    space = [[] for _ in range(n)]
    source = None
    for i in range(n):
        if parents[i] == -1: 
            source = i
        else: 
            space[parents[i]].append(i)

    def height_max(p):
        height = 1
        if not space[p]: 
            return height
        else:
            for sprout in space[p]:
                height = max(height,height_max(sprout))
            return height + 1
    return height_max(source)

def main():
    text=input("F or I: ")
    if "I" in text:
        n=int(input())
        parents=list(map(int, input().split()))
    elif "F" in text:
        file_name=input()
        file_path='./test/'
        file_full_name = path+name
        if "a" not in name:
            try:
                with open(file_full_name) as file:
                    n=int(file.readline())
                    parents=list(map(int,file.readline().split()))
            except Exception as e:
                print("Error", str(e))
                return
        else:
            print("Error")
            return

    print(compute_height(n,parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
