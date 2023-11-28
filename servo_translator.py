# Submit this file via brightspace

# You should not modify the signature (name, input, return type) of this function

#ChatGPT was used for guidance in writing this code
def translate(angle: float) -> int:
    """
    Converts an angle in degrees to the corresponding input
    for the duty_u16 method of the servo class
    See https://docs.micropython.org/en/latest/library/machine.PWM.html for more
    details on the duty_u16 method
    """
    # Your code here
    
    # Define the valid range of the servo motor angle and duty values
    ANGLE_MIN = 0
    ANGLE_MAX = 180
    DUTY_MIN = 1638
    DUTY_MAX = 8192
    
    # Ensure the input angle is within the valid range
    if angle < ANGLE_MIN:
        # If angle is less than the minimum, set it to the minimum
        angle = ANGLE_MIN
    elif angle > ANGLE_MAX:
        # If angle is more than the maximum, set it to the maximum
        angle = ANGLE_MAX
    # Calculate the proportional duty cycle using a linear mapping
    duty = int(DUTY_MIN + (angle - ANGLE_MIN) * (DUTY_MAX - DUTY_MIN) / (ANGLE_MAX - ANGLE_MIN))
    
    return duty # Replace with your return value
