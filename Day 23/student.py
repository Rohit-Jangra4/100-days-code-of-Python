def calculate_percentage(mark):
    return sum(mark)/len(mark)

if __name__=="__main__":
    mark=[80, 75, 90, 85, 70]

    percentage = calculate_percentage(mark)

    print("Percentage:", percentage)