import datetime

class SimpleTimeMachine:
    def __init__(self):
        self.current_year = 2024
        self.travel_log = []
        self.energy = 100
    
    def travel_to_year(self, target_year):
        if target_year == self.current_year:
            return "Already in target year"
        
        year_difference = abs(target_year - self.current_year)
        energy_cost = year_difference * 0.1
        
        if self.energy < energy_cost:
            return f"Insufficient energy. Need {energy_cost}, have {self.energy}"
        
        previous_year = self.current_year
        self.current_year = target_year
        self.energy -= energy_cost
        
        journey_record = {
            'from': previous_year,
            'to': target_year,
            'energy_used': energy_cost,
            'remaining_energy': self.energy,
            'timestamp': datetime.datetime.now()
        }
        
        self.travel_log.append(journey_record)
        
        return f"Time travel successful: {previous_year} → {target_year}"
    
    def recharge_energy(self, amount=50):
        self.energy += amount
        return f"Energy recharged. Current: {self.energy}"
    
    def get_status(self):
        return {
            'current_year': self.current_year,
            'energy_level': self.energy,
            'total_journeys': len(self.travel_log),
            'last_travel': self.travel_log[-1] if self.travel_log else None
        }
    
    def show_history(self):
        if not self.travel_log:
            return "No travel history"
        
        history_text = f"Travel History (Total: {len(self.travel_log)}):\n"
        for journey in self.travel_log[-5:]:
            history_text += f"  {journey['from']} → {journey['to']} (Energy: {journey['energy_used']})\n"
        
        return history_text
