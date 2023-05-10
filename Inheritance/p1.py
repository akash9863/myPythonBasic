class Vec2D:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class Vec3D(Vec2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
v2d = Vec2D(2,3)
v3d = Vec3D(4,5,6)
print(v2d)
print(v3d)