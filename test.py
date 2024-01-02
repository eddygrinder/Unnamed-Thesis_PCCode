import time
import gpiod
from gpiod.line import Direction, Value

LINE = 5
LINE2 = 6
OFF = Value.INACTIVE
ON = Value.ACTIVE

# Configuração para cada pino GPIO
configs = {
    LINE: gpiod.LineSettings(
        direction=Direction.OUTPUT, output_value=Value.ACTIVE
    ),
    LINE2: gpiod.LineSettings(
        direction=Direction.OUTPUT, output_value=Value.ACTIVE
    ),
}

request = gpiod.request_lines(
    "/dev/gpiochip4",
    consumer="controlo_GPIO's",
    config=configs
)

try:
    while True:
        request.set_value(LINE, Value.ACTIVE)
        request.set_value(LINE2, OFF)
        time.sleep(1)
        request.set_value(LINE, Value.INACTIVE)
        request.set_value(LINE2, Value.ACTIVE)
        time.sleep(1)
finally:
    request.release()
