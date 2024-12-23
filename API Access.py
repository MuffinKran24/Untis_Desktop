import datetime
import webuntis

s = webuntis.Session (
    server ='borys.webuntis.com',
    getSchool='JK Gym Weinsberg',
    useragent ='WebUntis Test',
    username ='finn.brandt',
    password ='R6X2ddAwkF'
)

s.login()