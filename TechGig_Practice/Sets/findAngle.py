'''Given a right angled triangle ABC, right angled at B. Find angle ABD, where D is the mid-point of the hypotenuse(side AC).
You will be given two integers denoting sides AB and BC respectively.
Round off your answer to the nearest Integer.'''

import math

def main():
    AB = int(input())
    BC = int(input())
    D = (BC/2, AB/2)
    dot = AB * D[1]
    magBD = math.sqrt(D[0]**2 + D[1]**2)
    magBA = AB
    cos_theta = dot / (magBD * magBA)
    cos_theta = max(min(cos_theta,1),-1)
    print(round(math.degrees(math.acos(cos_theta))))

main()