"""
Project Class file
Estimated time: 2 hour
Actual time: 2 hours 24 mins (not including breaks)
"""
from datetime import date


class Project:

    def __init__(self, name, start_date: date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')},"
                f"priority: {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def check_completion(self):
        return self.completion == 100

    def starts_after(self, other_date:date):
        return self.start_date > other_date