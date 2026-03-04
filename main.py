"""
Andrew Curtis Knoll
CSCI 332 Spring 2025
Programming Assignment #8
I acknowledge that I have worked on this assignment independently, except where explicitly noted
and referenced. Any collaboration or use of external resources has been properly cited. I am
fully aware of the consequences of academic dishonesty and agree to abide by the university's
academic integrity policy. I understand the importance the consequences of plagiarism.
"""



def orientation(p1:tuple[int, int],  p2: tuple[int, int], p3: tuple[int, int]):
    val = ((p2(1)-p1(1)) * (p3(0)-p2(0)) - (p2(0)-p1(0)) *(p3(1)-p2(1)))

    if val == 0:
        return 0 #Colinear
    
    if val > 0:
        return 1 #Clockwise
    
    if val < 0: 
        return 2 #Counter Clockwise
    
def on_segment(p1:tuple[int, int],  p2: tuple[int, int], p3: tuple[int, int]): #Returns True if point p2 lies on segment pr.
    cross_product = (p3(0) - p1(0)) * (p2(1) - p1(1)) - (p3(1) - p1(1)) * (p2(0) - p1(0))
   
    if p1(0) < p2(0) and p1(1) < p2(1) and p2(0) < p3(0) and p2(1) < p3(1) and cross_product == 0:
        return True
    else:
        return False
    
def do_intersection(seg1: tuple[tuple[int, int], tuple[int, int]], seg2: tuple[tuple[int, int], tuple[int, int]]):
    


if __name__ == "__main__":
    p1 = (1, 1)
    p2= (2, 2)
    p3 = (3,3)

    print(orientation(p1,p2,p3))
    print(on_segment(p1,p2,p3))