import almanac as an

class Deckhand:
    def __init__ (self, crew):
        self.crew = crew

    def getCurrentLocation (self):
        # Read out GPS data
        # ...
        # Convert to signed lattitude, longitude (see comment in almanac)
        # ...
        return lattitude, longitude

    def getCourseAngle (self):
        # Read out compass
        # ...
        # Convert to signed angle between -180 and 180 degrees, north == 0, east == 90, west == -90
        # ...
        return courseAngle

    def getVaneAngle (self):
        # Read out wind vane
        # ...
        # Convert to signed angle between -180 and 180 degrees, stern == 0, right == 90, left == -90
        # ...
        return vaneAngle

    def setRudderAngle (self, courseAngle):
        # Convert from signed angle between -180 and 180 degrees, stern == 0, right == 90, left == -90
        # ...
        # Write to rudder servo
        # ...

    def setSailAngle (self, sailAngle):
        # Convert from signed angle between -180 and 180 degrees, stern == 0, right == 90, left == -90
        # ...
        # Write to sheet winch, to sail servo or to the all encompassing nothing
        # ...