from django.shortcuts import render
from faker import Faker
from .models import EmpdataFake


def mainpage(request):
    return render(request, 'mainPage.html')


# Replace 'yourapp' with the name of your Django app

# Initialize Faker
fake = Faker()


# Define a function to generate fake data
def generate_fake_employees(num_records):
    for _ in range(num_records):
        EmpdataFake.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            salary=fake.random_int(min=30000, max=120000),
            email=fake.email(),
            location=fake.city(),
            hometown=fake.city(),
            qualification=fake.job(),
            skill=fake.word(),  # This can also be expanded to generate more specific skill terms
            company=fake.company(),
            percentage=fake.random_int(min=60, max=100)  # For fields that take integer percentages
        )


# Call the function to generate and save records
generate_fake_employees(12)  # Adjust the number to generate the desired number of records


def Hydarabad(request):
    employees = EmpdataFake.objects.all()  # Retrieve all records from EmpdataFake
    return render(request, 'Hydarabad.html', {'employees': employees})



from django.shortcuts import render
from .models import EmpdataFake  # Replace with your actual model name


def serch(request):
    employee = None  # Store single employee data if only one match is found
    employees = []  # Store multiple employee data if more than one match

    if request.method == 'POST':
        search_query = request.POST.get('Search')

        # Query to find employees with the specified location
        employees = EmpdataFake.objects.filter(location=search_query)  # `iexact` makes it case-insensitive

        # If only one employee is found, set `employee` and clear `employees`
        if employees.count() == 1:
            employee = employees.first()  # Get the single matching employee
            employees = []  # Clear the employees list to focus on the single result

    return render(request, 'Hyderabad.html', {'employee': employee, 'employees': employees})




