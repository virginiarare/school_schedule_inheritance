from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        middle_school_summary = super().summary()
        transport_msg = self.transporation_message()

        return "\n".join((middle_school_summary, transport_msg))

    def transportation_message(self):
        has_message = "has" if self.transportation_message else "doesn't have"
        return f"{self.name} {has_message} transporation services."




# Track whether the student receives school transportation using the boolean 
# attribute gets_transportation (can be set in the constructor, defaults to False)

# Update the summary method to include information about the student's 
# transportation status
