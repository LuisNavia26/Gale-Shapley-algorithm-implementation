from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class Hospital:
    # Index acts as the unique number for the hospital
    index: int
    # Ordered list of preferences, from most to least preferential
    preferences: List[int]
    # Matching between Hospital and Student
    matching: Optional[Student] = None

@dataclass
class Student:
    # Index acts as the unique number for the hospital
    index: int
    # Ordered list of preferences, from most to least preferential
    preferences: List[int]
    # Matching between Hospital and Student
    matching: Optional[Hospital] = None


@dataclass
class Problem:
    hospitals: List[Hospital]
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

# Returns the ranking of the hospital in the mind of the student. Smaller integer means more preferential
def ranking(student: Student, hospital: Hospital) -> int:
    target_index = hospital.index
    for i, preference in enumerate(student.preferences):
        if preference == target_index:
            return i
    raise Exception("hospital not found in preference list at all")


def solver(problem: Problem) -> Solution:
    assert(len(problem.hospitals) == len(problem.students))
    hospital_index = 0
    while hospital_index < len(problem.hospitals):
        hospital = problem.hospitals[hospital_index]
        # Skip until we have a hospital without a student
        if hospital.matching is not None:
            hospital_index += 1
            continue

        for student_index in hospital.preferences:
            student = problem.students[student_index]
            if student.matching is None:
                student.matching = hospital
                hospital.matching = student
                break
            elif ranking(student, hospital) < ranking(student, student.matching):
                hospital_prime = student.matching
                hospital_prime.matching = None
                student.matching = hospital
                # A previous hospital just lost their matching, so revisit earlier hospitals too
                hospital_index = 0
                break
    solution = []
    for hospital in problem.hospitals:
        assert(hospital.matching is not None)
        assert(hospital.matching.matching == hospital)
        solution.append((hospital.index + 1, hospital.matching.index + 1))
    return solution
