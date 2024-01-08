###

#include <gpiod.h>

struct gpiod_chip *chip;
struct gpiod_line *line;
int val;

chip = gpiod_chip_open("/dev/gpiochip0"); 		// Open the GPIO chip
line = gpiod_chip_get_line(chip, 24); 		   		// Replace 24 with your GPIO line number
gpiod_line_request_output(line, "example", 0); 	// Set as output, initial value to low

val = 1;
while (1) {
  gpiod_line_set_value(line, val);
  val = !val;
  sleep(1);
}

gpiod_line_release(line);
gpiod_chip_close(chip);