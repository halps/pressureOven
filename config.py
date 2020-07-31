import logging

########################################################################
#
#   General options

### Logging
log_level = logging.DEBUG
log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'

### Server
listening_ip = "0.0.0.0"
listening_port = 8081

### Cost Estimate
kwh_rate        = 0.26  # Rate in currency_type to calculate cost to run job
currency_type   = "CAD"   # Currency Symbol to show when calculating cost to run job

### Thermocouple Adapter selection:
#   max31855 - bitbang SPI interface
#   max31855spi - kernel SPI interface
#   max6675 - bitbang SPI interface
max6675 = 1
max31855 = 0
max31855spi = 0
########################################################################
#
#   GPIO Setup (BCM SoC Numbering Schema)
#
#   Check the RasPi docs to see where these GPIOs are
#   connected on the P1 header for your board type/rev.
#   These were tested on a Pi B Rev2 but of course you
#   can use whichever GPIO you prefer/have available.

### Outputs
# heaters
gpio_heatA = 21   # Switches solid-state-relay
gpio_heatB = 26  # Switches solid-state-relay
gpio_heatC = 20  # Switches solid-state-relay
gpio_heatD = 19  # Switches solid-state-relay
# lights, safety and motors
gpio_light = 27
#gpio_pressure_relay = 4
gpio_pressure_relay = 13
heater_invert = 0 # switches the polarity of the heater control

### Inputs
gpio_door = 12
gpio_cool = 22  # Regulates PWM for 12V DC Blower
gpio_air  = 25  # Switches 0-phase det. solid-state-relay
### Thermocouple Connection (using bitbang interfaces)
gpio_sensor_cs = 17
gpio_sensor_clock = 11
gpio_sensor_data = 9

### amount of time, in seconds, to wait between reads of the thermocouple
sensor_time_wait = .5

### hardcoded heater enable for now...
enable_heat_A = 1
enable_heat_B = 1
enable_heat_C = 1
enable_heat_D = 1

### max permitted setpoint for the oven
max_setpoint = 125


########################################################################
#
#   PID parameters

pid_ki = 0.1  # Integration
pid_kd = 0.4  # Derivative
pid_kp = 0.5  # Proportional


########################################################################
#
#   Simulation parameters

sim_t_env      = 25.0   # deg C
sim_c_heat     = 100.0  # J/K  heat capacity of heat element
sim_c_oven     = 2000.0 # J/K  heat capacity of oven
sim_p_heat     = 3500.0 # W    heating power of oven
sim_R_o_nocool = 1.0    # K/W  thermal resistance oven -> environment
sim_R_o_cool   = 0.05   # K/W  " with cooling
sim_R_ho_noair = 0.1    # K/W  thermal resistance heat element -> oven
sim_R_ho_air   = 0.05   # K/W  " with internal air circulation


########################################################################
#
#   Time and Temperature parameters

temp_scale          = "c" # c = Celsius | f = Fahrenheit - Unit to display 
time_scale_slope    = "m" # s = Seconds | m = Minutes | h = Hours - Slope displayed in temp_scale per time_scale_slope
time_scale_profile  = "m" # s = Seconds | m = Minutes | h = Hours - Enter and view target time in time_scale_profile

