class Computer:
    cpu_clock_frequency = ""
    count_cpu_core = ""
    ram = ""
    vram = ""
    free_hard_disk_space = ""
    
    def loading_the_operating_system(self):
        print(self.free_hard_disk_space, 'Операционная система загружена')


if __name__ == "__main__":
    my_computer = Computer()
    my_computer.cpu_clock_frequency = '3.0 ghz'
    my_computer.count_cpu_core = '4'
    my_computer.ram = '4 gb'
    my_computer.vram = '2 gb'
    my_computer.free_hard_disk_space = '120 gb'
    my_computer.loading_the_operating_system()