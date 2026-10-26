#Duck Typing
# Create three completely unrelated classes: PDFReport, ExcelSheet, and EmailMessage. Each has a method
# send(). Write a function dispatch(item) that calls send() using duck typing. Prove that no
# inheritance is needed.
class PDFReport:
    def send(self):
        print("sending PDFReporter")

class ExcelSheet:
    def send(self):
        print("sending Excel Sheet")

class EmailMessage:
    def send(self):
        print("Sending Email Message")

def dispatch(item):
    item.send()

dispatch(ExcelSheet())
dispatch(EmailMessage())
dispatch(PDFReport())