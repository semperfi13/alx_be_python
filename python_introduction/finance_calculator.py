monthly = int(input("Enter your monthly income: \n"));

depenses = int(input("Enter your total monthly expenses: \n"));

saving_m = monthly - depenses;

print("Your monthly savings are $",saving_m ,"\n");

interest = saving_m * 12 + (saving_m * 12 * 0.05);

print("Projected savings after one year, with interest, is: $",interest)
