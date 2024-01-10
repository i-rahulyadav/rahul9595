def main():
    # Prompt for the number of students and group size
    num_students = int(input("How many students? "))
    group_size = int(input("Required group size? "))

    # Calculate the number of groups and students left over
    num_groups = num_students // group_size
    students_left_over = num_students % group_size

    # Determine the appropriate grammar for the output
    group_str = "group" if num_groups == 1 else "groups"
    student_str = "student" if students_left_over == 1 else "students"

    # Display the result
    print(f'There will be {num_groups} {group_str} with {students_left_over} {student_str} left over.')

if __name__ == "__main__":
    main()
