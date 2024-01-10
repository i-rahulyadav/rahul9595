def main():
    # Prompt for the total number of sweets and the number of pupils
    total_sweets = int(input("How many sweets are there? "))
    num_pupils = int(input("How many pupils are there? "))

    # Calculate how many sweets each pupil will get and the remainder
    sweets_per_pupil = total_sweets // num_pupils
    sweets_left_over = total_sweets % num_pupils

    # Display the result
    print(f'The teacher should give each pupil {sweets_per_pupil} sweets, with {sweets_left_over} sweets left over.')

if __name__ == "__main__":
    main()
