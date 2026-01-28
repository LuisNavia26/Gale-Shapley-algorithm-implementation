from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class Student:
    # Index acts as the unique number for the hospital
    index: int
    # Ordered list of preferences, from most to least preferential
    preferences: List[int]

@dataclass
class Hospital:
    # Index acts as the unique number for the hospital
    index: int
    # Ordered list of preferences, from most to least preferential
    preferences: List[int]
    # Matching between Hospital and Student
    matching: Optional[Student] = None


@dataclass
class Problem:
    hospital: List[Hospital]
    students: List[Student]

@dataclass
class Solution:
    matchings: List[Tuple[int, int]]

# Converts raw text input into algorithm input
def input_parser(text: str) -> Problem:
    hospitals = []
    students = []

    lines = text.split('\n')

    n = int(lines[0].strip())
    for i in range(1, n + 1):
        index = i - 1
        preferences = [int(index) - 1 for index in lines[i].split(' ')]
        hospitals.append(Hospital(index, preferences))

    for i in range(n + 1, 2 * n + 1):
        index = i - (n + 1)
        preferences = [int(index) - 1 for index in lines[i].split(' ')]
        students.append(Student(index, preferences))

    return Problem(hospitals, students)

