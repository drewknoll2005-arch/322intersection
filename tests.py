import unittest
from main import orientation, on_segment, do_intersection

class TestMathFunctions(unittest.TestCase):
    def test_orientation_Colinear(self):
        p1 = (1, 1)
        p2= (2, 2)
        p3 = (3,3)
        self.assertEqual(orientation(p1,p2,p3), 0)

    def test_orientation_Clockwise(self):
        p1 = (1, 1)
        p2= (2, 2)
        p3 = (3,2)
        self.assertEqual(orientation(p1,p2,p3), 1)

    def test_orientation_Counter_Clockwise(self):
        p1 = (1, 1)
        p2= (2, 2)
        p3 = (3,4)
        self.assertEqual(orientation(p1,p2,p3), 2)
        
    def test_on_segment_true(self):
        p1 = (1, 1)
        p2= (2, 2)
        p3 = (3,3)
        self.assertEqual(on_segment(p1,p2,p3), True)

    def test_on_segment_false(self):
        p1 = (1, 1)
        p2= (2, 3)
        p3 = (3,3)
        self.assertEqual(on_segment(p1,p2,p3), False)

    def test_do_intersection(self):
        p4 = (-10,-10)
        p5 = (10,10)
        p6 = (-10,10)
        p7 = (10,-10)
        seg1 = (p4,p5)
        seg2 = (p6,p7)
        self.assertEqual(do_intersection(seg1,seg2), ((0.0, 0.0)))
    
    def test_do_intersection_parrelel(self):
        p4 = (-10,-10)
        p5 = (10,10)
        p6 = (-11,-11)
        p7 = (11, 11)
        seg1 = (p4,p5)
        seg2 = (p6,p7)
        self.assertEqual(do_intersection(seg1,seg2), None)
if __name__ == "__main__":
    unittest.main()