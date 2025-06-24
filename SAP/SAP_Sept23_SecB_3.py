intro = "UTP Average Grade Calculator"
print(len(intro) * "=")
print(intro)
print(len(intro) * "=")

def calc_average(list_scores):
    average = sum(list_scores) / len(list_scores)
    return average
    
def assign_grades(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B" 
    elif score >= 70:
        return "C" 
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"
        
def main(): 
    main_list = []
    num = int(input("Enter the number of students: "))
    
    for i in range(num):
        marks = float(input("Student #{} marks: ".format(i+1))) 
        main_list.append(marks) 
    
    average = calc_average(main_list)
    print("Average score is {:.2f}".format(average))
    print("Average grade is", assign_grades(average))
    
    option = int(input("\nEnter the next number of students or -1 to end program: ")) 
    if option != -1:
        main()
    else:
        print("End Program...")
main() 