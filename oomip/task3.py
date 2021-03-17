class Computer:
    def __init__(self, cpu_clock_frequency, count_cpu_core, ram, vram, free_hard_disk_space):
        self.cpu_clock_frequency = cpu_clock_frequency
        self.count_cpu_core = count_cpu_core
        self.ram = ram
        self.vram = vram
        self.free_hard_disk_space = free_hard_disk_space
    
    def get_ram(self):
        return self.ram
    
    def set_ram(self, ram):
        self.ram = ram


if __name__ == "__main__":
    pc_one = Computer('2.5ghz', '2', '2gb', '2gb', '90 mb')
    print(pc_one.get_ram())
    pc_one.set_ram('4 gb')
    print(pc_one.get_ram())
