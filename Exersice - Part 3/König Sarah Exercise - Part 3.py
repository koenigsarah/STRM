#Task 1: Some Classes and String represention
"""You are responsible for the design and implementation of a ticket system. Customers create tickets
with issues that they face when working with a software system.
A Ticket has
• an id (int). The id represents the ticket numerically.
• a description (str), which is a message from the user detailing the problem,
• the priority (IntEnum) of the ticket. Possible priorities are 1 – Severe, 2 – Significant, 3 –
Affecting, 4 – Non-Critical, and 5 – Routine,
• the status (Enum) of the ticket. The possible status are ‘Created’, ‘In progress’, ‘Testing’,
‘Closed’. All new tickets have status ‘Created’,
• [optionally] a created timestamp, when the ticket was created (datetime.now())
• a list of comments. Each comment consists of
o the actual text (str),
o the user (str) that added the comment
o the timestamp (datetime), when the comment was made
Two kinds of tickets exist:
• A Software Ticket has an error message (str) and the affected operating systems (Enum).
The possible operating systems are ‘Windows’, ‘macOS’, ‘Linux’, ‘Android’, or ‘iOS’. There
might be more than one operating system affected, but at least one is necessary. Ids of
software tickets start at 100.000.
• A Hardware Ticket has the affected component (str), its serial number (int), and, if
available, the error code (str). Ids of hardware tickets start at 200.000.
Design the classes necessary to manage these tickets, write constructors for these classes. Make sure
that the classes can represent themselves as strings."""


from enum import Enum, IntEnum #wie am 15.05 besprochen, Enum und Intenum
from datetime import datetime #für Timestamp

class Ticket:
    class Priority(IntEnum):#Unterklasse von Enum, für Ganzzahlen (als int behandelt)
        SEVERE, SIGNIFICANT, AFFECTING, NON_CRITICAL, ROUTINE = 1, 2, 3, 4, 5

    class Status(Enum):#Unterklasse, begrenzte Anzahl von Optionen darstellen (als string behandelt))
        CREATED, IN_PROGRESS, TESTING, CLOSED = "Created", "In progress", "Testing", "Closed"

    def __init__(self, description, priority, status=Status.CREATED, created_timestamp=None):#für Individualisierung, erster Parameter muss self sein, Attribute des Tickets hier; created_timestamp=None, weil sonst Syntax Error (Non-default argument follows default argument)
        self.description = description
        self.priority = priority
        self.status = status
        self.created_timestamp = created_timestamp if created_timestamp else datetime.now() #wenn Datum da ist, dann das nehmen - sont datetime.now() erstellen
        self.comments = []#für Liste

    def add_comment(self, text, user):#Methode für mit der ein Kommentar zum Ticket hinzugefügt werden kann mit Text, User und Timestamp dabei
        timestamp = datetime.now() #Timestamp von der Jetzt-Zeit, wenn Kommentar hinzugefügt wird
        self.comments.append((text, user, timestamp))#zum Kommentar text, user und timestamp anhängen(self.comments damit man auf comments von def__init__ zugreifen kann zugreifen kann)

    def __str__(self):#Methode um Ticket-Objekt zu String zu machen
        priority_str = f"Priority {self.priority.value} ({self.priority.name.replace('_', ' ')})" #Priority als Strg
        created_str = f"Created on {self.created_timestamp.strftime('%m/%d/%y %H:%M:%S')}" #Zeitstempel als str und in folgendem Datumformat (wie in Video von Studyflix erklärt)
        comment_str = "\nComments:" + "\n".join(f" {user}, {timestamp.strftime('%m/%d/%y %H:%M:%S')}: {text}" for text, user, timestamp in self.comments)

        return f"T: {self.id}: {self.description}, {created_str} - {priority_str} {comment_str}" #Und jetzt die oberen drei zusammen returnen, allgemeine Infos - das andere ist dann Software / Hardware spezifisch

class SoftwareTicket(Ticket):#eigene Klasse, ergbt von "Ticket" Klasse, zusätzliche Attribute wie Fehlermeldung und betroffene Betriebssysteme
    software_ticket_id = 100000#Start bei angegebener Nummer

    def __init__(self, description, priority, operating_systems, error_message, status=Ticket.Status.CREATED, created_timestamp=None):#Attribute festlegen, wieder bei init zuerst self vorne
        super().__init__(description, priority, status, created_timestamp)#damit ich Methode der Klasse "Tickets" aufrufen kann
        self.id = SoftwareTicket.software_ticket_id
        SoftwareTicket.software_ticket_id += 1
        self.operating_systems = operating_systems
        self.error_message = error_message

    def __str__(self):#Methode um Ticket-Objekt als String darzustellen
        base_str = super().__str__()
        os_str = ', '.join(self.operating_systems)
        return f"{base_str}\n Error message: '{self.error_message}', Affected OSs: {os_str}"

class HardwareTicket(Ticket): #eigene Klasse, erbet von Klasse "Ticket"
    hardware_ticket_id = 200000#Start bei angegebener Nummer

    def __init__(self, description, priority, component, serial_number, error_code=None, status=Ticket.Status.CREATED, created_timestamp=None):
        super().__init__(description, priority, status, created_timestamp)#damit ich Methode der Klasse "Tickets" aufrufen kann
        self.id = HardwareTicket.hardware_ticket_id
        HardwareTicket.hardware_ticket_id += 1
        self.component = component
        self.serial_number = serial_number
        self.error_code = error_code

    def __str__(self):#Methode um Ticket-Objekt als String darzustellen
        base_str = super().__str__()
        component_str = f"Component: {self.component}, s/n: {self.serial_number}, error code: {self.error_code or 'None'}"
        return f"{base_str}\n {component_str}"

# Beispiel:
software_ticket = SoftwareTicket("Login problems", Ticket.Priority.SEVERE, ["MacOS", "Windows"], "Document not found: 404")
software_ticket.add_comment("Android does not have that problem", "Tina")
software_ticket.add_comment("Android is developed separately", "Christoph")

hardware_ticket = HardwareTicket("Troubles with printer in main hall", Ticket.Priority.AFFECTING, "Printer C.1.08b", "234-23")

print(software_ticket, "\n")
print(hardware_ticket, "\n")


##Task 2
"""Internally, the Ticket System assigns tickets to various teams. Each team has a list of assigned tickets.
In this task, write two additional classes: Team and Assignments. 
Team has a name (str) representing the team’s name and a list of members (list[str]), which is a 
list of all the members of the team.
Assignments (dict[Team, list[Ticket]]) is a dictionary, where Team is the key referring to a list 
of Tickets assigned to a particular team. It has two methods: 
1. add(team: Team, ticket: Ticket) to add a ticket and 
2. a string representation.
"""

class Team:
    def __init__(self, name, *members): #für Individualisierung, * vor Members, um variable Anzahl von Argumenten für "members" aufzunehmen
        self.name = name
        self.members = list(members)#um Mitglieder in Liste abzuspeichern

    def __str__(self): #wieder als String darstellen
        return f"Team {self.name} ({', '.join(self.members)}):"#join um hier {} wegzugeben und Beistrich zwischen den Namen

class Assignments:
    def __init__(self):
        self.assignments = {}#Dictonary

    def add(self, team, ticket):
        if team not in self.assignments:
            self.assignments[team] = []
        self.assignments[team].append(ticket)

    def get(self, team):
        if team in self.assignments:
            return self.assignments[team]
        else:
            return []

    def __str__(self):
        result = "All assignments:\n"
        for team, tickets in self.assignments.items():
            result += str(team) + "\n"
            for ticket in tickets:
                result += str(ticket) + "\n"
        return result

# Beispiel
assignments = Assignments()
t1, t2 = Team("1", "Tina", "Philip"), Team("2", "Theresa", "Mirela")

assignments.add(t1, HardwareTicket("Troubles with printer in main hall", Ticket.Priority.AFFECTING,
                                  "Printer C.1.08b", "234-23"))

assignments.add(t2, SoftwareTicket("Login problems", Ticket.Priority.SEVERE,
                                   "Document not found: 404", "MacOS", "Windows"))

assignments.add(t2, SoftwareTicket("Layout issues", Ticket.Priority.AFFECTING,
                                   "ValueError", "Windows"))

print(assignments)

#Nur Aufgaben,die zu einem Team zugeordnet sind
print("Assignments of " + str(t1))
print(assignments.get(t1))
