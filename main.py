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
    val = ((p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) *(p3[1]-p2[1]))

    if val == 0:
        return 0 #Colinear
    
    if val > 0:
        return 1 #Clockwise
    
    if val < 0: 
        return 2 #Counter Clockwise
    
def on_segment(p1:tuple[int, int],  p2: tuple[int, int], p3: tuple[int, int]): #Returns True if point p2 lies on segment pr.
    cross_product = (p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0])
   
    if p1[0] < p2[0] and p1[1] < p2[1] and p2[0] < p3[0] and p2[1] < p3[1] and cross_product == 0:
        return True
    else:
        return False
    
def do_intersection(seg1: tuple[tuple[int, int], tuple[int, int]], seg2: tuple[tuple[int, int], tuple[int, int]]):
    x1 = seg1[0][0]
    y1 = seg1[0][1]
    x2 = seg1[1][0]
    y2 = seg1[1][1]
    x3 = seg2[0][0]
    y3 = seg2[0][1]
    x4 = seg2[1][0]
    y4 = seg2[1][1]

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)

    if denom == 0:
        return None 

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return (x, y)


if __name__ == "__main__":
    p1 = (1, 1)
    p2= (2, 2)
    p3 = (3,3)
    p4 = (-10,-10)
    p5 = (10,10)
    p6 = (-10,10)
    p7 = (10,-10)
    seg1 = (p4,p5)
    seg2 = (p6,p7)
    print(orientation(p1,p2,p3))
    print(on_segment(p1,p2,p3))
    print(do_intersection(seg1,seg2))