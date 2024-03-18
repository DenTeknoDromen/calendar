class Draw_Values:       
    window_width = 1600
    window_height = 900

    calendar_width = 1100
    calendar_height = 800

    def get_window_size(self):
        return f"{self.window_width}x{self.window_height}"
    
    def get_calendar_vector(self):
        calendar_vector = []
        calendar_vector.append(self.window_width - self.calendar_width)
        calendar_vector.append(self.window_height - self.calendar_height)

        calendar_vector.append(self.window_width - 100)
        calendar_vector.append(self.window_height - 100)

        return calendar_vector
    
    def get_cal_width(self):
        cal_vector = self.get_calendar_vector()
        cal_len = cal_vector[2] - cal_vector[0]
        return cal_len
    
    def get_cal_height(self):
        cal_vector = self.get_calendar_vector()
        cal_len = cal_vector[2] - cal_vector[0]
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
    
v = Draw_Values()
# for x, y in v.get_time_row().items():
#     print(f"{x}:{y}")