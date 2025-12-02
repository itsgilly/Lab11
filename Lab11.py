import matplotlib.pyplot as plt


def load_students(filename):
    students = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            i = 0
            while i < len(line) and line[i].isdigit():
                i += 1

            student_id = line[:i]
            name = line[i:].strip()

            students[student_id] = name

    return students


def load_assignments(filename):
    assignments = {}
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]
        for i in range(0, len(lines), 3):
            assignment = lines[i]
            student_id = lines[i+1]
            score = int(lines[i+2])
            assignments.setdefault(assignment, []).append((student_id, score))

        return assignments

def student_grade(students, assignments):
    name = input("Enter student name:").strip()

    student_id = None
    for id, n in students.items():
        if n.lower() == name.lower():
            student_id = id
            break

    if student_id is None:
        print("Student not found")
        return

    total = 0
    count = 0
    for recs in assignments.values():
        for id, score in recs:
            if id == student_id:
                total += score
                count += 1

    if count == 0:
        print("No scores found for this student")
        return

    percent = round(total/count)
    print(f"{students[student_id]}'s grade: {percent}% (based on {count} submissions)")

def assignment_stats(assignments):
    name = input("Enter assignment name: ").strip()

    if name not in assignments:
        print("Assignment not found")
        return

    scores = [score for (_, score) in assignments[name]]

    maximum = max(scores)
    minimum = min(scores)
    average = round(sum(scores)/len(scores))

    print(f"Max: {maximum}%")
    print(f"Min: {minimum}%")
    print(f"Average: {average}%")

def assignment_graph(assignments):
    name = input("Enter assignment name: ").strip()

    if name not in assignments:
        print("Assignment not found")
        return

    scores = [score for (_, score) in assignments[name]]

    plt.hist(scores, bins = [0, 25, 50, 75, 100] )
    plt.title(f"Scores for {name}")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()

def main():
    students = load_students("data/students.txt")
    assignments = load_assignments("data/assignments.txt")

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    print()
    choice = input("Enter your selection:").strip()

    if choice == "1":
        student_grade(students, assignments)

    elif choice == "2":
        assignment_stats(assignments)

    elif choice == "3":
        assignment_graph(assignments)

    else:
        print("Invalid selection")

main()