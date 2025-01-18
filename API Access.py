import datetime
import webuntis
import pygame

s = webuntis.Session(
    server='borys.webuntis.com',
    school='JK Gym Weinsberg',
    useragent='WebUntis Test',
    username='finn.brandt',
    password='R6X2ddAwkF'
)

s.login()

klasse = s.klassen().filter(name='9b')[0]

stundenplan = s.timetable(klasse=klasse.id, start=datetime.datetime.now(), end=datetime.datetime.now() + datetime.timedelta(days=7))

sorted_stundenplan = sorted(stundenplan, key=lambda x: x.start)

for lesson in sorted_stundenplan:
    print(f"{lesson.start} - {lesson.end}: {lesson.subjects[0].name} in {lesson.rooms[0].name}")

s.logout()

print("Done")