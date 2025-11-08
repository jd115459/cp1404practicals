"""
Project Management Program
"""

import datetime
from prac_07.project import Project

def parse_date(date_str):
    return datetime.datetime.strptime(date_str.strip(), "%d/%m/%Y").date()

def date_format(d:datetime.date):
    return d.strftime("%d/%m/%Y")

def load_projects(filename):
    projects = []
    with open(filename, "r", encoding="utf-8") as file:
        header = file.readline()
        for line in file:
            parts = line.strip().split()
            if len(parts) == 5:
                text_name = parts[0]
                start_date_text = parts[1]
                priority_text = parts[2]
                cost_text = parts[3]
                completion_text = parts[4]

                start_date = parse_date(start_date_text)
                priority = int(priority_text)
                cost = float(cost_text)
                completion = int(completion_text)

                project = Project(text_name, start_date, priority, cost, completion)
                projects.append(project)
        return projects

def save_projects(projects, filename):
    with open(filename, "w", encoding="utf-8") as file:
        print("Name Start_Date Priority Cost_Estimate Completion_Percentage", file=file)
        for project in projects:
            print(f"{project.name} {date_format(project.start_date)} {project.priority} {project.cost_estimate} {project.completion}", file=file)

def display_projects(projects):
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.check_completion():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)

    incomplete_projects.sort()
    complete_projects.sort()

    print(f"Incomplete Projects:")
    for p in incomplete_projects:
        print(" ", p)
    print(f"Complete Projects:")
    for p in complete_projects:
        print(" ", p)

def get_start_date(project):
    return project.start_date

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy):")
    chosen_date = parse_date(date_string)

    filtered  = []
    for p in projects:
        if p.starts_after(chosen_date):
            filtered.append(p)

    filtered.sort()
    for p in filtered:
        print(p)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_date_text = input("Start date (dd/mm/yyyy): ").strip()
    priority_text = input("Priority: ").strip()
    cost_text = input("Cost estimate: $").strip()
    completion_text = input("Percent complete: ").strip()

    start_date = parse_date(start_date_text)
    priority = int(priority_text)
    cost = float(cost_text)
    completion = int(completion_text)

    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")

        choice_text = input("Project choice: ").strip()
        index = int(choice_text)
        project = projects[index]
        print(project)

        new_percentage_text = input("New Percentage: ").strip()
        if new_percentage_text != "":
            project.completion = int(new_percentage_text)

        new_priority_text = input("New Priority: ").strip()
        if new_priority_text != "":
            project.priority = int(new_priority_text)

def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def main():
    print("Welcome to Pythonic Project Management")


    projects = load_projects("projects.txt")
    print("Loaded projects from projects.txt")

    print_menu()

    choice = ""
    while choice != "q":
        choice = input(">>> ").lower().strip()

        if choice == "l":
            filename = input("Filename to load projects from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == "s":
            filename = input("Filename to save projects to: ").strip()
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}")

        elif choice == "d":
            display_projects(projects)

        elif choice == "f":
            filter_projects_by_date(projects)

        elif choice == "a":
            add_new_project(projects)

        elif choice == "u":
            update_project(projects)

        elif choice == "q":
            answer = input("Would you like to save to projects.txt? (y/N): ").lower().strip()
            if answer == "y":
                save_projects(projects, "projects.txt")
                print("Saved projects to projects.txt")
            print("Thank you for using custom-built project management software.")

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()






