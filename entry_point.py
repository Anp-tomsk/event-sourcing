import motor
import tornado.web
import tornado.ioloop
from motorengine import connect
from handlers.main_handler import MainHandler
from handlers.device_handler import DeviceHandler
from handlers.patient_handler import PatientHandler
from handlers.device_handler import AssignDeviceHandler


def run_app(port):
    db = motor.MotorClient('mongodb://localhost:27017').test_db
    app = tornado.web.Application([(r"/", MainHandler),
                                   (r"/api/devices", DeviceHandler),
                                   (r"/api/patients", PatientHandler),
                                   (r"/api/assignment", AssignDeviceHandler)], db=db)

    app.listen(port=port)
    io_loop = tornado.ioloop.IOLoop.instance()
    connect('test_db', host='mongodb://localhost:27017', io_loop=io_loop)
    tornado.ioloop.IOLoop.current().start()

