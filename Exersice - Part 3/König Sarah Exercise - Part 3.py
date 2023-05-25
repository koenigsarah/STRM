# Task 1: Some Classes and String represention
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

from enum import Enum, IntEnum  # wie am 15.05 besprochen, Enum und Intenum
from datetime import datetime  # für Timestamp
from time import sleep # zurzeit auskommentiert

print("Task 1: ", "\n")

class Ticket:
    class Priority(IntEnum):  # Unterklasse von Enum, für Ganzzahlen (als int behandelt)
        SEVERE, SIGNIFICANT, AFFECTING, NON_CRITICAL, ROUTINE = 1, 2, 3, 4, 5

    class Status(Enum):  # Unterklasse, begrenzte Anzahl von Optionen darstellen (als string behandelt))
        CREATED, IN_PROGRESS, TESTING, CLOSED = "Created", "In progress", "Testing", "Closed"

    def __init__(self, description, priority, status=Status.CREATED,
                 created_timestamp=None):  # für Individualisierung, erster Parameter muss self sein, Attribute des Tickets hier; created_timestamp=None, weil sonst Syntax Error (Non-default argument follows default argument) - automatische Formatierung formatiert es mir so
        self.id = None  # damit die ID erst bei Hard/Software hinzugefügt wird, da sie spezifisch ist (startet mit unterschiedlichen Nummern)
        self.description = description
        self.priority = priority
        self.status = status
        self.created_timestamp = created_timestamp if created_timestamp else datetime.now()  # wenn Datum da ist, dann das nehmen - sonst datetime.now() erstellen
        self.comments = []  # für Liste (a list of comments)

    def add_comment(self, text,
                    user):  # Methode mit der ein Kommentar zum Ticket hinzugefügt werden kann mit Text, User und Timestamp dabei
        timestamp = datetime.now()  # Timestamp von der Jetzt-Zeit, wenn Kommentar hinzugefügt wird
        self.comments.append((text, user,
                              timestamp))  # zum Kommentar text, user und timestamp anhängen(self.comments damit man auf comments von def__init__ oberhalb zugreifen kann)

    def __str__(self):  # Methode um Ticket-Objekt zu String zu machen
        priority_str = f"Priority {self.priority.value} ({self.priority.name.replace('_', ' ')})"  # Priority als Strg (ist aber schon wegen ENUM string), ich will von Priority den Wert, dann in Klammern das Keyword - self damit ich auf das von oben zugreifen kann
        created_str = f"Created on {self.created_timestamp.strftime('%m/%d/%y %H:%M:%S')}"  # Zeitstempel als str und in folgendem Datumformat (wie in Video von Studyflix erklärt), self. damit ich auf created_timestamp von oben zugreifen kann
        comment_str = "\nComments:" + "\n".join(
            f" {user}, {timestamp.strftime('%m/%d/%y %H:%M:%S')}: {text}" for text, user, timestamp in
            self.comments)  # Kommentar - von wem, mit wann in welcher Formatierung +Text für text, user, timestamp in self.comments (dort hab ich vorher mit def add_commment - self.comment.append die Komm. drangehöngt)

        return f"T: {self.id:_}: {self.description}, {created_str} - {priority_str} {comment_str}"  # Und jetzt die oberen drei zusammen returnen und mit f String, für die Platzhalter, allgemeine Infos - das andere ist dann Software / Hardware spezifisch

# Funktioniert oben mal alles - allgemeine Zeile passt


class SoftwareTicket(Ticket):  # eigene Klasse, erbt von "Ticket" Klasse, zusätzliche Attribute: S-Ticket ID, Fehlermeldung und betroffene Betriebssysteme
    software_ticket_id = 100_000  # Start bei angegebener Nummer

    class OperatingSystem(Enum):  # Unterklasse, begrenzte Anzahl von Optionen darstellen (als string behandelt)
        WINDOWS, MACOS, LINUX, ANDROID, IOS = "Windows", "macOS", "Linux", "Android", "iOS"

    def __init__(self, description, priority, operating_systems, error_message, status=Ticket.Status.CREATED,
                 created_timestamp=None):  # Attribute festlegen, wieder bei init zuerst self vorne
        super().__init__(description, priority, status,
                         created_timestamp)  # damit ich Methode der Klasse "Tickets" aufrufen kann (dort festgelegte attribute)
        self.id = SoftwareTicket.software_ticket_id #ich greife auf software_ticket_id von oben zu, um es um 1 zu erhöhen (bei neuem Ticket) - damit wird die id von class Ticket überschreiben (vorher ID = None)
        SoftwareTicket.software_ticket_id += 1
        self.operating_systems = operating_systems
        # print(self.operating_systems)
        # print(self.operating_systems.value)
        self.error_message = error_message

    def __str__(self):  # Methode um Ticket-Objekt als String darzustellen, OperatingSystems durch Enum schon string, nicht mehr notwendig
        base_str = super().__str__()  # damit rufe ich die Eltern-Klasse Ticket (den return f)
        return f"{base_str}\n Error message: '{self.error_message}', Affected OSs: {self.operating_systems.value}"

    def __repr__(self):  # Methode um Ticket-Objekt als String darzustellen, OperatingSystems durch Enum schon string, nicht mehr notwendig
        base_str = super().__str__()  # damit rufe ich die Eltern-Klasse Ticket (den return f)
        return f"{base_str}\n Error message: '{self.error_message}', Affected OSs: {self.operating_systems.value}"


class HardwareTicket(Ticket):  # eigene Klasse, erbt von Klasse "Ticket"
    hardware_ticket_id = 200_000  # Start bei angegebener Nummer

    def __init__(self, description, priority, component, serial_number, error_code=None, status=Ticket.Status.CREATED,
                 created_timestamp=None):
        super().__init__(description, priority, status,
                         created_timestamp)  # damit ich Methode der Klasse "Tickets" aufrufen kann
        self.id = HardwareTicket.hardware_ticket_id
        HardwareTicket.hardware_ticket_id += 1
        self.component = component
        self.serial_number = serial_number
        self.error_code = error_code

    # def __str__(self):  # Methode um Ticket-Objekt als String darzustellen
    #     base_str = super().__str__()
    #     component_str = f"Component: {self.component}, Seriennummer: {self.serial_number}, Error code: {self.error_code or 'None'}"
    #     return f"{base_str}\n {component_str}"

    def __repr__(self):  # Methode um Ticket-Objekt als String darzustellen
        base_str = super().__str__()
        component_str = f"Component: {self.component}, Seriennummer: {self.serial_number}, Error code: {self.error_code or 'None'}"
        return f"{base_str}\n {component_str}"


# Beispiel:
software_ticket = SoftwareTicket("Login problems", Ticket.Priority.SEVERE, SoftwareTicket.OperatingSystem.WINDOWS,
                                 "Document not found: 404")
software_ticket.add_comment("Android does not have that problem", "Tina")  # 1.Kommentar
software_ticket.add_comment("Android is developed separately", "Christoph")  # 2.Kommentar


# sleep(5)
hardware_ticket = HardwareTicket("Troubles with printer in main hall", Ticket.Priority.AFFECTING, "Printer C.1.08b",
                                 "234-23")  # Nach und nach die fStrings auffüllen (zuerst allg. Ticket, dann Hardware Ticket)

software_ticket2 = SoftwareTicket("Layout issues", Ticket.Priority.AFFECTING, SoftwareTicket.OperatingSystem.LINUX, "ValueError")


print(software_ticket, "\n")
print(software_ticket2, "\n")
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
print("\n", "Task 2")

class Team:
    def __init__(self, name,
                 *members):  # für Individualisierung, * vor Members, um variable Anzahl von Argumenten für "members" aufzunehmen
        self.name = name
        self.members = list(members)  # um Mitglieder in Liste abzuspeichern

    def __str__(self):  # wieder als String darstellen, was oben in __init__ definiert wurde
        return f"Team {self.name} ({', '.join(self.members)}):"  # join um hier {} wegzugeben und Beistrich zwischen den Namen


class Assignments:  # Ticketzuweisungen
    def __init__(self):
        self.assignments = {}  # Dictonary

    def add(self, team, ticket):  # Methode add, um Team Ticket zuzuweisen
        if team not in self.assignments:
            self.assignments[team] = []
        self.assignments[team].append(ticket)  # 

    def get(self, team):  # Methode get, um Zuweisung von Team abzurufen
        if team in self.assignments:
            return self.assignments[team]
        else:
            return []  # wenn Team in assignment ist, dann assignemts[team9 returnen, sonst []

    # def __str__(self):  # wieder zu str
    #     result = "All assignments:\n"
    #     for team, tickets in self.assignments.items():  # für Team und Tickets in self assignment, result += str(team und Absatz)
    #         result += str(team) + "\n"
    #         for ticket in tickets:  # für ticket in Tickets, result += ticket und Abstand (vorher war ja Team dazu bei result)
    #             result += str(ticket) + "\n"
    #     return result

    def __repr__(self):  # Empfohlen von Alex: für textuelle Repräsentation des Objekts (jetzt ist auch der Fehler weg - hab vorher neue Tickets erstellt im 2. Part (ungewollt)
        result = "All assignments:\n"
        for team, tickets in self.assignments.items():
            result += str(team) + "\n"
            for ticket in tickets:
                result += str(ticket) + "\n"
        return result


# Beispiel
assignments = Assignments()
t1, t2 = Team("1", "Tina", "Philip"), Team("2", "Theresa", "Mirela")

assignments.add(t1, hardware_ticket)
assignments.add(t2, software_ticket)
assignments.add(t2, software_ticket2)

print(assignments)

# Nur Aufgaben, die zu einem Team zugeordnet sind
print("Assignments of " + str(t1))
print(assignments.get(t1))

print(assignments.assignments[t2])
