class prime:
    def __init__(self,x):
        self.n=x
    def determine(self):
        q=self.n
        m = 2
        flag=0
        while(m < q):
            if(q % m ==0):
                flag = 1
                break;
            m = m+1
        if (flag==0):
            return "Prime"
        else:
            print ("This number is not a prime")

import unittest

class TestMethods(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(z.determine(),"Prime")


if __name__ == "__main__":
    z=prime(7)
    unittest.main()
