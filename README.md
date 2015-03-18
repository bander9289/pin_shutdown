# Pin Shutdown via GPIO for Raspberry Pi
When the GPIO transitions from high to low, this service will begin a 20 second
countdown. If the GPIO is still low at 20 seconds, 'shutdown -f' will be called.

## Configuration
Modify pin_shutdown/pin_shutdown.py with correct GPIO number:

SHUTDOWN_PIN = 18
