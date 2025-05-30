class Grand_father:
    prop = 10000

    def grandfather_prop(self):
        print("The Grand father's property is:", self.prop)

class Father(Grand_father):  # Inherit from Grand_father
    prop_1 = Grand_father.prop + 90000

    def father_prop(self):
        print("The father's property is:", self.prop_1)

class Son(Father):  # Inherit from Father
    prop_2 = Father.prop_1 + 9000000

    def son_prop(self):
        print("The son's property is:", self.prop_2)

# Testing
g = Grand_father()
g.grandfather_prop()
# g.father_prop()  # Not defined for Grand_father
# g.son_prop()     # Not defined for Grand_father

f = Father()
f.grandfather_prop()
f.father_prop()
# f.son_prop()     # Not defined for Father

s = Son()
s.grandfather_prop()
s.father_prop()
s.son_prop()
