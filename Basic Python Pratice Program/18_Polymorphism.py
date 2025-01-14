--POLYMORPHISM--

The term "Polymorphism" is the combination of "poly" + "morphs" which means 
many forms. It is a greek word. In object-oriented programming, we use 3 main 
concepts: inheritance, encapsulation, and polymorphism.

Real Life Example Of Polymorphism :

Let's consider a real-life example of polymorphism. A lady behaves like a teacher in a
classroom, mother or daughter in a home and customer in a market. Here, a single person is
behaving differently according to the situations

There are two types of polymorphism --
1. Compile-time polymorphism 
2. Run-time polymorphism

* Compile time polymorphism:

The overloaded functions are invoked by matching the type and number of
arguments. This information is available at the compile time and, therefore,
compiler selects the appropriate function at the compile time. It is achieved
by function overloading and operator overloading which is also known as
static binding or early binding. 

Now, let's consider the case where function name and prototype is same.

 class A // base class declaration.
 {
 int a;
 public:
 void display()
 {
 cout<< "Class A ";
 }
 };
class B : public A // derived class declaration.
{
 int b;
 public:
 void display()
 {
 cout<<"Class B";
 }
};

In the above case, the prototype of display() function is the same in both the base and derived class. Therefore, 
the static binding cannot be applied. It would be great if the appropriate function is selected at the run time. This 
is known as run time polymorphism.

*Run time polymorphism:

Run time polymorphism is achieved when the object's method is invoked at the
run time instead of compile time. It is achieved by method overriding which is also
known as dynamic binding or late binding.

C++ Runtime Polymorphism Example
Let's see a simple example of run time polymorphism in C++.

// an example without the virtual keyword.
#include <iostream>
using namespace std;
class Animal {
 public:
void eat(){
cout<<"Eating...";
 }
};
class Dog: public Animal
{
 public:
 void eat()
 { cout<<"Eating bread...";
 }
};
int main(void) {
 Dog d = Dog();
 d.eat();
 return 0;
}

Output:
Eating bread...

Compile time polymorphism                                                                   Run time polymorphism
The function to be invoked is known at the compile time.                           The function to be invoked is known at the run time.
It is also known as overloading, early binding and static binding.                 It is also known as overriding, Dynamic binding and late binding.

Overloading is a compile time polymorphism where more than                         Overriding is a run time polymorphism where more than one 
one method is having the same name but with the different                          method is having the same name, number of parameters and 
number of parameters or the type of the parameters.                                the type of the parameters.

It is achieved by function overloading and operator                                It is achieved by virtual functions and pointers.
overloading.

It provides fast execution as it is known at the compile time.                     It provides slow execution as it is known at the run time.
It is less flexible as mainly all the things execute at the compile                It is more flexible as all the things execute at the run time.
time.
