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
        count = 0



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

                if clockwiseness == 'clockwise':
                    altTab()
                    playScratchForward()
                    altTab()








        for hand in frame.hands:
            handType = 'Left Hand' if hand.is_left else 'Right Hand'
            print handType
            print 'Height: ' + str(hand.palm_position.y)
            pitchValue = hand.palm_position.y
            hold = 0
            time.sleep(.3)

            if(hold ==0):

                if(handType == 'Right Hand' and pitchValue < 75):
                    altTab()
                    playPause()
                    altTab()
                    hold = 1

                if(handType == 'Left Hand' and pitchValue < 75):
                    altTab()
                    altSpace()
                    altTab()
                    hold = 1

            if (hold ==1):
                hold = 0




def altTab():
    keyboard = Controller()

    keyboard.press(Key.cmd) #Alt
    sleep(.2)
    keyboard.press(Key.tab) #Tab
    sleep(.2)
    keyboard.release(Key.tab) #~Tab
    sleep(.2)
    keyboard.release(Key.cmd) #~Alt

def altSpace():
    keyboard = Controller()

    keyboard.press(Key.alt) #Alt
    sleep(.2)
    keyboard.press(Key.space) #Space
    sleep(.2)
    keyboard.release(Key.space) #~Space
    sleep(.2)
    keyboard.release(Key.alt) #~Alt


def playPause():

    keyboard1 = Controller()
    time.sleep(.2)
    keyboard1.press('p')
    keyboard1.release('p')
    time.sleep(.2)

def playScratch():

    keyboard1 = Controller()
    time.sleep(.1)
    keyboard1.press('g')
    keyboard1.release('g')
    time.sleep(.1)
    keyboard1.press('g')
    keyboard1.release('g')
    time.sleep(.1)
    keyboard1.press('g')
    keyboard1.release('g')
    time.sleep(.1)
    keyboard1.press('g')
    keyboard1.release('g')
    time.sleep(.1)

def playScratchForward():

    keyboard1 = Controller()
    time.sleep(.1)
    keyboard1.press('f')
    keyboard1.release('f')
    time.sleep(.1)
    keyboard1.press('f')
    keyboard1.release('f')
    time.sleep(.1)
    keyboard1.press('f')
    keyboard1.release('f')
    time.sleep(.1)
    keyboard1.press('f')
    keyboard1.release('f')
    time.sleep(.1)
    keyboard1.press('f')
    keyboard1.release('f')
    time.sleep(.1)








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
