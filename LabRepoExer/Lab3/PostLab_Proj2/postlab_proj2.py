import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Tests for equality of two Student objects based on their names."""
        if isinstance(other, Student):
            return self.name == other.name
        return False

    def __lt__(self, other):
        """Tests if this Student is less than another Student based on their names."""
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    def __ge__(self, other):
        """Tests if this Student is greater than or equal to another Student based on their names."""
        if isinstance(other, Student):
            return self.name >= other.name
        return NotImplemented

def main():
    """A simple test."""
    # Create a list of Student objects
    students = [
        Student("Jonathan", 5),
        Student("Joseph", 5),
        Student("Jotaro", 5),
        Student("Josuke", 5),
        Student("Jolyne", 5)
    ]

    # Set random scores for each student
    for student in students:
        for i in range(1, 6):
            student.setScore(i, random.randint(60, 100))

    print("Original list of students:")
    for student in students:
        print(student)
        print()  # Add a blank line between students

    # Shuffle the list
    random.shuffle(students)

    print("Shuffled list of students:")
    for student in students:
        print(student)
        print()  # Add a blank line between students

    # Sort the list
    students.sort()

    print("Sorted list of students:")
    for student in students:
        print(student)
        print()  # Add a blank line between students

if __name__ == "__main__":
    main()