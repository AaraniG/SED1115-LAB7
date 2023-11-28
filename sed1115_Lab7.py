#CHATGPT WAS USED FOR GUIDANCE

from machine import Pin, PWM
from servo_translator import translate

def read_gcode_file(input_filename):
    '''
input -> filename

will return a list of lines

'''
    lines = []
    with open(input_filename, "r") as f:
       for line in f:
           lines.append(line.strip())
    return lines

def parsed_command(line):
    '''
input -> list of commands from line

produces a parsed gcode command

output-> parsed_command -> list

'''
    parts = line.split()  # Split the line into parts
    command = parts[0]    # Extract the command
    parameters = parts[1:]  # Extract parameters if present
    return [command] + parameters  # Return command and parameters as a list

def command_interpreter(parsed_command):
    '''
Input-> parsed_command

Output -> move 

move
-> shoulder => 
-> arm =>
-> pen =>

-> some parts can't move...
so need to set to null probably

Command-> list of commands parsed...

    if command is move command... have to do this
    if command is pick up pen.. have to do something


make a loop with servotranslator.py and

need to check what type of command is being returned...

from servo_translator import translate
'''
 #UNFINISHED
    
    if parsed_command[0] == 'MOVE':
        # Extract parameters: shoulder, arm, pen
        shoulder_angle = int(parsed_command[1])
        arm_angle = int(parsed_command[2])
        pen_position = int(parsed_command[3])

        # Control servo motors based on the extracted angles/positions
        # Translate angles to PWM duty cycle values using the translate function
        shoulder_pwm = translate(shoulder_angle)
        arm_pwm = translate(arm_angle)
        pen_pwm = translate(pen_position)

    

    elif parsed_command[0] == 'Pick_Up_Pen':
        # Perform actions to lift or change pen position 
        lift_pen()
        
'''
def control_shoulder_servo(pwm_value):
    # Implement control logic for the shoulder servo

def control_arm_servo(pwm_value):
    # Implement control logic for the arm servo

def control_pen_servo(pwm_value):
    # Implement control logic for the pen servo
    
def lift_pen():
    # Implement logic to lift or change the pen position

'''

def main():
    input_filename = "line.gcode" 
    lines = read_gcode_file(input_filename)

    for line in lines:
        parsed = parsed_command(line)
        command_interpreter(parsed)

if __name__ == "__main__":
    main()
    
