from src.time_machine import VirtualTimeMachine, TimeTravelType
from src.simple_time_machine import SimpleTimeMachine

def demo_virtual_machine():
    print("=== VIRTUAL TIME MACHINE DEMO ===")
    machine = VirtualTimeMachine()
    
    results = []
    results.append(machine.execute_time_travel(1969))
    results.append(machine.execute_time_travel(2050, TimeTravelType.FUTURE))
    
    for result in results:
        if result['success']:
            print(f"Traveled to {result['current_year']}")
            print(f"Event: {result['historical_event']}")
        else:
            print(f"Failed: {result['error']}")
    
    print(f"\nMultiverse Status: {machine.get_multiverse_status()}")

def demo_simple_machine():
    print("\n=== SIMPLE TIME MACHINE DEMO ===")
    machine = SimpleTimeMachine()
    
    print(machine.travel_to_year(1999))
    print(machine.travel_to_year(2024))
    print(machine.show_history())

if __name__ == "__main__":
    demo_virtual_machine()
    demo_simple_machine()
