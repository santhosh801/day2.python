# Create a Class


# To create a class, use the keyword class:

# ExampleGet your own Python Server
# Create a class named MyClass, with a property named x:

# Create Object


# Now we can use the class named MyClass to create objects:

# class Fs:
#   x = 5
# p1 = Fs()
# print(p1.x)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# # 
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}{self.age}"

# p1 = Person("John", 36)

# print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("Age is " + self.age)
p1 = Person("John", 36)
p1.myfunc()