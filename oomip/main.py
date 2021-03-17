class PC:
    cpu_clock_frequency = ""
    count_cpu_core = ""
    ram = ""
    vram = ""
    free_hard_disk_space = ""


class Computer:
    cpu_clock_frequency = ""
    count_cpu_core = ""
    ram = ""
    vram = ""
    free_hard_disk_space = ""
    
    def loading_the_operating_system():
        pass

if __name__ == "__main__":
    pc_one = PC()
    pc_two = PC()
    pc_three = PC()

    pc_one.cpu_clock_frequency = '2.5ghz'
    pc_one.count_cpu_core = '2'
    pc_one.ram = '2gb'
    pc_one.vram = '1gb'
    pc_one.free_hard_disk_space = '1 gb'

    pc_two.cpu_clock_frequency = '3.5ghz'
    pc_two.count_cpu_core = '2'
    pc_two.ram = '6gb'
    pc_two.vram = '2gb'
    pc_two.free_hard_disk_space = '12 gb'

    pc_three.cpu_clock_frequency = '1.2ghz'
    pc_three.count_cpu_core = '4'
    pc_three.ram = '8gb'
    pc_three.vram = '4gb'
    pc_three.free_hard_disk_space = '12 tb'
    
    print('PC 1')
    print(f"CPU clock frequency: {pc_one.cpu_clock_frequency}",
          f"CPU count core: {pc_one.count_cpu_core}",
          f"RAM : {pc_one.ram}",
          f"Video RAM: {pc_one.vram}",
          f"Free hard disk space: {pc_one.free_hard_disk_space}",
          end="\n"
          )
    print('PC 2')
    print(f"CPU clock frequency: {pc_two.cpu_clock_frequency}",
          f"CPU count core: {pc_two.count_cpu_core}",
          f"RAM : {pc_two.ram}",
          f"Video RAM: {pc_two.vram}",
          f"Free hard disk space: {pc_two.free_hard_disk_space}",
          end="\n"
          )
    print('PC 3')      
    print(f"CPU clock frequency: {pc_three.cpu_clock_frequency}",
          f"CPU count core: {pc_three.count_cpu_core}",
          f"RAM : {pc_three.ram}",
          f"Video RAM: {pc_three.vram}",
          f"Free hard disk space: {pc_three.free_hard_disk_space}",
          end="\n"
          )