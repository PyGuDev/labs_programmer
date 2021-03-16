class PC:
    def __init__(self, cpu_clock_frequency, count_cpu_core, ram, vram, free_hard_disk_space):
        self.cpu_clock_frequency = cpu_clock_frequency
        self.count_cpu_core = count_cpu_core
        self.ram = ram
        self.vram = vram
        self.free_hard_disk_space = free_hard_disk_space

    def get_full_info(self):
        print(f"CPU clock frequency: {self.cpu_clock_frequency}",
              f"CPU count core: {self.count_cpu_core}",
              f"RAM : {self.ram}",
              f"Video RAM: {self.vram}",
              f"Free hard disk space: {self.free_hard_disk_space}",
              end="\n"
              )


if __name__ == "__main__":
    pc_one = PC('2.5ghz', '2', '2gb', '2gb', '90 mb')
    pc_two = PC('2.0ghz', '2', '8gb', '2gb', '1200 mb')
    pc_three = PC('1.5ghz', '6', '16gb', '4gb', '220 mb')
    pc_one.get_full_info()
    pc_two.get_full_info()
    pc_three.get_full_info()