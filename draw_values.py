class Draw_Values:       
    window_width = 1200
    window_height = 800

    calendar_width = window_width * 0.6875
    calendar_height = window_height * 0.8888

    toolbar_width = window_width * 0.25
    toolbar_height = window_height * 1

    def get_window_size(self):
        return f"{self.window_width}x{self.window_height}"
    
    def get_calendar_vector(self):
        calendar_vector = []
        calendar_vector.append(0 )#+ (self.calendar_width)) #* 0.05))
        calendar_vector.append(0 )#+ (self.window_height)) * 0.05))

        calendar_vector.append(self.calendar_width)# - (self.calendar_width * 0.05))
        calendar_vector.append(self.calendar_height)# - (self.calendar_height * 0.05))

        return calendar_vector
    
    def get_cal_width(self):
        cal_vector = self.get_calendar_vector()
        cal_len = cal_vector[2] - cal_vector[0]
        return cal_len
    
    def get_cal_height(self):
        cal_vector = self.get_calendar_vector()
        cal_len = cal_vector[3] - cal_vector[1]
        return cal_len
    
    def get_time_row(self, start_time, end_time):
        cal_vector = self.get_calendar_vector()
        time_dict = {}
        time_height = self.calendar_height
        row = time_height / 24

        a = cal_vector[1]
        for x in range(start_time, end_time):
            a += row
            time_dict[str(x)] = a

        return time_dict
    
    def get_toolbar_width(self):
        return self.toolbar_width

    def get_toolbar_height(self):
        return self.toolbar_height
    
v = Draw_Values()
# for x, y in v.get_time_row().items():
#     print(f"{x}:{y}")