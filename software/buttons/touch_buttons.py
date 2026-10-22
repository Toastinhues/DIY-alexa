
import time

# Raspberry Pi GPIO pin numbers (BCM numbering)
MUTE_PIN = 17
LISTEN_PIN = 27
BLUETOOTH_PIN = 22

BLUETOOTH_HOLD_SECONDS = 3


def handle_mute():
    print("Mute button tapped")


def handle_listen():
    print("Listening button tapped")


def handle_bluetooth():
    print("Bluetooth mode activated")


def main():
    try:
        from gpiozero import Button

        mute = Button(MUTE_PIN, pull_up=False)
        listen = Button(LISTEN_PIN, pull_up=False)
        bluetooth = Button(BLUETOOTH_PIN, pull_up=False)

        mute.when_pressed = handle_mute
        listen.when_pressed = handle_listen

        bluetooth.when_held = handle_bluetooth
        bluetooth.hold_time = BLUETOOTH_HOLD_SECONDS

        print("Touch controls running.")
        print("Mute: tap")
        print("Listening: tap")
        print("Bluetooth: hold for 3 seconds")
        print("Press Ctrl+C to stop.")

        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nTouch controls stopped.")

    finally:
        print("Exiting touch controls.")


if __name__ == "__main__":
    main()
