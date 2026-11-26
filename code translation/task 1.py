# Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


student = Student("Asha", 20)
print(student.introduce())


##Java
public class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String introduce() {
        return "My name is " + name + " and I am " + age + " years old.";
    }

    public static void main(String[] args) {
        Student student = new Student("Asha", 20);
        System.out.println(student.introduce());
    }
}