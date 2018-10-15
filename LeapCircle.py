import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pynput.keyboard import Key, Controller
from time import sleep








class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Motion Sensor Connected")

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        print ("Motion Sensor Disconnected")

    def on_exit(self, controller):
        print ("Exited")

    def on_frame(self, controller):
        frame = controller.frame()
        clockwiseness = ''
        keyboard1 = Controller()


        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = 'clockwise'
                else:
                    clockwiseness = 'counter-clockwise'

                print 'ID: ' + str(circle.id)+ clockwiseness

        if clockwiseness == 'counter-clockwise':
            altTab()
            playScratch()
            altTab()


        for hand in frame.hands:
            handType = 'Left Hand' if hand.is_left else 'Right Hand'
            #print handType + ' Hand ID:' + str(hand.id) + "Palm Position" + str(hand.palm_position)
            #print( "Number of Gestures " + str(len(frame.gestures()))
            print 'Height: ' + str(hand.palm_position.y)
            normal = hand.palm_normal
            direction = hand.direction
            pitchValue = hand.palm_position.y
            hold = 0
            time.sleep(.3)
            if(hold ==0):

                if(pitchValue < 100):

                    altTab()
                    playPause()
                    altTab()
                    hold = 1
            if (hold ==1):
                hold = 0

"""
                if(pitchValue >300):

                    altTab()

                    time.sleep(2)
                    keyboard1.press('g')
                    keyboard1.release('g')
                    time.sleep(2)

                    altTab()
gggg

        #    print "Pitch:" + str(direction.pitch * Leap.RAD_TO_DEG) + ' Roll: ' +str(normal.roll * Leap.RAD_TO_DEG) + ' Yaw: '+ str(direction.yaw * Leap.RAD_TO_DEG)

            arm = hand.arm
            print "Arm Direct: " + str(arm.direction) + ' Wrist Position:' + str(arm.wrist_position) + " Elbow: " + str(arm.elbow_position)

            for finger in hand.fingers:
                print "Finger Type: " + self.finger_names[finger.Type()]


        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                screentap = ScreenTapGesture(gesture)
                print "Screen Tap ID: "
                time.sleep(2)
                scrnID = str(gesture.id)
                if(scrnID > 0):
                    keyboard.press(Key.space)
                    keyboard.release(Key.space)
"""


def altTab():
    keyboard = Controller()

    keyboard.press(Key.cmd) #Alt
    sleep(.3)
    keyboard.press(Key.tab) #Tab
    sleep(.3)
    keyboard.release(Key.tab) #~Tab
    sleep(.3)
    keyboard.release(Key.cmd) #~Alt

def playPause():

    keyboard1 = Controller()
    time.sleep(.3)
    keyboard1.press('p')
    keyboard1.release('p')
    time.sleep(.3)

def playScratch():

    keyboard1 = Controller()
    time.sleep(.3)
    keyboard1.press('g')
    keyboard1.release('g')
    time.sleep(.3)







def main():
    listener = LeapMotionListener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print ("Press Enter to Quit")

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
